# Accessing and Managing Moving Photos

A moving photo is a photo form that combines an image and a video, empowering a static image with dynamic video effect. It helps users capture dynamic moments and improves the fault tolerance rate of photographing.

The media library provides the capabilities of accessing and managing moving photo assets, including:

-   [Saving Moving Photo Assets](#saving-moving-photo-assets)
-   [Obtaining a Moving Photo Object](#obtaining-a-moving-photo-object)
-   [Playing Moving Photos with MovingPhotoView](../playing-moving-photos-with-movingphotoview/document.md)
-   [Reading Moving Photo Assets](#reading-moving-photo-assets)

The capability of taking moving photos is provided by Camera Kit. For details, see [Moving Photos (ArkTS)](../../../camera-kit/fundamental-capabilities-for-camera-application-development-arkts/moving-photos-arkts/document.md).

#### Saving Moving Photo Assets

Use the **SaveButton** security component to save the assets (image and video) of a moving photo.

With the **SaveButton** security component, the application does not need the **ohos.permission.WRITE\_IMAGEVIDEO** permission. When the user taps the button embedded with the **SaveButton** security component, the application obtains the temporary permission to save the assets to the specified media library directory.

For details, see [SaveButton](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-security-components-savebutton).

**How to Develop**

1.  Set the properties of the **SaveButton** security component.
    
2.  Create a button with **SaveButton**.
    
3.  Call [MediaAssetChangeRequest.createAssetRequest](https://developer.huawei.com/consumer/en/doc/harmonyos-references/kts-apis-photoaccesshelper-mediaassetchangerequest#createassetrequest11) to create an asset change request with **PhotoSubtype** set to **MOVING\_PHOTO**.
    
4.  Call [MediaAssetChangeRequest.addResource](https://developer.huawei.com/consumer/en/doc/harmonyos-references/kts-apis-photoaccesshelper-mediaassetchangerequest#addresource11) to set the image and video of the moving photo. The video duration of the moving photo cannot exceed 10s.
    
    In the following example, the image and video of the moving photo are specified by **fileUri** of the [application file](../../../../application-framework/core-file-kit/application-files/application-file-access-and-management/accessing-application-files-arkts/document.md) in the application sandbox.
    
    You can also specify the assets in **ArrayBuffer**. For details, see [MediaAssetChangeRequest.addResource(type: ResourceType, data: ArrayBuffer)](https://developer.huawei.com/consumer/en/doc/harmonyos-references/kts-apis-photoaccesshelper-mediaassetchangerequest#addresource11-1).
    
5.  Call [PhotoAccessHelper.applyChanges](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-photoaccesshelper-photoaccesshelper#applychanges11) to apply changes for the moving photo.
    

import { photoAccessHelper } from '@kit.MediaLibraryKit';
import { common } from '@kit.AbilityKit';

@Entry
@Component
struct Index {
  @State message: string = 'Hello World'
  @State saveButtonOptions: SaveButtonOptions = {
    icon: SaveIconStyle.FULL\_FILLED,
    text: SaveDescription.SAVE\_IMAGE,
    buttonType: ButtonType.Capsule
  } // Set properties of SaveButton.

  build() {
    Row() {
      Column() {
        Text(this.message)
          .fontSize(50)
          .fontWeight(FontWeight.Bold)
        SaveButton(this.saveButtonOptions)// Create a SaveButton.
          .onClick(async (event, result: SaveButtonOnClickResult) => {
             if (result == SaveButtonOnClickResult.SUCCESS) {
               try {
                 let context: Context = this.getUIContext().getHostContext() as common.UIAbilityContext;
                 let phAccessHelper = photoAccessHelper.getPhotoAccessHelper(context);
                 // Ensure that the assets specified by imageFileUri and videoFileUri exist. imageFileUri and videoFileUri specify the image and video of the moving photo to create.
                 let imageFileUri = 'file://com.example.temptest/data/storage/el2/base/haps/entry/files/create\_moving\_photo.jpg';
                 let videoFileUri = 'file://com.example.temptest/data/storage/el2/base/haps/entry/files/create\_moving\_photo.mp4';
                 let assetChangeRequest: photoAccessHelper.MediaAssetChangeRequest = photoAccessHelper.MediaAssetChangeRequest.createAssetRequest(context, photoAccessHelper.PhotoType.IMAGE, "jpg", {
                  title: "moving\_photo",
                  subtype: photoAccessHelper.PhotoSubtype.MOVING\_PHOTO
                 });
                 assetChangeRequest.addResource(photoAccessHelper.ResourceType.IMAGE\_RESOURCE, imageFileUri);
                 assetChangeRequest.addResource(photoAccessHelper.ResourceType.VIDEO\_RESOURCE, videoFileUri);
                 await phAccessHelper.applyChanges(assetChangeRequest);
                 console.info('create moving photo successfully, uri: ' + assetChangeRequest.getAsset().uri);
               } catch (err) {
                 console.error(\`create moving photo failed with error: ${err.code}, ${err.message}\`);
               }
             } else {
               console.error('SaveButtonOnClickResult create moving photo failed');
             }
          })
      }
      .width('100%')
    }
    .height('100%')
  }
}

#### Obtaining a Moving Photo Object

-   Use **Picker** to obtain a moving photo object from the media library.
    
-   Create a local moving photo object of the application by passing **fileUri** of an [application file](../../../../application-framework/core-file-kit/application-files/application-file-access-and-management/accessing-application-files-arkts/document.md) in the application sandbox.
    

If you want to play an obtained moving photo, see [Playing Moving Photos with MovingPhotoView](../playing-moving-photos-with-movingphotoview/document.md).

## Obtaining a Moving Photo Object from the Media Library

1.  Select the [URI of a media file](../../../../application-framework/core-file-kit/user-files/user-file-uri/document.md#media-file-uri) of the moving photo by using **Picker**.
2.  Call [PhotoAccessHelper.getAssets](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-photoaccesshelper-photoaccesshelper#getassets-1) and [FetchResult.getFirstObject](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-photoaccesshelper-fetchresult#getfirstobject-1) to obtain the photo asset corresponding to the URI.
3.  Call [MediaAssetManager.requestMovingPhoto](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-photoaccesshelper-mediaassetmanager#requestmovingphoto12) to obtain the moving photo object.

import { photoAccessHelper } from '@kit.MediaLibraryKit';
import { dataSharePredicates } from '@kit.ArkData';
import { common } from '@kit.AbilityKit';

@Entry
@Component
struct Index {
  build() {
    Row() {
      Button("example").onClick(async () => {
        let context: Context = this.getUIContext().getHostContext() as common.UIAbilityContext;
        let phAccessHelper = photoAccessHelper.getPhotoAccessHelper(context);
        example(phAccessHelper, context);
      }).width('100%')
    }
    .height('90%')
  }
}

async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper, context: Context) {
  try {
    // Use Picker to select the URI of the moving photo.
    let photoSelectOptions = new photoAccessHelper.PhotoSelectOptions();
    photoSelectOptions.MIMEType = photoAccessHelper.PhotoViewMIMETypes.MOVING\_PHOTO\_IMAGE\_TYPE;
    photoSelectOptions.maxSelectNumber = 9;
    let photoViewPicker = new photoAccessHelper.PhotoViewPicker();
    let photoSelectResult = await photoViewPicker.select(photoSelectOptions);
    let uris = photoSelectResult.photoUris;
    for (let i = 0; i < uris.length; i++) {
      // Obtain the photo asset corresponding to the URI.
      let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
      predicates.equalTo(photoAccessHelper.PhotoKeys.URI, uris\[i\]);
      let fetchOption: photoAccessHelper.FetchOptions = {
        fetchColumns: \[\],
        predicates: predicates
      };
      let fetchResult: photoAccessHelper.FetchResult<photoAccessHelper.PhotoAsset> = await phAccessHelper.getAssets(fetchOption);
      let photoAsset: photoAccessHelper.PhotoAsset = await fetchResult.getFirstObject();
      // Obtain the moving photo object corresponding to the photo asset.
      await photoAccessHelper.MediaAssetManager.requestMovingPhoto(context, photoAsset, {
        deliveryMode: photoAccessHelper.DeliveryMode.FAST\_MODE
      }, {
        async onDataPrepared(movingPhoto: photoAccessHelper.MovingPhoto) {
          if (movingPhoto !== undefined) {
            // Customize the logic for processing the moving photo.
            console.info('request moving photo successfully, uri: ' + movingPhoto.getUri());
          }
        }
      })
    }
  } catch (err) {
    console.error(\`request moving photo failed with error: ${err.code}, ${err.message}\`);
  }
}

## Obtaining a Moving Photo object in an Application Sandbox Directory

Call [MediaAssetManager.loadMovingPhoto](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-photoaccesshelper-mediaassetmanager#loadmovingphoto12) to load the moving photo object in the application sandbox directory.

import { photoAccessHelper } from '@kit.MediaLibraryKit';
import { common } from '@kit.AbilityKit';

@Entry
@Component
struct Index {
  @State outputText: string = 'Supported formats:\\n';

  build() {
    Row() {
      Button("example").onClick(async () => {
        let context: Context = this.getUIContext().getHostContext() as common.UIAbilityContext;
        example(context);
      }).width('100%')
    }
    .height('90%')
  }
}

async function example(context: Context) {
  try {
    let imageFileUri = 'file://com.example.temptest/data/storage/el2/base/haps/entry/files/local\_moving\_photo.jpg';
    let videoFileUri = 'file://com.example.temptest/data/storage/el2/base/haps/entry/files/local\_moving\_photo.mp4';
    let movingPhoto = await photoAccessHelper.MediaAssetManager.loadMovingPhoto(context, imageFileUri, videoFileUri);
    console.info('load moving photo successfully');
  } catch (err) {
    console.error(\`load moving photo failed with error: ${err.code}, ${err.message}\`);
  }
}

#### Reading Moving Photo Assets

Call [MovingPhoto.requestContent](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-photoaccesshelper-movingphoto#requestcontent12) to export the image and video of a moving photo to the application sandbox directory or read the image and video data from **ArrayBuffer**.

import { photoAccessHelper } from '@kit.MediaLibraryKit';

async function example(movingPhoto: photoAccessHelper.MovingPhoto) {
  try {
    let imageFileUri = 'file://com.example.temptest/data/storage/el2/base/haps/entry/files/request\_moving\_photo.jpg';
    let videoFileUri = 'file://com.example.temptest/data/storage/el2/base/haps/entry/files/request\_moving\_photo.mp4';
    await movingPhoto.requestContent(imageFileUri, videoFileUri); // Export the image and video of the moving photo to the application sandbox directory.
    let imageData = await movingPhoto.requestContent(photoAccessHelper.ResourceType.IMAGE\_RESOURCE); // Read ArrayBuffer to obtain the image data.
    let videoData = await movingPhoto.requestContent(photoAccessHelper.ResourceType.VIDEO\_RESOURCE); // Read ArrayBuffer to obtain the video data.
  } catch (err) {
    console.error(\`request content of moving photo failed with error: ${err.code}, ${err.message}\`);
  }
}
