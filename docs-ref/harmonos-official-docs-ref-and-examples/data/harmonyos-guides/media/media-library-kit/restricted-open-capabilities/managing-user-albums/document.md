# Managing User Albums

**photoAccessHelper** provides APIs for managing user albums, including querying and renaming albums, as well as adding and deleting images and videos within albums.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f3/v3/57umM5wVS1uHeSi9K98MQQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062044Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=DCBF744512A232361B421C12669681FD5EE29BF7D79DCF66473C651027382A6A)

Before you get started, obtain a PhotoAccessHelper instance and apply for required permissions. For details, see [Before You Start](../before-you-start/document.md).

Unless otherwise specified, the PhotoAccessHelper instance obtained in [Before You Start](../before-you-start/document.md) is used to call photoAccessHelper APIs. If the code for obtaining the PhotoAccessHelper instance is missing, an error will be reported to indicate that photoAccessHelper is not defined.

To ensure application running efficiency, most PhotoAccessHelper APIs are asynchronously implemented in callback or promise mode. The following examples of asynchronous API calls use the promise function. For more methods, see [Module Description](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-photoaccesshelper).

Unless otherwise specified, all the media assets to be obtained in this document exist in the database. If no media asset is obtained when the sample code is executed, check whether the media assets exist in the database.

#### Obtaining a User Album

