# Saving User Files

When a user needs to download a file from the Internet or save a file to another directory, use **FilePicker** to save the file. Pay attention to the following key points:

**Permission Description**

-   The read and write permissions on the file URI granted by Picker is temporary by default, and will be automatically invalidated once the application exits.
-   You can persist the permissions on the URI. For details, see [Persisting a Temporary Permission Granted by Picker](../persisting-temporary-permissions-arkts/document.md#persisting-a-temporary-permission-granted-by-picker).
-   No permission is required if your application uses Picker to save audio clips, images, videos, and document files.

**System Isolation Description**

-   The files saved by the Picker are stored in the specified directory. They are isolated from the assets managed by **Gallery** and cannot be viewed in **Gallery**.
-   To save images and videos to Gallery, [use the SaveButton](../../../../../media/media-library-kit/saving-media-assets/document.md#saving-media-assets-using-savebutton).

#### Saving Images or Videos

[PhotoViewPicker](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-file-picker#photoviewpickerdeprecated) will not be maintained in later versions. You are advised to use [Media Library Kit](../../../../../media/media-library-kit/saving-media-assets/document.md) to save media assets.

If the security component cannot be called to save images and videos in your development, use [PhotoAccessHelper.showAssetsCreationDialog](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-photoaccesshelper-photoaccesshelper#showassetscreationdialog12) to save images and videos.

#### Saving Documents

1.  Import modules.
    
    import { picker } from '@kit.CoreFileKit';
    import { fileIo as fs } from '@kit.CoreFileKit';
    import { BusinessError } from '@kit.BasicServicesKit';
    import { common } from '@kit.AbilityKit';
    
2.  Configure the save options.
    
    // Create a documentSaveOptions instance.
    const documentSaveOptions = new picker.DocumentSaveOptions();
    // (Optional) Name of the file to save. The default value is empty.
    documentSaveOptions.newFileNames = \["DocumentViewPicker01.txt"\];
    // Optional. Specify the path of the file or directory to save.
    documentSaveOptions.defaultFilePathUri = "file://docs/storage/Users/currentUser/test";
    // File type. The value is in \['Suffix type description|Suffix type'\] format. To save all files, use 'All files (\*.\*)|.\*' (optional). If multiple suffixes are selected (a maximum of 100 suffixes can be filtered), the first suffix is selected by default. If this parameter is not transferred, no suffix is filtered by default.
    documentSaveOptions.fileSuffixChoices = \['Document|.txt', '.pdf'\];
    
3.  Create a [DocumentViewPicker](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-file-picker#constructor12) instance, and call [save()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-file-picker#save) to start the FilePicker page to save the document.
    
    let uris: string\[\] = \[\];
    let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
    const documentViewPicker = new picker.DocumentViewPicker(context);
    documentViewPicker.save(documentSaveOptions).then((documentSaveResult: string\[\]) => {
      uris = documentSaveResult;
      console.info('documentViewPicker.save to file succeed and uris are:' + uris);
     // ···
    }).catch((err: BusinessError) => {
      console.error(\`Invoke documentViewPicker.save failed, code is ${err.code}, message is ${err.message}\`);
    });
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/59/v3/uzhys3N_QMKys8fkjrvj5w/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061951Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7900C104767AF87AD1CE11ED55F9C18ACF4FC094BD336E57AF0C111F3835D39F)
    
    -   URI storage:
        
        -   You should avoid directly using a URI in the Picker callback.
        -   You are advised to define a global variable to save the URI for future use.
    -   Quick saving:
        
        -   You can directly access the download directory in [DOWNLOAD mode](#saving-files-to-the-download-directory).
    
4.  After the application UI is returned from FilePicker, you can call [fs.openSync](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-file-fs#fsopensync) to open a document based on the URI. The FD is returned after the document is opened.
    
    if (uris.length > 0) {
        let uri: string = uris\[0\];
        // Note that the permission specified by the mode parameter of fs.openSync() is fs.OpenMode.READ\_WRITE.
        let file = fs.openSync(uri, fs.OpenMode.READ\_WRITE);
        console.info('file fd: ' + file.fd);
     }
    
5.  Call [fs.writeSync](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-file-fs#writesync) to modify the document based on the FD, and call **fs.closeSync()** to close the FD.
    
    let writeLen: number = fs.writeSync(file.fd, 'hello, world');
    console.info('write data to file succeed and size is:' + writeLen);
    fs.closeSync(file);
    

#### Saving Audio Clips

1.  Import modules.
    
    import { picker } from '@kit.CoreFileKit';
    import { fileIo as fs } from '@kit.CoreFileKit';
    import { BusinessError } from '@kit.BasicServicesKit';
    import { common } from '@kit.AbilityKit';
    
2.  Configure the save options.
    
    const audioSaveOptions = new picker.AudioSaveOptions();
    // (Optional) Name of the document to save.
    audioSaveOptions.newFileNames = \['AudioViewPicker01.mp3'\];
    
3.  Create an [AudioViewPicker](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-file-picker#audioviewpicker) instance and call [save()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-file-picker#save-5) to start the FilePicker page to save the audio clip.
    
    let uris: string\[\] = \[\];
    let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
    const audioViewPicker = new picker.AudioViewPicker(context);
    audioViewPicker.save(audioSaveOptions).then((audioSelectResult: string\[\]) => {
      uris = audioSelectResult;
      console.info('audioViewPicker.save to file succeed and uri is:' + uris);
      // ···
    }).catch((err: BusinessError) => {
      console.error(\`Invoke audioViewPicker.save failed, code is ${err.code}, message is ${err.message}\`);
    });
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/79/v3/iVGeDxb1SQ6ZLTrzH4xZlw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061951Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=558A49ACB19F297F60CBCFB25297A4B09E6238206C0A7BD1B063F737492089B6)
    
    -   URI storage:
        
        -   You should avoid directly using a URI in the Picker callback.
        -   You are advised to define a global variable to save the URI for future use.
    -   Quick saving:
        
        -   You can directly access the download directory in [DOWNLOAD mode](#saving-files-to-the-download-directory).
    
4.  After the application UI is returned from FilePicker, call [fs.openSync](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-file-fs#fsopensync) to open an audio clip based on the URI. The FD is returned after the audio clip is opened.
    
    if (uris.length > 0) {
       let uri: string = uris\[0\];
       // Note that the permission specified by the mode parameter of fs.openSync() is fileIo.OpenMode.READ\_WRITE.
       let file = fs.openSync(uri, fs.OpenMode.READ\_WRITE);
       console.info('file fd: ' + file.fd);
    }
    
5.  Call [fs.writeSync](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-file-fs#writesync) to modify the document based on the FD, and call **fs.closeSync()** to close the FD.
    
    let writeLen = fs.writeSync(file.fd, 'hello, world');
    console.info('write data to file succeed and size is:' + writeLen);
    fs.closeSync(file);
    

#### Saving Files to the Download Directory

**Characteristics**

-   The directory is automatically created in Download/bundle name/.
-   Files can be directly saved without file selection.
-   You can create files under the returned URI that has persisting permissions.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1c/v3/lbJVLCRlRV--qZre6CN8oA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061951Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8982E4C01CD96DD13DE919F752C66089BB8A691B94709AD222E85C4FBFBA36B6)

Directories created in DOWNLOAD mode are used only to store files. Directories are not isolated from each other. You are not advised to store sensitive application data.

1.  Import modules.
    
    import { fileUri, picker } from '@kit.CoreFileKit';
    import { fileIo as fs } from '@kit.CoreFileKit';
    import { BusinessError } from '@kit.BasicServicesKit';
    import { common } from '@kit.AbilityKit';
    
2.  Configure the download mode.
    
    const documentSaveOptions = new picker.DocumentSaveOptions();
    // Set pickerMode to DOWNLOAD, which takes precedence over the settings in documentSaveOptions.
    documentSaveOptions.pickerMode = picker.DocumentPickerMode.DOWNLOAD;
    
3.  Save the file to the **Download** directory.
    
    let uri: string = '';
    // Obtain the context from the component and ensure that the return value of this.getUIContext().getHostContext() is UIAbilityContext.
    let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
    const documentViewPicker = new picker.DocumentViewPicker(context);
    const documentSaveOptions = new picker.DocumentSaveOptions();
    documentSaveOptions.pickerMode = picker.DocumentPickerMode.DOWNLOAD;
    documentViewPicker.save(documentSaveOptions).then((documentSaveResult: Array<string>) => {
      uri = documentSaveResult\[0\];
      console.info('documentViewPicker.save succeed and uri is:' + uri);
      const testFilePath = new fileUri.FileUri(uri + '/test.txt').path;
      const file = fs.openSync(testFilePath, fs.OpenMode.CREATE | fs.OpenMode.READ\_WRITE);
      fs.writeSync(file.fd, 'Hello World!');
      fs.closeSync(file.fd);
    }).catch((err: BusinessError) => {
      console.error(\`Invoke documentViewPicker.save failed, code is ${err.code}, message is ${err.message}\`);
    })
