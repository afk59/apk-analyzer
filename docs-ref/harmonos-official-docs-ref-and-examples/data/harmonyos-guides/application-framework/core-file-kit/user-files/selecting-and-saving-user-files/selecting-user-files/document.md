# Selecting User Files

You can use [FilePicker](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-file-picker) to implement the capabilities required for sharing user files and saving images and videos. When Picker is used to access a file, the related application will be started and guide the user to complete related operation on the UI. The caller does not require any permission. The permission on the file URI granted by Picker, however, is temporary. If required, you can persist the permission on the URI. For details, see [Persisting a Temporary Permission Granted by Picker](../persisting-temporary-permissions-arkts/document.md#persisting-a-temporary-permission-granted-by-picker).

**FilePicker** provides the following types of Pickers by file type:

-   [PhotoViewPicker](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-file-picker#photoviewpickerdeprecated): used to select and save images and videos. However, the APIs of this Picker will not be maintained in later versions. Use [PhotoViewPicker of PhotoAccessHelper](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-photoaccesshelper-photoviewpicker) to select image files. and the [security component to save them](../../../../../media/media-library-kit/saving-media-assets/document.md).
    
-   [DocumentViewPicker](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-file-picker#documentviewpicker): used to select and save documents. The **DocumentViewPicker** API triggers the **FilePicker** application. Documents are not distinguished by file name extensions. For example, the images and files downloaded from a browser are documents.
    
-   [AudioViewPicker](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-file-picker#audioviewpicker): used to select and save audio clips. The **AudioViewPicker** API triggers the **AudioPicker** application.
    

#### Selecting Images or Videos

[PhotoViewPicker](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-file-picker#photoviewpickerdeprecated) will not be maintained in later versions. You are advised to use [PhotoViewPicker of PhotoAccessHelper](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-photoaccesshelper-photoviewpicker) to select images.

#### Selecting Documents

1.  Import modules.
    
    import  { picker } from '@kit.CoreFileKit';
    import { fileIo as fs } from '@kit.CoreFileKit';
    import { common } from '@kit.AbilityKit';
    import { BusinessError } from '@kit.BasicServicesKit';
    
2.  Create a **DocumentSelectOptions** instance.
    
    const documentSelectOptions = new picker.DocumentSelectOptions();
    // Optional. Set the maximum number of documents that can be selected.
    documentSelectOptions.maxSelectNumber = 5;
    // Optional. Specify the path of the files or folder to select.
    documentSelectOptions.defaultFilePathUri = "file://docs/storage/Users/currentUser/test";
    // Optional. Set the type of the documents to select. The default value is FILE. This parameter can be used on 2-in-1 devices but does not take effect on other devices.
    documentSelectOptions.selectMode = picker.DocumentSelectMode.FILE;
    // Select the file suffix type \['Suffix type description|Suffix type'\]. (Optional. If this parameter is not transferred, all files are displayed by default.) Use a comma to separate multiple file suffixes, which cannot exceed 100. The wildcard \['All files (\*.\*)|.\*'\] can be used on 2-in-1 devices (and smartphones since API version 17) to display all files.
     documentSelectOptions.fileSuffixFilters = \['Image(.png, .jpg)|.png, .jpg', 'Document|.txt', 'Video|.mp4', '.pdf'\];
    // Whether to grant the permission for the specified files or directory. The value true means to grant the permission, and the value false (default) means the opposite. If this parameter is true, defaultFilePathUri is mandatory and the file management authorization page is displayed. If this parameter is false, a common file management page is displayed. This parameter can be used on 2-in-1 devices but does not take effect on other devices.
    documentSelectOptions.authMode = false;
    // Whether to enable the batch authorization mode. The value true means to enable the batch authorization mode, and the value false (default) means the opposite. When multiAuthMode is set to true, only the multiUriArray parameter takes effect. This parameter can be used on smartphones but does not take effect on other devices.
    documentSelectOptions.multiAuthMode = false;
    // Whether to pass the URIs for batch authorization. (Only files are supported and folders are not supported.) This parameter does not take effect when multiAuthMode is set to false. This parameter can be used on smartphones but does not take effect on other devices.
    documentSelectOptions.multiUriArray = \["file://docs/storage/Users/currentUser/test", "file://docs/storage/Users/currentUser/2test"\];
    // Whether to enable the aggregation view mode to launch the file management application. The value DEFAULT means this parameter does not take effect and the aggregation view mode is disabled. Values other than DEFAULT indicate that other parameters do not take effect.
    // This parameter can be used on phones but has no effect on other devices.
    documentSelectOptions.mergeMode = picker.MergeTypeMode.DEFAULT;
    // Whether to support encryption (only files are supported). The default value is false. If this parameter is set to true, files can be encrypted on the Picker page. Note that this parameter is supported since API version 19.
    documentSelectOptions.isEncryptionSupported = false;
    
3.  Create a [DocumentViewPicker](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-file-picker#documentviewpicker) instance, and call [select()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-file-picker#select-3) to start the FilePicker application page for the user to select documents.
    
    let uris: string\[\] = \[\];
    let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
    const documentViewPicker = new picker.DocumentViewPicker(context);
    documentViewPicker.select(documentSelectOptions).then((documentSelectResult: string\[\]) => {
      uris = documentSelectResult;
      console.info('documentViewPicker.select to file succeed and uris are:' + uris);
      // ...
    }).catch((err: BusinessError) => {
      console.error(\`Invoke documentViewPicker.select failed, code is ${err.code}, message is ${err.message}\`);
    });
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d6/v3/WaSIE3zAQwOTPjF3D_-8xA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061951Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F42962A5521942616E3081D766087ACA51C795570CE621E962F15AE214552A8A)
    
    -   The permission for the URI returned by [select()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-file-picker#select-3) of Picker is a temporary read-only permission. The temporary permission will be invalidated once the application exits.
        
    -   You can persist the temporary permission for a URI. For details, see [Persisting a Temporary Permission Granted by Picker](../persisting-temporary-permissions-arkts/document.md#persisting-a-temporary-permission-granted-by-picker).
        
    -   Further operations can be performed on the documents based on the file URIs. You are advised to define a global variable to save the URI.
        
    -   If metadata needs to be obtained, you can use the [@ohos.file.fs](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-file-fs) and [@ohos.file.fileuri](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-file-fileuri) APIs to obtain document attribute information, such as the document name, size, access time, modification time, and path, based on the URI.
    
4.  After the application UI is returned from FilePicker, call [fs.openSync](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-file-fs#fsopensync) to open a document based on the URI. The file descriptor (FD) is returned after the document is opened.
    
    if (uris.length > 0) {
        let uri: string = uris\[0\];
        // Note that the mode parameter of fs.openSync() is fs.OpenMode.READ\_ONLY.
        let file = fs.openSync(uri, fs.OpenMode.READ\_ONLY);
        console.info('file fd: ' + file.fd);
     }
    
5.  Call [fs.readSync](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-file-fs#readsync) to read data from the document based on the FD.
    
    let buffer = new ArrayBuffer(4096);
    let readLen = fs.readSync(file.fd, buffer);
    console.info('readSync data to file succeed and buffer size is:' + readLen);
    // Close the FD after the data is read.
    fs.closeSync(file);
    

#### Selecting Audio Clips

1.  Import modules.
    
    import  { picker } from '@kit.CoreFileKit';
    import { fileIo as fs } from '@kit.CoreFileKit';
    import { BusinessError } from '@kit.BasicServicesKit';
    import { common } from '@kit.AbilityKit';
    
2.  Create an **AudioSelectOptions** instance.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b1/v3/ELnOKH6CQNO2w7VyZxv7jg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061951Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C7E78B1D9BFE8F09082F650B3CD2C63CD2FFF348670899CDFE09E21B04301981)
    
    Currently, **AudioSelectOptions** is not configurable. By default, all types of user files are selected.
    
    const audioSelectOptions = new picker.AudioSelectOptions();
    
3.  Create an [AudioViewPicker](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-file-picker#audioviewpicker) instance, and call [select()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-file-picker#select-5) to start the AudioPicker application page for the user to select audio clips.
    
    let uris: string\[\] = \[\];
    // Obtain the context from the component and ensure that the return value of this.getUIContext().getHostContext() is UIAbilityContext.
    let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
    const audioViewPicker = new picker.AudioViewPicker(context);
    audioViewPicker.select(audioSelectOptions).then((audioSelectResult: Array<string>) => {
      // After the files are selected, a result set containing the URIs of the audio files selected is returned.
      uris = audioSelectResult;
      console.info('audioViewPicker.select to file succeed and uri is:' + uris);
      // ...
    }).catch((err: BusinessError) => {
      console.error(\`Invoke audioViewPicker.select failed, code is ${err.code}, message is ${err.message}\`);
    })
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b0/v3/yvtDtE-2T56NfDcfi-feAQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061951Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5C69708E2311AC025B1A8628014BD263FCCCF391BADBA1AE5AAA1E9DBCE38C3C)
    
    -   The permission for the URI returned by [select()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-file-picker#select-3) of Picker is a temporary read-only permission. The temporary permission will be invalidated once the application exits.
        
    -   You can persist the temporary permission for a URI. For details, see [Persisting a Temporary Permission Granted by Picker](../persisting-temporary-permissions-arkts/document.md#persisting-a-temporary-permission-granted-by-picker).
        
    -   You can read file data based on the URI. You are advised to define a global variable to save the URI. For example, you can use the [@ohos.file.fs](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-file-fs) API to obtain the FD of the audio clip based on the URI, and then develop the audio playback application with the media service. For details, see [Audio Playback Development](../../../../../media/audio-kit/audio-playback/audio-playback-development/document.md).
    
4.  After the application UI is returned from AudioPicker, call [fs.openSync](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-file-fs#fsopensync) to open an audio clip based on the URI. The FD is returned after the audio clip is opened.
    
    if (uris.length > 0) {
       let uri: string = uris\[0\];
       // Note that the mode parameter of fs.openSync() is fs.OpenMode.READ\_ONLY.
       let file = fs.openSync(uri, fs.OpenMode.READ\_ONLY);
       console.info('file fd: ' + file.fd);
    }
    
5.  Call [fs.readSync](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-file-fs#readsync) to read data from the audio clip based on the FD.
    
    let buffer = new ArrayBuffer(4096);
    let readLen = fs.readSync(file.fd, buffer);
    console.info('readSync data to file succeed and buffer size is:' + readLen);
    // Close the FD after the data is read.
    fs.closeSync(file);
    

#### Sample Code

-   [Selecting and View Documents and Media Files](https://gitcode.com/HarmonyOS_Samples/picker)