Use [PhotoAccessHelper.getAlbums](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-photoaccesshelper-photoaccesshelper#getalbums-2) to obtain user albums.

**Prerequisites**

-   A PhotoAccessHelper instance is obtained.
-   Request the **ohos.permission.READ\_IMAGEVIDEO** permission. For details, see [Requesting Permissions](../before-you-start/document.md#requesting-permissions).

The following example describes how to obtain the user album **albumName**.

**How to Develop**

1.  Set **fetchOptions** for obtaining the user album.
2.  Call **PhotoAccessHelper.getAlbums** to obtain user albums.
3.  Call [FetchResult.getFirstObject](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-photoaccesshelper-fetchresult#getfirstobject-1) to obtain the first user album.

import { dataSharePredicates } from '@kit.ArkData';
import { photoAccessHelper } from '@kit.MediaLibraryKit';

async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper) {
  let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
  let albumName: photoAccessHelper.AlbumKeys = photoAccessHelper.AlbumKeys.ALBUM\_NAME;
  predicates.equalTo(albumName, 'albumName');
  let fetchOptions: photoAccessHelper.FetchOptions = {
    fetchColumns: \[\],
    predicates: predicates
  };

  try {
    let fetchResult: photoAccessHelper.FetchResult<photoAccessHelper.Album> = await phAccessHelper.getAlbums(photoAccessHelper.AlbumType.USER, photoAccessHelper.AlbumSubtype.USER\_GENERIC, fetchOptions);
    let album: photoAccessHelper.Album = await fetchResult.getFirstObject();
    console.info('getAlbums successfully, albumName: ' + album.albumName);
    fetchResult.close();
  } catch (err) {
    console.error('getAlbums failed with err: ' + err);
  }
}

#### Renaming a User Album

To rename a user album, modify the **Album.albumName** attribute of the album.

Use [MediaAlbumChangeRequest.setAlbumName](https://developer.huawei.com/consumer/en/doc/harmonyos-references/kts-apis-photoaccesshelper-mediaalbumchangerequest#setalbumname11) to set the new name, and then use [PhotoAccessHelper.applyChanges](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-photoaccesshelper-photoaccesshelper#applychanges11) to apply the changes to the database.

Use [FetchResult](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-photoaccesshelper-fetchresult) to obtain the user album to rename.

The new user album names must meet the following requirements:

-   The total length of the album name must be between 1 and 255 characters.
-   It must not contain any invalid characters, which are:
    
    . \\ / : \* ? " ' \` < > | { } \[ \]
    
-   The album name is case-insensitive.
-   Duplicate album names are not allowed.

**Prerequisites**

-   A PhotoAccessHelper instance is obtained.
-   Request the **ohos.permission.READ\_IMAGEVIDEO** and **ohos.permission.WRITE\_IMAGEVIDEO** permissions. For details, see [Requesting Permissions](../before-you-start/document.md#requesting-permissions).

The following example describes how to rename the user album **albumName**.

**How to Develop**

1.  Set **fetchOptions** for obtaining the user album.
2.  Call **PhotoAccessHelper.getAlbums** to obtain user albums.
3.  Call [FetchResult.getFirstObject](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-photoaccesshelper-fetchresult#getfirstobject-1) to obtain the first user album.
4.  Call **MediaAlbumChangeRequest.setAlbumName** to set a new album name.
5.  Call **PhotoAccessHelper.applyChanges** to save the new album name to the database.

import { dataSharePredicates } from '@kit.ArkData';
import { photoAccessHelper } from '@kit.MediaLibraryKit';

async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper) {
  let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
  let albumName: photoAccessHelper.AlbumKeys = photoAccessHelper.AlbumKeys.ALBUM\_NAME;
  predicates.equalTo(albumName, 'albumName');
  let fetchOptions: photoAccessHelper.FetchOptions = {
    fetchColumns: \[\],
    predicates: predicates
  };

  try {
    let fetchResult: photoAccessHelper.FetchResult<photoAccessHelper.Album> = await phAccessHelper.getAlbums(photoAccessHelper.AlbumType.USER, photoAccessHelper.AlbumSubtype.USER\_GENERIC, fetchOptions);
    let album: photoAccessHelper.Album = await fetchResult.getFirstObject();
    console.info('getAlbums successfully, albumName: ' + album.albumName);
    let albumChangeRequest: photoAccessHelper.MediaAlbumChangeRequest = new photoAccessHelper.MediaAlbumChangeRequest(album);
    let newAlbumName: string = 'newAlbumName';
    albumChangeRequest.setAlbumName(newAlbumName);
    await phAccessHelper.applyChanges(albumChangeRequest);
    console.info('setAlbumName successfully, new albumName: ' + album.albumName);
    fetchResult.close();
  } catch (err) {
    console.error('setAlbumName failed with err: ' + err);
  }
}

#### Adding Images or Videos to a User Album

[Obtain the user album](#obtaining-a-user-album) and the images or videos to be added to the user album, and then call [MediaAlbumChangeRequest.addAssets](https://developer.huawei.com/consumer/en/doc/harmonyos-references/kts-apis-photoaccesshelper-mediaalbumchangerequest#addassets11) and [PhotoAccessHelper.applyChanges](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-photoaccesshelper-photoaccesshelper#applychanges11) to add the images or videos to the user album.

**Prerequisites**

-   A PhotoAccessHelper instance is obtained.
-   Request the **ohos.permission.READ\_IMAGEVIDEO** and **ohos.permission.WRITE\_IMAGEVIDEO** permissions. For details, see [Requesting Permissions](../before-you-start/document.md#requesting-permissions).

The following example describes how to add an image to the user album **albumName**.

**How to Develop**

1.  Set **albumFetchOptions** for obtaining the user album.
2.  Set **photoFetchOptions** for obtaining the image.
3.  Call **PhotoAccessHelper.getAlbums** to obtain user albums.
4.  Call [FetchResult.getFirstObject](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-photoaccesshelper-fetchresult#getfirstobject) to obtain the first user album.
5.  Call [PhotoAccessHelper.getAssets](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-photoaccesshelper-photoaccesshelper#getassets) to obtain image assets.
6.  Call [FetchResult.getFirstObject](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-photoaccesshelper-fetchresult#getfirstobject) to obtain the first image from the result set.
7.  Call **MediaAlbumChangeRequest.addAssets** to add the image to the user album.
8.  Call **PhotoAccessHelper.applyChanges** to apply the changes.

import { dataSharePredicates } from '@kit.ArkData';
import { photoAccessHelper } from '@kit.MediaLibraryKit';

async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper) {
  let albumPredicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
  let albumName: photoAccessHelper.AlbumKeys = photoAccessHelper.AlbumKeys.ALBUM\_NAME;
  albumPredicates.equalTo(albumName, 'albumName');
  let albumFetchOptions: photoAccessHelper.FetchOptions = {
    fetchColumns: \[\],
    predicates: albumPredicates
  };

  let photoPredicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
  let photoFetchOptions: photoAccessHelper.FetchOptions = {
    fetchColumns: \[\],
    predicates: photoPredicates
  };

  try {
    let albumFetchResult: photoAccessHelper.FetchResult<photoAccessHelper.Album> = await phAccessHelper.getAlbums(photoAccessHelper.AlbumType.USER, photoAccessHelper.AlbumSubtype.USER\_GENERIC, albumFetchOptions);
    let album: photoAccessHelper.Album = await albumFetchResult.getFirstObject();
    console.info('getAlbums successfully, albumName: ' + album.albumName);
    let photoFetchResult: photoAccessHelper.FetchResult<photoAccessHelper.PhotoAsset> = await phAccessHelper.getAssets(photoFetchOptions);
    let photoAsset: photoAccessHelper.PhotoAsset = await photoFetchResult.getFirstObject();
    console.info('getAssets successfully, albumName: ' + photoAsset.displayName);
    let albumChangeRequest: photoAccessHelper.MediaAlbumChangeRequest = new photoAccessHelper.MediaAlbumChangeRequest(album);
    albumChangeRequest.addAssets(\[photoAsset\]);
    await phAccessHelper.applyChanges(albumChangeRequest);
    console.info('succeed to add ' + photoAsset.displayName + ' to ' + album.albumName);
    albumFetchResult.close();
    photoFetchResult.close();
  } catch (err) {
    console.error('addAssets failed with err: ' + err);
  }
}

#### Obtaining Images and Videos in a User Album

[Obtain the user album](#obtaining-a-user-album), and call [Album.getAssets](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-photoaccesshelper-absalbum#getassets-1) to obtain the assets in the user album.

**Prerequisites**

-   A PhotoAccessHelper instance is obtained.
-   Request the **ohos.permission.READ\_IMAGEVIDEO** and **ohos.permission.WRITE\_IMAGEVIDEO** permissions. For details, see [Requesting Permissions](../before-you-start/document.md#requesting-permissions).

The following example describes how to obtain an image in the user album **albumName**.

**How to Develop**

1.  Set **albumFetchOptions** for obtaining the user album.
2.  Set **photoFetchOptions** for obtaining the image.
3.  Call **PhotoAccessHelper.getAlbums** to obtain user albums.
4.  Call [FetchResult.getFirstObject](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-photoaccesshelper-fetchresult#getfirstobject-1) to obtain the first user album.
5.  Call **Album.getAssets** to obtain the media assets in the user album.
6.  Call [FetchResult.getFirstObject](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-photoaccesshelper-fetchresult#getfirstobject-1) to obtain the first image from the result set.

import { dataSharePredicates } from '@kit.ArkData';
import { photoAccessHelper } from '@kit.MediaLibraryKit';

async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper) {
  let albumPredicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
  let albumName: photoAccessHelper.AlbumKeys = photoAccessHelper.AlbumKeys.ALBUM\_NAME;
  albumPredicates.equalTo(albumName, 'albumName');
  let albumFetchOptions: photoAccessHelper.FetchOptions = {
    fetchColumns: \[\],
    predicates: albumPredicates
  };

  let photoPredicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
  let photoFetchOptions: photoAccessHelper.FetchOptions = {
    fetchColumns: \[\],
    predicates: photoPredicates
  };

  try {
    let albumFetchResult: photoAccessHelper.FetchResult<photoAccessHelper.Album> = await phAccessHelper.getAlbums(photoAccessHelper.AlbumType.USER, photoAccessHelper.AlbumSubtype.USER\_GENERIC, albumFetchOptions);
    let album: photoAccessHelper.Album = await albumFetchResult.getFirstObject();
    console.info('getAlbums successfully, albumName: ' + album.albumName);
    let photoFetchResult = await album.getAssets(photoFetchOptions);
    let photoAsset = await photoFetchResult.getFirstObject();
    console.info('album getAssets successfully, albumName: ' + photoAsset.displayName);
    albumFetchResult.close();
    photoFetchResult.close();
  } catch (err) {
    console.error('album getAssets failed with err: ' + err);
  }
}

#### Removing Images and Videos from a User Album

[Obtain the user album](#obtaining-a-user-album), and call [Album.getAssets](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-photoaccesshelper-absalbum#getassets-1) to obtain the assets in the user album.

Select the assets to remove, and use [MediaAlbumChangeRequest.removeAssets](https://developer.huawei.com/consumer/en/doc/harmonyos-references/kts-apis-photoaccesshelper-mediaalbumchangerequest#removeassets11) and [PhotoAccessHelper.applyChanges](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-photoaccesshelper-photoaccesshelper#applychanges11) to remove the selected media assets.

**Prerequisites**

-   A PhotoAccessHelper instance is obtained.
-   Request the **ohos.permission.READ\_IMAGEVIDEO** and **ohos.permission.WRITE\_IMAGEVIDEO** permissions. For details, see [Requesting Permissions](../before-you-start/document.md#requesting-permissions).

The following example describes how to remove an image from the user album **albumName**.

**How to Develop**

1.  Set **albumFetchOptions** for obtaining the user album.
2.  Set **photoFetchOptions** for obtaining the image.
3.  Call **PhotoAccessHelper.getAlbums** to obtain user albums.
4.  Call [FetchResult.getFirstObject](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-photoaccesshelper-fetchresult#getfirstobject-1) to obtain the first user album.
5.  Call **Album.getAssets** to obtain the media assets.
6.  Call [FetchResult.getFirstObject](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-photoaccesshelper-fetchresult#getfirstobject-1) to obtain the first image from the result set.
7.  Call **MediaAlbumChangeRequest.removeAssets** to remove the image from the user album.
8.  Call **PhotoAccessHelper.applyChanges** to apply the changes.

import { dataSharePredicates } from '@kit.ArkData';
import { photoAccessHelper } from '@kit.MediaLibraryKit';

async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper) {
  let albumPredicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
  let albumName: photoAccessHelper.AlbumKeys = photoAccessHelper.AlbumKeys.ALBUM\_NAME;
  albumPredicates.equalTo(albumName, 'albumName');
  let albumFetchOptions: photoAccessHelper.FetchOptions = {
    fetchColumns: \[\],
    predicates: albumPredicates
  };

  let photoPredicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
  let photoFetchOptions: photoAccessHelper.FetchOptions = {
    fetchColumns: \[\],
    predicates: photoPredicates
  };

  try {
    let albumFetchResult: photoAccessHelper.FetchResult<photoAccessHelper.Album> = await phAccessHelper.getAlbums(photoAccessHelper.AlbumType.USER, photoAccessHelper.AlbumSubtype.USER\_GENERIC, albumFetchOptions);
    let album: photoAccessHelper.Album = await albumFetchResult.getFirstObject();
    if (album === undefined) {
      console.error('album is undefined');
      albumFetchResult.close();
      return;
    }
    console.info('getAlbums successfully, albumName: ' + album.albumName);
    let photoFetchResult = await album.getAssets(photoFetchOptions);
    let photoAsset = await photoFetchResult.getFirstObject();
    if (photoAsset === undefined) {
      console.error('photoAsset is undefined');
      photoFetchResult.close();
      return;
    }
    console.info('album getAssets successfully, albumName: ' + photoAsset.displayName);
    let albumChangeRequest: photoAccessHelper.MediaAlbumChangeRequest = new photoAccessHelper.MediaAlbumChangeRequest(album);
    albumChangeRequest.removeAssets(\[photoAsset\]);
    await phAccessHelper.applyChanges(albumChangeRequest);
    console.info('succeed to remove ' + photoAsset.displayName + ' from ' + album.albumName);
    albumFetchResult.close();
    photoFetchResult.close();
  } catch (err) {
    console.error('removeAssets failed with err: ' + err);
  }
}
