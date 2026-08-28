# How do I generate a PixelMap based on a photo selected from an album?

Method 1:

1.  Create a **photoViewPicker** instance, and call **select()** to open the photo picker for the user to select an image and return **PhotoSelectResult** after the image is selected.
2.  Call the **getAssets** API of the photoAccessHelper module to obtain the URI of the media file.
3.  Call **getThumbnail** to obtain the thumbnail.

Refer to the code snippet below.

import { photoAccessHelper } from '@kit.MediaLibraryKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { dataSharePredicates } from '@kit.ArkData';
import { common } from '@kit.AbilityKit';

const context = AppStorage.get("context") as common.UIAbilityContext;
@Entry
@Component
struct WebComponent {
  build() {
    Column() {
      Button('Select Image').onClick(() => {
        try {
          let uris: Array<string> = \[\];
          let PhotoSelectOptions = new photoAccessHelper.PhotoSelectOptions();
          PhotoSelectOptions.MIMEType = photoAccessHelper.PhotoViewMIMETypes.IMAGE\_TYPE;
          PhotoSelectOptions.maxSelectNumber = 1;
          let photoPicker = new photoAccessHelper.PhotoViewPicker();
          photoPicker.select(PhotoSelectOptions).then((PhotoSelectResult: photoAccessHelper.PhotoSelectResult) => {
            console.info('photoPicker.select successfully, PhotoSelectResult uri: ' + JSON.stringify(PhotoSelectResult));
            uris = PhotoSelectResult.photoUris;
            let phAccessHelper = photoAccessHelper.getPhotoAccessHelper(context);
            let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
            // Configure query conditions, use PhotoViewPicker to select the URI of the image to be queried
            predicates.equalTo('uri', uris\[0\]);
            let fetchOptions: photoAccessHelper.FetchOptions = {
              fetchColumns: \[\],
              predicates: predicates
            };
            phAccessHelper.getAssets(fetchOptions, async (err, fetchResult) => {
              if (fetchResult !== undefined) {
                console.info('fetchResult success');
                let photoAsset: photoAccessHelper.PhotoAsset = await fetchResult.getFirstObject();
                if (photoAsset !== undefined) {
                  // Get Thumbnail
                  photoAsset.getThumbnail((err, pixelMap) => {
                    if (err == undefined) {
                      console.info('getThumbnail successful ' + JSON.stringify(pixelMap));
                    } else {
                      console.error('getThumbnail fail', err);
                    }
                  });
                  console.info('photoAsset.displayName : ' + photoAsset.displayName);
                }
              } else {
                console.error(\`fetchResult fail with error: ${err.code}, ${err.message}\`);
              }
            });
          }).catch((err: BusinessError) => {
            console.error('photoPicker.select failed with err: ' + JSON.stringify(err));
          });
        } catch (error) {
          let err: BusinessError = error as BusinessError;
          console.error('photoPicker failed with err: ' + JSON.stringify(err));
        }
      })
    }
  }
}

Method 2:

1\. Create a **photoViewPicker** instance, and call **select()** to open the photo picker for the user to select an image and return **PhotoSelectResult** after the image is selected.

1.  After the application UI is returned from Gallery, call **fs.openSync** to open the file based on the URI and obtain the file descriptor (FD). Note that the permission must be set to **fs.OpenMode.READ\_ONLY** for the API.
2.  Use **image.createImageSource** to create an image source instance.
3.  Then, create a PixelMap based on the image source.

Refer to the code snippet below.

import { photoAccessHelper } from '@kit.MediaLibraryKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { image } from '@kit.ImageKit';
import { fileIo } from '@kit.CoreFileKit';

@Entry
@Component
struct WebComponent {
  build() {
    Column() {
      Button('Select Picture').onClick(() => {
        try {
          let uris: Array<string> = \[\];
          let PhotoSelectOptions = new photoAccessHelper.PhotoSelectOptions();
          PhotoSelectOptions.MIMEType = photoAccessHelper.PhotoViewMIMETypes.IMAGE\_TYPE;
          PhotoSelectOptions.maxSelectNumber = 1;
          let photoPicker = new photoAccessHelper.PhotoViewPicker();
          photoPicker.select(PhotoSelectOptions).then((PhotoSelectResult: photoAccessHelper.PhotoSelectResult) => {
            uris = PhotoSelectResult.photoUris;
            let file = fileIo.openSync(uris\[0\], fileIo.OpenMode.READ\_ONLY);
            console.info('file fd: ' + file.fd);
            let buffer = new ArrayBuffer(4096);
            let readLen = fileIo.readSync(file.fd, buffer);
            console.info('readSync data to file succeed and buffer size is:' + readLen);
            const imageSource: image.ImageSource = image.createImageSource(file.fd);
            let decodingOptions: image.DecodingOptions = {
              editable: true,
              desiredPixelFormat: 3,
            }
            imageSource.createPixelMap(decodingOptions, (err: BusinessError, pixelMap: image.PixelMap) => {
              if (err !== undefined) {
                console.error(\`Failed to create pixelMap.code is ${err.code},message is ${err.message}\`);
              } else {
                console.info('Succeeded in creating pixelMap object.');
              }
            })
          }).catch((err: BusinessError) => {
            console.error(\`Invoke photoPicker.select failed, code is ${err.code}, message is ${err.message}\`);
          })
        } catch (error) {
          let err: BusinessError = error as BusinessError;
          console.error('photoPicker failed with err: ' + JSON.stringify(err));
        }
      })
    }
  }
}
