# File Open Boost Status Awareness

If an app, such as a browser, supports file download, the app can integrate with the status awareness APIs to detect the file preloading status and provide a unique user interface (UI) identifier for the boosted file, improving experience when opening the file. These APIs have been available since version 5.0.5(17).

#### API Description

For details about the APIs, please refer to [openFileBoost](https://developer.huawei.com/consumer/en/doc/harmonyos-references/preview-arkts-openfileboost-api).

**Table 1** Preloading status awareness APIs (ArkTS APIs)
| 
API

 | 

Description

 |
| :-- | :-- |
| 

on(type: 'filePreloadStateChanged', callback: Callback<FilePreloadStatusInfo>): void

 | 

Registers the callback for file preloading status events. This API uses an asynchronous callback to return the result.

 |
| 

off(type: 'filePreloadStateChanged', callback?: Callback<FilePreloadStatusInfo>): void

 | 

Unregisters the callback for file preloading status events. This API uses an asynchronous callback to return the result.

 |
| 

addFile(file: string): void

 | 

Listener for the file preloading status, which is used to listen to the file preloading status after the app passes the file path. If the file status changes, the change is returned to the app through the **filePreloadStateChanged** event callback.

You need to call **openFileBoost.on('filePreloadStateChanged')** before calling this API to add a listener for file preloading status.

For details about the file types that support boost, see [File Types Supported by File Open Boost](../about-this-kit/document.md#section7910758192912). For file types that are not supported, the file will not be preloaded by default. In this case, you do not need to call this API to listen to the file preloading status change.

 |
| 

removeFile(file: string): void

 | 

Cancels the listening on the preloading status of a file. The preloading status change will not be notified to the service through callback.

 |
| 

queryFilePreloadStatusInfo(file: string): FilePreloadStatusInfo

 | 

Queries the preloading status of a file. The file preloading status will be returned after the file path is passed.

 |

#### Getting Started

Use [Syscap](< https://developer.huawei.com/consumer/en/doc/harmonyos-references/syscap#checking-whether-an-api-is-available>) to check whether the target device supports the **SystemCapability.PCService.OpenFileBoost** system capability. Currently, this capability is supported only on 2-in-1 devices.

#### Development Procedure

1.  Import required modules.
    
    import { openFileBoost } from '@kit.PreviewKit';
    import { BusinessError } from '@kit.BasicServicesKit';
    import { hilog } from '@kit.PerformanceAnalysisKit';
    
2.  Register the callback for the file preloading status info.
    
    // Definition of the callback function of file preloading status info, which returns the result if the file preloading status changes.
    function callback(filePreloadStatusInfo: openFileBoost.FilePreloadStatusInfo): void {
      if (filePreloadStatusInfo.state === openFileBoost.FilePreloadState.PRELOADING) {
        // The file is preloading, and the app can customize its UX design.
        hilog.info(0x0000, 'testTag', \`file is PRELOADING, suggest to show loading animation\`);
      }
      if (filePreloadStatusInfo.state === openFileBoost.FilePreloadState.PRELOADED) {
        // Preloading is complete, and the app can display a boost completion message.
        hilog.info(0x0000, 'testTag', \`file is PRELOADED, suggest to show loaded animation\`);
      }
      if (filePreloadStatusInfo.state === openFileBoost.FilePreloadState.NOT\_PRELOADED) {
        // No file is preloaded, and the app displays nothing.
        hilog.info(0x0000, 'testTag', \`file is UNPRELOADED, suggest do not show animation \`);
      }
    }
    // Call the **register** function to register the callback for the file preloading status info.
    function register(): void {
      try {
        openFileBoost.on('filePreloadStateChanged', callback);
      } catch(error) {
        let code = (error as BusinessError).code;
        let message = (error as BusinessError).message;
        hilog.error(0x0000, 'testTag', \`register filePreloadStateChanged failed, error code: ${code}, message: ${message}.\`);
      }
    }
    
3.  Call the **addFile** API to pass the sandbox path of the target file. For example, after the app downloads a file, the sandbox path of the file can be registered. If the file status changes, the system will notify the app of the change using the callback function in Step [2](#en-us_topic_0000002232379348_li13424101995516).
    
    // Add a listener for the file preloading status of the 10MB\_file.docx file.
    function testAddFile(): void {
      try {
        const file:string = "/storage/Users/currentUser/Desktop/10MB\_file.docx";
        openFileBoost.addFile(file);
      } catch(error) {
        let code = (error as BusinessError).code;
        let message = (error as BusinessError).message;
        hilog.error(0x0000, 'testTag', \`addFile failed, error code: ${code}, message: ${message}.\`);
      }
    }
    
4.  Cancel the listening on unnecessary files using the **removeFile** API since a maximum of 50 files can be listened on using the **addFile** API.
    
    const file:string = "/storage/Users/currentUser/Desktop/10MB\_file.docx";
    try {
      openFileBoost.removeFile(file);
    } catch(error) {
      let code = (error as BusinessError).code;
      let message = (error as BusinessError).message;
      hilog.error(0x0000, 'testTag', \`removeFile failed, error code: ${code}, message: ${message}.\`);
    }
    
5.  Unregister the callback for the file preloading status info if you do not wish to listen to any file preloading status changes. If a specific callback function is passed, only the function is canceled. If no specific callback function is passed, all callbacks for listening to the event are canceled.
    
    // Assume that callback1, callback2, and callback3 have been registered in different service logic of the process.
    openFileBoost.on('filePreloadStateChanged', callback1);
    openFileBoost.on('filePreloadStateChanged', callback2);
    openFileBoost.on('filePreloadStateChanged', callback3);
    
    function testUnregister(): void {
      try {
        // To cancel only the listening of callback1, pass callback1 as a parameter. Then callback1 will not be called for notification.
        openFileBoost.off('filePreloadStateChanged', callback1);
        // To cancel the listening of all callbacks, do not specify the second optional parameter. Then callback2 and callback3 will not be called for notification.
        openFileBoost.off('filePreloadStateChanged');
      } catch(error) {
        let code = (error as BusinessError).code;
        let message = (error as BusinessError).message;
        hilog.error(0x0000, 'testTag', \`off filePreloadStateChanged failed, error code: ${code}, message: ${message}.\`);
      }
    }
    
6.  The app can also query the real-time preloading status of a file through the query API when the app is just started. Each time the API is called, the sandbox path of the file is passed.
    
    function testQuery(): void {
    try {
      const file:string = "/storage/Users/currentUser/Desktop/10MB\_file.docx";
      let statusInfo : openFileBoost.FilePreloadStatusInfo = openFileBoost.queryFilePreloadStatusInfo(file);
      hilog.info(0x0000, 'testTag', 'file, %{public}s, progress:%{public}d  preloadState:%{public}d',
        statusInfo.sandboxPath, statusInfo.progress, statusInfo.state);
    } catch(error) {
      let code = (error as BusinessError).code;
      let message = (error as BusinessError).message;
      hilog.error(0x0000, 'testTag', \`query failed, error code: ${code}, message: ${message}.\`);
    }
    }
