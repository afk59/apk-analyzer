# Drawing Images (ArkTS)

A bitmap is a data structure used to store and represent images in memory. It is a collection of uncompressed pixels. Images in formats such as JPEG and PNG are compressed, and are different from bitmaps. If you want to draw a JPEG or PNG image on the screen, you need to decode the image into a bitmap first. For details, see the image decoding section in [Image Kit](../../../../../media/image-kit/about-this-kit/document.md).

Currently, bitmap drawing in Drawing (ArkTS) depends on PixelMap, which can be used to read or write image data and obtain image information. For details about the APIs, see [PixelMap](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-image-pixelmap).

1.  Create a **PixelMap** instance.
    
    You can use multiple APIs to create a PixelMap. The following uses createPixelMapSync() as an example. For details about more creation modes and APIs, see @ohos.multimedia.image (Image Processing).
    
    // Image width and height
    let width = 600;
    let height = 400;
    // Byte length. Each pixel of RGBA\_8888 occupies four bytes.
    let byteLength = width \* height \* 4;
    const color: ArrayBuffer = new ArrayBuffer(byteLength);
    let bufferArr = new Uint8Array(color);
    for (let i = 0; i < bufferArr.length; i += 4) {
      // Traverse and edit each pixel to form red, green, and blue stripes.
      bufferArr\[i\] = 0x00;
      bufferArr\[i+1\] = 0x00;
      bufferArr\[i+2\] = 0x00;
      bufferArr\[i+3\] = 0xFF;
      let n = Math.floor(i / 80) % 3;
      if (n == 0) {
        bufferArr\[i\] = 0xFF;
      } else if (n == 1) {
        bufferArr\[i+1\] = 0xFF;
      } else {
        bufferArr\[i+2\] = 0xFF;
      }
    }
    // Set pixel attributes.
    let opts: image.InitializationOptions =
      { editable: true, pixelFormat: image.PixelMapFormat.RGBA\_8888, size: { height: height, width: width } };
    // Create a PixelMap instance.
    pixelMap = image.createPixelMapSync(color, opts);
    
2.  (Optional) Edit pixels in the PixelMap. If no pixel needs to be edited, skip this step.
    
    Several APIs are available to edit pixels in a PixelMap. The following uses writePixelsSync() as an example. For details about other methods and APIs, please refer to [PixelMap](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-image-pixelmap).
    
    // Set the width and height of the editing area.
    let innerWidth = 400;
    let innerHeight = 200;
    // Set the byte length of the editing area. Each pixel in RGBA\_8888 occupies four bytes.
    let innerByteLength = innerWidth \* innerHeight \* 4;
    const innerColor: ArrayBuffer = new ArrayBuffer(innerByteLength);
    let innerBufferArr = new Uint8Array(innerColor);
    for (let i = 0; i < innerBufferArr.length; i += 4) {
      // Set the pixels in the editing area to black and white stripes.
      let n = Math.floor(i / 80) % 2;
      if (n == 0) {
        innerBufferArr\[i\] = 0x00;
        innerBufferArr\[i+1\] = 0x00;
        innerBufferArr\[i+2\] = 0x00;
      } else {
        innerBufferArr\[i\] = 0xFF;
        innerBufferArr\[i+1\] = 0xFF;
        innerBufferArr\[i+2\] = 0xFF;
      }
      innerBufferArr\[i+3\] = 0xFF;
    }
    // Set the pixels, width, height, and offset of the editing area.
    const area: image.PositionArea = {
      pixels: innerColor,
      offset: 0,
      stride: innerWidth \* 4,
      region: { size: { height: innerHeight, width: innerWidth }, x: 100, y: 100 }
    };
    // Edit the bitmap to form black and white stripes in the middle.
    pixelMap.writePixelsSync(area);
    //To display the entire image, change the start point of the drawing to (0, 0).
    canvas.drawImage(pixelMap, 0, 0);
    
3.  Draw the PixelMap.
    
    You need to use the Canva APIs to draw the bitmap. The following uses drawImage() as an example. For details about more methods and APIs, see [drawing.Canvas](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-graphics-drawing-canvas).
    
    The drawImage() function accepts four parameters. The first parameter is the PixelMap created above, the second parameter is the x-coordinate of the upper left corner of the image to be drawn, the third parameter is the y-coordinate of the upper left corner, and the fourth parameter is the sampling option object. By default, the original sampling option object constructed without any parameter is used.
    
    //To display the entire image, change the start point of the drawing to (0, 0).
    canvas.drawImage(pixelMap, 0, 0);
    
    The drawing effect is as follows:
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/68/v3/aVyJWQiIQJG_AipgErw5jw/en-us_image_0000002568684941.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062049Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F596922022ED3134D366F6F7940AF4943E81DD43AED29D38DCCF74351B973841)
