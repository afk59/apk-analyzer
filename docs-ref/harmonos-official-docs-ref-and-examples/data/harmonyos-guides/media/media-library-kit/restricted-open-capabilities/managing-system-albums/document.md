# Managing System Albums

The photoAccessHelper module provides APIs for managing system albums, including **Favorites**, **Videos**, and **Screenshots**.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9f/v3/J9dLUGhWQ7auoxwwPWTNNQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062044Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=BCBE53C23F4A957FCF76B3B3EE9AB19ECB56434A230E3B0140C92490914A03B3)

Before you get started, obtain a PhotoAccessHelper instance and apply for required permissions. For details, see [Before You Start](../before-you-start/document.md).

Unless otherwise specified, the PhotoAccessHelper instance obtained in [Before You Start](../before-you-start/document.md) is used to call photoAccessHelper APIs. If the code for obtaining the PhotoAccessHelper instance is missing, an error will be reported to indicate that photoAccessHelper is not defined.

To ensure application running efficiency, most PhotoAccessHelper APIs are asynchronously implemented in callback or promise mode. The following examples of asynchronous API calls use the promise function. For more methods, see [Module Description](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-photoaccesshelper).

Unless otherwise specified, all the media assets to be obtained in this document exist in the database. If no media asset is obtained when the sample code is executed, check whether the media assets exist in the database.

#### Favorites

**Favorites** is a system album. Favoriting an image or video adds the image or video to **Favorites**; unfavoriting an image or video removes the image or video from **Favorites**.

## Obtaining a Favorites Object

