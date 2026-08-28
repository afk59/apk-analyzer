# User File URI

As a unique identifier of a user file, the uniform resource identifier (URI) is usually used to specify the user file to be accessed or modified. Avoid using part of a URI for service code development.

#### URI Types

URIs can be classified into the following types:

-   Document URI: URI of a file selected or saved by the file manager started by picker, or obtained via the **fileAccess** module. For details, see [Obtaining a Document URI](#obtaining-a-document-uri).
-   Media file URI: URI of an image or video selected from **Gallery** by picker; URI of an image or video obtained via the **photoAccessHelper** module; URI of an image, video, or audio file obtained via the **userFileManager** module. For details, see [Obtaining a Media File URI](#obtaining-a-media-file-uri).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8b/v3/I56XxptkRPOj4Ada7pquCQ/en-us_image_0000002537765046.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061951Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=92DE7F4D434F2A08E7B5BEBE476499FB9CC8DE71C851D6211FB14602B9B17E18)

#### Document URI

## Overview

The document URIs are in the following format:

'file://docs/storage/Users/currentUser/<relative\_path>/test.txt'

The following table describes the fields in a document URI.

| URI Field | Description |
| :-- | :-- |
| 'file://docs/storage/Users/currentUser/' | Root directory of the file manager. |
| '<relative\_path>/' | Relative path of the file, for example, **Download/** and **Documents/**. |
| 'test.txt' | Name of the file stored in the user file system. The supported file types vary depending on the file manager used. Common file types include TXT, JPG, MP4, and MP3. |

## Obtaining a Document URI

1.  Call **select()** or **save()** of [DocumentViewPicker](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-file-picker#documentviewpicker) to select or save a document.
    
2.  Call **select()** or **save()** of [AudioViewPicker](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-file-picker#audioviewpicker) to select or save an audio file.
    

## Using a Document URI

Applications of the normal APL can call [@ohos.file.fs](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-file-fs) APIs only to access files based on document URIs. For details about the sample code, see [Selecting Documents](../selecting-and-saving-user-files/selecting-user-files/document.md#selecting-documents) and [Saving Documents](../selecting-and-saving-user-files/saving-user-files/document.md#saving-documents).

#### Media File URI

## Overview

The URI format varies depending on the media file type.

Image URI format:

-   'file://media/Photo/<id>/IMG\_datetime\_0001/displayName.jpg'

Video URI format:

-   'file://media/Photo/<id>/VID\_datetime\_0001/displayName.mp4'

Audio URI format:

-   'file://media/Audio/<id>/AUD\_datetime\_0001/displayName.mp3'

The following table describes the fields in a media file URI.

| URI Field | Description |
| :-- | :-- |
| 'file://media' | URI of a media file. |
| 'Photo' | URI of an image or video. |
| 'Audio' | URI of an audio file. |
| '<id>' | ID of the file after being processed in multiple tables in the database. It is not the value in the **file\_id** column in the table. Do not use this ID to query files in the database. |
| 'IMG\_datetime\_0001' | Name of the image stored in the user file system without the file name extension. |
| 'VID\_datetime\_0001' | Name of the video stored in the user file system without the file name extension. |
| 'AUD\_datetime\_0001' | Name of the audio file stored in the user file system without the file name extension. |

## Obtaining a Media File URI

1.  Call [PhotoViewPicker of PhotoAccessHelper](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-photoaccesshelper-photoviewpicker) to select media files. The URIs of the selected files are returned.
    
2.  Call [getAssets](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-photoaccesshelper-photoaccesshelper#getassets) or [createAsset](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-photoaccesshelper-photoaccesshelper#createasset) API in [photoAccessHelper](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-photoaccesshelper) to obtain the URIs of the selected files.
    

## Using a Media File URI

Applications of the normal APL can call [photoAccessHelper](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-photoaccesshelper) APIs to process media files based on their URIs. For details about the sample code, see [Obtaining an Image or Video by URI](../../../../media/media-library-kit/selecting-media-assets-using-picker/document.md#obtaining-an-image-or-video-by-uri). To call the API, the application must have the [ohos.permission.READ\_IMAGEVIDEO](../../../../media/media-library-kit/about-this-kit/document.md#available-capabilities) permission.

If you do not want to request the permission for a normal application, call [PhotoViewPicker of PhotoAccessHelper](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-photoaccesshelper-photoviewpicker) to obtain the file URI and call [photoAccessHelper.getAssets](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-photoaccesshelper-photoaccesshelper#getassets) to obtain the **PhotoAsset** object based on the URI. Based on the **PhotoAsset** object, you can use [getThumbnail](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-photoaccesshelper-photoasset#getthumbnail) to obtain the image thumbnail or use [get](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-photoaccesshelper-photoasset#get) to obtain information from [PhotoKeys](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-photoaccesshelper-e#photokeys).

The following information can be obtained from **PhotoKeys** through temporary authorization:

| Name | Value | Description |
| :-- | :-- | :-- |
| URI | 'uri' | URI of the file. |
| PHOTO\_TYPE | 'media\_type' | Type of the media file. |
| DISPLAY\_NAME | 'display\_name' | File name displayed. |
| SIZE | 'size' | Size of the file. |
| DATE\_ADDED | 'date\_added' | Unix timestamp when the file was added, in seconds. |
| DATE\_MODIFIED | 'date\_modified' | Unix timestamp when the file content (not the file name) was last modified, in seconds. |
| DURATION | 'duration' | Duration, in milliseconds. |
| WIDTH | 'width' | Image width, in pixels. |
| HEIGHT | 'height' | Image height, in pixels. |
| DATE\_TAKEN | 'date\_taken' | Unix timestamp when the photo was taken, in seconds. |
| ORIENTATION | 'orientation' | Orientation of the image file. |
| TITLE | 'title' | Title in the file. |

The following example shows how to obtain the thumbnail and file information based on the media file URI with temporary authorization.

import { BusinessError } from '@kit.BasicServicesKit';
// ···
import { common } from '@kit.AbilityKit';
// ···
import { dataSharePredicates } from '@kit.ArkData';
// ···
import { photoAccessHelper } from '@kit.MediaLibraryKit';

// Define a URI array to receive the URIs returned by PhotoViewPicker.select.
let uris: string\[\] = \[\];

// context is passed by EntryAbility.
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
// ···

// Call PhotoViewPicker.select to select an image.
async function photoPickerGetUri() {
  try {
    let photoSelectOptions = new photoAccessHelper.PhotoSelectOptions();
    photoSelectOptions.MIMEType = photoAccessHelper.PhotoViewMIMETypes.IMAGE\_TYPE;
    // Set the maximum number of images that can be selected to 1.
    photoSelectOptions.maxSelectNumber = 1;
    let photoPicker = new photoAccessHelper.PhotoViewPicker();
    // Wait for the user to select an image.
    let photoSelectResult: photoAccessHelper.PhotoSelectResult = await photoPicker.select(photoSelectOptions);
    console.info('PhotoViewPicker.select successfully, PhotoSelectResult uri: ' + JSON.stringify(photoSelectResult));
    uris = photoSelectResult.photoUris;
  } catch (err) {
    let err: BusinessError = error as BusinessError;
    console.error(\`PhotoViewPicker failed with err, code is ${err.code}, message is ${err.message}\`);
  }
}

async function uriGetAssets(): Promise<string> {
  // Check whether the uris array is empty.
  if (uris.length === 0) {
    throw new Error('No URIs available');
  }
  try {
    let phAccessHelper = photoAccessHelper.getPhotoAccessHelper(context);
    let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
    // Configure search criteria to query the image based on the URI returned by PhotoViewPicker.select.
    predicates.equalTo('uri', uris\[0\]);
    let fetchOption: photoAccessHelper.FetchOptions = {
      fetchColumns: \[photoAccessHelper.PhotoKeys.WIDTH, photoAccessHelper.PhotoKeys.HEIGHT,
        photoAccessHelper.PhotoKeys.TITLE, photoAccessHelper.PhotoKeys.DURATION\],
      predicates: predicates
    };
    let fetchResult: photoAccessHelper.FetchResult<photoAccessHelper.PhotoAsset> =
      await phAccessHelper.getAssets(fetchOption);
    // Obtain the PhotoAsset object corresponding to the URI. The file information is obtained from the PhotoAsset object.
    const asset: photoAccessHelper.PhotoAsset = await fetchResult.getFirstObject();
    console.info('asset displayName: ', asset.displayName);
    console.info('asset uri: ', asset.uri);
    console.info('asset photoType: ', asset.photoType);
    console.info('asset width: ', asset.get(photoAccessHelper.PhotoKeys.WIDTH));
    console.info('asset height: ', asset.get(photoAccessHelper.PhotoKeys.HEIGHT));
    console.info('asset title: ' + asset.get(photoAccessHelper.PhotoKeys.TITLE));
    // Obtain the thumbnail.
    asset.getThumbnail((err, pixelMap) => {
      if (err == undefined) {
        console.info('getThumbnail successful ' + JSON.stringify(pixelMap));
      } else {
        console.error('getThumbnail fail', err);
      }
    });
    // ···
  } catch (error) {
    console.error(\`uriGetAssets failed with err, code is ${error.code}, message is ${error.message}\`);
    return 'ReadMediaUriFail';
  }
  return 'ReadMediaUriFail';
}
