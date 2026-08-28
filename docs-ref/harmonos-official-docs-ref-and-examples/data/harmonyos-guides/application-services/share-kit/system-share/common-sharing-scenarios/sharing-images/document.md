# Sharing Images

Image sharing allows users to share one or more images to the target device or app.

-   When receiving the images, the target device will save them to Gallery.
-   When receiving the images, the target app can conveniently process the images. For example, a user can share an image with a MeeTime friend.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e1/v3/P81uqikyTiedcyztmljvGg/en-us_image_0000002513409505.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062121Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=36BE8A9752007C49C82323B6077B167B6842F6E1717AA08D367A3F9D46ADE6F0 "Click to enlarge")

#### Development Procedure

1.  Import required modules.
    
    import { systemShare } from '@kit.ShareKit';
    import { uniformTypeDescriptor as utd } from '@kit.ArkData';
    import { common } from '@kit.AbilityKit';
    import { fileUri } from '@kit.CoreFileKit';
    import { BusinessError } from '@kit.BasicServicesKit';
    
2.  Construct the data to be shared.
    
    // Construct **ShareData**. You need to configure a valid data record.
    let uiContext: UIContext = this.getUIContext();
    let contextFaker: Context = uiContext.getHostContext() as Context;
    let filePath = contextFaker.filesDir + '/exampleImage.jpg'; // This is only an example. Replace it with the correct file path.
    // Obtain the precise UTD type.
    let utdTypeId = utd.getUniformDataTypeByFilenameExtension('.jpg', utd.UniformDataType.IMAGE);
    let shareData: systemShare.SharedData = new systemShare.SharedData({
      utd: utdTypeId,
      uri: fileUri.getUriFromPath(filePath),
      title: 'Image title', // If this parameter is not passed, the image file name will be displayed.
      description: 'Image description', // If this parameter is not passed, the image size will be displayed.
      // thumbnail: new Uint8Array() // You are advised to pass a suitable thumbnail for preview. If no thumbnail is passed, the original image will be used as the preview image by default.
    });
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/71/v3/yxBN1Bk9T427dmiLfhj_BA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062121Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F647D929E84CCE6FE5BE3CE2916833EBB3C8D7FA95D71068DC817950F2F97561)
    
    You can use the [fileUri.getUriFromPath](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-file-fileuri#fileurigeturifrompath) method to obtain the file URI from the sandbox path.
    
3.  Add a record.
    
    shareData.addRecord({
      utd: utdTypeId,
      uri: fileUri.getUriFromPath(filePath),
      title: 'Image title', // If this parameter is not passed, the image file name will be displayed.
      description: 'Image description', // If this parameter is not passed, the image size will be displayed.
    });
    
4.  Start the sharing panel.
    
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
    
    For details about the complete sample code, please refer to [Sample Code - Sharing Images](https://gitcode.com/harmonyos_samples/share-kit_-sample-code_-clientdemo_-arkts/blob/master/entry/src/main/ets/scenario/ImageScenario.ets).
