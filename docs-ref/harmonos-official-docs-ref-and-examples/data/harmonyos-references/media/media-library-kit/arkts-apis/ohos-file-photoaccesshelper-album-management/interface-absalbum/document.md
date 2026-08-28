# Interface (AbsAlbum)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/de/v3/XJbgFJSHTNamQopRHr9ddw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062442Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C9578C32CC3E6E5D030BD9F740B60ADDCDDD53A08E8E49CE15A88D4BAD59B587)

The initial APIs of this module are supported since API version 10. Newly added APIs will be marked with a superscript to indicate their earliest API version.

#### Modules to Import

import { photoAccessHelper } from '@kit.MediaLibraryKit';

#### Properties

**System capability**: SystemCapability.FileManagement.PhotoAccessHelper.Core

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| albumType | [AlbumType](../enums/document.md#albumtype) | Yes | No | Type of the album. |
| albumSubtype | [AlbumSubtype](../enums/document.md#albumsubtype) | Yes | No | Subtype of the album. |
| albumName | string | No | No | Name of the album. System albums are not writable, whereas user albums can be written to. |
| albumUri | string | Yes | No | URI of the album. |
| count | number | Yes | No | Number of files in the album. |
| coverUri | string | Yes | No | URI of the cover file of the album. |
| lpath23+ | string | Yes | Yes | Virtual path of the album. |
| changeTime23+ | number | Yes | Yes | Time when the album is changed. |

#### getAssets

getAssets(options: FetchOptions, callback: AsyncCallback<FetchResult<PhotoAsset>>): void

Obtains image and video assets. This API uses an asynchronous callback to return the result.

**Required permissions**: ohos.permission.READ\_IMAGEVIDEO

**System capability**: SystemCapability.FileManagement.PhotoAccessHelper.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| options | [FetchOptions](../interfaces-others/document.md#fetchoptions) | Yes | Retrieval options. |
| callback | AsyncCallback<[FetchResult](../interface-fetchresult/document.md)<[PhotoAsset](../interface-photoasset/document.md)\>> | Yes | Callback function. If files from the album are obtained successfully, **err** is **undefined**, and **data** is the result set of the obtained image and video data ([FetchResult](../interface-fetchresult/document.md)). Otherwise, **err** is an error object. |

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
  console.info('albumGetAssetsDemoCallback');
  let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
  let albumFetchOptions: photoAccessHelper.FetchOptions = {
    fetchColumns: \[\],
    predicates: predicates
  };
  let fetchOption: photoAccessHelper.FetchOptions = {
    fetchColumns: \[\],
    predicates: predicates
  };
  let albumList: photoAccessHelper.FetchResult<photoAccessHelper.Album> = await phAccessHelper.getAlbums(photoAccessHelper.AlbumType.USER, photoAccessHelper.AlbumSubtype.USER\_GENERIC, albumFetchOptions);
  let album: photoAccessHelper.Album = await albumList.getFirstObject();
  album.getAssets(fetchOption, (err, albumFetchResult) => {
    if (albumFetchResult !== undefined) {
      console.info('album getAssets successfully, getCount: ' + albumFetchResult.getCount());
    } else {
      console.error(\`album getAssets failed with error: ${err.code}, ${err.message}\`);
    }
  });
}

#### getAssets

getAssets(options: FetchOptions): Promise<FetchResult<PhotoAsset>>

Obtains image and video assets. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 20.

**Required permissions**: ohos.permission.READ\_IMAGEVIDEO

**System capability**: SystemCapability.FileManagement.PhotoAccessHelper.Core

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
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 201 | Permission denied. |
| 13900020 | Invalid argument. |
| 14000011 | System inner fail. |

**Example**

For details about how to create a phAccessHelper instance, see the example provided in [photoAccessHelper.getPhotoAccessHelper](../functions/document.md#photoaccesshelpergetphotoaccesshelper).

import { dataSharePredicates } from '@kit.ArkData';
import { BusinessError } from '@kit.BasicServicesKit';

async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper) {
  console.info('albumGetAssetsDemoPromise');
  let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
  let albumFetchOptions: photoAccessHelper.FetchOptions = {
    fetchColumns: \[\],
    predicates: predicates
  };
  let fetchOption: photoAccessHelper.FetchOptions = {
    fetchColumns: \[\],
    predicates: predicates
  };
  let albumList: photoAccessHelper.FetchResult<photoAccessHelper.Album> = await phAccessHelper.getAlbums(photoAccessHelper.AlbumType.USER, photoAccessHelper.AlbumSubtype.USER\_GENERIC, albumFetchOptions);
  let album: photoAccessHelper.Album = await albumList.getFirstObject();
  album.getAssets(fetchOption).then((albumFetchResult) => {
    console.info('album getAssets successfully, getCount: ' + albumFetchResult.getCount());
  }).catch((err: BusinessError) => {
    console.error(\`album getAssets failed with error: ${err.code}, ${err.message}\`);
  });
}
