# Using ImagePacker to Encode Pictures

Image encoding refers to the process of encoding a [Picture](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-image-picture) object into an image in different formats (only JPEG and HEIF are supported currently) for subsequent processing, such as storage and transmission.

#### How to Develop

Read the [API reference](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-image-imagepacker) for APIs related to image encoding.

1.  Import the required modules.
    
    // Import the required modules.
    import { image } from '@kit.ImageKit';
    import { BusinessError } from '@kit.BasicServicesKit';
    import { common } from '@kit.AbilityKit';
    import { fileIo as fs } from '@kit.CoreFileKit';
    import { resourceManager } from '@kit.LocalizationKit';
    
2.  Set the [encoding options](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-image-i#packingoption).
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b3/v3/85jD5GbBTl69hTNcEkRyfg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062041Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=AE420799A52DBCE7581C1A8CF99A122CBAAA63357E56F7D55944E4CC51CA31E1)
    
    The JPEG image encoding is used as an example. The target format of the encoding follows the MIME standard definition. Therefore, **PackingOption.format** should be set to **image/jpeg**, and the encoded file name extension can be set to **.jpg** or **.jpeg**.
    
    let packOpts: image.PackingOption = {
      format: 'image/jpeg',
      quality: 95,
      desiredDynamicRange: image.PackingDynamicRange.AUTO,
      needsPackProperties: true
    };
    
3.  Encapsulate a function that takes **picture** as input, then use the [packing](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-image-imagepacker#packing13) API to encode the data into an **ArrayBuffer**, or use the [packToFile](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-image-imagepacker#packtofile11-2) API to encode it into a file.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c0/v3/FQFgWNVzQBOcl0cXUQlOeA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062041Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1932A1B3867550CF901642DD561F76079EFFC888234F2EF70D6689B3EC01E810)
    
    Before encoding, you need to obtain a Picture object through decoding. For details, see [Using ImageSource to Decode Pictures](../../image-decoding/using-imagesource-to-decode-pictures/document.md).
    
    -   Encode the **picture** object into an **ArrayBuffer**.
        
        async function packing(picture: image.Picture, packOpts: image.PackingOption) {
          const imagePackerApi = image.createImagePacker();
          try {
            let data = await imagePackerApi.packing(picture, packOpts);
            copyData = data;
            console.info('Succeeded in packing the image.');
          } catch (error) {
            console.error('Failed to pack the picture to data. And the error is: ' + error);
          }
        }
        
    -   Encode the **picture** object into a file.
        
        async function packToFile(picture: image.Picture, packOpts: image.PackingOption, context: Context) {
          const path : string = context.cacheDir + '/picture.jpg';
          let file = fs.openSync(path, fs.OpenMode.CREATE | fs.OpenMode.READ\_WRITE);
          const imagePackerApi = image.createImagePacker();
          try {
            await imagePackerApi.packToFile(picture, file.fd, packOpts);
          } catch (error) {
            console.error('Failed to pack the picture to file. And the error is: ' + error);
          }
        }
