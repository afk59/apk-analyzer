# Customizing the Page Background

You can implement real-time background color and image change for reading content on your app through the **themeColor** and **themeBgImg** attributes of [ReaderSetting](https://developer.huawei.com/consumer/en/doc/harmonyos-references/reader-read-core#section13615732174218), respectively.

Changing the page background color may involve compatibility between the font color and dark mode. For example, if the background is set to white but the system is in dark mode, the white font color will cause the text to be invisible.

Custom page background images can be stored in either of the following directories:

-   **resources/rawfile** in the project directory
-   [App sandbox directory](../../../../../application-framework/core-file-kit/application-files/application-sandbox/document.md)

#### Service Process

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ef/v3/vXfjWIcNQ_2i0iXGCwFppQ/en-us_image_0000002224338886.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062118Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=16C407379E743086DA50A73A9C1D62967C1430E88E0A5F909917BA94517C3136 "Click to enlarge")

#### API Description

This function involves one API. See the following table for detailed API information.

| 
API

 | 

Description

 |
| :-- | :-- |
| 

[setPageConfig](https://developer.huawei.com/consumer/en/doc/harmonyos-references/reader-read-core#section6297758718)(pageConfig: ReaderSetting): void

 | 

Sets or modifies page typesetting attributes.

 |

#### Preparations

-   Before customizing the page background, ensure that you have [built a reader](../../building-a-reader/document.md).
-   You have prepared background image files and stored them in the correct directory.

#### Development Procedure

1.  Import required modules.
    
    import { fileIo as fs } from '@kit.CoreFileKit';
    import { common } from '@kit.AbilityKit';
    import { hilog } from '@kit.PerformanceAnalysisKit';
    
2.  Set the background color. If a background image is set, the background color is used to draw the back theme color in simulated page turning. If no background image is set, the background color is used to render the background color of the reading page.
    
    this.readerSetting.themeColor = '#000000';
    this.readerSetting.themeBgImg = '';
    // If a light background color is set, disable the dark mode.
    this.readerSetting.nightMode = false;
    // Adjust the font color for a light background color.
    this.readerSetting.fontColor = '#FFFFFF';
    
3.  Set the background image. Concurrently, you also need to set a theme color similar to the background image for the rendering of the back theme color in simulated page turning.
    
    this.readerSetting.themeBgImg = 'dark\_sky\_first.jpg';
    this.readerSetting.themeColor = '#000000';
    // If a light background image is set, disable the dark mode.
    this.readerSetting.nightMode = false;
    // Adjust the font color for a light background image.
    this.readerSetting.fontColor = '#FFFFFF';
    
4.  Call the **setPageConfig** API of **ReaderComponentController** to re-render the UI.
    
    this.readerComponentController.setPageConfig(this.readerSetting);
    
5.  Register the resource request API of the typesetting engine and return the corresponding background image.
    
    Upon detecting custom background image usage, the typesetting engine requests the image through the API. Your app needs to determine whether it is a background image request based on the returned file path. If yes, the app returns **ArrayBuffer** based on the background image file path.
    
    aboutToAppear(): void {
      // Register a resource request callback.
      this.readerComponentController.on('resourceRequest', this.resourceRequest);
    }
    
    aboutToDisappear(): void {
      // Deregister the resource request callback.
      this.readerComponentController.off('resourceRequest');
    }
    
    /\*\*
     \* Resource request callback.
     \*/
    private resourceRequest: bookParser.CallbackRes<string, ArrayBuffer> = (filePath: string): ArrayBuffer => {
      hilog.info(0x0000, 'testTag', 'resourceRequest : filePath = ' + filePath);
      if(filePath.length === 0){
        return new ArrayBuffer(0);
      }
      try {
        let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
        // Obtain the background image file as a Uint8Array from the **resources/rawfile** directory.
        let value: Uint8Array = context.resourceManager.getRawFileContentSync(filePath);
        hilog.info(0x0000, 'testTag', 'resourceRequest : get other resource succeeded ');
        return value.buffer as ArrayBuffer;
      } catch (error) {
        let code = (error as BusinessError).code;
        let message = (error as BusinessError).message;
        hilog.error(0x0000, 'testTag',
          \`resourceRequest : get other resource failed, error code: ${code}, message: ${message}.\`);
      }
      // If the background image file data fails to be obtained from the **resources/rawfile** directory, obtain it from the sandbox directory.
      return this.loadFileFromPath(filePath);
    }
    
    private loadFileFromPath(filePath: string): ArrayBuffer {
      try {
        let stats = fs.statSync(filePath);
        let file = fs.openSync(filePath, fs.OpenMode.READ\_ONLY);
        let buffer = new ArrayBuffer(stats.size);
        fs.readSync(file.fd, buffer);
        fs.closeSync(file);
        return buffer;
      } catch (err) {
        hilog.error(0x0000, 'testTag', "mkdir failed with error message: ", err.message, ", error code: ", err.code);
        return new ArrayBuffer(0);
      }
    }
