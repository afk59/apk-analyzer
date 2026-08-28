# Class (PhotoViewPicker)

PhotoViewPicker provides APIs for the user to select images and videos. Before using the APIs of PhotoViewPicker, you need to create a PhotoViewPicker instance.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f0/v3/JmrTSjIuQxq9s4ZSRP5bMA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062442Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7D8266F0B9434B22980609F62C234A6F41FF735B497A220CBF3D93F04B54B9B8)

The initial APIs of this module are supported since API version 10. Newly added APIs will be marked with a superscript to indicate their earliest API version.

#### Modules to Import

import { photoAccessHelper } from '@kit.MediaLibraryKit';

#### select

select(option?: PhotoSelectOptions) : Promise<PhotoSelectResult>

Starts a **photoPicker** page for the user to select one or more images or videos. This API uses a promise to return the result. You can pass in **PhotoSelectOptions** to specify the type and maximum number of the files to select. A **PhotoSelectResult** object is returned.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/45/v3/ONR4yqc9QhipS0i3cYdsKw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062442Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=464D80AC599F063D992B4C132E193E5434E8DC91901E334BE799EB1C9E162774)

**photoUris** in the PhotoSelectResult object returned by this API has permanent authorization and can be used only by calling [photoAccessHelper.getAssets](../interface-photoaccesshelper/document.md#getassets). For details, see [Using a Media File URI](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/user-file-uri-intro#using-a-media-file-uri).

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.FileManagement.PhotoAccessHelper.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| option | [PhotoSelectOptions](../classes-others/document.md#photoselectoptions) | No | Options for selecting files. If this parameter is not specified, up to 50 images and videos are selected by default. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[PhotoSelectResult](../classes-others/document.md#photoselectresult)\> | Promise used to return information about the images or videos selected. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md), [File Management Error Codes](../../../../../application-framework/core-file-kit/error-codes/file-management-error-codes/document.md), and [Media Library Error Codes](../../../error-codes/media-library-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 13900042 | Unknown error. |
| 23800151 | Scene parameters validate failed, possible causes:1. An illegal enumeration value was passed to PhotoSelectOptions.globalMovingPhotoState. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

async function example01(phAccessHelper: photoAccessHelper.PhotoAccessHelper) {
  try {
    let photoSelectOptions = new photoAccessHelper.PhotoSelectOptions();
    photoSelectOptions.MIMEType = photoAccessHelper.PhotoViewMIMETypes.IMAGE\_TYPE;
    photoSelectOptions.maxSelectNumber = 5;
    let photoPicker = new photoAccessHelper.PhotoViewPicker();
    photoPicker.select(photoSelectOptions).then((photoSelectResult: photoAccessHelper.PhotoSelectResult) => {
      console.info('PhotoViewPicker.select successfully, photoSelectResult uri: ' + JSON.stringify(photoSelectResult));
    }).catch((err: BusinessError) => {
      console.error(\`PhotoViewPicker.select failed with err: ${err.code}, ${err.message}\`);
    });
  } catch (error) {
    let err: BusinessError = error as BusinessError;
    console.error(\`PhotoViewPicker failed with err: ${err.code}, ${err.message}\`);
  }
}

#### select

select(option: PhotoSelectOptions, callback: AsyncCallback<PhotoSelectResult>) : void

Starts a **photoPicker** page for the user to select one or more images or videos. This API uses an asynchronous callback to return the result. You can pass in **PhotoSelectOptions** to specify the media file type and the maximum number of files to select.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/13/v3/mLniNvlxSWyDNys0DleL2Q/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062442Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=884FAB41AB34CEF179E46CB1E8B419B3D5A9DF18AAAFAC0C7FAA5A4DD9B0B737)

**photoUris** in the PhotoSelectResult object returned by this API has permanent authorization and can be used only by calling [photoAccessHelper.getAssets](../interface-photoaccesshelper/document.md#getassets). For details, see [Using a Media File URI](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/user-file-uri-intro#using-a-media-file-uri).

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.FileManagement.PhotoAccessHelper.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| option | [PhotoSelectOptions](../classes-others/document.md#photoselectoptions) | Yes | Options for selecting images or videos. |
| callback | AsyncCallback<[PhotoSelectResult](../classes-others/document.md#photoselectresult)\> | Yes | Callback used to return information about the images or videos selected. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md), [File Management Error Codes](../../../../../application-framework/core-file-kit/error-codes/file-management-error-codes/document.md), and [Media Library Error Codes](../../../error-codes/media-library-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 13900042 | Unknown error. |
| 23800151 | Scene parameters validate failed, possible causes:1. An illegal enumeration value was passed to PhotoSelectOptions.globalMovingPhotoState. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

async function example02(phAccessHelper: photoAccessHelper.PhotoAccessHelper) {
  try {
    let photoSelectOptions = new photoAccessHelper.PhotoSelectOptions();
    photoSelectOptions.MIMEType = photoAccessHelper.PhotoViewMIMETypes.IMAGE\_TYPE;
    photoSelectOptions.maxSelectNumber = 5;
    let photoPicker = new photoAccessHelper.PhotoViewPicker();
    photoPicker.select(photoSelectOptions, (err: BusinessError, photoSelectResult: photoAccessHelper.PhotoSelectResult) => {
      if (err) {
        console.error(\`PhotoViewPicker.select failed with err: ${err.code}, ${err.message}\`);
        return;
      }
      console.info('PhotoViewPicker.select successfully, photoSelectResult uri: ' + JSON.stringify(photoSelectResult));
    });
  } catch (error) {
    let err: BusinessError = error as BusinessError;
    console.error(\`PhotoViewPicker failed with err: ${err.code}, ${err.message}\`);
  }
}

#### select

select(callback: AsyncCallback<PhotoSelectResult>) : void

Starts a **photoPicker** page for the user to select one or more images or videos. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bd/v3/nQQD-tvMQVWZRTZMPiK8KQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062442Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A66D62879AC4745E08F488917C2F12BE6C4EEB261ED1A3B6B9C33F720C3AAF56)

**photoUris** in the PhotoSelectResult object returned by this API has permanent authorization and can be used only by calling [photoAccessHelper.getAssets](../interface-photoaccesshelper/document.md#getassets). For details, see [Using a Media File URI](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/user-file-uri-intro#using-a-media-file-uri).

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.FileManagement.PhotoAccessHelper.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<[PhotoSelectResult](../classes-others/document.md#photoselectresult)\> | Yes | Callback used to return information about the images or videos selected. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [File Management Error Codes](../../../../../application-framework/core-file-kit/error-codes/file-management-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 13900042 | Unknown error. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

async function example03(phAccessHelper: photoAccessHelper.PhotoAccessHelper) {
  try {
    let photoPicker = new photoAccessHelper.PhotoViewPicker();
    photoPicker.select((err: BusinessError, photoSelectResult: photoAccessHelper.PhotoSelectResult) => {
      if (err) {
        console.error(\`PhotoViewPicker.select failed with err: ${err.code}, ${err.message}\`);
        return;
      }
      console.info('PhotoViewPicker.select successfully, photoSelectResult uri: ' + JSON.stringify(photoSelectResult));
    });
  } catch (error) {
    let err: BusinessError = error as BusinessError;
    console.error(\`PhotoViewPicker failed with err: ${err.code}, ${err.message}\`);
  }
}
