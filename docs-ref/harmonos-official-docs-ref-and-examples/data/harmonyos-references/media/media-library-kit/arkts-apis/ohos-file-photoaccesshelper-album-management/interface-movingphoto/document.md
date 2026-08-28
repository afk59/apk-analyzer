# Interface (MovingPhoto)

MovingPhoto provides APIs for managing a moving photo instance.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1b/v3/lhEx90tNQPC7_aflyc5sYQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062442Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A9BB034A6663E0B8F67A9EB0D42477B09556FFCF5AC42C8F91FEFA2DE577CCBA)

-   The initial APIs of this module are supported since API version 10. Newly added APIs will be marked with a superscript to indicate their earliest API version.
-   The initial APIs of this interface are supported since API version 12.

#### Modules to Import

import { photoAccessHelper } from '@kit.MediaLibraryKit';

#### getUri12+

getUri(): string

Obtains the URI of this moving photo.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.FileManagement.PhotoAccessHelper.Core

**Return value**

| Type | Description |
| :-- | :-- |
| string | URI of the moving photo obtained. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [File Management Error Codes](../../../../../application-framework/core-file-kit/error-codes/file-management-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 14000011 | System inner fail. |

**Example**

For details about how to create a phAccessHelper instance, see the example provided in [photoAccessHelper.getPhotoAccessHelper](../functions/document.md#photoaccesshelpergetphotoaccesshelper).

import { dataSharePredicates } from '@kit.ArkData';

class MovingPhotoHandler implements photoAccessHelper.MediaAssetDataHandler<photoAccessHelper.MovingPhoto> {
  async onDataPrepared(movingPhoto: photoAccessHelper.MovingPhoto) {
    if (movingPhoto === undefined) {
      console.error('Error occurred when preparing data');
      return;
    }
    console.info("moving photo acquired successfully, uri: " + movingPhoto.getUri());
  }
}

async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper, context: Context) {
  let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
  predicates.equalTo(photoAccessHelper.PhotoKeys.PHOTO\_SUBTYPE, photoAccessHelper.PhotoSubtype.MOVING\_PHOTO);
  let fetchOptions: photoAccessHelper.FetchOptions = {
    fetchColumns: \[\],
    predicates: predicates
  };
  // Ensure that there are moving photos in Gallery.
  let assetResult: photoAccessHelper.FetchResult<photoAccessHelper.PhotoAsset> = await phAccessHelper.getAssets(fetchOptions);
  let asset: photoAccessHelper.PhotoAsset = await assetResult.getFirstObject();
  if (asset === undefined) {
    console.error('asset is undefined');
    return;
  }
  let requestOptions: photoAccessHelper.RequestOptions = {
    deliveryMode: photoAccessHelper.DeliveryMode.FAST\_MODE,
  }
  const handler = new MovingPhotoHandler();
  try {
    let requestId: string = await photoAccessHelper.MediaAssetManager.requestMovingPhoto(context, asset, requestOptions, handler);
    console.info("moving photo requested successfully, requestId: " + requestId);
  } catch (err) {
    console.error(\`failed to request moving photo, error code is ${err.code}, message is ${err.message}\`);
  }
}

#### requestContent12+

requestContent(imageFileUri: string, videoFileUri: string): Promise<void>

Requests the image data and video data of this moving photo and writes them to the specified URIs, respectively. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.FileManagement.PhotoAccessHelper.Core

**Required permissions**: ohos.permission.READ\_IMAGEVIDEO

-   When you call this API in Picker mode, you do not need to request the **ohos.permission.READ\_IMAGEVIDEO** permission. For details, see [Accessing and Managing Moving Photos](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/photoaccesshelper-movingphoto).
-   For moving photos saved to the media library by this application, the application can access them without the **ohos.permission.READ\_IMAGEVIDEO** permission.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| imageFileUri | string | Yes | URI to which the image data of the moving photo is to be written. Example: **"file://com.example.temptest/data/storage/el2/base/haps/ImageFile.jpg"**. |
| videoFileUri | string | Yes | URI to which the video data of the moving photo is to be written. Example: **"file://com.example.temptest/data/storage/el2/base/haps/VideoFile.mp4"**. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [File Management Error Codes](../../../../../application-framework/core-file-kit/error-codes/file-management-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 14000011 | System inner fail. |

**Example**

For details about how to create a phAccessHelper instance, see the example provided in [photoAccessHelper.getPhotoAccessHelper](../functions/document.md#photoaccesshelpergetphotoaccesshelper).

import { dataSharePredicates } from '@kit.ArkData';

class MovingPhotoHandler implements photoAccessHelper.MediaAssetDataHandler<photoAccessHelper.MovingPhoto> {
  async onDataPrepared(movingPhoto: photoAccessHelper.MovingPhoto) {
    if (movingPhoto === undefined) {
      console.error('Error occurred when preparing data');
      return;
    }
    // The URIs must be valid.
    let imageFileUri: string = "file://com.example.temptest/data/storage/el2/base/haps/ImageFile.jpg";
    let videoFileUri: string = "file://com.example.temptest/data/storage/el2/base/haps/VideoFile.mp4";
    try {
      await movingPhoto.requestContent(imageFileUri, videoFileUri);
      console.info("moving photo contents retrieved successfully");
    } catch (err) {
      console.error(\`failed to retrieve contents of moving photo, error code is ${err.code}, message is ${err.message}\`);
    }
  }
}

async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper, context: Context) {
  let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
  predicates.equalTo(photoAccessHelper.PhotoKeys.PHOTO\_SUBTYPE, photoAccessHelper.PhotoSubtype.MOVING\_PHOTO);
  let fetchOptions: photoAccessHelper.FetchOptions = {
    fetchColumns: \[\],
    predicates: predicates
  };
  // Ensure that there are moving photos in Gallery.
  let assetResult: photoAccessHelper.FetchResult<photoAccessHelper.PhotoAsset> = await phAccessHelper.getAssets(fetchOptions);
  if (assetResult === undefined) {
    console.error('assetResult is undefined');
    return;
  }
  let asset: photoAccessHelper.PhotoAsset = await assetResult.getFirstObject();
  if (asset === undefined) {
    console.error('asset is undefined');
    return;
  }
  let requestOptions: photoAccessHelper.RequestOptions = {
    deliveryMode: photoAccessHelper.DeliveryMode.FAST\_MODE,
  }
  const handler = new MovingPhotoHandler();
  try {
    let requestId: string = await photoAccessHelper.MediaAssetManager.requestMovingPhoto(context, asset, requestOptions, handler);
    console.info("moving photo requested successfully, requestId: " + requestId);
  } catch (err) {
    console.error(\`failed to request moving photo, error code is ${err.code}, message is ${err.message}\`);
  }
}

#### requestContent12+

requestContent(resourceType: ResourceType, fileUri: string): Promise<void>

Requests the moving photo content of the specified resource type and writes it to the specified URI. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.FileManagement.PhotoAccessHelper.Core

**Required permissions**: ohos.permission.READ\_IMAGEVIDEO

-   When you call this API in Picker mode, you do not need to request the **ohos.permission.READ\_IMAGEVIDEO** permission. For details, see [Accessing and Managing Moving Photos](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/photoaccesshelper-movingphoto).
-   For moving photos saved to the media library by this application, the application can access them without the **ohos.permission.READ\_IMAGEVIDEO** permission.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| resourceType | [ResourceType](../enums/document.md#resourcetype11) | Yes | Resource type of the moving photo content to request. |
| fileUri | string | Yes | URI to which the moving photo content is to be written. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [File Management Error Codes](../../../../../application-framework/core-file-kit/error-codes/file-management-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 14000011 | System inner fail. |

**Example**

For details about how to create a phAccessHelper instance, see the example provided in [photoAccessHelper.getPhotoAccessHelper](../functions/document.md#photoaccesshelpergetphotoaccesshelper).

import { dataSharePredicates } from '@kit.ArkData';

class MovingPhotoHandler implements photoAccessHelper.MediaAssetDataHandler<photoAccessHelper.MovingPhoto> {
  async onDataPrepared(movingPhoto: photoAccessHelper.MovingPhoto) {
    if (movingPhoto === undefined) {
      console.error('Error occurred when preparing data');
      return;
    }
    // The URIs must be valid.
    let imageFileUri: string = "file://com.example.temptest/data/storage/el2/base/haps/ImageFile.jpg";
    try {
      await movingPhoto.requestContent(photoAccessHelper.ResourceType.IMAGE\_RESOURCE, imageFileUri);
      console.info("moving photo image content retrieved successfully");
    } catch (err) {
      console.error(\`failed to retrieve image content of moving photo, error code is ${err.code}, message is ${err.message}\`);
    }
  }
}

async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper, context: Context) {
  let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
  predicates.equalTo(photoAccessHelper.PhotoKeys.PHOTO\_SUBTYPE, photoAccessHelper.PhotoSubtype.MOVING\_PHOTO);
  let fetchOptions: photoAccessHelper.FetchOptions = {
    fetchColumns: \[\],
    predicates: predicates
  };
  // Ensure that there are moving photos in Gallery.
  let assetResult: photoAccessHelper.FetchResult<photoAccessHelper.PhotoAsset> = await phAccessHelper.getAssets(fetchOptions);
  let asset: photoAccessHelper.PhotoAsset = await assetResult.getFirstObject();
  if (asset === undefined) {
    console.error('asset is undefined');
    return;
  }
  let requestOptions: photoAccessHelper.RequestOptions = {
    deliveryMode: photoAccessHelper.DeliveryMode.FAST\_MODE,
  }
  const handler = new MovingPhotoHandler();
  try {
    let requestId: string = await photoAccessHelper.MediaAssetManager.requestMovingPhoto(context, asset, requestOptions, handler);
    console.info("moving photo requested successfully, requestId: " + requestId);
  } catch (err) {
    console.error(\`failed to request moving photo, error code is ${err.code}, message is ${err.message}\`);
  }
}

#### requestContent12+

requestContent(resourceType: ResourceType): Promise<ArrayBuffer>

Requests the moving photo content of the specified resource type and returns it in ArrayBuffer format. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.FileManagement.PhotoAccessHelper.Core

**Required permissions**: ohos.permission.READ\_IMAGEVIDEO

-   When you call this API in Picker mode, you do not need to request the **ohos.permission.READ\_IMAGEVIDEO** permission. For details, see [Accessing and Managing Moving Photos](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/photoaccesshelper-movingphoto).
-   For moving photos saved to the media library by this application, the application can access them without the **ohos.permission.READ\_IMAGEVIDEO** permission.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| resourceType | [ResourceType](../enums/document.md#resourcetype11) | Yes | Resource type of the moving photo content to request. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<ArrayBuffer> | Promise used to return the requested content in an ArrayBuffer. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [File Management Error Codes](../../../../../application-framework/core-file-kit/error-codes/file-management-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 14000011 | System inner fail. |

**Example**

For details about how to create a phAccessHelper instance, see the example provided in [photoAccessHelper.getPhotoAccessHelper](../functions/document.md#photoaccesshelpergetphotoaccesshelper).

import { dataSharePredicates } from '@kit.ArkData';

class MovingPhotoHandler implements photoAccessHelper.MediaAssetDataHandler<photoAccessHelper.MovingPhoto> {
  async onDataPrepared(movingPhoto: photoAccessHelper.MovingPhoto) {
    if (movingPhoto === undefined) {
      console.error('Error occurred when preparing data');
      return;
    }
    try {
      let buffer: ArrayBuffer = await movingPhoto.requestContent(photoAccessHelper.ResourceType.IMAGE\_RESOURCE);
      console.info("moving photo image content retrieved successfully, buffer length: " + buffer.byteLength);
    } catch (err) {
      console.error(\`failed to retrieve image content of moving photo, error code is ${err.code}, message is ${err.message}\`);
    }
  }
}

async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper, context: Context) {
  let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
  predicates.equalTo(photoAccessHelper.PhotoKeys.PHOTO\_SUBTYPE, photoAccessHelper.PhotoSubtype.MOVING\_PHOTO);
  let fetchOptions: photoAccessHelper.FetchOptions = {
    fetchColumns: \[\],
    predicates: predicates
  };
  // Ensure that there are moving photos in Gallery.
  let assetResult: photoAccessHelper.FetchResult<photoAccessHelper.PhotoAsset> = await phAccessHelper.getAssets(fetchOptions);
  let asset: photoAccessHelper.PhotoAsset = await assetResult.getFirstObject();
  if (asset === undefined) {
    console.error('asset is undefined');
    return;
  }
  let requestOptions: photoAccessHelper.RequestOptions = {
    deliveryMode: photoAccessHelper.DeliveryMode.FAST\_MODE,
  }
  const handler = new MovingPhotoHandler();
  try {
    let requestId: string = await photoAccessHelper.MediaAssetManager.requestMovingPhoto(context, asset, requestOptions, handler);
    console.info("moving photo requested successfully, requestId: " + requestId);
  } catch (err) {
    console.error(\`failed to request moving photo, error code is ${err.code}, message is ${err.message}\`);
  }
}
