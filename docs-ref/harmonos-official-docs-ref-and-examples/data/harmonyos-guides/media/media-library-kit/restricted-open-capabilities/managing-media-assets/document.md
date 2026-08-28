# Managing Media Assets

Applications can call photoAccessHelper APIs to manage media assets (images and videos).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/85/v3/mcLA68NeRsCRi3nGEq6HqA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062044Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=42012E494F029533A49229E94CE771706292DA151C7FD04198172868C85869EF)

-   Before you get started, obtain a PhotoAccessHelper instance and apply for required permissions. For details, see [Before You Start](../before-you-start/document.md).
-   Unless otherwise specified, the PhotoAccessHelper instance obtained in [Before You Start](../before-you-start/document.md) is used to call photoAccessHelper APIs. If the code for obtaining the PhotoAccessHelper instance is missing, an error will be reported to indicate that photoAccessHelper is not defined.

To ensure application running efficiency, most PhotoAccessHelper APIs are asynchronously implemented in callback or promise mode. The following example uses the promise function. For more methods, see [Module Description](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-photoaccesshelper).

#### Obtaining Media Assets

You can obtain media assets based on the specified conditions, such as the media type, date, or album name.

Use [PhotoAccessHelper.getAssets](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-photoaccesshelper-photoaccesshelper#getassets-1) with the [FetchOptions](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-photoaccesshelper-i#fetchoptions) object to specify the search criteria. Unless otherwise specified, all the media assets to be obtained in this document exist in the database. If no media asset is obtained, check whether the media assets exist in the database.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5a/v3/2GGK9Ra6Rt-G1t2WQTQyMQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062044Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C1863118B51C6E144D7C538CFC80EB3AA86D16FEA7FAFD5893822688B9F0240B)

When [PhotoAccessHelper.PhotoKeys](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-photoaccesshelper-e#photokeys) is used as the search criterion, only the [DataSharePredicates.equalTo](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-data-datasharepredicates#equalto10) API is supported.

To obtain the object at the specified position (for example, the first one, the last one, or the one with the specified index) in the result set, use [FetchResult](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-photoaccesshelper-fetchresult).

**Prerequisites**

-   A PhotoAccessHelper instance is obtained.
-   Request the **ohos.permission.READ\_IMAGEVIDEO** permission. For details, see [Requesting Permissions](../before-you-start/document.md#requesting-permissions).
-   The [dataSharePredicates](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-data-datasharepredicates) module is imported.

## Obtaining an Image or Video by Name

The following example describes how to obtain the image **test.jpg**.

import { dataSharePredicates } from '@kit.ArkData';
import { photoAccessHelper } from '@kit.MediaLibraryKit';

async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper) {
  let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
  predicates.equalTo(photoAccessHelper.PhotoKeys.DISPLAY\_NAME, 'test.jpg');
  let fetchOptions: photoAccessHelper.FetchOptions = {
    fetchColumns: \[\],
    predicates: predicates
  };
  try {
    let fetchResult: photoAccessHelper.FetchResult<photoAccessHelper.PhotoAsset> = await phAccessHelper.getAssets(fetchOptions);
    let photoAsset: photoAccessHelper.PhotoAsset = await fetchResult.getFirstObject();
    console.info('getAssets photoAsset.displayName : ' + photoAsset.displayName);
    fetchResult.close();
  } catch (err) {
    console.error('getAssets failed with err: ' + err);
  }
}

#### Obtaining an Image or Video Thumbnail

To display images and videos in Gallery or to preview edits, applications must obtain image and video thumbnails.

The thumbnails offer a quick preview on images and videos. You can use [PhotoAsset.getThumbnail](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-photoaccesshelper-photoasset#getthumbnail-2) with the thumbnail size specified to obtain the image or video thumbnail.

**Prerequisites**

-   A PhotoAccessHelper instance is obtained.
-   Request the **ohos.permission.READ\_IMAGEVIDEO** permission. For details, see [Requesting Permissions](../before-you-start/document.md#requesting-permissions).
-   The [dataSharePredicates](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-data-datasharepredicates) module is imported.

For example, obtain the file descriptor (FD) of an image, and decode the image into a PixelMap for display or processing. For details, see [Image Decoding](../../../image-kit/image-development-arkts/image-decoding/using-imagesource-to-decode-images/document.md).

Example: Obtain the thumbnail at the size of 720 x 720 of an image.

**How to Develop**

1.  Set the fetch options.
2.  Call [PhotoAccessHelper.getAssets](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-photoaccesshelper-photoaccesshelper#getassets-1) to obtain image assets.
3.  Call [FetchResult.getFirstObject](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-photoaccesshelper-fetchresult#getfirstobject-1) to obtain the first image from the result set.
4.  Call **PhotoAsset.getThumbnail** to obtain the [PixelMap](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-image-pixelmap) of the thumbnail of the image.

import { dataSharePredicates } from '@kit.ArkData';
import { image } from '@kit.ImageKit';
import { photoAccessHelper } from '@kit.MediaLibraryKit';

async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper) {
  let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
  let fetchOptions: photoAccessHelper.FetchOptions = {
    fetchColumns: \[\],
    predicates: predicates
  };

  try {
    let fetchResult: photoAccessHelper.FetchResult<photoAccessHelper.PhotoAsset> = await phAccessHelper.getAssets(fetchOptions);
    let photoAsset: photoAccessHelper.PhotoAsset = await fetchResult.getFirstObject();
    console.info('getAssets photoAsset.displayName : ' + photoAsset.displayName);
    let size: image.Size = { width: 720, height: 720 };
    let pixelMap: image.PixelMap =  await photoAsset.getThumbnail(size);
    let imageInfo: image.ImageInfo = await pixelMap.getImageInfo()
    console.info('getThumbnail successful, pixelMap ImageInfo size: ' + JSON.stringify(imageInfo.size));
    fetchResult.close();
  } catch (err) {
    console.error('getThumbnail failed with err: ' + err);
  }
}

#### Renaming a Media Asset

To rename a media asset, change the **PhotoAsset.displayName** attribute, that is, the file name (including the file name extension) displayed.

Use [MediaAssetChangeRequest.setTitle](https://developer.huawei.com/consumer/en/doc/harmonyos-references/kts-apis-photoaccesshelper-mediaassetchangerequest#settitle11) to set the new name, and then use [PhotoAccessHelper.applyChanges](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-photoaccesshelper-photoaccesshelper#applychanges11) to apply the changes to the database.

Use [FetchResult](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-photoaccesshelper-fetchresult) to obtain the file to rename.

**Prerequisites**

-   A PhotoAccessHelper instance is obtained.
-   Request the **ohos.permission.WRITE\_IMAGEVIDEO** and **ohos.permission.READ\_IMAGEVIDEO** permissions. For details, see [Requesting Permissions](../before-you-start/document.md#requesting-permissions).

The following example describes how to rename an image named **oldTestPhoto**.

**How to Develop**

1.  Set the fetch options.
2.  Call [PhotoAccessHelper.getAssets](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-photoaccesshelper-photoaccesshelper#getassets-1) to obtain image assets.
3.  Call [FetchResult.getFirstObject](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-photoaccesshelper-fetchresult#getfirstobject-1) to obtain the image asset to rename.
4.  Call [MediaAssetChangeRequest.setTitle](https://developer.huawei.com/consumer/en/doc/harmonyos-references/kts-apis-photoaccesshelper-mediaassetchangerequest#settitle11) to rename the image.
5.  Call [PhotoAccessHelper.applyChanges](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-photoaccesshelper-photoaccesshelper#applychanges11) to save the modification to the database.

import { dataSharePredicates } from '@kit.ArkData';
import { photoAccessHelper } from '@kit.MediaLibraryKit';

async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper) {
  let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
  predicates.equalTo(photoAccessHelper.PhotoKeys.TITLE, 'oldTestPhoto')
  let fetchOptions: photoAccessHelper.FetchOptions = {
    fetchColumns: \['title'\],
    predicates: predicates
  };
  let newTitle: string = 'newTestPhoto';

  try {
    let fetchResult: photoAccessHelper.FetchResult<photoAccessHelper.PhotoAsset> = await phAccessHelper.getAssets(fetchOptions);
    let photoAsset: photoAccessHelper.PhotoAsset = await fetchResult.getFirstObject();
    let assetChangeRequest: photoAccessHelper.MediaAssetChangeRequest = new photoAccessHelper.MediaAssetChangeRequest(photoAsset);
    assetChangeRequest.setTitle(newTitle);
    await phAccessHelper.applyChanges(assetChangeRequest);
    fetchResult.close();
  } catch (err) {
    console.error(\`rename failed with error: ${err.code}, ${err.message}\`);
  }
}

#### Moving a Media Asset to the Trash

You can use [MediaAssetChangeRequest.deleteAssets](https://developer.huawei.com/consumer/en/doc/harmonyos-references/kts-apis-photoaccesshelper-mediaassetchangerequest#deleteassets11) to move files to the trash.

The file moved to the trash will be retained for 30 days before being deleted permanently. Before a file is deleted permanently from the trash, the user can restore it using the system application **Files** or **Gallery**.

**Prerequisites**

-   A PhotoAccessHelper instance is obtained.
-   Request the **ohos.permission.WRITE\_IMAGEVIDEO** and **ohos.permission.READ\_IMAGEVIDEO** permissions. For details, see [Requesting Permissions](../before-you-start/document.md#requesting-permissions).

Example: Move the first file in the result set to the trash.

**How to Develop**

1.  Set the fetch options.
2.  Call [PhotoAccessHelper.getAssets](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-photoaccesshelper-photoaccesshelper#getassets-1) to obtain image assets.
3.  Call [FetchResult.getFirstObject](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-photoaccesshelper-fetchresult#getfirstobject-1) to obtain the first image.
4.  Call [MediaAssetChangeRequest.deleteAssets](https://developer.huawei.com/consumer/en/doc/harmonyos-references/kts-apis-photoaccesshelper-mediaassetchangerequest#deleteassets11) to move the image to the trash.

import { dataSharePredicates } from '@kit.ArkData';
import { photoAccessHelper } from '@kit.MediaLibraryKit';

async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper, context: Context) {
  let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
  let fetchOptions: photoAccessHelper.FetchOptions = {
    fetchColumns: \[\],
    predicates: predicates
  };

  try {
    let fetchResult: photoAccessHelper.FetchResult<photoAccessHelper.PhotoAsset> = await phAccessHelper.getAssets(fetchOptions);
    let photoAsset: photoAccessHelper.PhotoAsset = await fetchResult.getFirstObject();
    await photoAccessHelper.MediaAssetChangeRequest.deleteAssets(context, \[photoAsset\]);
    fetchResult.close();
  } catch (err) {
    console.error(\`deleteAssets failed with error: ${err.code}, ${err.message}\`);
  }
}