Use [PhotoAccessHelper.getAlbums](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-photoaccesshelper-photoaccesshelper#getalbums-2) to obtain a Favorites object.

**Prerequisites**

-   A PhotoAccessHelper instance is obtained.
-   Request the **ohos.permission.READ\_IMAGEVIDEO** permission. For details, see [Requesting Permissions](../before-you-start/document.md#requesting-permissions).

**How to Develop**

1.  Set the album type to **photoAccessHelper.AlbumType.SYSTEM** and the album subtype to **photoAccessHelper.AlbumSubtype.FAVORITE**.
2.  Call **PhotoAccessHelper.getAlbums** to obtain a Favorites object.

import { photoAccessHelper } from '@kit.MediaLibraryKit';

async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper) {
  try {
    let fetchResult: photoAccessHelper.FetchResult<photoAccessHelper.Album> = await phAccessHelper.getAlbums(photoAccessHelper.AlbumType.SYSTEM, photoAccessHelper.AlbumSubtype.FAVORITE);
    let album: photoAccessHelper.Album = await fetchResult.getFirstObject();
    console.info('get favorite album successfully, albumUri: ' + album.albumUri);
    fetchResult.close();
  } catch (err) {
    console.error('get favorite album failed with err: ' + err);
  }
}

## Obtaining Images and Videos in Favorites

[Obtain a Favorites object](#obtaining-a-favorites-object), and call [Album.getAssets](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-photoaccesshelper-absalbum#getassets-1) to obtain the assets in **Favorites**.

**Prerequisites**

-   A PhotoAccessHelper instance is obtained.
-   Request the **ohos.permission.READ\_IMAGEVIDEO** permission. For details, see [Requesting Permissions](../before-you-start/document.md#requesting-permissions).

Example: Obtain an image from **Favorites**.

**How to Develop**

1.  [Obtain a Favorites object](#obtaining-a-favorites-object).
2.  Set **fetchOptions** for obtaining the image.
3.  Call **Album.getAssets** to obtain image assets.
4.  Call [FetchResult.getFirstObject](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-photoaccesshelper-fetchresult#getfirstobject-1) to obtain the first image from the result set.

import { dataSharePredicates } from '@kit.ArkData';
import { photoAccessHelper } from '@kit.MediaLibraryKit';

async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper) {
  let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
  let fetchOptions: photoAccessHelper.FetchOptions = {
    fetchColumns: \[\],
    predicates: predicates
  };

  try {
    let albumFetchResult: photoAccessHelper.FetchResult<photoAccessHelper.Album> = await phAccessHelper.getAlbums(photoAccessHelper.AlbumType.SYSTEM, photoAccessHelper.AlbumSubtype.FAVORITE);
    let album: photoAccessHelper.Album = await albumFetchResult.getFirstObject();
    console.info('get favorite album successfully, albumUri: ' + album.albumUri);

    let photoFetchResult: photoAccessHelper.FetchResult<photoAccessHelper.PhotoAsset> = await album.getAssets(fetchOptions);
    let photoAsset: photoAccessHelper.PhotoAsset = await photoFetchResult.getFirstObject();
    console.info('favorite album getAssets successfully, photoAsset displayName: ' + photoAsset.displayName);
    photoFetchResult.close();
    albumFetchResult.close();
  } catch (err) {
    console.error('favorite failed with err: ' + err);
  }
}

#### Videos

**Videos** is a system album that holds media assets of the video type in user files.

## Obtaining a Videos Object

Use [PhotoAccessHelper.getAlbums](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-photoaccesshelper-photoaccesshelper#getalbums-2) to obtain a Videos object.

**Prerequisites**

-   A PhotoAccessHelper instance is obtained.
-   Request the **ohos.permission.READ\_IMAGEVIDEO** permission. For details, see [Requesting Permissions](../before-you-start/document.md#requesting-permissions).

**How to Develop**

1.  Set the album type to **photoAccessHelper.AlbumType.SYSTEM** and the album subtype to **photoAccessHelper.AlbumSubtype.VIDEO**.
2.  Use **PhotoAccessHelper.getAlbums** to obtain a Videos object.

import { photoAccessHelper } from '@kit.MediaLibraryKit';

async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper) {
  try {
    let fetchResult: photoAccessHelper.FetchResult<photoAccessHelper.Album> = await phAccessHelper.getAlbums(photoAccessHelper.AlbumType.SYSTEM, photoAccessHelper.AlbumSubtype.VIDEO);
    let album: photoAccessHelper.Album = await fetchResult.getFirstObject();
    console.info('get video album successfully, albumUri: ' + album.albumUri);
    fetchResult.close();
  } catch (err) {
    console.error('get video album failed with err: ' + err);
  }
}

## Obtaining a Video from Videos

[Obtain a Videos object](#obtaining-a-videos-object), and call [Album.getAssets](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-photoaccesshelper-absalbum#getassets-1) to obtain the video assets in the **Videos** album.

**Prerequisites**

-   A PhotoAccessHelper instance is obtained.
-   Request the **ohos.permission.READ\_IMAGEVIDEO** permission. For details, see [Requesting Permissions](../before-you-start/document.md#requesting-permissions).

Example: Obtain a video in **Videos**.

**How to Develop**

1.  [Obtain a Videos object](#obtaining-a-videos-object).
2.  Set **fetchOptions** for obtaining the video.
3.  Call **Album.getAssets** to obtain video assets.
4.  Call [FetchResult.getFirstObject](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-photoaccesshelper-fetchresult#getfirstobject-1) to obtain the first video asset.

import { dataSharePredicates } from '@kit.ArkData';
import { photoAccessHelper } from '@kit.MediaLibraryKit';

async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper) {
  let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
  let fetchOptions: photoAccessHelper.FetchOptions = {
    fetchColumns: \[\],
    predicates: predicates
  };

  try {
    let albumFetchResult: photoAccessHelper.FetchResult<photoAccessHelper.Album> = await phAccessHelper.getAlbums(photoAccessHelper.AlbumType.SYSTEM, photoAccessHelper.AlbumSubtype.VIDEO);
    let album: photoAccessHelper.Album = await albumFetchResult.getFirstObject();
    console.info('get video album successfully, albumUri: ' + album.albumUri);

    let videoFetchResult: photoAccessHelper.FetchResult<photoAccessHelper.PhotoAsset> = await album.getAssets(fetchOptions);
    let photoAsset: photoAccessHelper.PhotoAsset = await videoFetchResult.getFirstObject();
    console.info('video album getAssets successfully, photoAsset displayName: ' + photoAsset.displayName);
    videoFetchResult.close();
    albumFetchResult.close();
  } catch (err) {
    console.error('video failed with err: ' + err);
  }
}
