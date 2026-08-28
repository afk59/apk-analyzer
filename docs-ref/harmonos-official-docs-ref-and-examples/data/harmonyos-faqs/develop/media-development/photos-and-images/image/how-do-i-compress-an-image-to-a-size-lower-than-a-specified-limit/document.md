# How do I compress an image to a size lower than a specified limit?

**Question**

Only quality compression is provided. No other API is available for compressing an image to a size less than a specified limit, for example, compressing a PixelMap to 30 KB. What should I do?

**Answer**

Currently, there is no API for compressing a PixelMap to a size below a specified limit. However, you can achieve the desired size by iteratively compress the PixelMap as follows:

1.  Call the custom API **compressedImage** and pass the PixelMap of the image to be compressed and the target compression size.
2.  Check, when the **quality** parameter is set to **0**, whether the minimum size of the image that can be compressed by **packToData** meets the specified limit. If it does, use a binary search with **packToData** to find the quality value that is closest to the target size for iterative compression. If not, use **scale** to scale down the image, use a **while** loop to reduce the image size by 0.4 times in each iteration, and then use **packToData** (with **quality** set to **0**) to obtain the size of the compressed image. Finally, you can obtain the compressed image data that is closest to the target size.
    
    Note that compressing an image using **quality** does not change the image size. If the quality value is too small, artifacts may occur in the image. It is recommended that the quality value be greater than or equal to 80. On the other hand, when **scale** is used, the image dimensions will be directly altered. It is recommended that the image resolution be greater than 1080\*1080 and the width and height be compressed proportionally to avoid image distortion.
    
    import { image } from '@kit.ImageKit';
    import { fileIo } from '@kit.CoreFileKit';
    import { common } from '@kit.AbilityKit';
    
    class CompressedImageInfo {
      imageUri: string = ""; // URI of compressed image storage location
      imageByteLength: number = 0; // Compressed image byte length
    }
    
    /\*\*
     \* Image compression, saving
     \* @param sourcePixelMap: PixelMap object of the original image to be compressed
     \* @param maxCompressedImageSize: Specify the compression target size for the image, in kb
     \* @returns compressedImageInfo: Return the final compressed image information
     \*/
    async function compressedImage(sourcePixelMap: image.PixelMap,
      maxCompressedImageSize: number): Promise<CompressedImageInfo> {
      // Create an ImagePacker object for image encoding
      const imagePackerApi = image.createImagePacker();
      const IMAGE\_QUALITY = 80;
      const packOpts: image.PackingOption = { format: "image/jpeg", quality: IMAGE\_QUALITY };
      // Encode through PixelMap. Compressed ImageData is the image file stream obtained by packaging.
      let compressedImageData: ArrayBuffer = await imagePackerApi.packToData(sourcePixelMap, packOpts);
    
      const maxCompressedImageByte = maxCompressedImageSize \* 1024;
      // Image compression. First, determine whether the minimum byte size of the image that can be compressed by packToData meets the specified image compression size when setting the image quality parameter quality to 80.
      // If satisfied, use the packToData method to binary search for the quality closest to the specified image compression target size to compress the image.
      // If it is not satisfied, use scale to scale the image first, use a while loop to scale the image by 0.4 times each time,
      // then use packToData (with the image quality parameter quality set to 80) to obtain the compressed image size,
      // and finally find the compressed image data with the closest scaling factor to the specified image compression target size.
      if (maxCompressedImageByte > compressedImageData.byteLength) {
        // Using packToData binary compression to obtain image file streams
        compressedImageData =
          await packingImage(compressedImageData, sourcePixelMap, IMAGE\_QUALITY, maxCompressedImageByte);
      } else {
        // Use scale to scale the image first, use a while loop to decrease the scale by 0.4 times each time, then use packToData (with the image quality parameter quality set to 80) to obtain the compressed image size,
        // and finally find the compressed image data with the closest scaling factor to the specified image compression target size
        let imageScale = 1;
        const REDUCE\_SCALE = 0.4;
        // Determine whether the compressed image size is greater than the specified compression target size. If it is, continue to reduce the scaling factor for compression.
        while (compressedImageData.byteLength > maxCompressedImageByte) {
          if (imageScale > 0) {
            // Performance knowledge point: As scale directly modifies the PixelMap data of the image, binary search for scale scaling factor is not applicable. Here, we use a cyclic decrease of 0.4 times to scale the image,
            // in order to find and determine the most suitable scaling factor. If you do not have high requirements for image compression quality,
            // it is recommended to increase the scaling factor reduceScale each time to reduce loops and improve scale compression performance.
            imageScale = imageScale - REDUCE\_SCALE;
            await sourcePixelMap.scale(imageScale, imageScale);
            compressedImageData = await packToData(sourcePixelMap, IMAGE\_QUALITY);
          } else {
            // When the imageScale scaling is less than or equal to 0, it is meaningless and the compression ends. We do not consider the case where the image scaling factor is less than reduceScale here.
            break;
          }
        }
      }
      // Save the image and return the compressed image information.
      const compressedImageInfo: CompressedImageInfo = await saveImage(compressedImageData);
      return compressedImageInfo;
    }
    
    /\*\*
     \* Packing compression
     \* @param sourcePixelMap: PixelMap of the original image to be compressed
     \* @param imageQuality: Image quality parameters
     \* @returns data: Return compressed image data
     \*/
    async function packToData(sourcePixelMap: image.PixelMap, imageQuality: number): Promise<ArrayBuffer> {
      const imagePackerApi = image.createImagePacker();
      const packOpts: image.PackingOption = { format: "image/jpeg", quality: imageQuality };
      const data: ArrayBuffer = await imagePackerApi.packToData(sourcePixelMap, packOpts);
      return data;
    }
    
    /\*\*
     \* Packing binary method cyclic compression
     \* @param compressedImageData: Arrays Buffer for image compression
     \* @param sourcePixelMap: PixelMap of the original image to be compressed
     \* @param imageQuality: Image quality parameters
     \* @param maxCompressedImageByte: Compress the byte length of the target image
     \* @returns compressedImageData: Return the compressed image data after binary packToData
     \*/
    async function packingImage(compressedImageData: ArrayBuffer, sourcePixelMap: image.PixelMap, imageQuality: number,
      maxCompressedImageByte: number): Promise<ArrayBuffer> {
      // The range of image quality parameters is 80-100. Here, an array for packToData binary image quality parameters is created with 5 as the minimum binary unit.
      const packingArray: number\[\] = \[\];
      const DICHOTOMY\_ACCURACY = 5;
      // Performance knowledge point: If the requirements for image compression quality are not high, it is recommended to increase the minimum binary unit dichotomyAccuracy,
      // reduce loops, and improve packToData compression performance.
      for (let i = 80; i <= 100; i += DICHOTOMY\_ACCURACY) {
        packingArray.push(i);
      }
      let left = 0;
      let right = packingArray.length - 1;
      // Binary compressed image
      while (left <= right) {
        const mid = Math.floor((left + right) / 2);
        imageQuality = packingArray\[mid\];
        compressedImageData = await packToData(sourcePixelMap, imageQuality);
        // Perform packToData compression based on the input image quality parameters and return the compressed image file stream data.
        if (compressedImageData.byteLength <= maxCompressedImageByte) {
          left = mid + 1;
          if (mid === packingArray.length - 1) {
            break;
          }
          // Obtain the compressed image file stream data with the next binary image quality parameter (mid+1)
          compressedImageData = await packToData(sourcePixelMap, packingArray\[mid + 1\]);
          // Determine whether the size of the image compressed with the next image quality parameter (mid+1) is greater than the specified compression target size of the image.
          // If it is greater than, it indicates that the current image quality parameter (mid) compresses the image size closest to the compression target size of the specified image.
          // Pass in the current image quality parameter mid to obtain the final compressed data of the target image.
          if (compressedImageData.byteLength > maxCompressedImageByte) {
            compressedImageData = await packToData(sourcePixelMap, packingArray\[mid\]);
            break;
          }
        } else {
          // The target value is not in the right half of the current range. Move the right boundary of the search range to the left to narrow down the search range
          // and continue searching for the left half in the next iteration.
          right = mid - 1;
        }
      }
      return compressedImageData;
    }
    
    /\*\*
     \* pictures saving
     \* @param compressedImageData: Compressed image data
     \* @returns compressedImageInfo: Return compressed image information
     \*/
    async function saveImage(compressedImageData: ArrayBuffer): Promise<CompressedImageInfo> {
      // Obtain the context from the component and ensure that the return value of this.getUIContext().getHostContext() is UIAbilityContext
      const context: Context = this.getUIContext().getHostContext() as common.UIAbilityContext;
      // Define the compressed image URI to be saved. AfterCompression.jpeg represents the compressed image.
      const compressedImageUri: string = context.filesDir + '/' + 'afterCompression.jpeg';
      try {
        const res = fileIo.accessSync(compressedImageUri);
        if (res) {
          // If the image afterCompression.jpeg already exists, delete it
          fileIo.unlinkSync(compressedImageUri);
        }
      } catch (err) {
        console.error(\`AccessSync failed with error message: ${err.message}, error code: ${err.code}\`);
      }
      // Knowledge point: Save images. Obtain the final compressed image data compressed ImageData and save the image.
      // Compress image data and write it to a file
      const file: fileIo.File = fileIo.openSync(compressedImageUri, fileIo.OpenMode.READ\_WRITE | fileIo.OpenMode.CREATE);
      fileIo.writeSync(file.fd, compressedImageData);
      fileIo.closeSync(file);
      // Obtain compressed image information
      let compressedImageInfo: CompressedImageInfo = new CompressedImageInfo();
      compressedImageInfo.imageUri = compressedImageUri;
      compressedImageInfo.imageByteLength = compressedImageData.byteLength;
      return compressedImageInfo;
    }
