# Using ImagePacker to Encode Images

Image encoding refers to the process of compressing a PixelMap into different image file formats for the purpose of saving and transferring.

You can use [PackToData](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-image-imagepacker#packtodata13-1) and [PackToFile](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-image-imagepacker#packtofile11-2) to encode a [PixelMap](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-image-pixelmap) into JPEG, WebP, PNG, and HEIC images.

Starting from API version 18, you can use [PackToDataFromPixelmapSequence](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-image-imagepacker#packtodatafrompixelmapsequence18) and [PackToFileFromPixelmapSequence](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-image-imagepacker#packtofilefrompixelmapsequence18) to encode multiple PixelMaps into the GIF format.

#### How to Develop

Read the [API reference](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-image-imagepacker) for APIs related to image encoding.

## Encoding Images into File Streams

1.  Import the required modules.
    
    // Import the required module.
    import { image } from '@kit.ImageKit';
    import { BusinessError } from '@kit.BasicServicesKit';
    import { common } from '@kit.AbilityKit';
    import { fileIo as fs } from '@kit.CoreFileKit';
    import { resourceManager } from '@kit.LocalizationKit';
    
2.  Set the [encoding options](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-image-i#packingoption).
    
    2.1 The JPEG image encoding is used as an example. The target format of the encoding follows the MIME standard definition. Therefore, **PackingOption.format** should be set to **image/jpeg**, and the encoded file name extension can be set to **.jpg** or **.jpeg**.
    
    let packOpts : image.PackingOption = { format: 'image/jpeg', quality: 95 };
    
    2.2 If the image source is HDR and you want to encode it as an HDR image file, you need to configure **desiredDynamicRange** additionally.
    
    // If the resource is HDR and the device supports HDR encoding, the content is encoded in HDR. (This requires the resource to be HDR and the device to support HDR encoding and JPEG format.)
    packOpts.desiredDynamicRange = image.PackingDynamicRange.AUTO;
    
3.  Encapsulate a function that takes **imageSource** or **pixelMap** as input, then use the [packToData](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-image-imagepacker#packtodata13) API to encode the data into an **ArrayBuffer**, or use the [packToFile](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-image-imagepacker#packtofile11) API to encode it into a file.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/87/v3/4MXuC1H7TQuVL9MgtcV4eg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062041Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=14532D6065713E30345994A8EABF899FB263D5602D003B54CDFDF852449F5955)
    
    Before encoding, you need to obtain **imageSource** or **pixelMap** first. For details, please refer to [Using ImageSource to Decode Images](../../image-decoding/using-imagesource-to-decode-images/document.md).
    
    -   Encode the pixelMap into an **ArrayBuffer**.
        
        async function packToDataFromPixelMap(pixelMap : image.PixelMap) {
          const imagePackerApi = image.createImagePacker();
          let packOpts : image.PackingOption = { format: 'image/jpeg', quality: 95 };
          // If the resource is HDR and the device supports HDR encoding, the content is encoded in HDR. (This requires the resource to be HDR and the device to support HDR encoding and JPEG format.)
          packOpts.desiredDynamicRange = image.PackingDynamicRange.AUTO;
          try{
            let data = await imagePackerApi.packToData(pixelMap, packOpts);
            // data is the file stream obtained after encoding. You can write the file and save it to obtain an image.
            copyData = new ArrayBuffer(0);
            copyData = data;
          } catch (error) {
            console.error('Failed to pack the pixelMap to data. And the error is: ' + error);
          }
        }
        
    -   Encode the **imageSource** into an **ArrayBuffer**.
        
        async function packToDataFromImageSource(imageSource : image.ImageSource) {
          const imagePackerApi = image.createImagePacker();
          let packOpts : image.PackingOption = { format: 'image/jpeg', quality: 95 };
          try {
            let data = await imagePackerApi.packToData(imageSource, packOpts);
            // data is the file stream obtained after encoding. You can write the file and save it to obtain an image.
            copyData = new ArrayBuffer(0);
            copyData = data;
          } catch (error) {
            console.error('Failed to pack the imageSource to data. And the error is: ' + error);
          }
        }
        
    -   Encode the **pixelMap** into a file.
        
        async function packToFileFromPixelMap(context : Context, pixelMap : image.PixelMap) {
          const imagePackerApi = image.createImagePacker();
          let packOpts : image.PackingOption = { format: 'image/jpeg', quality: 95 };
          const path : string = context.cacheDir + '/pixel\_map.jpg';
          let file = fs.openSync(path, fs.OpenMode.CREATE | fs.OpenMode.READ\_WRITE);
          try {
            await imagePackerApi.packToFile(pixelMap, file.fd, packOpts);
          } catch (error) {
            console.error('Failed to pack the pixelMap to file. And the error is: ' + error);
          }
        }
        
    -   Encode the **imageSource** into a file.
        
        async function packToFileFromImageSource(context : Context, imageSource : image.ImageSource) {
          const imagePackerApi = image.createImagePacker();
          let packOpts : image.PackingOption = { format: 'image/jpeg', quality: 95 };
          const filePath : string = context.cacheDir + '/image\_source.jpg';
          let file = fs.openSync(filePath, fs.OpenMode.CREATE | fs.OpenMode.READ\_WRITE);
          try {
            await imagePackerApi.packToFile(imageSource, file.fd, packOpts);
          } catch (error) {
            console.error('Failed to pack the imageSource to file. And the error is: ' + error);
          }
        }
        
4.  Save an image to Gallery.
    

After an image is encoded to an **ArrayBuffer** or file, you can use the relevant APIs of the [Media Library Kit](../../../../media-library-kit/about-this-kit/document.md) to [save the media assets](../../../../media-library-kit/saving-media-assets/document.md) to Gallery.
