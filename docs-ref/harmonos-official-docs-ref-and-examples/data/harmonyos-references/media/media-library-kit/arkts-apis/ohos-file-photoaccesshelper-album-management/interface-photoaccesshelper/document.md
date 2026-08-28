# Interface (PhotoAccessHelper)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/59/v3/EJ1wDg4cQz-M9rTrB7jiOw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062443Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=36A21ABA7014E3E22E6D7D8A30F870663CFB879EE380E04BBF6FDC14A236BC8B)

The initial APIs of this module are supported since API version 10. Newly added APIs will be marked with a superscript to indicate their earliest API version.

#### Modules to Import

import { photoAccessHelper } from '@kit.MediaLibraryKit';

#### getAssets

getAssets(options: FetchOptions, callback: AsyncCallback<FetchResult<PhotoAsset>>): void

Obtains image and video assets. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.FileManagement.PhotoAccessHelper.Core

**Required permissions**: ohos.permission.READ\_IMAGEVIDEO

When this API is called in picker mode to query the image or video resource corresponding to a specified URI, the **ohos.permission.READ\_IMAGEVIDEO** permission is not required. For details, see [Obtaining an Image or Video by URI](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/photoaccesshelper-photoviewpicker#obtaining-an-image-or-video-by-uri).

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| options | [FetchOptions](../interfaces-others/document.md#fetchoptions) | Yes | Retrieval options. |
| callback | AsyncCallback<[FetchResult](../interface-fetchresult/document.md)<[PhotoAsset](../interface-photoasset/document.md)\>> | Yes | Callback used to return the image and video assets obtained. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [File Management Error Codes](../../../../../application-framework/core-file-kit/error-codes/file-management-error-codes/document.md).

In API version 13 and earlier versions, if the caller does not have the required permission, error code 13900012 is returned. Starting from API version 14, the same situation raises error code 201.

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 201 | Permission denied. |
| 13900020 | Invalid argument. |
| 14000011 | System inner fail. |

**Example**

For details about how to create a phAccessHelper instance, see the example provided in [photoAccessHelper.getPhotoAccessHelper](../functions/document.md#photoaccesshelpergetphotoaccesshelper).

import { dataSharePredicates } from '@kit.ArkData';

async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper) {
  console.info('getAssets');
  let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
  let fetchOptions: photoAccessHelper.FetchOptions = {
    fetchColumns: \[\],
    predicates: predicates
  };

  phAccessHelper.getAssets(fetchOptions, async (err, fetchResult) => {
    if (fetchResult !== undefined) {
      console.info('fetchResult success');
      let photoAsset: photoAccessHelper.PhotoAsset = await fetchResult.getFirstObject();
      if (photoAsset !== undefined) {
        console.info('photoAsset.displayName : ' + photoAsset.displayName);
      }
    } else {
      console.error(\`fetchResult fail with error: ${err.code}, ${err.message}\`);
    }
  });
}

#### getAssets

getAssets(options: FetchOptions): Promise<FetchResult<PhotoAsset>>

Obtains image and video assets. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.FileManagement.PhotoAccessHelper.Core

**Required permissions**: ohos.permission.READ\_IMAGEVIDEO

When this API is called in picker mode to query the image or video resource corresponding to a specified URI, the **ohos.permission.READ\_IMAGEVIDEO** permission is not required. For details, see [Obtaining an Image or Video by URI](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/photoaccesshelper-photoviewpicker#obtaining-an-image-or-video-by-uri).

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| options | [FetchOptions](../interfaces-others/document.md#fetchoptions) | Yes | Retrieval options. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[FetchResult](../interface-fetchresult/document.md)<[PhotoAsset](../interface-photoasset/document.md)\>> | Promise used to return the image and video assets obtained. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [File Management Error Codes](../../../../../application-framework/core-file-kit/error-codes/file-management-error-codes/document.md).

In API version 13 and earlier versions, if the caller does not have the required permission, error code 13900012 is returned. Starting from API version 14, the same situation raises error code 201.

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 13900020 | Invalid argument. |
| 14000011 | System inner fail. |

**Example**

For details about how to create a phAccessHelper instance, see the example provided in [photoAccessHelper.getPhotoAccessHelper](../functions/document.md#photoaccesshelpergetphotoaccesshelper).

import { dataSharePredicates } from '@kit.ArkData';

async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper) {
  console.info('getAssets');
  let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
  let fetchOptions: photoAccessHelper.FetchOptions = {
    fetchColumns: \[\],
    predicates: predicates
  };
  try {
    let fetchResult: photoAccessHelper.FetchResult<photoAccessHelper.PhotoAsset> = await phAccessHelper.getAssets(fetchOptions);
    if (fetchResult !== undefined) {
      console.info('fetchResult success');
      let photoAsset: photoAccessHelper.PhotoAsset = await fetchResult.getFirstObject();
      if (photoAsset !== undefined) {
        console.info('photoAsset.displayName :' + photoAsset.displayName);
      }
    }
  } catch (err) {
    console.error(\`getAssets failed, error: ${err.code}, ${err.message}\`);
  }
}

#### getBurstAssets12+

getBurstAssets(burstKey: string, options: FetchOptions): Promise<FetchResult<PhotoAsset>>

Obtains burst assets. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.FileManagement.PhotoAccessHelper.Core

**Required permissions**: ohos.permission.READ\_IMAGEVIDEO

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| burstKey | string | Yes | Universally Unique Identifier (UUID) of a group of burst photos, that is, **BURST\_KEY** of [PhotoKeys](../enums/document.md#photokeys). The string contains 36 bytes. |
| options | [FetchOptions](../interfaces-others/document.md#fetchoptions) | Yes | Retrieval options. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[FetchResult](../interface-fetchresult/document.md)<[PhotoAsset](../interface-photoasset/document.md)\>> | Promise used to return the result. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [File Management Error Codes](../../../../../application-framework/core-file-kit/error-codes/file-management-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 14000011 | Internal system error. |

**Example**

For details about how to create a phAccessHelper instance, see the example provided in [photoAccessHelper.getPhotoAccessHelper](../functions/document.md#photoaccesshelpergetphotoaccesshelper).

import { dataSharePredicates } from '@kit.ArkData';

async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper) {
  console.info('getBurstAssets');
  let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
  let fetchOptions: photoAccessHelper.FetchOptions = {
    fetchColumns: \[\],
    predicates: predicates
  };
  // burstKey is a 36-bit UUID, which can be obtained from photoAccessHelper.PhotoKeys.
  let burstKey: string = "e719d696-09fa-44f8-8e9e-ec3f215aa62a";
  try {
    let fetchResult: photoAccessHelper.FetchResult<photoAccessHelper.PhotoAsset> = await
      phAccessHelper.getBurstAssets(burstKey, fetchOptions);
    if (fetchResult !== undefined) {
      console.info('fetchResult success');
      let photoAsset: photoAccessHelper.PhotoAsset = await fetchResult.getFirstObject();
      if (photoAsset !== undefined) {
        console.info('photoAsset.displayName :' + photoAsset.displayName);
      }
    }
  } catch (err) {
    console.error(\`getBurstAssets failed, error: ${err.code}, ${err.message}\`);
  }
}

#### createAsset

createAsset(photoType: PhotoType, extension: string, options: CreateOptions, callback: AsyncCallback<string>): void

Creates an image or video asset with the specified file type, file name extension, and options. This API uses an asynchronous callback to return the result.

If you do not have the **ohos.permission.WRITE\_IMAGEVIDEO** permission, you can create a media asset by using a security component or an authorization pop-up. For details, see [Saving Media Assets](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/photoaccesshelper-savebutton).

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.FileManagement.PhotoAccessHelper.Core

**Required permissions**: ohos.permission.WRITE\_IMAGEVIDEO

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| photoType | [PhotoType](../enums/document.md#phototype) | Yes | Type of the file to create, which can be **IMAGE** or **VIDEO**. |
| extension | string | Yes | File name extension, for example, **'jpg'**. |
| options | [CreateOptions](../interfaces-others/document.md#createoptions) | Yes | 
Options used for creation. Currently, only **title** is supported, for example, **{title: 'testPhoto'}**.

**NOTE**

If a **subtype** option is passed, the configuration does not take effect. Only DEFAULT images can be saved.

The file name must not contain any invalid characters, which are:.. \\ / : \* ? " ' \` < > | { } \[ \]

 |
| callback | AsyncCallback<string> | Yes | Callback used to return the URI of the created image or video asset. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [File Management Error Codes](../../../../../application-framework/core-file-kit/error-codes/file-management-error-codes/document.md).

In API version 13 and earlier versions, if the caller does not have the required permission, error code 13900012 is returned. Starting from API version 14, the same situation raises error code 201.

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 201 | Permission denied. |
| 13900020 | Invalid argument. |
| 14000011 | System inner fail. |

**Example**

For details about how to create a phAccessHelper instance, see the example provided in [photoAccessHelper.getPhotoAccessHelper](../functions/document.md#photoaccesshelpergetphotoaccesshelper).

async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper) {
  console.info('createAssetDemo');
  let photoType: photoAccessHelper.PhotoType = photoAccessHelper.PhotoType.IMAGE;
  let extension:string = 'jpg';
  let options: photoAccessHelper.CreateOptions = {
    title: 'testPhoto'
  }
  phAccessHelper.createAsset(photoType, extension, options, (err, uri) => {
    if (uri !== undefined) {
      console.info('createAsset uri' + uri);
      console.info('createAsset successfully');
    } else {
      console.error(\`createAsset failed, error: ${err.code}, ${err.message}\`);
    }
  });
}

#### createAsset

createAsset(photoType: PhotoType, extension: string, callback: AsyncCallback<string>): void

Creates an image or video asset with the specified file type and file name extension. This API uses an asynchronous callback to return the result.

If you do not have the **ohos.permission.WRITE\_IMAGEVIDEO** permission, you can create a media asset by using a security component or an authorization pop-up. For details, see [Saving Media Assets](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/photoaccesshelper-savebutton).

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.FileManagement.PhotoAccessHelper.Core

**Required permissions**: ohos.permission.WRITE\_IMAGEVIDEO

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| photoType | [PhotoType](../enums/document.md#phototype) | Yes | Type of the file to create, which can be **IMAGE** or **VIDEO**. |
| extension | string | Yes | File name extension, for example, **'jpg'**. |
| callback | AsyncCallback<string> | Yes | Callback used to return the URI of the created image or video asset. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [File Management Error Codes](../../../../../application-framework/core-file-kit/error-codes/file-management-error-codes/document.md).

In API version 13 and earlier versions, if the caller does not have the required permission, error code 13900012 is returned. Starting from API version 14, the same situation raises error code 201.

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 201 | Permission denied. |
| 13900020 | Invalid argument. |
| 14000011 | System inner fail. |

**Example**

For details about how to create a phAccessHelper instance, see the example provided in [photoAccessHelper.getPhotoAccessHelper](../functions/document.md#photoaccesshelpergetphotoaccesshelper).

async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper) {
  console.info('createAssetDemo');
  let photoType: photoAccessHelper.PhotoType = photoAccessHelper.PhotoType.IMAGE;
  let extension: string = 'jpg';
  phAccessHelper.createAsset(photoType, extension, (err, uri) => {
    if (uri !== undefined) {
      console.info('createAsset uri' + uri);
      console.info('createAsset successfully');
    } else {
      console.error(\`createAsset failed, error: ${err.code}, ${err.message}\`);
    }
  });
}

#### createAsset

createAsset(photoType: PhotoType, extension: string, options?: CreateOptions): Promise<string>

Creates an image or video asset with the specified file type, file name extension, and options. This API uses a promise to return the result.

If you do not have the **ohos.permission.WRITE\_IMAGEVIDEO** permission, you can create a media asset by using a security component or an authorization pop-up. For details, see [Saving Media Assets](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/photoaccesshelper-savebutton).

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.FileManagement.PhotoAccessHelper.Core

**Required permissions**: ohos.permission.WRITE\_IMAGEVIDEO

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| photoType | [PhotoType](../enums/document.md#phototype) | Yes | Type of the file to create, which can be **IMAGE** or **VIDEO**. |
| extension | string | Yes | File name extension, for example, **'jpg'**. |
| options | [CreateOptions](../interfaces-others/document.md#createoptions) | No | 
Options used for creation. Currently, only **title** is supported, for example, **{title: 'testPhoto'}**.

**NOTE**

If a **subtype** option is passed, the configuration does not take effect. Only DEFAULT images can be saved.

The file name must not contain any invalid characters, which are:.. \\ / : \* ? " ' \` < > | { } \[ \]

 |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<string> | Promise used to return the URI of the created image or video asset. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [File Management Error Codes](../../../../../application-framework/core-file-kit/error-codes/file-management-error-codes/document.md).

In API version 13 and earlier versions, if the caller does not have the required permission, error code 13900012 is returned. Starting from API version 14, the same situation raises error code 201.

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 201 | Permission denied. |
| 13900020 | Invalid argument. |
| 14000011 | System inner fail. |

**Example**

For details about how to create a phAccessHelper instance, see the example provided in [photoAccessHelper.getPhotoAccessHelper](../functions/document.md#photoaccesshelpergetphotoaccesshelper).

async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper) {
  console.info('createAssetDemo');
  try {
    let photoType: photoAccessHelper.PhotoType = photoAccessHelper.PhotoType.IMAGE;
    let extension: string = 'jpg';
    let options: photoAccessHelper.CreateOptions = {
      title: 'testPhoto'
    }
    let uri: string = await phAccessHelper.createAsset(photoType, extension, options);
    console.info('createAsset uri' + uri);
    console.info('createAsset successfully');
  } catch (err) {
    console.error(\`createAsset failed, error: ${err.code}, ${err.message}\`);
  }
}

#### getAlbums

getAlbums(type: AlbumType, subtype: AlbumSubtype, options: FetchOptions, callback: AsyncCallback<FetchResult<Album>>): void

Obtains albums based on the specified options and album type. This API uses an asynchronous callback to return the result.

Before the operation, ensure that the albums to obtain exist.

**System capability**: SystemCapability.FileManagement.PhotoAccessHelper.Core

**Required permissions**: ohos.permission.READ\_IMAGEVIDEO

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | [AlbumType](../enums/document.md#albumtype) | Yes | Type of the album. |
| subtype | [AlbumSubtype](../enums/document.md#albumsubtype) | Yes | Subtype of the album. |
| options | [FetchOptions](../interfaces-others/document.md#fetchoptions) | Yes | Retrieval options. |
| callback | AsyncCallback<[FetchResult](../interface-fetchresult/document.md)<[Album](../interface-album/document.md)\>> | Yes | Callback used to return the result. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [File Management Error Codes](../../../../../application-framework/core-file-kit/error-codes/file-management-error-codes/document.md).

In API version 13 and earlier versions, if the caller does not have the required permission, error code 13900012 is returned. Starting from API version 14, the same situation raises error code 201.

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 201 | Permission denied. |
| 13900020 | Invalid argument. |
| 14000011 | System inner fail. |

**Example**

For details about how to create a phAccessHelper instance, see the example provided in [photoAccessHelper.getPhotoAccessHelper](../functions/document.md#photoaccesshelpergetphotoaccesshelper).

import { dataSharePredicates } from '@kit.ArkData';

async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper) {
  // Obtain the album named newAlbumName.
  console.info('getAlbumsDemo');
  let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
  predicates.equalTo('album\_name', 'newAlbumName');
  let fetchOptions: photoAccessHelper.FetchOptions = {
    fetchColumns: \[\],
    predicates: predicates
  };
  phAccessHelper.getAlbums(photoAccessHelper.AlbumType.USER, photoAccessHelper.AlbumSubtype.USER\_GENERIC, fetchOptions, async (err, fetchResult) => {
    if (err) {
      console.error(\`getAlbumsCallback failed with err: ${err.code}, ${err.message}\`);
      return;
    }
    if (fetchResult === undefined) {
      console.error('getAlbumsCallback fetchResult is undefined');
      return;
    }
    let album = await fetchResult.getFirstObject();
    console.info('getAlbumsCallback successfully, albumName: ' + album.albumName);
    fetchResult.close();
  });
}

#### getAlbums

getAlbums(type: AlbumType, subtype: AlbumSubtype, callback: AsyncCallback<FetchResult<Album>>): void

Obtains albums by type. This API uses an asynchronous callback to return the result.

Before the operation, ensure that the albums to obtain exist.

**System capability**: SystemCapability.FileManagement.PhotoAccessHelper.Core

**Required permissions**: ohos.permission.READ\_IMAGEVIDEO

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | [AlbumType](../enums/document.md#albumtype) | Yes | Type of the album. |
| subtype | [AlbumSubtype](../enums/document.md#albumsubtype) | Yes | Subtype of the album. |
| callback | AsyncCallback<[FetchResult](../interface-fetchresult/document.md)<[Album](../interface-album/document.md)\>> | Yes | Callback used to return the result. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [File Management Error Codes](../../../../../application-framework/core-file-kit/error-codes/file-management-error-codes/document.md).

In API version 13 and earlier versions, if the caller does not have the required permission, error code 13900012 is returned. Starting from API version 14, the same situation raises error code 201.

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 201 | Permission denied. |
| 13900020 | Invalid argument. |
| 14000011 | System inner fail. |

**Example**

For details about how to create a phAccessHelper instance, see the example provided in [photoAccessHelper.getPhotoAccessHelper](../functions/document.md#photoaccesshelpergetphotoaccesshelper).

async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper) {
  // Obtain the system album VIDEO, which is preset by default.
  console.info('getAlbumsDemo');
  phAccessHelper.getAlbums(photoAccessHelper.AlbumType.SYSTEM, photoAccessHelper.AlbumSubtype.VIDEO, async (err, fetchResult) => {
    if (err) {
      console.error(\`getAlbumsCallback failed with err: ${err.code}, ${err.message}\`);
      return;
    }
    if (fetchResult === undefined) {
      console.error('getAlbumsCallback fetchResult is undefined');
      return;
    }
    let album: photoAccessHelper.Album = await fetchResult.getFirstObject();
    console.info('getAlbumsCallback successfully, albumUri: ' + album.albumUri);
    fetchResult.close();
  });
}

#### getAlbums

getAlbums(type: AlbumType, subtype: AlbumSubtype, options?: FetchOptions): Promise<FetchResult<Album>>

Obtains albums based on the specified options and album type. This API uses a promise to return the result.

Before the operation, ensure that the albums to obtain exist.

**System capability**: SystemCapability.FileManagement.PhotoAccessHelper.Core

**Required permissions**: ohos.permission.READ\_IMAGEVIDEO

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | [AlbumType](../enums/document.md#albumtype) | Yes | Type of the album. |
| subtype | [AlbumSubtype](../enums/document.md#albumsubtype) | Yes | Subtype of the album. |
| options | [FetchOptions](../interfaces-others/document.md#fetchoptions) | No | Retrieval options. If this parameter is not specified, the albums are obtained based on the album type by default. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[FetchResult](../interface-fetchresult/document.md)<[Album](../interface-album/document.md)\>> | Promise used to return the result. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [File Management Error Codes](../../../../../application-framework/core-file-kit/error-codes/file-management-error-codes/document.md).

If error code 13900012 is returned, follow the instructions provided in [Before You Start](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/photoaccesshelper-preparation).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 201 | Permission denied. |
| 13900020 | Invalid argument. |
| 14000011 | System inner fail. |

**Example**

For details about how to create a phAccessHelper instance, see the example provided in [photoAccessHelper.getPhotoAccessHelper](../functions/document.md#photoaccesshelpergetphotoaccesshelper).

import { dataSharePredicates } from '@kit.ArkData';
import { BusinessError } from '@kit.BasicServicesKit';

async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper) {
  // Obtain the album named newAlbumName.
  console.info('getAlbumsDemo');
  let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
  predicates.equalTo('album\_name', 'newAlbumName');
  let fetchOptions: photoAccessHelper.FetchOptions = {
    fetchColumns: \[\],
    predicates: predicates
  };
  phAccessHelper.getAlbums(photoAccessHelper.AlbumType.USER, photoAccessHelper.AlbumSubtype.USER\_GENERIC, fetchOptions).then( async (fetchResult) => {
    if (fetchResult === undefined) {
      console.error('getAlbumsPromise fetchResult is undefined');
      return;
    }
    let album: photoAccessHelper.Album = await fetchResult.getFirstObject();
    console.info('getAlbumsPromise successfully, albumName: ' + album.albumName);
    fetchResult.close();
  }).catch((err: BusinessError) => {
    console.error(\`getAlbumsPromise failed with err: ${err.code}, ${err.message}\`);
  });
}

#### registerChange

registerChange(uri: string, forChildUris: boolean, callback: Callback<ChangeData>) : void

Registers listening for the specified URI. This API uses a callback to return the result.

**System capability**: SystemCapability.FileManagement.PhotoAccessHelper.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| uri | string | Yes | URI of the photo asset, URI of the album, or [DefaultChangeUri](../enums/document.md#defaultchangeuri). |
| forChildUris | boolean | Yes | 
Whether to perform fuzzy listening.

If **uri** is the URI of an album, the value **true** means to listen for the changes of the files in the album; the value **false** means to listen for the changes of the album only.

If **uri** is the URI of a photoAsset, there is no difference between **true** and false for **forChildUris**.

If **uri** is **DefaultChangeUri**, **forChildUris** must be set to **true**. If **forChildUris** is false, the URI cannot be found and no message can be received.

 |
| callback | Callback<[ChangeData](../interfaces-others/document.md#changedata)\> | Yes | Callback used to return [ChangeData](../interfaces-others/document.md#changedata). **NOTE**: Multiple callback listeners can be registered for a URI. You can use [unRegisterChange](#unregisterchange) to unregister all listeners for the URI or a specified callback listener. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [File Management Error Codes](../../../../../application-framework/core-file-kit/error-codes/file-management-error-codes/document.md).

If error code 13900012 is returned, follow the instructions provided in [Before You Start](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/photoaccesshelper-preparation).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 13900012 | Permission denied. |
| 13900020 | Invalid argument. |

**Example**

For details about how to create a phAccessHelper instance, see the example provided in [photoAccessHelper.getPhotoAccessHelper](../functions/document.md#photoaccesshelpergetphotoaccesshelper).

import { dataSharePredicates } from '@kit.ArkData';

async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper, context: Context) {
  console.info('registerChangeDemo');
  let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
  let fetchOptions: photoAccessHelper.FetchOptions = {
    fetchColumns: \[\],
    predicates: predicates
  };
  let fetchResult: photoAccessHelper.FetchResult<photoAccessHelper.PhotoAsset> = await phAccessHelper.getAssets(fetchOptions);
  let photoAsset: photoAccessHelper.PhotoAsset = await fetchResult.getFirstObject();
  if (photoAsset !== undefined) {
    console.info('photoAsset.displayName : ' + photoAsset.displayName);
  }
  let onCallback1 = (changeData: photoAccessHelper.ChangeData) => {
      console.info('onCallback1 success, changData: ' + JSON.stringify(changeData));
    // file had changed, do something.
  }
  let onCallback2 = (changeData: photoAccessHelper.ChangeData) => {
      console.info('onCallback2 success, changData: ' + JSON.stringify(changeData));
    // file had changed, do something.
  }
  // Register onCallback1.
  phAccessHelper.registerChange(photoAsset.uri, false, onCallback1);
  // Register onCallback2.
  phAccessHelper.registerChange(photoAsset.uri, false, onCallback2);

  await photoAccessHelper.MediaAssetChangeRequest.deleteAssets(context, \[photoAsset\]);
}

#### unRegisterChange

unRegisterChange(uri: string, callback?: Callback<ChangeData>): void

Unregisters listening for the specified URI. Multiple callbacks can be registered for a URI for listening. You can use this API to unregister the listening of the specified callbacks or all callbacks.

**System capability**: SystemCapability.FileManagement.PhotoAccessHelper.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| uri | string | Yes | URI of the photo asset, URI of the album, or [DefaultChangeUri](../enums/document.md#defaultchangeuri). |
| callback | Callback<[ChangeData](../interfaces-others/document.md#changedata)\> | No | Callback to unregister. If this parameter is not specified, all the callbacks for listening for the URI will be canceled. **NOTE**: The specified callback unregistered will not be invoked when the data changes. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [File Management Error Codes](../../../../../application-framework/core-file-kit/error-codes/file-management-error-codes/document.md).

If error code 13900012 is returned, follow the instructions provided in [Before You Start](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/photoaccesshelper-preparation).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 13900012 | Permission denied. |
| 13900020 | Invalid argument. |

**Example**

For details about how to create a phAccessHelper instance, see the example provided in [photoAccessHelper.getPhotoAccessHelper](../functions/document.md#photoaccesshelpergetphotoaccesshelper).

import { dataSharePredicates } from '@kit.ArkData';

async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper, context: Context) {
  console.info('offDemo');
  let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
  let fetchOptions: photoAccessHelper.FetchOptions = {
    fetchColumns: \[\],
    predicates: predicates
  };
  let fetchResult: photoAccessHelper.FetchResult<photoAccessHelper.PhotoAsset> = await phAccessHelper.getAssets(fetchOptions);
  let photoAsset: photoAccessHelper.PhotoAsset = await fetchResult.getFirstObject();
  if (photoAsset !== undefined) {
    console.info('photoAsset.displayName : ' + photoAsset.displayName);
  }
  let onCallback1 = (changeData: photoAccessHelper.ChangeData) => {
    console.info('onCallback1 on');
  }
  let onCallback2 = (changeData: photoAccessHelper.ChangeData) => {
    console.info('onCallback2 on');
  }
  // Register onCallback1.
  phAccessHelper.registerChange(photoAsset.uri, false, onCallback1);
  // Register onCallback2.
  phAccessHelper.registerChange(photoAsset.uri, false, onCallback2);
  // Unregister the listening of onCallback1.
  phAccessHelper.unRegisterChange(photoAsset.uri, onCallback1);
  await photoAccessHelper.MediaAssetChangeRequest.deleteAssets(context, \[photoAsset\]);
}

#### applyChanges11+

applyChanges(mediaChangeRequest: MediaChangeRequest): Promise<void>

Applies media changes. This API uses a promise to return the result.

**Required permissions**: ohos.permission.WRITE\_IMAGEVIDEO

If you do not have the **ohos.permission.WRITE\_IMAGEVIDEO** permission, you can create a media asset by using a security component or an authorization pop-up. For details, see [Saving Media Assets](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/photoaccesshelper-savebutton).

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.FileManagement.PhotoAccessHelper.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| mediaChangeRequest | [MediaChangeRequest](../interfaces-others/document.md#mediachangerequest11) | Yes | Request for asset changes or album changes. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [File Management Error Codes](../../../../../application-framework/core-file-kit/error-codes/file-management-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 14000011 | System inner fail. |

**Example**

This API depends on the [MediaChangeRequest](../interfaces-others/document.md#mediachangerequest11) object. For details about the sample code, see the examples of [MediaAssetChangeRequest](../class-mediaassetchangerequest/document.md) and [MediaAlbumChangeRequest](../class-mediaalbumchangerequest/document.md).

#### release

release(callback: AsyncCallback<void>): void

Releases the **PhotoAccessHelper** instance. This API uses an asynchronous callback to return the result.

Call this API when the APIs of the PhotoAccessHelper instance are no longer used.

**System capability**: SystemCapability.FileManagement.PhotoAccessHelper.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [File Management Error Codes](../../../../../application-framework/core-file-kit/error-codes/file-management-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 13900020 | Invalid argument. |
| 14000011 | System inner fail. |

**Example**

For details about how to create a phAccessHelper instance, see the example provided in [photoAccessHelper.getPhotoAccessHelper](../functions/document.md#photoaccesshelpergetphotoaccesshelper).

async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper) {
  console.info('releaseDemo');
  phAccessHelper.release((err) => {
    if (err !== undefined) {
      console.error(\`release failed. error: ${err.code}, ${err.message}\`);
    } else {
      console.info('release ok.');
    }
  });
}

#### release

release(): Promise<void>

Releases the **PhotoAccessHelper** instance. This API uses a promise to return the result.

Call this API when the APIs of the PhotoAccessHelper instance are no longer used.

**System capability**: SystemCapability.FileManagement.PhotoAccessHelper.Core

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [File Management Error Codes](../../../../../application-framework/core-file-kit/error-codes/file-management-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 13900020 | Invalid argument. |
| 14000011 | System inner fail. |

**Example**

For details about how to create a phAccessHelper instance, see the example provided in [photoAccessHelper.getPhotoAccessHelper](../functions/document.md#photoaccesshelpergetphotoaccesshelper).

async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper) {
  console.info('releaseDemo');
  try {
    await phAccessHelper.release();
    console.info('release ok.');
  } catch (err) {
    console.error(\`release failed. error: ${err.code}, ${err.message}\`);
  }
}

#### showAssetsCreationDialog12+

showAssetsCreationDialog(srcFileUris: Array<string>, photoCreationConfigs: Array<PhotoCreationConfig>): Promise<Array<string>>

Displays a dialog box for the user to confirm whether to save the images or videos. If the user agrees to save the images or videos, this API returns a list of URIs that have been created and granted save permissions (this list is permanent), and the application can use these URIs to write the images or videos. If the user declines to save the images or videos, this API returns an empty list.

The dialog box must display the application name, but this cannot be directly obtained. Therefore, before calling this API, ensure that the **label** and **icon** items are configured in the **abilities** tag in the [module.json5 configuration file](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/module-configuration-file). Note that the icon is not affected by the **icon** item in the **abilities** tag and cannot be modified.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/65/v3/ebYLDVRTTX-JmXf4G82BKQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062443Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7FFA2CAAC9F879A40A71C5701EC6FD498C80A0932158BCC47B7F0569404B690C)

If the passed URI is a sandbox path, images or videos can be saved but cannot be previewed.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.FileManagement.PhotoAccessHelper.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| srcFileUris | Array<string> | Yes | 
[URIs](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/user-file-uri-intro#media-file-uri) of the images or videos to be saved to the media library.

**NOTE**

\- A maximum of 100 images can be saved at a time.

\- Only image and video URIs are supported.

\- URIs cannot be manually constructed. You must call APIs to obtain them. For details, see [Obtaining a Media File URI](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/user-file-uri-intro#obtaining-a-media-file-uri).

 |
| photoCreationConfigs | Array<[PhotoCreationConfig](../interfaces-others/document.md#photocreationconfig12)\> | Yes | 

Configuration for saving the images or videos, including the file names. The value must be consistent with that of **srcFileUris**.

**NOTE**

If a **subtype** option is passed, the configuration does not take effect. Only DEFAULT images can be saved.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<Array<string>> | 
Promise used to return a URI list. The URIs are granted with the permission for the application to write data. If the URIs fail to be generated, a batch creation error code will be returned.

The return values are as follows:

\- **\-3006**: Invalid characters, which are not allowed.

\-**\-2004**: The image type does not match the file name extension.

\-**\-203**: Invalid file operation.

 |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [File Management Error Codes](../../../../../application-framework/core-file-kit/error-codes/file-management-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 14000011 | Internal system error. |

**Example**

For details about how to create a phAccessHelper instance, see the example provided in [photoAccessHelper.getPhotoAccessHelper](../functions/document.md#photoaccesshelpergetphotoaccesshelper).

import { dataSharePredicates } from '@kit.ArkData';

async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper) {
  console.info('ShowAssetsCreationDialogDemo.');

  try {
    // Obtain the sandbox URIs of the images or videos to be saved to the media library.
    let srcFileUris: Array<string> = \[
      'file://fileUriDemo1' // The URI here is an example only.
    \];
    let photoCreationConfigs: Array<photoAccessHelper.PhotoCreationConfig> = \[
      {
        title: 'test2', // Optional.
        fileNameExtension: 'jpg',
        photoType: photoAccessHelper.PhotoType.IMAGE,
        subtype: photoAccessHelper.PhotoSubtype.DEFAULT, // This parameter is optional.
      }
    \];
    let desFileUris: Array<string> = await phAccessHelper.showAssetsCreationDialog(srcFileUris, photoCreationConfigs);
    console.info('showAssetsCreationDialog success, data is ' + desFileUris);
  } catch (err) {
    console.error('showAssetsCreationDialog failed, errCode is ' + err.code + ', errMsg is ' + err.message);
  }
}

#### createAssetWithShortTermPermission12+

createAssetWithShortTermPermission(photoCreationConfig: PhotoCreationConfig): Promise<string>

Creates an asset with a temporary permission of the given period. When this API is called by an application for the first time, a dialog box will be displayed for the user to confirm whether to save the asset. If the user agrees to save the asset, the asset instance will be created and the file URI granted with the save permission will be returned. The application can write the asset based on the URI.

Within 5 minutes after the user agrees to save the asset, if the same application calls this API again, the authorized URI can be automatically returned without the need to display the confirmation dialog box. Exiting the application will terminate the authorization, and the user will need to re-trigger the pop-up dialog for authorization confirmation when the application is re-launched.

**System capability**: SystemCapability.FileManagement.PhotoAccessHelper.Core

**Required permissions**: ohos.permission.SHORT\_TERM\_WRITE\_IMAGEVIDEO

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| photoCreationConfig | [PhotoCreationConfig](../interfaces-others/document.md#photocreationconfig12); | Yes | 
Configuration for saving a media asset (image or video) to the media library, including the file name.

**NOTE**

If a **subtype** option is passed, the configuration does not take effect. Only DEFAULT images can be saved.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<string> | 
Promise used to return the URI of the asset saved. The URIs are granted with the permission for the application to write data. If the URIs fail to be generated, a batch creation error code will be returned.

The error code **\-3006** means that there are invalid characters; **\-2004** means that the image type does not match the file name extension; **\-203** means that the file operation is abnormal.

 |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [File Management Error Codes](../../../../../application-framework/core-file-kit/error-codes/file-management-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 14000011 | Internal system error |

**Example**

For details about how to create a phAccessHelper instance, see the example provided in [photoAccessHelper.getPhotoAccessHelper](../functions/document.md#photoaccesshelpergetphotoaccesshelper).

import { fileIo } from '@kit.CoreFileKit';

async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper) {
    console.info('createAssetWithShortTermPermissionDemo.');
    
    try {
        let photoCreationConfig: photoAccessHelper.PhotoCreationConfig = {
            title: '123456',
            fileNameExtension: 'jpg',
            photoType: photoAccessHelper.PhotoType.IMAGE,
            subtype: photoAccessHelper.PhotoSubtype.DEFAULT,
        };

        let resultUri: string = await phAccessHelper.createAssetWithShortTermPermission(photoCreationConfig);
        let resultFile: fileIo.File = fileIo.openSync(resultUri, fileIo.OpenMode.READ\_WRITE);
        // Use the actual URI and file size.
        let srcFile:  fileIo.File = fileIo.openSync("file://test.jpg", fileIo.OpenMode.READ\_ONLY);
        let bufSize: number = 2000000;
        let readSize: number = 0;
        let buf = new ArrayBuffer(bufSize);
        let readLen = fileIo.readSync(srcFile.fd, buf, {
            offset: readSize,
            length: bufSize
        });
        if (readLen > 0) {
            readSize += readLen;
            fileIo.writeSync(resultFile.fd, buf, { length: readLen });
        }
        fileIo.closeSync(srcFile);
        fileIo.closeSync(resultFile);
    } catch (err) {
        console.error('createAssetWithShortTermPermission failed, errCode is ' + err.code + ', errMsg is ' + err.message);
    }
    
}

#### requestPhotoUrisReadPermission14+

requestPhotoUrisReadPermission(srcFileUris: Array<string>): Promise<Array<string>>

For a switching from HarmonyOS 3.1/4.0 to HarmonyOS 5.0, Grants the read permission for unauthorized URIs, returning a list of URIs that have been created and granted the permission.

**Atomic service API**: This API can be used in atomic services since API version 14.

**System capability**: SystemCapability.FileManagement.PhotoAccessHelper.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| srcFileUris | Array<string> | Yes | 
[URIs](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/user-file-uri-intro#media-file-uri) of the images or videos to be granted with the permission.

**NOTE**

Only image and video URIs are supported, and the maximum number of URIs is 100.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<Array<string>> | Promise used to return the URIs granted with the permission. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [File Management Error Codes](../../../../../application-framework/core-file-kit/error-codes/file-management-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 14000011 | Internal system error |

**Example**

For details about how to create a phAccessHelper instance, see the example provided in [photoAccessHelper.getPhotoAccessHelper](../functions/document.md#photoaccesshelpergetphotoaccesshelper).

import { dataSharePredicates } from '@kit.ArkData';

async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper, context: Context) {
  console.info('requestPhotoUrisReadPermissionDemo.');

  try {
    // Obtain the URIs of the images or videos to be granted with the permission.
    let srcFileUris: Array<string> = \[
      'file://fileUriDemo1' // The URI here is an example only.
    \];
    let desFileUris: Array<string> = await phAccessHelper.requestPhotoUrisReadPermission(srcFileUris);
    console.info('requestPhotoUrisReadPermission success, data is ' + desFileUris);
  } catch (err) {
    console.error('requestPhotoUrisReadPermission failed, errCode is ' + err.code + ', errMsg is ' + err.message);
  }
}

#### getSupportedPhotoFormats18+

getSupportedPhotoFormats(photoType: PhotoType): Promise<Array<string>>

Obtains the list of image or video file name extensions supported by the media library.

**System capability**: SystemCapability.FileManagement.PhotoAccessHelper.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| photoType | [PhotoType](../enums/document.md#phototype) | Yes | Type of the file. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<Array<string>> | Promise used to return an array of the supported image or video file name extensions. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [File Management Error Codes](../../../../../application-framework/core-file-kit/error-codes/file-management-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 14000011 | Internal system error. It is recommended to retry and check the logs. |

**Example**

For details about how to create a phAccessHelper instance, see the example provided in [photoAccessHelper.getPhotoAccessHelper](../functions/document.md#photoaccesshelpergetphotoaccesshelper).

async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper, photoTypeNumber: number){
  console.info('getSupportedPhotoFormatsDemo.');

  try {
    let outputText: string;
    if (photoTypeNumber !== photoAccessHelper.PhotoType.IMAGE && photoTypeNumber !== photoAccessHelper.PhotoType.VIDEO) {
      outputText = 'Does not support querying formats other than images or videos';
      return;
    }
    outputText = 'The supported types are:\\n';
    let imageFormat  = await phAccessHelper.getSupportedPhotoFormats(photoAccessHelper.PhotoType.IMAGE);
    let result = "";
    for (let i = 0; i < imageFormat.length; i++) {
      result += imageFormat\[i\];
      if (i !== imageFormat.length - 1) {
        result += ', ';
      }
    }
    outputText += result;
    console.info('getSupportedPhotoFormats success, data is ' + outputText);
  } catch (error) {
    console.error('getSupportedPhotoFormats failed, errCode is', error);
  }
}

#### on('photoChange')20+

on(type: 'photoChange', callback: Callback<PhotoAssetChangeInfos>): void

Registers a listener for the **'photoChange'** event to monitor media asset changes. This API uses a callback to return the result, and it accepts multiple callbacks.

**Required permissions**: ohos.permission.READ\_IMAGEVIDEO

**System capability**: SystemCapability.FileManagement.PhotoAccessHelper.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The value is fixed at **'photoChange'**. After the registration is complete, any change to the media assets is returned through the callback. |
| callback | Callback<[PhotoAssetChangeInfos](../interfaces-others/document.md#photoassetchangeinfos20)\> | Yes | 
Callback used to return the media asset information after change, which is [PhotoAssetChangeInfos](../interfaces-others/document.md#photoassetchangeinfos20).

**NOTE**

You can register multiple listeners using this API, and you can call [off('photoChange')](#offphotochange20) to unregister all listeners or a specific one.

 |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [Media Library Error Codes](../../../error-codes/media-library-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 23800151 | 
The scenario parameter verification fails.

Possible causes: 1. The type is not fixed at 'photoChange'; 2. The same callback is registered repeatedly.

 |
| 23800301 | 

Internal system error. You are advised to retry and check the logs.

Possible causes: 1. The database is corrupted. 2. The file system is abnormal. 3. The IPC request timed out.

 |

**Example**

For details about how to create a phAccessHelper instance, see the example provided in [photoAccessHelper.getPhotoAccessHelper](../functions/document.md#photoaccesshelpergetphotoaccesshelper).

import { dataSharePredicates } from '@kit.ArkData'

let onCallback1 = (changeData: photoAccessHelper.PhotoAssetChangeInfos) => {
    console.info('onCallback1 success, changData: ' + JSON.stringify(changeData));
  // file had changed, do something.
}
let onCallback2 = (changeData: photoAccessHelper.PhotoAssetChangeInfos) => {
    console.info('onCallback2 success, changData: ' + JSON.stringify(changeData));
  // file had changed, do something.
}

async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper, context: Context){
  console.info('onPhotoChangeDemo.');

  try {
    // Register onCallback1.
    phAccessHelper.on('photoChange', onCallback1);
    // Register onCallback2.
    phAccessHelper.on('photoChange', onCallback2);
  } catch (error) {
    console.error('onPhotoChangeDemo failed, errCode is', error);
  }
}

#### off('photoChange')20+

off(type: 'photoChange', callback?: Callback<PhotoAssetChangeInfos>): void

Unregisters the listener for the **'photoChange'** event to stop monitoring media asset changes. If multiple listeners are registered, you can unregister a specific listener by specifying **callback**. Alternatively, you can unregister all of them without specifying **callback**.

**Required permissions**: ohos.permission.READ\_IMAGEVIDEO

**System capability**: SystemCapability.FileManagement.PhotoAccessHelper.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The value is fixed at **'photoChange'**. After the unregistration is complete, any change to the media assets is no longer returned through the callback. |
| callback | Callback<[PhotoAssetChangeInfos](../interfaces-others/document.md#photoassetchangeinfos20)\> | No | 
Exact callback you previously registered with [on('photoChange')](#onphotochange20). If this parameter is left unspecified, all listeners for the **'photoChange'** event are unregistered.

**NOTE**

Once a specific callback is unregistered, it will not be invoked when a media asset changes.

 |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [Media Library Error Codes](../../../error-codes/media-library-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 23800151 | 
The scenario parameter verification fails.

Possible causes: 1. The type is not fixed at 'photoChange'; 2. The same callback is unregistered repeatedly.

 |
| 23800301 | 

Internal system error. You are advised to retry and check the logs.

Possible causes: 1. The database is corrupted. 2. The file system is abnormal. 3. The IPC request timed out.

 |

**Example**

For details about how to create a phAccessHelper instance, see the example provided in [photoAccessHelper.getPhotoAccessHelper](../functions/document.md#photoaccesshelpergetphotoaccesshelper).

import { dataSharePredicates } from '@kit.ArkData'

let onCallback1 = (changeData: photoAccessHelper.PhotoAssetChangeInfos) => {
    console.info('onCallback1 success, changData: ' + JSON.stringify(changeData));
  // file had changed, do something.
}
let onCallback2 = (changeData: photoAccessHelper.PhotoAssetChangeInfos) => {
    console.info('onCallback2 success, changData: ' + JSON.stringify(changeData));
  // file had changed, do something.
}

async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper, context: Context){
  console.info('offPhotoChangeDemo.');

  try {
    // Register onCallback1.
    phAccessHelper.on('photoChange', onCallback1);
    // Register onCallback2.
    phAccessHelper.on('photoChange', onCallback2);

    // Unregister the listening of onCallback1.
    phAccessHelper.off('photoChange', onCallback1);
  } catch (error) {
    console.error('offPhotoChangeDemo failed, errCode is', error);
  }
}

#### on('photoAlbumChange')20+

on(type: 'photoAlbumChange', callback: Callback<AlbumChangeInfos>): void

Registers a listener for the **'photoAlbumChange'** event to monitor album changes. This API uses a callback to return the result, and it accepts multiple callbacks.

**Required permissions**: ohos.permission.READ\_IMAGEVIDEO

**System capability**: SystemCapability.FileManagement.PhotoAccessHelper.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The value is fixed at **'photoAlbumChange'**. After the registration is complete, any change to the albums is returned through the callback. |
| callback | Callback<[AlbumChangeInfos](../interfaces-others/document.md#albumchangeinfos20)\> | Yes | 
Callback used to return the album information after change, which is [AlbumChangeInfos](../interfaces-others/document.md#albumchangeinfos20).

**NOTE**

You can register multiple listeners using this API, and you can call [off('photoAlbumChange')](#offphotoalbumchange20) to unregister all listeners or a specific one.

 |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [Media Library Error Codes](../../../error-codes/media-library-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 23800151 | 
The scenario parameter verification fails.

Possible causes: 1. The type is not fixed at 'photoAlbumChange'; 2. The same callback is registered repeatedly.

 |
| 23800301 | 

Internal system error. You are advised to retry and check the logs.

Possible causes: 1. The database is corrupted. 2. The file system is abnormal. 3. The IPC request timed out.

 |

**Example**

For details about how to create a phAccessHelper instance, see the example provided in [photoAccessHelper.getPhotoAccessHelper](../functions/document.md#photoaccesshelpergetphotoaccesshelper).

import { dataSharePredicates } from '@kit.ArkData'

let onCallback1 = (changeData: photoAccessHelper.AlbumChangeInfos) => {
    console.info('onCallback1 success, changData: ' + JSON.stringify(changeData));
  // file had changed, do something.
}
let onCallback2 = (changeData: photoAccessHelper.AlbumChangeInfos) => {
    console.info('onCallback2 success, changData: ' + JSON.stringify(changeData));
  // file had changed, do something.
}

async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper, context: Context){
  console.info('onPhotoAlbumChangeDemo.');

  try {
    // Register onCallback1.
    phAccessHelper.on('photoAlbumChange', onCallback1);
    // Register onCallback2.
    phAccessHelper.on('photoAlbumChange', onCallback2);
  } catch (error) {
    console.error('onPhotoAlbumChangeDemo failed, errCode is', error);
  }
}

#### off('photoAlbumChange')20+

off(type: 'photoAlbumChange', callback?: Callback<AlbumChangeInfos>): void

Unregisters a listener for the **'photoAlbumChange'** event to stop monitoring album changes. If multiple listeners are registered, you can unregister a specific listener by specifying **callback**. Alternatively, you can unregister all of them without specifying **callback**.

**Required permissions**: ohos.permission.READ\_IMAGEVIDEO

**System capability**: SystemCapability.FileManagement.PhotoAccessHelper.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The value is fixed at **'photoAlbumChange'**. After the unregistration is complete, any change to the albums is no longer returned through the callback. |
| callback | Callback<[AlbumChangeInfos](../interfaces-others/document.md#albumchangeinfos20)\> | No | 
Exact callback you previously registered with [on('photoAlbumChange')](#onphotoalbumchange20). If this parameter is left unspecified, all listeners for the **'photoAlbumChange'** event are unregistered.

**NOTE**

Once a specific callback is unregistered, it will not be invoked when an album changes.

 |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [Media Library Error Codes](../../../error-codes/media-library-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 23800151 | 
The scenario parameter verification fails.

Possible causes: 1. The type is not fixed at 'photoAlbumChange'; 2. The same callback is unregistered repeatedly.

 |
| 23800301 | 

Internal system error. You are advised to retry and check the logs.

Possible causes: 1. The database is corrupted. 2. The file system is abnormal. 3. The IPC request timed out.

 |

**Example**

For details about how to create a phAccessHelper instance, see the example provided in [photoAccessHelper.getPhotoAccessHelper](../functions/document.md#photoaccesshelpergetphotoaccesshelper).

import { dataSharePredicates } from '@kit.ArkData'

let onCallback1 = (changeData: photoAccessHelper.AlbumChangeInfos) => {
    console.info('onCallback1 success, changData: ' + JSON.stringify(changeData));
  // file had changed, do something.
}
let onCallback2 = (changeData: photoAccessHelper.AlbumChangeInfos) => {
    console.info('onCallback2 success, changData: ' + JSON.stringify(changeData));
  // file had changed, do something.
}

async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper, context: Context){
  console.info('onPhotoAlbumChangeDemo.');

  try {
    // Register onCallback1.
    phAccessHelper.on('photoAlbumChange', onCallback1);
    // Register onCallback2.
    phAccessHelper.on('photoAlbumChange', onCallback2);

    // Unregister the listening of onCallback1.
    phAccessHelper.off('photoAlbumChange', onCallback1);
  } catch (error) {
    console.error('onPhotoAlbumChangeDemo failed, errCode is', error);
  }
}

#### getPhotoPickerComponentDefaultAlbumName20+

getPhotoPickerComponentDefaultAlbumName(): Promise<string>

Obtains the name of the album that the **PhotoPickerComponent** shows by default. The name string is localized to match the current system language. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.FileManagement.PhotoAccessHelper.Core

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<string> | Promise used to return the name of the default album. |

**Error codes**

For details about the error codes, see [File Management Error Codes](../../../../../application-framework/core-file-kit/error-codes/file-management-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 23800301 | Internal system error. It is recommended to retry and check the logs. Possible causes: 1. The IPC request timed out. 2. system running error. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
import {photoAccessHelper} from '@kit.MediaLibraryKit';

async function example(context: Context) {
  console.info('getPhotoPickerComponentDefaultAlbumNameDemo');
  let phAccessHelper: photoAccessHelper.PhotoAccessHelper = photoAccessHelper.getPhotoAccessHelper(context);

  phAccessHelper.getPhotoPickerComponentDefaultAlbumName().then((defaultAlbumName) => {
    console.info('getPhotoPickerComponentDefaultAlbumName success, defaultAlbumName is ' + defaultAlbumName);
  }).catch((err: BusinessError) => {
    console.error(\`getPhotoPickerComponentDefaultAlbumName failed with error: ${err.code}, ${err.message}\`);
  });
}

#### createDeleteRequest(deprecated)

createDeleteRequest(uriList: Array<string>, callback: AsyncCallback<void>): void

Creates a dialog box for deleting media files. This API uses an asynchronous callback to return the result. The deleted media files are moved to the trash.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a6/v3/UpQubG7wQOqe5Tq9Q8mskg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062443Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E78C9671922FD5B4B40188B908C477B348C04288D10F3E4C6BC9C945E2B6457E)

This API is supported since API version 10 and deprecated since API version 11. You are advised to use [MediaAssetChangeRequest.deleteAssets](../class-mediaassetchangerequest/document.md#deleteassets11-1) instead.

**Required permissions**: ohos.permission.WRITE\_IMAGEVIDEO

**System capability**: SystemCapability.FileManagement.PhotoAccessHelper.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| uriList | Array<string> | Yes | URIs of the media files to delete. A maximum of 300 media files can be deleted. |
| callback | AsyncCallback<void> | Yes | Callback that returns no value. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [File Management Error Codes](../../../../../application-framework/core-file-kit/error-codes/file-management-error-codes/document.md).

If error code 13900012 is returned, follow the instructions provided in [Before You Start](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/photoaccesshelper-preparation).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 13900012 | Permission denied. |
| 13900020 | Invalid argument. |
| 14000011 | System inner fail. |

**Example**

For details about how to create a phAccessHelper instance, see the example provided in [photoAccessHelper.getPhotoAccessHelper](../functions/document.md#photoaccesshelpergetphotoaccesshelper).

import { dataSharePredicates } from '@kit.ArkData';

async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper) {
  console.info('createDeleteRequestDemo');
  let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
  let fetchOptions: photoAccessHelper.FetchOptions = {
    fetchColumns: \[\],
    predicates: predicates
  };
  try {
    let fetchResult: photoAccessHelper.FetchResult<photoAccessHelper.PhotoAsset> = await phAccessHelper.getAssets(fetchOptions);
    let asset: photoAccessHelper.PhotoAsset = await fetchResult.getFirstObject();
    if (asset === undefined) {
      console.error('asset not exist');
      return;
    }
    phAccessHelper.createDeleteRequest(\[asset.uri\], (err) => {
      if (err === undefined) {
        console.info('createDeleteRequest successfully');
      } else {
        console.error(\`createDeleteRequest failed with error: ${err.code}, ${err.message}\`);
      }
    });
  } catch (err) {
    console.error(\`fetch failed, error: ${err.code}, ${err.message}\`);
  }
}

#### createDeleteRequest(deprecated)

createDeleteRequest(uriList: Array<string>): Promise<void>

Creates a dialog box for deleting media files. This API uses a promise to return the result. The deleted media files are moved to the trash.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f0/v3/7WzfcD5aRcWq5-1lo87cSw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062443Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=40C5B00179737DA521249291E910A337E240E4263709615A6B7B9D811DB07D41)

This API is supported since API version 10 and deprecated since API version 11. You are advised to use [MediaAssetChangeRequest.deleteAssets](../class-mediaassetchangerequest/document.md#deleteassets11-1) instead.

**Required permissions**: ohos.permission.WRITE\_IMAGEVIDEO

**System capability**: SystemCapability.FileManagement.PhotoAccessHelper.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| uriList | Array<string> | Yes | URIs of the media files to delete. A maximum of 300 media files can be deleted. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [File Management Error Codes](../../../../../application-framework/core-file-kit/error-codes/file-management-error-codes/document.md).

If error code 13900012 is returned, follow the instructions provided in [Before You Start](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/photoaccesshelper-preparation).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 13900012 | Permission denied. |
| 13900020 | Invalid argument. |
| 14000011 | System inner fail. |

**Example**

For details about how to create a phAccessHelper instance, see the example provided in [photoAccessHelper.getPhotoAccessHelper](../functions/document.md#photoaccesshelpergetphotoaccesshelper).

import { dataSharePredicates } from '@kit.ArkData';

async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper) {
  console.info('createDeleteRequestDemo');
  let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
  let fetchOptions: photoAccessHelper.FetchOptions = {
    fetchColumns: \[\],
    predicates: predicates
  };
  try {
    let fetchResult: photoAccessHelper.FetchResult<photoAccessHelper.PhotoAsset> = await phAccessHelper.getAssets(fetchOptions);
    let asset: photoAccessHelper.PhotoAsset = await fetchResult.getFirstObject();
    if (asset === undefined) {
      console.error('asset not exist');
      return;
    }
    await phAccessHelper.createDeleteRequest(\[asset.uri\]);
    console.info('createDeleteRequest successfully');
  } catch (err) {
    console.error(\`createDeleteRequest failed with error: ${err.code}, ${err.message}\`);
  }
}

#### getRecentPhotoInfo20+

getRecentPhotoInfo(options?: RecentPhotoOptions): Promise<RecentPhotoInfo>

Obtains the information about the recent image or video when the application uses the **RecentPhotoComponent** to view recent images or videos. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.FileManagement.PhotoAccessHelper.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| options | [RecentPhotoOptions](../classes-others/document.md#recentphotooptions20) | No | 
Options for retrieving the recent image or video. If this parameter is not specified, the latest image is retrieved according to the creation time.

If this parameter is specified, it must match the **options** configuration in the **RecentPhotoComponent**. Otherwise, there may be discrepancies where the API finds a recent image or video but the component does not.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[RecentPhotoInfo](../classes-others/document.md#recentphotoinfo20)\> | Promise used to return the information about the recent image or video. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
import { photoAccessHelper, PhotoSource, RecentPhotoOptions} from '@kit.MediaLibraryKit';

async function example(context: Context) {
  console.info('getRecentPhotoInfoDemo');
  let phAccessHelper: photoAccessHelper.PhotoAccessHelper = photoAccessHelper.getPhotoAccessHelper(context);
  let recentPhotoOptions: RecentPhotoOptions = {
    period: 60 \* 60,
    MIMEType: photoAccessHelper.PhotoViewMIMETypes.IMAGE\_VIDEO\_TYPE,
    photoSource: PhotoSource.ALL
  }

  phAccessHelper.getRecentPhotoInfo(recentPhotoOptions).then((recentPhotoInfo) => {
    console.info('getRecentPhotoInfo success, recentPhotoInfo is ' + JSON.stringify(recentPhotoInfo));
  }).catch((err: BusinessError) => {
    console.error(\`getRecentPhotoInfo failed with error: ${err.code}, ${err.message}\`);
  });
}

#### getAlbumIdByLpath22+

getAlbumIdByLpath(lpath: string): Promise<number>

Obtains the album ID in the media library based on the album's virtual path. This API uses a promise to return the result.

This API supports the following albums: camera application album (**/DCIM/Camera**), screenshot application album (**/Pictures/Screenshots**), and screen recording application album (**/Pictures/Screenrecords**).

​**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.FileManagement.PhotoAccessHelper.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| lpath | string | Yes | Virtual path of the album. The value can contain a maximum of 255 characters. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<number> | Promise used to return the album ID. |

**Error codes**

For details about the error codes, see [Media Library Error Codes](../../../error-codes/media-library-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 23800151 | The lpath is invalid, such as null, undefined and empty. |
| 23800301 | Internal system error. You are advised to retry and check the logs. Possible causes: 1. The database is corrupted. 2. The file system is abnormal. 3. The IPC request timed out. |

**Example**

For details about how to create a phAccessHelper instance, see the example provided in [photoAccessHelper.getPhotoAccessHelper](../functions/document.md#photoaccesshelpergetphotoaccesshelper).

async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper) {
  console.info('getAlbumIdByLpath');

  try {
      let albumId: number = await phAccessHelper.getAlbumIdByLpath('testLpath');
      console.info('requestFile:: albumId: ', albumId);

      console.info('getAlbumIdByLpath completed.');
      console.info(\`albumId : ${albumId}\`);
    } catch (err) {
      console.error(\`getAlbumIdByLpath failed: ${err.code}, ${err.message}\`);
    }
}
