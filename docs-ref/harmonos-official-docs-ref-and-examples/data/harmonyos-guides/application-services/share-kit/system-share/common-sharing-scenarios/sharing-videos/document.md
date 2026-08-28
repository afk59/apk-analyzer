# Sharing Videos

Video sharing allows users to share one or more videos to the target device or app.

-   When receiving the videos, the target device will save them to Gallery.
-   When receiving the videos, the target app can conveniently process the videos. For example, a user can share a video with a MeeTime friend.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/af/v3/Vnx8zoOqTSSehBBH_2zrcg/en-us_image_0000002481329632.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062121Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=74243B8FC539A2AA900F42D064C51553613394684DE19AB6F9D859720126FD68 "Click to enlarge")

#### Development Procedure

1.  Import required modules.
    
    import { systemShare } from '@kit.ShareKit';
    import { uniformTypeDescriptor as utd } from '@kit.ArkData';
    import { common } from '@kit.AbilityKit';
    import { fileUri } from '@kit.CoreFileKit';
    import { image } from '@kit.ImageKit';
    import { BusinessError } from '@kit.BasicServicesKit';
    
2.  (Recommended) Generate a video cover image.
    
    // Generate a video cover image.
    let uiContext: UIContext = this.getUIContext();
    let contextFaker: Context = uiContext.getHostContext() as Context;
    let thumbnailPath = contextFaker.filesDir + '/exampleImage.jpg'; // This is only an example. Replace it with the correct file path.
    let imageSource: image.ImageSource = image.createImageSource(thumbnailPath);
    let imagePacker: image.ImagePacker = image.createImagePacker();
    let buffer: ArrayBuffer = await imagePacker.packToData(imageSource, {
      // The value of **format** can only be **image/jpeg**, **image/webp**, or **image/png**.
      format: 'image/jpeg', 
      // Quality of the output image in JPEG encoding. The value ranges from 0 to 100.
      // You are advised to compress the image to a reasonable size. An oversized image will fail to be shared.
      quality: 30 
    });
    
3.  Construct the data to be shared.
    
    // Construct **ShareData**. You need to configure a valid data record.
    let filePath = contextFaker.filesDir + '/exampleVideo.mp4'; // This is only an example. Replace it with the correct file path.
    // Obtain the precise UTD type.
    let utdTypeId = utd.getUniformDataTypeByFilenameExtension('.mp4', utd.UniformDataType.VIDEO);
    let shareData: systemShare.SharedData = new systemShare.SharedData({
      utd: utdTypeId,
      uri: fileUri.getUriFromPath(filePath),
      title: 'Video title', // If this parameter is not passed, the video file name will be displayed.
      description: 'Video description', // If this parameter is not passed, the video size will be displayed.
      thumbnail: new Uint8Array(buffer), // You are advised to pass a suitable thumbnail for preview. If no thumbnail is passed, the first frame of the video will be used for preview by default.
    });
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d1/v3/78lCUqZOQKCop0tLdmJnTQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062121Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=348FEE24D987A34E30A9EC2E16DE367C853877A1BCA3DE94B9B4305604EDE382)
    
    You can use the [fileUri.getUriFromPath](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-file-fileuri#fileurigeturifrompath) method to obtain the file URI from the sandbox path.
    
4.  Add a record.
    
    shareData.addRecord({
      utd: utdTypeId,
      uri: fileUri.getUriFromPath(filePath),
      title: 'Video title', // If this parameter is not passed, the video file name will be displayed.
      description: 'Video description', // If this parameter is not passed, the video size will be displayed.
    });
    
5.  Start the sharing panel.
    
    // Display the sharing panel.
    let controller: systemShare.ShareController = new systemShare.ShareController(shareData);
    let context: common.UIAbilityContext = uiContext.getHostContext() as common.UIAbilityContext;
    controller.show(context, {
      selectionMode: systemShare.SelectionMode.SINGLE,
      previewMode: systemShare.SharePreviewMode.DETAIL,
    }).then(() => {
      console.info('ShareController show success.');
    }).catch((error: BusinessError) => {
      console.error(\`ShareController show error. code: ${error.code}, message: ${error.message}\`);
    });
    
    For details about the complete sample code, please refer to [Sample Code - Sharing Videos](https://gitcode.com/harmonyos_samples/share-kit_-sample-code_-clientdemo_-arkts/blob/master/entry/src/main/ets/scenario/VideoScenario.ets).
