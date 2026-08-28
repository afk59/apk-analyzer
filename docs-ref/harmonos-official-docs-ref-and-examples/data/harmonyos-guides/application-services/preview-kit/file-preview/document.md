# File Preview

The file preview function of Preview Kit is implemented by launching a new window. The file to be previewed is displayed in this window using a standardized UI design. If you intend to use this feature, take note of the following considerations:

-   Preview Kit only supports file preview by launching an external window and does not support in-app preview.
-   For Office-type files, the preview feature relies on WPS technology. As a result, phrases such as "Powered by WPS" or "Open with WPS Office" may appear during file preview.
-   Currently, Preview Kit does not support secure preview features, such as disabling screenshots and screen recordings, blocking access from other apps, or hiding sharing options during preview.
-   To enable file preview, the calling app must support delegated URI access, allowing Preview Kit to obtain the necessary permissions to read the file. For more details, please refer to [Preview Fails When the URI Obtained by DocumentViewPicker Is Opened Through the openPreview API](../faqs/preview-fails-when-the-uri-obtained-by-documentviewpicker-is-opened-through-the-/document.md).

#### API Description

The APIs use either a callback or promise to return the result. They two return values in different ways, but provide the same functions. For details about the APIs, please refer to the [API document](https://developer.huawei.com/consumer/en/doc/harmonyos-references/preview-arkts).

**Table 1** Preview Kit APIs
| 
API

 | 

Description

 |
| :-- | :-- |
| 

openPreview(context: Context, file: PreviewInfo, info?: DisplayInfo): Promise<void>

 | 

Enables the preview function. Displays the preview window based on the preview information of a single file and floating window attributes. Calling this API repeatedly within 1 second will not take effect. This API returns the result asynchronously through a promise.

 |
| 

openPreview(context: Context, file: PreviewInfo, info: DisplayInfo, callback: AsyncCallback<void>): void

 | 

Enables the preview function. Displays the preview window based on the preview information of a single file and floating window attributes. Calling this API repeatedly within 1 second will not take effect. This API returns the result asynchronously through a callback.

 |
| 

openPreview(context: Context, files: Array<PreviewInfo>, index?: number): Promise<void>

 | 

Enables the preview function. Displays the preview window based on the preview information of multiple files and selected file information subscripts. Calling this API repeatedly within 1 second will not take effect. This API returns the result asynchronously through a promise. This API is available only on mobile devices.

 |
| 

canPreview(context: Context, uri: string): Promise<boolean>

 | 

Checks whether a file or folder can be previewed based on the URI.

-   If the URI of a file that supports preview and exists is passed, **true** will be returned. (Supported file types include images, videos, audio, text, and HTML.)
-   If the URI of a file that cannot be previewed is passed, **false** will be returned.

 |
| 

hasDisplayed(context: Context): Promise<boolean>

 | 

Checks whether a preview window already exists. The preview window is implemented as a singleton.

-   If the preview window has been opened and is not closed, **true** will be returned.
-   If the preview window has not been opened or has been closed after being opened, **false** will be returned.

 |
| 

closePreview(context: Context): Promise<void>

 | 

Closes the preview window and takes effect only when a preview window exists.

 |
| 

loadData(context: Context, file: PreviewInfo): Promise<void>

 | 

Loads information about the file to be previewed. This API can take effect only when a preview window exists. Calling this API repeatedly within 100 milliseconds will not take effect.

-   If a file that can be previewed is passed, the preview page will be displayed.
-   If a file that cannot be previewed is passed, a message will be displayed, indicating that file preview is not supported.

 |

#### Development Procedure

1.  Import required modules.
    
    import { filePreview } from '@kit.PreviewKit';
    import { BusinessError } from '@kit.BasicServicesKit';
    
2.  Check whether a file can be previewed.
    
    let uri = 'file://docs/storage/Users/currentUser/Documents/1.txt';  
    let uiContext = this.getUIContext().getHostContext() as Context;
    filePreview.canPreview(uiContext, uri).then((result) => {    // If the file supports preview and it exists, **true** will be returned.
      console.info(\`Succeeded in obtaining the result of whether it can be previewed. result = ${result}\`);
    }).catch((err: BusinessError) => {
      console.error(\`Failed to obtain the result of whether it can be previewed, err.code = ${err.code}, err.message = ${err.message}\`);
    });
    
3.  Call **openPreview** to enable the file preview function.
    
    -   Open a file using a promise.
        
        let uiContext = this.getUIContext().getHostContext() as Context;
        let displayInfo: filePreview.DisplayInfo = {
          x: 100,
          y: 100,
          width: 800,
          height: 800
        };
        let fileInfo: filePreview.PreviewInfo = {
          title: '1.txt',
          uri: 'file://docs/storage/Users/currentUser/Documents/1.txt',
          mimeType: 'text/plain'
        };
        filePreview.openPreview(uiContext, fileInfo, displayInfo).then(() => {
          console.info('Succeeded in opening preview');
        }).catch((err: BusinessError) => {
          console.error(\`Failed to open preview, err.code = ${err.code}, err.message = ${err.message}\`);
        });
        
    
    -   Open a file using a callback.
        
        let uiContext = this.getUIContext().getHostContext() as Context;
        let displayInfo: filePreview.DisplayInfo = {
          x: 100,
          y: 100,
          width: 800,
          height: 800
        };
        let fileInfo: filePreview.PreviewInfo = {
          title: '1.txt',
          uri: 'file://docs/storage/Users/currentUser/Documents/1.txt',
          mimeType: 'text/plain'
        };
        filePreview.openPreview(uiContext, fileInfo, displayInfo, (err) => {
          if (err && err.code) {
            console.error(\`Failed to open preview, err.code = ${err.code}, err.message = ${err.message}\`);    
            return;
          }
          console.info('Succeeded in opening preview');
        });
        
    -   Pass multiple files for preview. Only available on mobile devices.
        
        let uiContext = this.getUIContext().getHostContext() as Context;
        let fileInfo: filePreview.PreviewInfo = {
          title: '1.txt',
          uri: 'file://docs/storage/Users/currentUser/Documents/1.txt',
          mimeType: 'text/plain'
        };
        let fileInfo1: filePreview.PreviewInfo = {
          title: '2.txt',
          uri: 'file://docs/storage/Users/currentUser/Documents/2.txt',
          mimeType: 'text/plain'
        };
        let files: Array<filePreview.PreviewInfo> = new Array();
        files.push(fileInfo);
        files.push(fileInfo1);
        filePreview.openPreview(uiContext, files, 0).then(() => {
          console.info('Succeeded in opening preview');
        }).catch((err: BusinessError) => {
          console.error(\`Failed to open preview, err.code = ${err.code}, err.message = ${err.message}\`);
        });
        
4.  (Optional) If the preview window has been opened and the page needs to be reloaded, call the **loadData** API for file loading.
    
    let uiContext = this.getUIContext().getHostContext() as Context;
    let fileInfo: filePreview.PreviewInfo = {
      title: '2.txt',
      uri: 'file://docs/storage/Users/currentUser/Documents/2.txt',
      mimeType: 'text/plain'
    };
    filePreview.loadData(uiContext, fileInfo).then(() => {   // Can take effect only when a preview window exists.
      console.info('Succeeded in loading data.');
    }).catch((err: BusinessError) => {
      console.error(\`Failed to load data, err.code = ${err.code}, err.message = ${err.message}\`);
    });
    
5.  (Optional) To close the preview window, call **closePreview**.
    
    let uiContext = this.getUIContext().getHostContext() as Context;
    filePreview.closePreview(uiContext).then(() => {   // Can take effect only when a preview window exists.
      console.info('Succeeded in closing preview');
    }).catch((err: BusinessError) => {
      console.error(\`Failed to close preview, err.code = ${err.code}, err.message = ${err.message}\`);
    });
