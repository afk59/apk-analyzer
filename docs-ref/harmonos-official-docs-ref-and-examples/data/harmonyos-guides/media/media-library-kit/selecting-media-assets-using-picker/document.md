# Selecting Media Assets Using Picker

When a user needs to share files such as images and videos, use **Picker** to start Gallery for the user to select the files to share. No permission is required when Picker is used. Currently, a UIAbility is used to start Gallery with the window component. The procedure is as follows:

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/60/v3/_EaatKa9SmqGjURwdx65og/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062044Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=FC388938F3A8BDE12CEC9047E49F6BF203D242D5CEE8A1DEFBBB57BD0FA87431)

Media Library Kit handles image and video management. If you need to read and save audio files, use [AudioViewPicker](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-file-picker#audioviewpicker).

1.  Import modules.
    
    import { fileIo } from '@kit.CoreFileKit';
    import photoAccessHelper from '@ohos.file.photoAccessHelper';
    
2.  Create a PhotoSelectOptions instance.
    
    const photoSelectOptions = new photoAccessHelper.PhotoSelectOptions();
    
3.  Set the type and maximum number of media files to select.
    
    The following uses images as an example. For details about the media file types, see [PhotoViewMIMETypes](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-photoaccesshelper-e#photoviewmimetypes).
    
    photoSelectOptions.maxSelectNumber = 5;
    photoSelectOptions.MIMEType = photoAccessHelper.PhotoViewMIMETypes.IMAGE\_VIDEO\_TYPE;
    photoSelectOptions.isPhotoTakingSupported = true;
    
4.  Create a photoViewPicker instance and call [PhotoViewPicker.select](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-photoaccesshelper-photoviewpicker#select) to open Gallery for the user to select images. After the images are selected, [PhotoSelectResult](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-photoaccesshelper-class#photoselectresult) is returned.
    
    const result = await photoViewPicker.select(photoSelectOptions);
                
    // After the files are selected, PhotoSelectResult is returned.
    console.log('Selection successful, returning result: ' + JSON.stringify(result));
    console.log('Number of selected files: ' + result.photoUris.length);
          
    // Update the selected URI list.
    this.selectedUris = result.photoUris;
    // Set the first URI as the default selection for read operations.
    if (this.selectedUris.length > 0) {
      this.selectedUriForRead = this.selectedUris\[0\];
    }
          
    // Invoke the utility class to process the result.
    this.processedItems = MediaLibraryPickerUtils.handleSelectResult(this.selectedUris);
    console.log('Number of processed results: ' + this.processedItems.length);
    
    The permission on the URIs returned by **select()** is read-only. File data can be read based on the URI. Note that the URI cannot be directly used in the Picker callback to open a file. You need to define a global variable to save the URI and use a button to open the file. For details, see [Reading File Data by URI](#reading-file-data-by-uri).
    
    You can also [obtain an image or video based on the URI](#obtaining-an-image-or-video-by-uri).
    
    If metadata needs to be obtained, you can use the [@ohos.file.fs](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-file-fs) and [@ohos.file.fileuri](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-file-fileuri) APIs to obtain file attribute information, such as the file name, size, access time, modification time, and path, based on the URI.
    

#### Reading File Data by URI

1.  After the UI returns from Gallery, use a button to call other functions. Specifically, use[fileIo.openSync](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-file-fs#fsopensync) to open the file and obtain its FD through the [media file URI](../../../application-framework/core-file-kit/user-files/user-file-uri/document.md#media-file-uri). Note that the **mode** parameter of **fileIo.openSync()** must be **fileIo.OpenMode.READ\_ONLY**.
    
    try {
      const file = fileIo.openSync(uri, fileIo.OpenMode.READ\_ONLY);
      console.info('file fd: ' + file.fd);
      return { fd: file.fd, file: file };
    } catch (error) {
      console.error('openSync failed with err: ' + error);
      return null;
    }
    
2.  Call [fileIo.readSync](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-file-fs#readsync) to read the file based on the FD, and close the FD after the data is read.
    
    try {
      const buffer = new ArrayBuffer(bufferSize);
      const readLen = fileIo.readSync(fileObj.fd, buffer);
      console.info('readSync data to file succeed and buffer size is:' + readLen);
      return { data: buffer, length: readLen };
    } catch (error) {
      console.error('readSync failed with err: ' + error);
      return null;
    }
    

#### Obtaining an Image or Video by URI

The media library allows **Picker** to select a [media file URI](../../../application-framework/core-file-kit/user-files/user-file-uri/document.md#media-file-uri) and obtain the corresponding image or video. The following describes how to query a URI named **file://media/Photo/1/IMG\_datetime\_0001/displayName.jpg**.

1.  Define a media asset handler called [MediaAssetDataHandler](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-photoaccesshelper-mediaassetdatahandler). The system calls back to the application with **onDataPrepared** when the asset is ready.
    
    export class MediaAssetDataHandler implements photoAccessHelper.MediaAssetDataHandler<ArrayBuffer> {
      private callback?: MediaDataHandlerCallback;
      
      constructor(callback?: MediaDataHandlerCallback) {
        this.callback = callback;
      }
    
      // Use the arrow function to ensure that the this reference is not lost.
      onDataPrepared = (data: ArrayBuffer) => {
        if (data === undefined) {
          console.error('Error occurred when preparing data');
          return;
        }
        console.info('on image data prepared');
        // Now this always refers to the MediaAssetDataHandler instance.
        if (this.callback) {
          this.callback(data);
        }
      };
    }
    
2.  Call [getAssets](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-photoaccesshelper-photoaccesshelper#getassets-1) to obtain the assets, and call [requestImageData](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-photoaccesshelper-mediaassetmanager#requestimagedata11) to obtain the specific asset.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d8/v3/DPlyOigrRHy00aTTmY5f8w/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062044Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4E03EAEAE200699D71AD334236A74B7A455698A361708EE653DF5783B5B817F9)
    
    To protect user privacy, sensitive EXIF metadata, including geographical location and shooting parameters, is automatically anonymized in media files. To retrieve the original, non-anonymized EXIF information, your application must [request the permission](../restricted-open-capabilities/before-you-start/document.md#requesting-permissions) ohos.permission.MEDIA\_LOCATION from the **PhotoAccessHelper** module.
    
    static async getMediaResourceByUri(uri: string, context: common.Context, callback?: MediaDataHandlerCallback)
    : Promise<void> {
      try {
        // Create a PhotoAccessHelper instance.
        const phAccessHelper = photoAccessHelper.getPhotoAccessHelper(context);
          
        // Create search criteria.
        const predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
        predicates.equalTo(photoAccessHelper.PhotoKeys.URI, uri);
          
        // Set the query option.
        const fetchOptions: photoAccessHelper.FetchOptions = {
          fetchColumns: \[photoAccessHelper.PhotoKeys.TITLE\],
          predicates: predicates
        };
    
        // Query assets.
        const fetchResult: photoAccessHelper.FetchResult<photoAccessHelper.PhotoAsset> =
          await phAccessHelper.getAssets(fetchOptions);
          
        const photoAsset: photoAccessHelper.PhotoAsset = await fetchResult.getFirstObject();
        if (photoAsset) {
          console.info('getAssets photoAsset.uri : ' + photoAsset.uri);
          // Obtain the title property.
          console.info('title : ' + photoAsset.get(photoAccessHelper.PhotoKeys.TITLE));
            
          // Set request options.
          const requestOptions: photoAccessHelper.RequestOptions = {
            deliveryMode: photoAccessHelper.DeliveryMode.HIGH\_QUALITY\_MODE,
          };
            
          // Request image data.
          await photoAccessHelper.MediaAssetManager.requestImageData(
            context, photoAsset, requestOptions, new MediaAssetDataHandler(callback));
            
          console.info('requestImageData successfully');
        } else {
          console.error('No asset found for URI: ' + uri);
        }
          
        // Close the query result.
        fetchResult.close();
      } catch (err) {
        console.error('getMediaResourceByUri failed with err: ' + err);
      }
    }
