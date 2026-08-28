# Using PixelMap for PixelMap Operations

To process a certain area in an image, you can perform PixelMap operations, which are usually used to beautify the image.

As shown in the figure below, the pixel data of a rectangle in an image is read, modified, and then written back to the corresponding area of the original image.

**Figure 1** PixelMap operation

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/28/v3/p7SNxNhFRWane2QemVlKjA/en-us_image_0000002568684901.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062041Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2C5E2C07FA18964F74212D2C35FB71C5B984BA8D57F79B82585B538B72116301)

#### How to Develop

Read the [API reference](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-image-pixelmap) for APIs related to PixelMap operations.

1.  Complete [image decoding](../../image-decoding/using-imagesource-to-decode-images/document.md) and obtain a PixelMap object.
    
2.  Obtain information from the PixelMap object.
    
    import { image } from '@kit.ImageKit';
    import { BusinessError } from '@kit.BasicServicesKit';
    // Obtain the total number of bytes of this PixelMap object.
    let pixelBytesNumber: number = pixelMap.getPixelBytesNumber();
    // Obtain the number of bytes per row of this PixelMap object.
    let rowBytes: number = pixelMap.getBytesNumberPerRow();
    // Obtain the pixel density of this PixelMap object. Pixel density refers to the number of pixels per inch of an image. A larger value of the pixel density indicates a finer image.
    let density: number = pixelMap.getDensity();
    
3.  Read and modify the pixel data of the target area, and write the modified data back to the original image.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6c/v3/5n5sFy-6Sm2Kh01u23V7iA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062041Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5F7C97FDC75FBA23CE10BC2CB58A21097B0A457DBC7C38453ABB10B63BDA8BA4)
    
    To prevent issues with the PixelMap due to inconsistent pixel formats, you are advised to use **readPixelsToBuffer** with **writeBufferToPixels** and **readPixels** with **writePixels** in corresponding pairs.
    
    import { image } from '@kit.ImageKit';
    import { BusinessError } from '@kit.BasicServicesKit';
    // Scenario 1: Read and modify data of the entire image.
    // Read the pixel data of the PixelMap based on the PixelMap's pixel format and write the data to the buffer.
    const buffer = new ArrayBuffer(pixelBytesNumber);
    pixelMap.readPixelsToBuffer(buffer).then(() => {
      console.info('Succeeded in reading image pixel data.');
    }).catch((error : BusinessError) => {
      console.error('Failed to read image pixel data. The error is: ' + error);
    })
    // Read the pixel data in the buffer based on the PixelMap's pixel format and write the data to the PixelMap.
    pixelMap.writeBufferToPixels(buffer).then(() => {
      console.info('Succeeded in writing image pixel data.');
    }).catch((error : BusinessError) => {
      console.error('Failed to write image pixel data. The error is: ' + error);
    })
    
    // Scenario 2: Read and modify image data in a specified area.
    // Read the pixel data in the area specified by PositionArea.region in the PixelMap in the BGRA\_8888 format and write the data to the PositionArea.pixels buffer.
    const area : image.PositionArea = {
      pixels: new ArrayBuffer(8),
      offset: 0,
      stride: 8,
      region: { size: { height: 1, width: 2 }, x: 0, y: 0 }
    }
    pixelMap.readPixels(area).then(() => {
      console.info('Succeeded in reading the image data in the area.');
    }).catch((error : BusinessError) => {
      console.error('Failed to read the image data in the area. The error is: ' + error);
    })
    // Read the pixel data in the PositionArea.pixels buffer in the BGRA\_8888 format and write the data to the area specified by PositionArea.region in the PixelMap.
    pixelMap.writePixels(area).then(() => {
      console.info('Succeeded in writing the image data in the area.');
    }).catch((error : BusinessError) => {
      console.error('Failed to write the image data in the area. The error is: ' + error);
    })
    

#### Development Example

## Copying (Deep Copy) a PixelMap and Changing Its Pixel Format

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a4/v3/JqzWdNVvT0il13VHm7lnPg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062041Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=CFA00905AC5D73C567F36F15CC516CE7D5B374116E6067F21579CC9998DB9449)

