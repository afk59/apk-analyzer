# Using ImageSource to Decode Images

Image decoding refers to the process of decoding an image in a supported format into a [PixelMap](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-image-pixelmap) for image display or processing. Currently, the following image formats are supported: JPEG, PNG, GIF, WebP, BMP, SVG, ICO, DNG, and HEIC. The supported formats may vary depending on the hardware.

Starting from API version 22, decoding is supported for embedded preview images (typically in JPEG format) of pictures in the following formats captured by professional cameras: CR2, CR3, ARW, NEF, RAF, NRW, ORF, RW2, PEF, and SRW. This decoding capability is not restricted by the type of running device.

#### How to Develop

Read the [API reference](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-image-imagesource) for APIs related to image decoding.

1.  Import the image module.
    
    // Import the required modules.
    import { image } from '@kit.ImageKit';
    import { BusinessError } from '@kit.BasicServicesKit';
    import { common } from '@kit.AbilityKit';
    import { fileIo as fs } from '@kit.CoreFileKit';
    import { resourceManager } from '@kit.LocalizationKit';
    
2.  Obtain an image.
    
    -   Method 1: Directly obtain the image through the sandbox path. This method applies only to images in the application sandbox path. For details about how to obtain the sandbox path, see [Obtaining Application File Paths](../../../../../application-framework/ability-kit/stage-model-development/stage-model-application-components/context-stage-model/document.md#obtaining-application-file-paths). For details about the application sandbox and how to push files to the application sandbox directory, see [File Management](../../../../../application-framework/core-file-kit/application-files/application-sandbox/document.md).
        
        function getFilePath(context: Context, fileName: string): string {
          const filePath: string = context.cacheDir + '/' + fileName;
          return filePath;
        }
        
    -   Method 2: Obtain the file descriptor of the image through the sandbox path. For details, see [file.fs API Reference](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-file-fs). To use this method, you must import the @kit.CoreFileKit module first.
        
        function getFileFd(context: Context, fileName: string): number | undefined {
          const filePath: string = context.cacheDir + '/' + fileName;
          const file: fs.File = fs.openSync(filePath, fs.OpenMode.READ\_ONLY);
          const fd: number = file?.fd;
          return fd;
        }
        
    -   Method 3: Obtain the array buffer of the resource file through the resource manager. For details, see [ResourceManager API Reference](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-resource-manager#getrawfilecontent9-1). To use this method, you must import the @kit.LocalizationKit module first.
        
        async function getFileBuffer(context: Context, fileName: string): Promise<ArrayBuffer | undefined> {
          try {
            const resourceMgr: resourceManager.ResourceManager = context.resourceManager;
            // Obtain the resource file content. The Uint8Array is returned.
            const fileData: Uint8Array = await resourceMgr.getRawFileContent(fileName);
            console.info('Successfully get the RawFileContent.');
            // Convert the array to an ArrayBuffer and return the ArrayBuffer.
            const buffer: ArrayBuffer = fileData.buffer.slice(0);
            return buffer;
          } catch (error) {
            console.error(\`Failed to get the RawFileContent with error: ${error}.\`);
            return undefined;
          }
        }
        
    -   Method 4: Obtain the raw file descriptor of the resource file through the resource manager. For details, see [ResourceManager API Reference](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-resource-manager#getrawfd9-1). To use this method, you must import the @kit.LocalizationKit module first.
        
        async function getRawFd(context: Context, fileName: string): Promise<resourceManager.RawFileDescriptor | undefined> {
          try {
            const resourceMgr: resourceManager.ResourceManager = context.resourceManager;
            const rawFileDescriptor: resourceManager.RawFileDescriptor = await resourceMgr.getRawFd(fileName);
            console.info('Successfully get the RawFileDescriptor.');
            return rawFileDescriptor;
          } catch (error) {
            console.error(\`Failed to get the RawFileDescriptor with error: ${error}.\`);
            return undefined;
          }
        }
        
3.  Create an ImageSource instance.
    
    -   Method 1: Create an ImageSource instance using the sandbox path. The sandbox path can be obtained by using method 1 in step 2.
        
        // path indicates the obtained sandbox path.
        const imageSource : image.ImageSource = image.createImageSource(filePath);
        
    -   Method 2: Create an ImageSource instance using the file descriptor. The file descriptor can be obtained by using method 2 in step 2.
        
        // fd is the obtained file descriptor.
        const imageSource: image.ImageSource = image.createImageSource(fd);
        
    -   Method 3: Create an ImageSource instance using an array buffer. The array buffer can be obtained by using method 3 in step 2.
        
        const imageSource: image.ImageSource = image.createImageSource(buffer);
        
    -   Method 4: Create an ImageSource instance using the raw file descriptor of the resource file. The raw file descriptor can be obtained by using method 4 in step 2.
        
        const imageSource: image.ImageSource = image.createImageSource(rawFileDescriptor);
        
4.  Set **DecodingOptions** and decode the image to obtain a PixelMap.
    
    Carry out decoding after the setting.
    
    async createPixelMap(imageSource: image.ImageSource | undefined): Promise<image.PixelMap | undefined> {
      if (!imageSource) {
        console.error('imageSource is undefined.');
        return undefined;
      }
      // Set the decoding options.
      let decodingOptions: image.DecodingOptions = {
        editable: true,
        desiredPixelFormat: image.PixelMapFormat.RGBA\_8888,
        // If AUTO is passed, decoding is performed based on the image format and device capabilities. If the image is an HDR resource and the device supports HDR decoding, an HDR PixelMap is obtained after decoding.
        desiredDynamicRange: image.DecodingDynamicRange.HDR,
      };
    
      try {
        // Generate a PixelMap and return it.
        const pixelMap = await imageSource.createPixelMap(decodingOptions);
        if (pixelMap) {
          console.info('Create PixelMap successfully.');
          // Check whether the PixelMap is the HDR content.
          let imageInfo = await pixelMap.getImageInfo();
          console.info(\`Create PixelMap successfully with imageInfo.isHdr: ${imageInfo.isHdr}.\`);
          return pixelMap;
        } else {
          console.info('Create PixelMap failed.');
          return undefined;
        }
      } catch (error) {
        console.error(\`Failed to create PixelMap: ${error}.\`);
        return undefined;
      }
    }
    
    After the decoding is complete and the PixelMap is obtained, you can perform subsequent [image processing](../../image-editing-and-processing/using-pixelmap-to-transform-images/document.md).
    
5.  Release the PixelMap and ImageSource instances.
    
    Ensure that the asynchronous operations of the PixelMap and ImageSource instances have finished executing. After these variables are no longer needed, you can manually call the APIs below to release them.
    
    async release(pixelMap: image.PixelMap | undefined, imageSource: image.ImageSource | undefined) {
      pixelMap?.release();
      pixelMap = undefined;
      imageSource?.release();
      imageSource = undefined;
    }
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b0/v3/CJRKKKSxRsaYzhXyLqqZrg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062040Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=11B94AD852CA4FC0DD26E744E176E98DDEA9606558DF230EB3A74C1149E66DBC)
    
    1.  When to release the ImageSource instance: After successfully executing **createPixelMap** and obtaining the PixelMap instance, if you are certain that no other APIs of ImageSource will be used, you can manually release the ImageSource instance. Since the PixelMap instance obtained from decoding is independent, releasing the ImageSource instance will not make the PixelMap instance unusable.
    2.  When to release the PixelMap instance: If you are using the [**Image** component](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-basic-components-image) for displaying images, there is no need to manually release the PixelMap instance, as the Image component will automatically manage the PixelMap instance passed to it. If your application handles the PixelMap instance on its own, you are advised to manually release the PixelMap instance of the old page during page transitions or when the application switches to the background. In scenarios where memory resources are tight, you are advised to release the PixelMap instances of all invisible pages except the current one.
