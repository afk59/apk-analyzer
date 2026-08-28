# Interface (ImageSource)

The **ImageSource** class provides APIs to obtain image information.

Before calling any API in ImageSource, you must use [image.createImageSource](../functions/document.md#imagecreateimagesource) to create an ImageSource instance.

All APIs in ImageSource cannot be called concurrently.

Images occupy a large amount of memory. When you finish using an ImageSource instance, call [release](#release) to free the memory promptly. Before releasing the instance, ensure that all asynchronous operations associated with the instance have finished and the instance is no longer needed.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/98/v3/zSYvxx1yQ5Ci1U3esjG7dw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062431Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=DFBA63E99DEB789DDD0EB9D654C15D27DF396A90950287755A106F7B71C47293)

The initial APIs of this module are supported since API version 6. Newly added APIs will be marked with a superscript to indicate their earliest API version.

#### Modules to Import

import { image } from '@kit.ImageKit';

#### Properties

**System capability**: SystemCapability.Multimedia.Image.ImageSource

| Name | Type | Read Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| supportedFormats | Array<string> | Yes | No | Supported formats, including .png, .jpeg, .bmp, .gif, .webp, .dng, and .heic12+ (depending on the hardware). |

#### getImageInfo

getImageInfo(index: number, callback: AsyncCallback<ImageInfo>): void

Obtains the image information with the specified index. This API uses an asynchronous callback to return the result.

**Widget capability**: This API can be used in ArkTS widgets since API version 12.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Multimedia.Image.ImageSource

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| index | number | Yes | Index of the image source. The default value is **0**, indicating the first image. If this parameter is set to N, the (N+1)th image is used. For single-frame images, the value is always **0**. For multi-frame images such as animations, the value ranges from 0 to (Number of frames – 1). |
| callback | AsyncCallback<[ImageInfo](../interfaces-others/document.md#imageinfo)\> | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined** and **data** is the image information obtained; otherwise, **err** is an error object. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

async function GetImageInfo(imageSourceObj : image.ImageSource) {
  imageSourceObj.getImageInfo(0, (error: BusinessError, imageInfo: image.ImageInfo) => {
    if (error) {
      console.error(\`Failed to obtain the image information.code is ${error.code}, message is ${error.message}\`);
    } else {
      console.info('Succeeded in obtaining the image information.');
    }
  })
}

#### getImageInfo

getImageInfo(callback: AsyncCallback<ImageInfo>): void

Obtains the image information. This API uses an asynchronous callback to return the result.

**Widget capability**: This API can be used in ArkTS widgets since API version 12.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Multimedia.Image.ImageSource

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<[ImageInfo](../interfaces-others/document.md#imageinfo)\> | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined** and **data** is the image information obtained; otherwise, **err** is an error object. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

async function GetImageInfo(imageSourceObj : image.ImageSource) {
  imageSourceObj.getImageInfo((err: BusinessError, imageInfo: image.ImageInfo) => {
    if (err) {
      console.error(\`Failed to obtain the image information.code is ${err.code}, message is ${err.message}\`);
    } else {
      console.info('Succeeded in obtaining the image information.');
    }
  })
}

#### getImageInfo

getImageInfo(index?: number): Promise<ImageInfo>

Obtains the image information. This API uses a promise to return the result.

**Widget capability**: This API can be used in ArkTS widgets since API version 12.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Multimedia.Image.ImageSource

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| index | number | No | Index of the image source. The default value is **0**, indicating the first image. If this parameter is set to N, the (N+1)th image is used. For single-frame images, the value is always **0**. For multi-frame images such as animations, the value ranges from 0 to (Number of frames – 1). |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[ImageInfo](../interfaces-others/document.md#imageinfo)\> | Promise used to return the image information. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

async function GetImageInfo(imageSourceObj : image.ImageSource) {
  imageSourceObj.getImageInfo(0)
    .then((imageInfo: image.ImageInfo) => {
      console.info('Succeeded in obtaining the image information.');
    }).catch((error: BusinessError) => {
      console.error(\`Failed to obtain the image information.code is ${error.code}, message is ${error.message}\`);
    })
}

#### getImageInfoSync12+

getImageInfoSync(index?: number): ImageInfo

Obtains the image information with the specified index. This API returns the result synchronously.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c1/v3/DNQbTiD-S1SsIEof1Dp2eg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062431Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=DA2B91D35D6AAE5CED48845C2DD9E04DFF2AE9E2E1F9A2589F5CC5075DA635C2)

This API operates synchronously and will block the current thread during execution. It should not be invoked from the main thread, as doing so can lead to application lag, frame drops, or delayed responsiveness. For details, see [Overview of Concurrency in Time-Consuming Tasks](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/time-consuming-task-overview).

**System capability**: SystemCapability.Multimedia.Image.ImageSource

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| index | number | No | Index of the image source. The default value is **0**, indicating the first image. If this parameter is set to N, the (N+1)th image is used. For single-frame images, the value is always **0**. For multi-frame images such as animations, the value ranges from 0 to (Number of frames – 1). |

**Return value**

| Type | Description |
| :-- | :-- |
| [ImageInfo](../interfaces-others/document.md#imageinfo) | Image information. |

**Example**

function GetImageInfoSync(context : Context) {
  // "test.jpg" is only an example. Replace it with the actual one in use. Otherwise, the imageSource instance fails to be created, and subsequent operations cannot be performed.
  let filePath: string = context.filesDir + "/test.jpg";
  let imageSource = image.createImageSource(filePath);
  let imageInfo = imageSource.getImageInfoSync(0);
  if (imageInfo == undefined) {
    console.error('Failed to obtain the image information.');
  } else {
    console.info('Succeeded in obtaining the image information.');
    console.info('imageInfo.size.height:' + imageInfo.size.height);
    console.info('imageInfo.size.width:' + imageInfo.size.width);
  }
}

#### getImageProperty11+

getImageProperty(key:PropertyKey, options?: ImagePropertyOptions): Promise<string>

Obtains the value of a property with the specified index in this image. This API uses a promise to return the result.

This API applies only to images that are in JPEG, PNG, or HEIF12+ format and contain the Exif information. (The supported formats may vary depending on the hardware.) You can use the **supportedFormats** property to check whether the Exif read/write operation for images in HEIF format is supported.

**System capability**: SystemCapability.Multimedia.Image.ImageSource

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| key | [PropertyKey](../enums/document.md#propertykey7) | Yes | Name of the property. |
| options | [ImagePropertyOptions](../interfaces-others/document.md#imagepropertyoptions11) | No | Image properties, including the image index and default property value. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<string> | Promise used to return the property value. If the operation fails, the default value is returned. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [Image Error Codes](../../../error-codes/image-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error.Possible causes:1.Mandatory parameters are left unspecified;2.Incorrect parameter types;3.Parameter verification failed; |
| 62980096 | The operation failed. Possible cause: 1.Image upload exception. 2. Decoding process exception. 3. Insufficient memory. |
| 62980103 | The image data is not supported. |
| 62980110 | The image source data is incorrect. |
| 62980111 | The image source data is incomplete. |
| 62980112 | The image format does not match. |
| 62980113 | Unknown image format.The image data provided is not in a recognized or supported format, or it may be corrupted. |
| 62980115 | Invalid image parameter. |
| 62980118 | Failed to create the image plugin. |
| 62980122 | Failed to decode the image header. |
| 62980123 | The image does not support EXIF decoding. |
| 62980135 | The EXIF value is invalid. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

async function GetImageProperty(imageSourceObj : image.ImageSource) {
  let options: image.ImagePropertyOptions = { index: 0, defaultValue: '9999' }
  imageSourceObj.getImageProperty(image.PropertyKey.BITS\_PER\_SAMPLE, options)
    .then((data: string) => {
      console.info('Succeeded in getting the value of the specified attribute key of the image.');
    }).catch((error: BusinessError) => {
    console.error(\`Failed to get the value of the specified attribute key of the image, error.code ${error.code}, error.message ${error.message}\`);
  })
}

#### getImageProperties12+

getImageProperties(key: Array<PropertyKey>): Promise<Record<PropertyKey, string|null>>

Obtains the values of properties with the given names in this image. This API uses a promise to return the result.

This API applies only to images that are in JPEG, PNG, or HEIF format and contain the Exif information. (The supported formats may vary depending on the hardware.) You can use the **supportedFormats** property to check whether the Exif read/write operation for images in HEIF format is supported.

**System capability**: SystemCapability.Multimedia.Image.ImageSource

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| key | Array<[PropertyKey](../enums/document.md#propertykey7)\> | Yes | Array of properties names. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<Record<[PropertyKey](../enums/document.md#propertykey7), string | null>> | Promise used to return the property values. If the operation fails, **null** is returned. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [Image Error Codes](../../../error-codes/image-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error.Possible causes:1.Mandatory parameters are left unspecified;2.Incorrect parameter types;3.Parameter verification failed; |
| 62980096 | The operation failed. Possible cause: 1.Image upload exception. 2. Decoding process exception. 3. Insufficient memory. |
| 62980110 | The image source data is incorrect. |
| 62980113 | Unknown image format.The image data provided is not in a recognized or supported format, or it may be corrupted. |
| 62980116 | Failed to decode the image. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

async function GetImageProperties(imageSourceObj : image.ImageSource) {
  let key = \[image.PropertyKey.IMAGE\_WIDTH, image.PropertyKey.IMAGE\_LENGTH\];
  imageSourceObj.getImageProperties(key).then((data) => {
    console.info(JSON.stringify(data));
  }).catch((err: BusinessError) => {
    console.error(JSON.stringify(err));
  });
}

#### getImagePropertySync20+

getImagePropertySync(key:PropertyKey): string

Obtains the value of a specified Exif property. This API returns the result synchronously.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/27/v3/AohJf-guQlOS-Y9j6i9hmQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062431Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=FD4C1164599745DA17A2A15920FDA248A7B03CF1FE9DDCCEF28C00B2D3AE842F)

-   This API applies only to images that are in JPEG, PNG, or HEIF format and contain the Exif information. (The supported formats may vary depending on the hardware.)
    
-   Exif information is metadata of the image, including shooting time, camera model, aperture, focal length, and ISO.
    
-   This API operates synchronously and will block the current thread during execution. It should not be invoked from the main thread, as doing so can lead to application lag, frame drops, or delayed responsiveness. For details, see [Overview of Concurrency in Time-Consuming Tasks](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/time-consuming-task-overview).
    

**System capability**: SystemCapability.Multimedia.Image.ImageSource

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| key | [PropertyKey](../enums/document.md#propertykey7) | Yes | Name of the property. |

**Return value**

| Type | Description |
| :-- | :-- |
| string | Value of the specified Exif property. If retrieval fails, the default value of the property is returned. For details about the meaning of each data value, see [PropertyKey](../enums/document.md#propertykey7). |

**Error codes**

For details about the error codes, see [Image Error Codes](../../../error-codes/image-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 7700101 | Bad source. e.g.,1. Image has invalid width or height. 2. Image source incomplete. 3. Read image data failed. 4. Codec create failed. |
| 7700102 | Unsupported MIME type. |
| 7700202 | Unsupported metadata. For example, key is not supported. |

**Example**

function GetImagePropertySync(context : Context) {
  let resourceMgr = context.resourceManager;
  if (resourceMgr == null) {
    return;
  }
  let fd = resourceMgr.getRawFdSync("example.jpg");

  const imageSourceObj = image.createImageSource(fd);
  console.info("getImagePropertySync");
  let bits\_per\_sample = imageSourceObj.getImagePropertySync(image.PropertyKey.BITS\_PER\_SAMPLE);
  console.info("bits\_per\_sample : " + bits\_per\_sample);
}

#### modifyImageProperty11+

modifyImageProperty(key: PropertyKey, value: string): Promise<void>

Modifies the value of a property in this image. This API uses a promise to return the result.

This API applies only to images that are in JPEG, PNG, or HEIF12+ format and contain the Exif information. (The supported formats may vary depending on the hardware.) You can use the **supportedFormats** property to check whether the Exif read/write operation for images in HEIF format is supported.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/75/v3/6n0eu89TRNejZcgVUxW3Ug/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062431Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B8C1FFA3641B5B3841E9A67818A20DC6776CCDA132D2042A9B6EC2D95FE5FB3A)

The property byte length is changed when the **modifyImageProperty** API is called to modify the value of a property. Currently, you can call the API in an ImageSource instance created based on a file descriptor or path, but not an ImageSource instance created based on buffers.

**System capability**: SystemCapability.Multimedia.Image.ImageSource

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| key | [PropertyKey](../enums/document.md#propertykey7) | Yes | Name of the property. |
| value | string | Yes | New value of the property. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [Image Error Codes](../../../error-codes/image-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error.Possible causes:1.Mandatory parameters are left unspecified;2.Incorrect parameter types; |
| 62980123 | The image does not support EXIF decoding. |
| 62980133 | The EXIF data is out of range. |
| 62980135 | The EXIF value is invalid. |
| 62980146 | The EXIF data failed to be written to the file. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

async function ModifyImageProperty(imageSourceObj : image.ImageSource) {
  imageSourceObj.modifyImageProperty(image.PropertyKey.IMAGE\_WIDTH, "120").then(() => {
    imageSourceObj.getImageProperty(image.PropertyKey.IMAGE\_WIDTH).then((width: string) => {
      console.info(\`ImageWidth is :${width}\`);
    }).catch((error: BusinessError) => {
      console.error(\`Failed to get the Image Width, error.code ${error.code}, error.message ${error.message}\`);
    })
  }).catch((error: BusinessError) => {
    console.error(\`Failed to modify the Image Width, error.code ${error.code}, error.message ${error.message}\`);
  })
}

#### modifyImageProperties12+

modifyImageProperties(records: Record<PropertyKey, string|null>): Promise<void>

Modifies the values of properties in this image. This API uses a promise to return the result.

This API applies only to images that are in JPEG, PNG, or HEIF format and contain the Exif information. (The supported formats may vary depending on the hardware.) You can use the **supportedFormats** property to check whether the Exif read/write operation for images in HEIF format is supported.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/36/v3/RMoErGzxRdGG35r-n1ErTg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062431Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1C03FD94027303AF884AB04532B2654D13E089EE021BFEB4FDC9921111E27F2D)

The property byte length is changed when the **modifyImageProperties** API is called to modify the values of properties. Currently, you can call the API in an ImageSource instance created based on a file descriptor or path, but not an ImageSource instance created based on buffers.

**System capability**: SystemCapability.Multimedia.Image.ImageSource

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| records | Record<[PropertyKey](../enums/document.md#propertykey7), string | null> | Yes | Array of property names and property values. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [Image Error Codes](../../../error-codes/image-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error.Possible causes:1.Mandatory parameters are left unspecified;2.Incorrect parameter types;3.Parameter verification failed; |
| 62980123 | The image does not support EXIF decoding. |
| 62980135 | The EXIF value is invalid. |
| 62980146 | The EXIF data failed to be written to the file. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

async function ModifyImageProperties(imageSourceObj : image.ImageSource) {
  let keyValues: Record<PropertyKey, string|null> = {
    \[image.PropertyKey.IMAGE\_WIDTH\] : "1024",
    \[image.PropertyKey.IMAGE\_LENGTH\] : "1024"
  };
  let checkKey = \[image.PropertyKey.IMAGE\_WIDTH, image.PropertyKey.IMAGE\_LENGTH\];
  imageSourceObj.modifyImageProperties(keyValues).then(() => {
    imageSourceObj.getImageProperties(checkKey).then((data) => {
      console.info(\`Image Width and Image Height:${data}\`);
    }).catch((err: BusinessError) => {
      console.error(\`Failed to modify the Image Width and Image Height, error.code ${err.code}, error.message ${err.message}\`);
    });
  }).catch((err: BusinessError) => {
    console.error(\`Failed to modify the Image Width and Image Height, error.code ${err.code}, error.message ${err.message}\`);
  });
}

#### modifyImagePropertiesEnhanced22+

modifyImagePropertiesEnhanced(records: Record<string, string | null>): Promise<void>

Modifies image properties in batches. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e8/v3/W265AE8QROKPoqKKphJ5mw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062431Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6133637EB3AF0457392D7C252523E773564A03239AF6963460083E40B5F2342F)

-   Calling this API to modify properties alters the property byte length. You are advised to create an [ImageSource](../functions/document.md#imagecreateimagesource7) instance by passing a file descriptor or an [ImageSource](../functions/document.md#imagecreateimagesource) instance by passing a URI.
-   This API modifies batch data in memory and writes the data to the file in a single operation. It is more efficient than [modifyImageProperties](#modifyimageproperties12).
-   This API applies only to images that are in JPEG, PNG, or HEIF format and contain the Exif information. Before modifying properties, use the **supportedFormats** property to check whether the device supports Exif information read/write in HEIF format.

**System capability**: SystemCapability.Multimedia.Image.ImageSource

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| records | Record<string, string | null> | Yes | Key-value pairs of image property names and property values. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Image Error Codes](../../../error-codes/image-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 7700102 | Unsupported MIME type. |
| 7700202 | Unsupported metadata. For example, the property key is not supported, or the property value is invalid. |
| 7700304 | Failed to write image properties to the file. |

**Example**

import { image } from '@kit.ImageKit';
import { BusinessError } from '@kit.BasicServicesKit';

async function ModifyImagePropertiesEnhanced(imageSourceObj : image.ImageSource) {
  let keyValues: Record<string, string|null> = {
    "ImageWidth" : "1024",
    "ImageLength" : "1024"
  };
  let checkKey = \[image.PropertyKey.IMAGE\_WIDTH, image.PropertyKey.IMAGE\_LENGTH\];
  imageSourceObj.modifyImagePropertiesEnhanced(keyValues).then(() => {
    imageSourceObj.getImageProperties(checkKey).then((data) => {
      console.info(\`Image Width and Image Height:${data}\`);
    }).catch((err: BusinessError) => {
      console.error(\`Failed to modify the Image Width and Image Height, error.code ${err.code}, error.message ${err.message}\`);
    });
  }).catch((err: BusinessError) => {
    console.error(\`Failed to modify the Image Width and Image Height, error.code ${err.code}, error.message ${err.message}\`);
  });
}

#### updateData9+

updateData(buf: ArrayBuffer, isFinished: boolean, offset: number, length: number): Promise<void>

Updates incremental data. This API uses a promise to return the result.

**System capability**: SystemCapability.Multimedia.Image.ImageSource

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| buf | ArrayBuffer | Yes | Buffer for storing the incremental data. |
| isFinished | boolean | Yes | Whether data update is complete. The value **true** means that the data update is complete and the last segment of data is stored in the buffer. The value **false** means that the data update is still in progress. |
| offset | number | Yes | Offset of the data in the buffer, measured from the start of the entire image file, in bytes. |
| length | number | Yes | Length of the buffer, in bytes. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

async function UpdateDatay(imageSourceObj : image.ImageSource) {
  const array: ArrayBuffer = new ArrayBuffer(100);
  imageSourceObj.updateData(array, false, 0, 10).then(() => {
    console.info('Succeeded in updating data.');
  }).catch((err: BusinessError) => {
    console.error(\`Failed to update data.code is ${err.code},message is ${err.message}\`);
  })
}

#### updateData9+

updateData(buf: ArrayBuffer, isFinished: boolean, offset: number, length: number, callback: AsyncCallback<void>): void

Updates incremental data. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Multimedia.Image.ImageSource

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| buf | ArrayBuffer | Yes | Buffer for storing the incremental data. |
| isFinished | boolean | Yes | Whether data update is complete. The value **true** means that the data update is complete and the last segment of data is stored in the buffer. The value **false** means that the data update is still in progress. |
| offset | number | Yes | Offset of the data in the buffer, measured from the start of the entire image file, in bytes. |
| length | number | Yes | Length of the buffer, in bytes. |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined**; otherwise, **err** is an error object. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

async function UpdateDatay(imageSourceObj : image.ImageSource) {
  const array: ArrayBuffer = new ArrayBuffer(100);
  imageSourceObj.updateData(array, false, 0, 10, (err: BusinessError) => {
    if (err) {
      console.error(\`Failed to update data.code is ${err.code},message is ${err.message}\`);
    } else {
      console.info('Succeeded in updating data.');
    }
  })
}

#### createPicture13+

createPicture(options?: DecodingOptionsForPicture): Promise<Picture>

Creates a Picture object based on decoding options. This API uses a promise to return the result.

Images occupy a large amount of memory. When you finish using a Picture instance, call [release](../interface-picture/document.md#release13) to free the memory promptly.

Before releasing the instance, ensure that all asynchronous operations associated with the instance have finished and the instance is no longer needed.

**System capability**: SystemCapability.Multimedia.Image.ImageSource

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| options | [DecodingOptionsForPicture](../interfaces-others/document.md#decodingoptionsforpicture13) | No | Decoding options. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[Picture](../interface-picture/document.md)\> | Promise used to return the Picture object. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [Image Error Codes](../../../error-codes/image-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error.Possible causes: 1.Mandatory parameters are left unspecified.2.Incorrect parameter types; 3.Parameter verification failed. |
| 7700203 | Unsupported options. For example, unsupported desiredPixelFormat causes a failure in converting an image into the desired pixel format. |
| 7700301 | Decode failed. |

**Example**

async function CreatePicture(imageSourceObj : image.ImageSource) {
  let options: image.DecodingOptionsForPicture = {
    desiredAuxiliaryPictures: \[image.AuxiliaryPictureType.GAINMAP\] // GAINMAP indicates the type of the auxiliary picture to be decoded.
  };
  let pictureObj: image.Picture = await imageSourceObj.createPicture(options);
  if (pictureObj != null) {
    console.info('Create picture succeeded');
  } else {
    console.error('Create picture failed');
  }
}

#### createPictureAtIndex20+

createPictureAtIndex(index: number): Promise<Picture>

Creates a Picture object from the specified index of an image. Only GIF images are supported. This API uses a promise to return the result.

Images occupy a large amount of memory. When you finish using a Picture instance, call [release](../interface-picture/document.md#release13) to free the memory promptly.

Before releasing the instance, ensure that all asynchronous operations associated with the instance have finished and the instance is no longer needed.

**System capability**: SystemCapability.Multimedia.Image.ImageSource

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| index | number | Yes | Index of the image. The value range is \[0, Number of frames – 1\]. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[Picture](../interface-picture/document.md)\> | Promise used to return the Picture object. |

**Error codes**

For details about the error codes, see [Image Error Codes](../../../error-codes/image-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 7700101 | Bad source. |
| 7700102 | Unsupported MIME type. |
| 7700103 | Image too large. |
| 7700203 | Unsupported options. For example, index is invalid. |
| 7700301 | Decoding failed. |

**Example**

async function CreatePictures(imageSourceObj : image.ImageSource) {
  let frameCount: number = await imageSourceObj.getFrameCount();
  for (let index = 0; index < frameCount; index++) {
    try {
      let pictureObj: image.Picture = await imageSourceObj.createPictureAtIndex(index);
      console.info('Create picture succeeded for frame: ' + index);
    } catch (e) {
      console.error('Create picture failed for frame: ' + index);
    }
  }
}

#### createPixelMap7+

createPixelMap(options?: DecodingOptions): Promise<PixelMap>

Creates a PixelMap object based on decoding options. This API uses a promise to return the result. This API uses a promise to return the result.

Starting from API version 15, you are advised to use [createPixelMapUsingAllocator](#createpixelmapusingallocator15). This API can be used to specify the memory type [AllocatorType](../enums/document.md#allocatortype15) of the output PixelMap. For details, see [Optimizing Memory for Image Decoding (ArkTS)](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/image-allocator-type).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/87/v3/Kwv3RD6lSF6UCg5CxiMsFA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062431Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8B8CDA1DEDC33C3272BD55DC9361B5B543C7C8E5C3A1D898C9CCE01A3B38E0FA)

-   This method is not thread-safe and does not support concurrent calls on the same ImageSource instance.
-   Images occupy a large amount of memory. When you finish using a PixelMap instance, call [release](../interface-pixelmap/document.md#release7) to free the memory promptly.
-   Before releasing the instance, ensure that all asynchronous operations associated with the instance have finished and the instance is no longer needed.

**Widget capability**: This API can be used in ArkTS widgets since API version 12.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Multimedia.Image.ImageSource

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| options | [DecodingOptions](../interfaces-others/document.md#decodingoptions7) | No | Decoding options. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[PixelMap](../interface-pixelmap/document.md)\> | Promise used to return the PixelMap object. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

async function CreatePixelMap(imageSourceObj : image.ImageSource) {
  imageSourceObj.createPixelMap().then((pixelMap: image.PixelMap) => {
    console.info('Succeeded in creating pixelMap object through image decoding parameters.');
  }).catch((error: BusinessError) => {
    console.error(\`Failed to create pixelMap object through image decoding parameters, error.code ${error.code}, error.message ${error.message}\`);
  })
}

#### createPixelMap7+

createPixelMap(callback: AsyncCallback<PixelMap>): void

Creates a PixelMap object based on the default parameters. This API uses an asynchronous callback to return the result.

Starting from API version 15, you are advised to use [createPixelMapUsingAllocator](#createpixelmapusingallocator15). This API can be used to specify the memory type [AllocatorType](../enums/document.md#allocatortype15) of the output PixelMap. For details, see [Optimizing Memory for Image Decoding (ArkTS)](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/image-allocator-type).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/34/v3/ocgybjLbTluFQxNY1cv2Pw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062431Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F62598FC98DF391EF4FC8215457E22F1233227A024A4C18AD69C44BE141EC28D)

-   This method is not thread-safe and does not support concurrent calls on the same ImageSource instance.
-   Images occupy a large amount of memory. When you finish using a PixelMap instance, call [release](../interface-pixelmap/document.md#release7) to free the memory promptly.
-   Before releasing the instance, ensure that all asynchronous operations associated with the instance have finished and the instance is no longer needed.

**Widget capability**: This API can be used in ArkTS widgets since API version 12.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Multimedia.Image.ImageSource

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<[PixelMap](../interface-pixelmap/document.md)\> | Yes | Callback used to return the result. If the operation is successful, **err** is undefined and **data** is the PixelMap object obtained; otherwise, **err** is an error object. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

async function CreatePixelMap(imageSourceObj : image.ImageSource) {
  imageSourceObj.createPixelMap((err: BusinessError, pixelMap: image.PixelMap) => {
    if (err) {
      console.error(\`Failed to create pixelMap.code is ${err.code},message is ${err.message}\`);
    } else {
      console.info('Succeeded in creating pixelMap object.');
    }
  })
}

#### createPixelMap7+

createPixelMap(options: DecodingOptions, callback: AsyncCallback<PixelMap>): void

Creates a PixelMap object based on decoding options. This API uses a promise to return the result. This API uses an asynchronous callback to return the result.

Starting from API version 15, you are advised to use [createPixelMapUsingAllocator](#createpixelmapusingallocator15). This API can be used to specify the memory type [AllocatorType](../enums/document.md#allocatortype15) of the output PixelMap. For details, see [Optimizing Memory for Image Decoding (ArkTS)](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/image-allocator-type).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d7/v3/TFIp2pM3ShKMyyLM01VHxg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062431Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2E9FAB3B2D9210948ED049577C4B866BDE18F3AD0ED5B382E354F4B46A478668)

-   This method is not thread-safe and does not support concurrent calls on the same ImageSource instance.
-   Images occupy a large amount of memory. When you finish using a PixelMap instance, call [release](../interface-pixelmap/document.md#release7) to free the memory promptly.
-   Before releasing the instance, ensure that all asynchronous operations associated with the instance have finished and the instance is no longer needed.

**Widget capability**: This API can be used in ArkTS widgets since API version 12.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Multimedia.Image.ImageSource

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| options | [DecodingOptions](../interfaces-others/document.md#decodingoptions7) | Yes | Decoding options. |
| callback | AsyncCallback<[PixelMap](../interface-pixelmap/document.md)\> | Yes | Callback used to return the result. If the operation is successful, **err** is undefined and **data** is the PixelMap object obtained; otherwise, **err** is an error object. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

async function CreatePixelMap(imageSourceObj : image.ImageSource) {
  let decodingOptions: image.DecodingOptions = {
    sampleSize: 1,
    editable: true,
    desiredSize: { width: 1, height: 2 },
    rotate: 10,
    desiredPixelFormat: image.PixelMapFormat.RGBA\_8888,
    desiredRegion: { size: { width: 1, height: 2 }, x: 0, y: 0 },
    // If both desiredSize and desiredRegion are passed to the decoding API, you must also include cropAndScaleStrategy to determine whether to crop or scale first. CROP\_FIRST is recommended.
    cropAndScaleStrategy: image.CropAndScaleStrategy.CROP\_FIRST,
    index: 0
  };
  imageSourceObj.createPixelMap(decodingOptions, (err: BusinessError, pixelMap: image.PixelMap) => {
    if (err) {
      console.error(\`Failed to create pixelMap.code is ${err.code},message is ${err.message}\`);
    } else {
      console.info('Succeeded in creating pixelMap object.');
    }
  })
}

#### createPixelMapSync12+

createPixelMapSync(options?: DecodingOptions): PixelMap

Creates a PixelMap object based on decoding options. This API returns the result synchronously.

Images occupy a large amount of memory. When you finish using a PixelMap instance, call [release](../interface-pixelmap/document.md#release7) to free the memory promptly.

Before releasing the instance, ensure that all asynchronous operations associated with the instance have finished and the instance is no longer needed.

Starting from API version 15, you are advised to use [createPixelMapUsingAllocatorSync](#createpixelmapusingallocatorsync15). This API can be used to specify the memory type [AllocatorType](../enums/document.md#allocatortype15) of the output PixelMap. For details, see [Optimizing Memory for Image Decoding (ArkTS)](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/image-allocator-type).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7f/v3/m1Ysxp97T6C_xLhWkKugYQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062431Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=03307BC0D902F690E7DC47E98A30059D9AA86F8E1E05336A4579C82BAB9702F3)

This API operates synchronously and will block the current thread during execution. It should not be invoked from the main thread, as doing so can lead to application lag, frame drops, or delayed responsiveness. For details, see [Overview of Concurrency in Time-Consuming Tasks](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/time-consuming-task-overview).

**System capability**: SystemCapability.Multimedia.Image.ImageSource

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| options | [DecodingOptions](../interfaces-others/document.md#decodingoptions7) | No | Decoding options. |

**Return value**

| Type | Description |
| :-- | :-- |
| [PixelMap](../interface-pixelmap/document.md) | PixelMap object. |

**Example**

function CreatePixelMapSync(context : Context) {
  // "test.jpg" is only an example. Replace it with the actual one in use. Otherwise, the imageSource instance fails to be created, and subsequent operations cannot be performed.
  let filePath: string = context.filesDir + "/test.jpg";
  let imageSource = image.createImageSource(filePath);
  let decodingOptions: image.DecodingOptions = {
    sampleSize: 1,
    editable: true,
    desiredSize: { width: 1, height: 2 },
    rotate: 10,
    desiredPixelFormat: image.PixelMapFormat.RGBA\_8888,
    desiredRegion: { size: { width: 1, height: 2 }, x: 0, y: 0 },
    // If both desiredSize and desiredRegion are passed to the decoding API, you must also include cropAndScaleStrategy to determine whether to crop or scale first. CROP\_FIRST is recommended.
    cropAndScaleStrategy: image.CropAndScaleStrategy.CROP\_FIRST,
    index: 0
  };
  let pixelmap = imageSource.createPixelMapSync(decodingOptions);
  if (pixelmap != undefined) {
    console.info('Succeeded in creating pixelMap object.');
  } else {
    console.error('Failed to create pixelMap.');
  }
}

#### createPixelMapList10+

createPixelMapList(options?: DecodingOptions): Promise<Array<PixelMap>>

Creates an array of PixelMap objects based on decoding options. This API uses a promise to return the result.

For dynamic images such as GIF and WebP images, this API returns the data of each frame of the image. For static images, this API returns the data of the unique frame of the image.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6f/v3/FRLn5Q9RQ9eF3sD8itTixg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062431Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A1C77CC458AA6A9CDD5A6B6F910107A1820860E954DEDA6FF7D2B63328A8F26B)

-   This method is not thread-safe and does not support concurrent calls on the same ImageSource instance.
-   Images occupy a large amount of memory. When you finish using a PixelMap instance, call [release](../interface-pixelmap/document.md#release7) to free the memory promptly.
-   Before releasing the instance, ensure that all asynchronous operations associated with the instance have finished and the instance is no longer needed.
-   This function decodes all frames at once. If the number of frames is high or the size of individual frames is large, it can lead to significant memory usage. In these cases, you are advised to use the **Image** component for displaying animations. The **Image** component decodes frames one by one, which uses less memory than this function.

**System capability**: SystemCapability.Multimedia.Image.ImageSource

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| options | [DecodingOptions](../interfaces-others/document.md#decodingoptions7) | No | Decoding options. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<Array<[PixelMap](../interface-pixelmap/document.md)\>> | Promise used to return an array of PixelMap objects. |

**Error codes**

For details about the error codes, see [Image Error Codes](../../../error-codes/image-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 62980096 | The operation failed. Possible cause: 1.Image upload exception. 2. Decoding process exception. 3. Insufficient memory. |
| 62980099 | The shared memory data is abnormal. |
| 62980101 | The image data is abnormal. |
| 62980103 | The image data is not supported. |
| 62980106 | The image data is too large. This status code is thrown when an error occurs during the process of checking size. |
| 62980109 | Failed to crop the image. |
| 62980111 | The image source data is incomplete. |
| 62980115 | Invalid image parameter. |
| 62980116 | Failed to decode the image. |
| 62980118 | Failed to create the image plugin. |
| 62980137 | Invalid media operation. |
| 62980173 | The DMA memory does not exist. |
| 62980174 | The DMA memory data is abnormal. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

async function CreatePixelMapList(imageSourceObj : image.ImageSource) {
  let decodeOpts: image.DecodingOptions = {
    sampleSize: 1,
    editable: true,
    desiredSize: { width: 198, height: 202 },
    rotate: 0,
    desiredPixelFormat: image.PixelMapFormat.RGBA\_8888,
    index: 0,
  };
  imageSourceObj.createPixelMapList(decodeOpts).then((pixelMapList: Array<image.PixelMap>) => {
    console.info('Succeeded in creating pixelMapList object.');
  }).catch((err: BusinessError) => {
    console.error(\`Failed to create pixelMapList object, error code is ${err}\`);
  })
}

#### createPixelMapList10+

createPixelMapList(callback: AsyncCallback<Array<PixelMap>>): void

Creates an array of PixelMap objects based on the default parameters. This API uses an asynchronous callback to return the result.

For dynamic images such as GIF and WebP images, this API returns the data of each frame of the image. For static images, this API returns the data of the unique frame of the image.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d8/v3/nWEbO1ZvR0GGxa2LxLuFcQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062431Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=BD11ABA27AD028E8CBCF660484EABF62B8C7FB42D50CDE9AA9C28441FA47E9C4)

-   This method is not thread-safe and does not support concurrent calls on the same ImageSource instance.
-   Images occupy a large amount of memory. When you finish using a PixelMap instance, call [release](../interface-pixelmap/document.md#release7) to free the memory promptly.
-   Before releasing the instance, ensure that all asynchronous operations associated with the instance have finished and the instance is no longer needed.
-   This function decodes all frames at once. If the number of frames is high or the size of individual frames is large, it can lead to significant memory usage. In these cases, you are advised to use the **Image** component for displaying animations. The **Image** component decodes frames one by one, which uses less memory than this function.

**System capability**: SystemCapability.Multimedia.Image.ImageSource

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<Array<[PixelMap](../interface-pixelmap/document.md)\>> | Yes | Callback used to return the result. If the operation is successful, **err** is undefined and **data** is the array of PixelMap objects obtained; otherwise, **err** is an error object. |

**Error codes**

For details about the error codes, see [Image Error Codes](../../../error-codes/image-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 62980096 | The operation failed. Possible cause: 1.Image upload exception. 2. Decoding process exception. 3. Insufficient memory. |
| 62980099 | The shared memory data is abnormal. |
| 62980101 | The image data is abnormal. |
| 62980103 | The image data is not supported. |
| 62980106 | The image data is too large. This status code is thrown when an error occurs during the process of checking size. |
| 62980109 | Failed to crop the image. |
| 62980111 | The image source data is incomplete. |
| 62980115 | Invalid image parameter. |
| 62980116 | Failed to decode the image. |
| 62980118 | Failed to create the image plugin. |
| 62980137 | Invalid media operation. |
| 62980173 | The DMA memory does not exist. |
| 62980174 | The DMA memory data is abnormal. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

async function CreatePixelMapList(imageSourceObj : image.ImageSource) {
  imageSourceObj.createPixelMapList((err: BusinessError, pixelMapList: Array<image.PixelMap>) => {
    if (err) {
      console.error(\`Failed to create pixelMapList object, error code is ${err}\`);
    } else {
      console.info('Succeeded in creating pixelMapList object.');
    }
  })
}

#### createPixelMapList10+

createPixelMapList(options: DecodingOptions, callback: AsyncCallback<Array<PixelMap>>): void

Creates an array of PixelMap objects based on decoding options. This API uses an asynchronous callback to return the result.

For dynamic images such as GIF and WebP images, this API returns the data of each frame of the image. For static images, this API returns the data of the unique frame of the image.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a0/v3/ju0IrMcHQQenkLE41SerMA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062431Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=CA1DDE1FF8C21F8CC56DD26CE5EB0722773210D79DEA41D9B93D897702416428)

-   This method is not thread-safe and does not support concurrent calls on the same ImageSource instance.
-   Images occupy a large amount of memory. When you finish using a PixelMap instance, call [release](../interface-pixelmap/document.md#release7) to free the memory promptly.
-   Before releasing the instance, ensure that all asynchronous operations associated with the instance have finished and the instance is no longer needed.
-   This function decodes all frames at once. If the number of frames is high or the size of individual frames is large, it can lead to significant memory usage. In these cases, you are advised to use the **Image** component for displaying animations. The **Image** component decodes frames one by one, which uses less memory than this function.

**System capability**: SystemCapability.Multimedia.Image.ImageSource

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| options | [DecodingOptions](../interfaces-others/document.md#decodingoptions7) | Yes | Decoding options. |
| callback | AsyncCallback<Array<[PixelMap](../interface-pixelmap/document.md)\>> | Yes | Callback used to return the result. If the operation is successful, **err** is undefined and **data** is the array of PixelMap objects obtained; otherwise, **err** is an error object. |

**Error codes**

For details about the error codes, see [Image Error Codes](../../../error-codes/image-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 62980096 | The operation failed. Possible cause: 1.Image upload exception. 2. Decoding process exception. 3. Insufficient memory. |
| 62980099 | The shared memory data is abnormal. |
| 62980101 | The image data is abnormal. |
| 62980103 | The image data is not supported. |
| 62980106 | The image data is too large. This status code is thrown when an error occurs during the process of checking size. |
| 62980109 | Failed to crop the image. |
| 62980111 | The image source data is incomplete. |
| 62980115 | Invalid image parameter. |
| 62980116 | Failed to decode the image. |
| 62980118 | Failed to create the image plugin. |
| 62980137 | Invalid media operation. |
| 62980173 | The DMA memory does not exist. |
| 62980174 | The DMA memory data is abnormal. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

async function CreatePixelMapList(imageSourceObj : image.ImageSource) {
  let decodeOpts: image.DecodingOptions = {
    sampleSize: 1,
    editable: true,
    desiredSize: { width: 198, height: 202 },
    rotate: 0,
    desiredPixelFormat: image.PixelMapFormat.RGBA\_8888,
    index: 0,
  };
  imageSourceObj.createPixelMapList(decodeOpts, (err: BusinessError, pixelMapList: Array<image.PixelMap>) => {
    if (err) {
      console.error(\`Failed to create pixelMapList object, error code is ${err}\`);
    } else {
      console.info('Succeeded in creating pixelMapList object.');
    }
  })
}

#### createPixelMapUsingAllocator15+

createPixelMapUsingAllocator(options?: DecodingOptions, allocatorType?: AllocatorType): Promise<PixelMap>

Creates a PixelMap object based on decoding options and memory type. This API uses a promise to return the result. For details, see [Optimizing Memory for Image Decoding (ArkTS)](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/image-allocator-type).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4e/v3/6T3mcX1jRPC89fxUTDF7Mw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062431Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D46BE475FE0CB9E029DE6B4CB8CFFA50B3F420013BB0ABE0941D8223B30D9A0F)

-   This method is not thread-safe and does not support concurrent calls on the same ImageSource instance.
-   Images occupy a large amount of memory. When you finish using a PixelMap instance, call [release](../interface-pixelmap/document.md#release7) to free the memory promptly.
-   Before releasing the instance, ensure that all asynchronous operations associated with the instance have finished and the instance is no longer needed.

**System capability**: SystemCapability.Multimedia.Image.ImageSource

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| options | [DecodingOptions](../interfaces-others/document.md#decodingoptions7) | No | Decoding options. |
| allocatorType | [AllocatorType](../enums/document.md#allocatortype15) | No | Type of the memory. The default value is **AllocatorType.AUTO**. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[PixelMap](../interface-pixelmap/document.md)\> | Promise used to return the PixelMap object. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [Image Error Codes](../../../error-codes/image-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error.Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types;3.Parameter verification failed. |
| 7700101 | Bad source. e.g.,1. Image has invalid width or height. 2. Image source incomplete. 3. Read image data failed. 4. Codec create failed. |
| 7700102 | Unsupported mimetype. |
| 7700103 | Image too large. This status code is thrown when an error occurs during the process of checking size. |
| 7700201 | Unsupported allocator type, e.g., use share memory to decode a HDR image as only DMA supported hdr metadata. |
| 7700203 | Unsupported options, e.g., cannot convert image into desired pixel format. |
| 7700301 | Failed to decode image. |
| 7700302 | Failed to allocate memory. |

**Example**

async function CreatePixelMapUsingAllocator(context : Context) {
  // "test.jpg" is only an example. Replace it with the actual one in use. Otherwise, the imageSource instance fails to be created, and subsequent operations cannot be performed.
  let filePath: string = context.filesDir + "/test.jpg";
  let imageSource = image.createImageSource(filePath);
  let decodingOptions: image.DecodingOptions = {
    editable: true,
    desiredSize: { width: 3072, height: 4096 },
    rotate: 10,
    desiredPixelFormat: image.PixelMapFormat.RGBA\_8888,
    desiredRegion: { size: { width: 3072, height: 4096 }, x: 0, y: 0 },
    // If both desiredSize and desiredRegion are passed to the decoding API, you must also include cropAndScaleStrategy to determine whether to crop or scale first. CROP\_FIRST is recommended.
    cropAndScaleStrategy: image.CropAndScaleStrategy.CROP\_FIRST,
    index: 0
  };
  let pixelmap = imageSource.createPixelMapUsingAllocator(decodingOptions, image.AllocatorType.AUTO);
  if (pixelmap != undefined) {
    console.info('Succeeded in creating pixelMap object.');
  } else {
    console.error('Failed to create pixelMap.');
  }
}

#### createPixelMapUsingAllocatorSync15+

createPixelMapUsingAllocatorSync(options?: DecodingOptions, allocatorType?: AllocatorType): PixelMap

Creates a PixelMap object based on decoding options and memory type. This API returns the result synchronously. For details, see [Optimizing Memory for Image Decoding (ArkTS)](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/image-allocator-type).

Images occupy a large amount of memory. When you finish using a PixelMap instance, call [release](../interface-pixelmap/document.md#release7) to free the memory promptly.

Before releasing the instance, ensure that all asynchronous operations associated with the instance have finished and the instance is no longer needed.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c0/v3/IE7TQgCqRTWXqUYxsu_Olw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062431Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B16B2FBB52DD8849C9DC506CEF206B824667AA9A9E291E408032C7DEC03C6C48)

This API operates synchronously and will block the current thread during execution. It should not be invoked from the main thread, as doing so can lead to application lag, frame drops, or delayed responsiveness. For details, see [Overview of Concurrency in Time-Consuming Tasks](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/time-consuming-task-overview).

**System capability**: SystemCapability.Multimedia.Image.ImageSource

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| options | [DecodingOptions](../interfaces-others/document.md#decodingoptions7) | No | Decoding options. |
| allocatorType | [AllocatorType](../enums/document.md#allocatortype15) | No | Type of the memory. The default value is **AllocatorType.AUTO**. |

**Return value**

| Type | Description |
| :-- | :-- |
| [PixelMap](../interface-pixelmap/document.md) | PixelMap object. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [Image Error Codes](../../../error-codes/image-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error.Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types;3.Parameter verification failed. |
| 7700101 | Bad source. e.g.,1. Image has invalid width or height. 2. Image source incomplete. 3. Read image data failed. 4. Codec create failed. |
| 7700102 | Unsupported mimetype. |
| 7700103 | Image too large. This status code is thrown when an error occurs during the process of checking size. |
| 7700201 | Unsupported allocator type, e.g., use share memory to decode a HDR image as only DMA supported hdr metadata. |
| 7700203 | Unsupported options, e.g., cannot convert image into desired pixel format. |
| 7700301 | Failed to decode image. |
| 7700302 | Failed to allocate memory. |

**Example**

async function CreatePixelMapUsingAllocator(context : Context) {
  // "test.jpg" is only an example. Replace it with the actual one in use. Otherwise, the imageSource instance fails to be created, and subsequent operations cannot be performed.
  let filePath: string = context.filesDir + "/test.jpg";
  let imageSource = image.createImageSource(filePath);
  let decodingOptions: image.DecodingOptions = {
    editable: true,
    desiredSize: { width: 3072, height: 4096 },
    rotate: 10,
    desiredPixelFormat: image.PixelMapFormat.RGBA\_8888,
    desiredRegion: { size: { width: 3072, height: 4096 }, x: 0, y: 0 },
    // If both desiredSize and desiredRegion are passed to the decoding API, you must also include cropAndScaleStrategy to determine whether to crop or scale first. CROP\_FIRST is recommended.
    cropAndScaleStrategy: image.CropAndScaleStrategy.CROP\_FIRST,
    index: 0
  };
  let pixelmap = imageSource.createPixelMapUsingAllocatorSync(decodingOptions, image.AllocatorType.AUTO);
  if (pixelmap != undefined) {
    console.info('Succeeded in creating pixelMap object.');
  } else {
    console.error('Failed to create pixelMap.');
  }
}

#### getDelayTimeList10+

getDelayTimeList(callback: AsyncCallback<Array<number>>): void

Obtains an array of delay times. This API uses an asynchronous callback to return the result. This API applies only to images in GIF or WebP format.

**System capability**: SystemCapability.Multimedia.Image.ImageSource

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<Array<number>> | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined** and **data** is the array of delay times obtained; otherwise, **err** is an error object. |

**Error codes**

For details about the error codes, see [Image Error Codes](../../../error-codes/image-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 62980096 | The operation failed. Possible cause: 1.Image upload exception. 2. Decoding process exception. 3. Insufficient memory. |
| 62980110 | The image source data is incorrect. |
| 62980111 | The image source data is incomplete. |
| 62980115 | Invalid image parameter. |
| 62980116 | Failed to decode the image. |
| 62980118 | Failed to create the image plugin. |
| 62980122 | Failed to decode the image header. |
| 62980149 | Invalid MIME type for the image source. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

async function GetDelayTimeList(imageSourceObj : image.ImageSource) {
  imageSourceObj.getDelayTimeList((err: BusinessError, delayTimes: Array<number>) => {
    if (err) {
      console.error(\`Failed to get delayTimes object.code is ${err.code},message is ${err.message}\`);
    } else {
      console.info('Succeeded in getting delayTimes object.');
    }
  })
}

#### getDelayTimeList10+

getDelayTimeList(): Promise<Array<number>>

Obtains an array of delay times. This API uses a promise to return the result. This API applies only to images in GIF or WebP format.

**System capability**: SystemCapability.Multimedia.Image.ImageSource

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<Array<number>> | Promise used to return an array of delay times. |

**Error codes**

For details about the error codes, see [Image Error Codes](../../../error-codes/image-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 62980096 | The operation failed. Possible cause: 1.Image upload exception. 2. Decoding process exception. 3. Insufficient memory. |
| 62980110 | The image source data is incorrect. |
| 62980111 | The image source data is incomplete. |
| 62980115 | Invalid image parameter. |
| 62980116 | Failed to decode the image. |
| 62980118 | Failed to create the image plugin. |
| 62980122 | Failed to decode the image header. |
| 62980149 | Invalid MIME type for the image source. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

async function GetDelayTimeList(imageSourceObj : image.ImageSource) {
  imageSourceObj.getDelayTimeList().then((delayTimes: Array<number>) => {
    console.info('Succeeded in getting delayTimes object.');
  }).catch((err: BusinessError) => {
    console.error(\`Failed to get delayTimes object.code is ${err.code},message is ${err.message}\`);
  })
}

#### getFrameCount10+

getFrameCount(callback: AsyncCallback<number>): void

Obtains the number of frames. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Multimedia.Image.ImageSource

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<number> | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined** and **data** is the number of frames obtained; otherwise, **err** is an error object. |

**Error codes**

For details about the error codes, see [Image Error Codes](../../../error-codes/image-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 62980096 | The operation failed. Possible cause: 1.Image upload exception. 2. Decoding process exception. 3. Insufficient memory. |
| 62980111 | The image source data is incomplete. |
| 62980112 | The image format does not match. |
| 62980113 | Unknown image format.The image data provided is not in a recognized or supported format, or it may be corrupted. |
| 62980115 | Invalid image parameter. |
| 62980116 | Failed to decode the image. |
| 62980118 | Failed to create the image plugin. |
| 62980122 | Failed to decode the image header. |
| 62980137 | Invalid media operation. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

async function GetFrameCount(imageSourceObj : image.ImageSource) {
  imageSourceObj.getFrameCount((err: BusinessError, frameCount: number) => {
    if (err) {
      console.error(\`Failed to get frame count.code is ${err.code},message is ${err.message}\`);
    } else {
      console.info('Succeeded in getting frame count.');
    }
  })
}

#### getFrameCount10+

getFrameCount(): Promise<number>

Obtains the number of frames. This API uses a promise to return the result.

**System capability**: SystemCapability.Multimedia.Image.ImageSource

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<number> | Promise used to return the number of frames. |

**Error codes**

For details about the error codes, see [Image Error Codes](../../../error-codes/image-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 62980096 | The operation failed. Possible cause: 1.Image upload exception. 2. Decoding process exception. 3. Insufficient memory. |
| 62980111 | The image source data is incomplete. |
| 62980112 | The image format does not match. |
| 62980113 | Unknown image format.The image data provided is not in a recognized or supported format, or it may be corrupted. |
| 62980115 | Invalid image parameter. |
| 62980116 | Failed to decode the image. |
| 62980118 | Failed to create the image plugin. |
| 62980122 | Failed to decode the image header. |
| 62980137 | Invalid media operation. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

async function GetFrameCount(imageSourceObj : image.ImageSource) {
  imageSourceObj.getFrameCount().then((frameCount: number) => {
    console.info('Succeeded in getting frame count.');
  }).catch((err: BusinessError) => {
    console.error(\`Failed to get frame count.code is ${err.code},message is ${err.message}\`);
  })
}

#### getDisposalTypeList12+

getDisposalTypeList(): Promise<Array<number>>

Obtains the list of disposal types. This API uses a promise to return the result. It is used only for GIF images.

**System capability**: SystemCapability.Multimedia.Image.ImageSource

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<Array<number>> | Promise used to return an array of disposal types. |

**Error codes**

For details about the error codes, see [Image Error Codes](../../../error-codes/image-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 62980096 | The operation failed. Possible cause: 1.Image upload exception. 2. Decoding process exception. 3. Insufficient memory. |
| 62980101 | The image data is abnormal. |
| 62980137 | Invalid media operation. |
| 62980149 | Invalid MIME type for the image source. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

async function GetDisposalTypeList(imageSourceObj : image.ImageSource) {
  imageSourceObj.getDisposalTypeList().then((disposalTypes: Array<number>) => {
    console.info('Succeeded in getting disposalTypes object.');
  }).catch((err: BusinessError) => {
    console.error(\`Failed to get disposalTypes object.code ${err.code},message is ${err.message}\`);
  })
}

#### release

release(callback: AsyncCallback<void>): void

Releases this ImageSource instance. This API uses an asynchronous callback to return the result.

Images occupy a large amount of memory. When you finish using an ImageSource instance, call this API to free the memory promptly.

Before releasing the instance, ensure that all asynchronous operations associated with the instance have finished and the instance is no longer needed.

**System capability**: SystemCapability.Multimedia.Image.ImageSource

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined**; otherwise, **err** is an error object. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

async function Release(imageSourceObj : image.ImageSource) {
  imageSourceObj.release((err: BusinessError) => {
    if (err) {
      console.error(\`Failed to release the image source instance.code ${err.code},message is ${err.message}\`);
    } else {
      console.info('Succeeded in releasing the image source instance.');
    }
  })
}

#### release

release(): Promise<void>

Releases this ImageSource instance. This API uses a promise to return the result.

Images occupy a large amount of memory. When you finish using an ImageSource instance, call this API to free the memory promptly.

Before releasing the instance, ensure that all asynchronous operations associated with the instance have finished and the instance is no longer needed.

**System capability**: SystemCapability.Multimedia.Image.ImageSource

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

async function Release(imageSourceObj : image.ImageSource) {
  imageSourceObj.release().then(() => {
    console.info('Succeeded in releasing the image source instance.');
  }).catch((error: BusinessError) => {
    console.error(\`Failed to release the image source instance.code ${error.code},message is ${error.message}\`);
  })
}

#### getImageProperty(deprecated)

getImageProperty(key:string, options?: GetImagePropertyOptions): Promise<string>

Obtains the value of a property with the specified index in this image. This API uses a promise to return the result.

This API applies only to images that are in JPEG, PNG, or HEIF12+ format and contain the Exif information. (The supported formats may vary depending on the hardware.) You can use the **supportedFormats** property to check whether the Exif read/write operation for images in HEIF format is supported.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c9/v3/B4yz0SixTc21aM1qWKy4FA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062431Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=377C643C1509A02BDE274485F8B7CE3D2A6216C5C9FDE71102E0ACFD6B48BFCF)

This API is supported since API version 7 and is deprecated since API version 11. You are advised to use [getImageProperty](#getimageproperty11) instead.

**System capability**: SystemCapability.Multimedia.Image.ImageSource

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| key | string | Yes | Name of the property. |
| options | [GetImagePropertyOptions](../interfaces-others/document.md#getimagepropertyoptionsdeprecated) | No | Image properties, including the image index and default property value. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<string> | Promise used to return the property value. If the operation fails, the default value is returned. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

async function GetImageProperty(imageSourceObj : image.ImageSource) {
  imageSourceObj.getImageProperty("BitsPerSample")
    .then((data: string) => {
      console.info('Succeeded in getting the value of the specified attribute key of the image.');
    }).catch((error: BusinessError) => {
    console.error(\`Failed to get the value of the specified attribute key of the image, error.code ${error.code}, error.message ${error.message}\`);
  })
}

#### getImageProperty(deprecated)

getImageProperty(key:string, callback: AsyncCallback<string>): void

Obtains the value of a property with the specified index in this image. This API uses an asynchronous callback to return the result.

This API applies only to images that are in JPEG, PNG, or HEIF12+ format and contain the Exif information. (The supported formats may vary depending on the hardware.) You can use the **supportedFormats** property to check whether the Exif read/write operation for images in HEIF format is supported.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a9/v3/AdsTrQ4mROWgeogrtCnhoQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062431Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=EEF34BFF1DD77338E672B51FFE13032BECDC6E18199BCEC4137DAD9B6F857E9B)

This API is supported since API version 7 and is deprecated since API version 11. You are advised to use [getImageProperty](#getimageproperty11) instead.

**System capability**: SystemCapability.Multimedia.Image.ImageSource

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| key | string | Yes | Name of the property. |
| callback | AsyncCallback<string> | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined** and **data** is the property value obtained; otherwise, **err** is an error object. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

async function GetImageProperty(imageSourceObj : image.ImageSource) {
  imageSourceObj.getImageProperty("BitsPerSample", (error: BusinessError, data: string) => {
    if (error) {
      console.error('Failed to get the value of the specified attribute key of the image.');
    } else {
      console.info('Succeeded in getting the value of the specified attribute key of the image.');
    }
  })
}

#### getImageProperty(deprecated)

getImageProperty(key:string, options: GetImagePropertyOptions, callback: AsyncCallback<string>): void

Obtains the value of a property in this image. This API uses an asynchronous callback to return the result.

This API applies only to images that are in JPEG, PNG, or HEIF12+ format and contain the Exif information. (The supported formats may vary depending on the hardware.) You can use the **supportedFormats** property to check whether the Exif read/write operation for images in HEIF format is supported.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/65/v3/dlpOI0PoQeuELBY4ePPiHg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062431Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=18552C2C4AB28B1158D75705CAB11F04BED77D5D3D1456893FD2B18E00AABA34)

This API is supported since API version 7 and is deprecated since API version 11. You are advised to use [getImageProperty](#getimageproperty11) instead.

**System capability**: SystemCapability.Multimedia.Image.ImageSource

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| key | string | Yes | Name of the property. |
| options | [GetImagePropertyOptions](../interfaces-others/document.md#getimagepropertyoptionsdeprecated) | Yes | Image properties, including the image index and default property value. |
| callback | AsyncCallback<string> | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined** and **data** is the property value obtained; otherwise, **err** is an error object. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

async function GetImageProperty(imageSourceObj : image.ImageSource) {
  let property: image.GetImagePropertyOptions = { index: 0, defaultValue: '9999' }
  imageSourceObj.getImageProperty("BitsPerSample", property, (error: BusinessError, data: string) => {
    if (error) {
      console.error('Failed to get the value of the specified attribute key of the image.');
    } else {
      console.info('Succeeded in getting the value of the specified attribute key of the image.');
    }
  })
}

#### modifyImageProperty(deprecated)

modifyImageProperty(key: string, value: string): Promise<void>

Modifies the value of a property in this image. This API uses a promise to return the result.

This API applies only to images that are in JPEG, PNG, or HEIF12+ format and contain the Exif information. (The supported formats may vary depending on the hardware.) You can use the **supportedFormats** property to check whether the Exif read/write operation for images in HEIF format is supported.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/54/v3/sA8aavLST1SqC1vIPzWZ_w/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062431Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=80B20DFE8623E848AB41466E6389370F6FA9FF00811913A38533444E88E36E64)

-   The property byte length is changed when the **modifyImageProperty** API is called to modify the value of a property. Currently, you can call the API in an ImageSource instance created based on a file descriptor or path, but not an ImageSource instance created based on buffers.
    
-   This API is supported since API version 9 and is deprecated since API version 11. You are advised to use [modifyImageProperty](#modifyimageproperty11) instead.
    

**System capability**: SystemCapability.Multimedia.Image.ImageSource

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| key | string | Yes | Name of the property. |
| value | string | Yes | New value of the property. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

async function ModifyImageProperty(imageSourceObj : image.ImageSource) {
  imageSourceObj.modifyImageProperty("ImageWidth", "120").then(() => {
    imageSourceObj.getImageProperty("ImageWidth").then((width: string) => {
      console.info(\`ImageWidth is :${width}\`);
    }).catch((error: BusinessError) => {
      console.error(\`Failed to get the Image Width, error.code ${error.code}, error.message ${error.message}\`);
    })
  }).catch((error: BusinessError) => {
    console.error(\`Failed to modify the Image Width, error.code ${error.code}, error.message ${error.message}\`);
  })
}

#### modifyImageProperty(deprecated)

modifyImageProperty(key: string, value: string, callback: AsyncCallback<void>): void

Modifies the value of a property in this image. This API uses an asynchronous callback to return the result.

This API applies only to images that are in JPEG, PNG, or HEIF12+ format and contain the Exif information. (The supported formats may vary depending on the hardware.) You can use the **supportedFormats** property to check whether the Exif read/write operation for images in HEIF format is supported.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b1/v3/A491r8GUSCqo_HyjJVmBHQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062431Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C6F9D7FCCDCC5CF1F8ACBB10B763E8D28CDB8DD313485D3B1991CE7316CEF5AA)

-   The property byte length is changed when the **modifyImageProperty** API is called to modify the value of a property. Currently, you can call the API in an ImageSource instance created based on a file descriptor or path, but not an ImageSource instance created based on buffers.
    
-   This API is supported since API version 9 and is deprecated since API version 11. You are advised to use [modifyImageProperty](#modifyimageproperty11) instead.
    

**System capability**: SystemCapability.Multimedia.Image.ImageSource

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| key | string | Yes | Name of the property. |
| value | string | Yes | New value of the property. |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined**; otherwise, **err** is an error object. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

async function ModifyImageProperty(imageSourceObj : image.ImageSource) {
  imageSourceObj.modifyImageProperty("ImageWidth", "120", (err: BusinessError) => {
    if (err) {
      console.error(\`Failed to modify the Image Width.code is ${err.code}, message is ${err.message}\`);
    } else {
      console.info('Succeeded in modifying the Image Width.');
    }
  })
}