-   This method only copies the basic content of a PixelMap; it does not support copying color gamut or HDR metadata. If you do not need to change the pixel format of the new PixelMap, use [clone](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-image-pixelmap#clone18) or [cloneSync](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-image-pixelmap#clonesync18) instead.
-   This method does not support converting the new PixelMap to the following pixel formats: RGBA\_1010102, YCBCR\_P010, YCRCB\_P010, and ASTC\_4x4.

1.  Complete [image decoding](../../image-decoding/using-imagesource-to-decode-images/document.md) and obtain a PixelMap object.
    
2.  Refer to the following code to perform a deep copy of the PixelMap.
    
    /\*\*
     \* Copy (deep copy) a PixelMap and change its pixel format.
     \*
     \* @param pixelMap - The original PixelMap.
     \* @param desiredPixelFormat - Pixel format of the new PixelMap. If this parameter is not specified, the pixel format of the current PixelMap is used.
     \* @return Returns a new PixelMap.
     \*/
    function clonePixelMap(pixelMap: PixelMap, desiredPixelFormat?: image.PixelMapFormat): PixelMap {
      // Obtain the image information of the original PixelMap.
      const imageInfo = pixelMap.getImageInfoSync();
      // Read the pixel data of the original PixelMap and write the data to the buffer in the original pixel format.
      const buffer = new ArrayBuffer(pixelMap.getPixelBytesNumber());
      pixelMap.readPixelsToBufferSync(buffer);
    
      // Generate initialization options based on the image information of the original PixelMap.
      const options: image.InitializationOptions = {
        // Pixel format of the data source, which must match that of the original PixelMap. Otherwise, the new PixelMap will display abnormally.
        srcPixelFormat: imageInfo.pixelFormat,
        // Pixel format of the new PixelMap.
        pixelFormat: desiredPixelFormat || imageInfo.pixelFormat,
        // Alpha type of the new PixelMap.
        alphaType: imageInfo.alphaType,
        // Size of the new PixelMap, which must match that of the original PixelMap. Scaling to other sizes is not supported.
        size: imageInfo.size
      };
    
      // Create a new PixelMap based on the pixel data and initialization options.
      return image.createPixelMapSync(buffer, options);
    }
    

## Vertically Concatenating Two PixelMaps of the Same Width into a Single Long Image

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/65/v3/zlXNHqA5Rbi4csohWeUr0A/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062041Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=35923A53A58898788F824151751B41046B9ABB01260F67AFEA43739EC7B5E354)

This method supports only PixelMaps with the following pixel formats: RGBA\_8888, BGRA\_8888, and RGBA\_F16.

1.  Complete [image decoding](../../image-decoding/using-imagesource-to-decode-images/document.md) and obtain two PixelMap objects with the same width and pixel format.
    
2.  Refer to the following code to concatenate the two PixelMaps.
    
    function concatPixelMap(pixelMap1: PixelMap, pixelMap2: PixelMap): PixelMap {
      // Read the pixel data of pixelMap1 to area1.pixels.
      const imageInfo1 = pixelMap1.getImageInfoSync();
      const area1: image.PositionArea = {
        pixels: new ArrayBuffer(pixelMap1.getPixelBytesNumber()),
        offset: 0,
        stride: pixelMap1.getBytesNumberPerRow(),
        region: {
          size: imageInfo1.size,
          x: 0,
          y: 0
        }
      };
      pixelMap1.readPixels(area1);
    
      // Read the pixel data of pixelMap2 to area2.pixels.
      const imageInfo2 = pixelMap2.getImageInfoSync();
      const area2: image.PositionArea = {
        pixels: new ArrayBuffer(pixelMap2.getPixelBytesNumber()),
        offset: 0,
        stride: pixelMap2.getBytesNumberPerRow(),
        region: {
          size: imageInfo2.size,
          x: 0,
          y: 0
        }
      };
      pixelMap2.readPixels(area2);
    
      // Create an empty PixelMap with the same width as pixelMap1/pixelMap2 and height equal to the sum of both.
      const options: image.InitializationOptions = {
        srcPixelFormat: imageInfo1.pixelFormat,
        pixelFormat: imageInfo1.pixelFormat,
        size: {
          width: imageInfo1.size.width,
          height: imageInfo1.size.height + imageInfo2.size.height
        }
      };
      const newPixelMap = image.createPixelMapSync(options);
    
      // Write the pixel data of pixelMap1 and pixelMap2 to the new PixelMap in sequence.
      newPixelMap.writePixels(area1);
      area2.region.y = imageInfo1.size.height; // The pixel data of pixelMap2 should start writing from the row after the last row of pixelMap1.
      newPixelMap.writePixels(area2);
    
      return newPixelMap;
    }
