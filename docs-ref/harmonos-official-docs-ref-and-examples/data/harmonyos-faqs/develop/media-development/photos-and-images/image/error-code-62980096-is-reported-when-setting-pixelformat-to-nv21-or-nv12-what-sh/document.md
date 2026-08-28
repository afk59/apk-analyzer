# Error code 62980096 is reported when setting pixelFormat to NV21 or NV12. What should I do?

**Symptom**

When **createPixelMap** is called to set **pixelFormat** to NV21 or NV12, error code 62980096 is reported. You are advised to perform the following checks:

Check whether the value of **pixelFormat** is correct.

Check whether other parameters of **createPixelMap** meet the requirements.

Check whether the system environment supports the NV21 or NV12 formats.

If the issue persists, refer to the official documentation or contact technical support.

**Solution**

The enum **pixelFormat** is used by **ImageSource**. To create a PixelMap for an image in NV21 or NV12 format, perform the following steps:

1.  Use **createImageSource** to create an image source.
    
    In this API, set the **sourceOption** parameter as follows: For **sourcePixelFormat**, set it to **8** for the NV21 format or **9** for the NV12 format. Set **sourceSize** to the width and height of the original YUV image, where the width must be an even number.
    
2.  Use **createPixelMap** of **ImageSource** to create a PixelMap.

Refer to the code snippet below.

import { image } from '@kit.ImageKit';

@Entry
@Component
struct Index {
  @State message: string = 'NV21AndNV12ToPixelMap';
  @State private pixelMap: PixelMap | null = null;
  @State private pixelMap2: PixelMap | null = null;

  build() {
    Row() {
      Column() {
        Image(this.pixelMap)
          .width(200).height(200).margin(15)
        Text(this.message)
          .fontSize(50)
          .fontWeight(FontWeight.Bold)
          .onClick(async () => {
            let resourceManager = this.getUIContext().getHostContext()!.resourceManager
            let imageArray = await resourceManager.getMediaContent($r("app.media.sample14\_NV21\_fromJPG\_510X510"));
            let pixelBuffer = new Uint8Array(imageArray).buffer as Object as ArrayBuffer;
            // The value 8 of the sourcePixelFormat parameter corresponds to NV21 format, and 9 corresponds to NV12 format; The sourceSize parameter needs to set the width and height (the width and height data of the original yuv image), and the width value cannot be odd.
            let sourceOptions: image.SourceOptions =
              { sourceDensity: 120, sourcePixelFormat: 8, sourceSize: { width: 510, height: 510 } };
            let imageResource = image.createImageSource(pixelBuffer, sourceOptions);
            let opts: image.DecodingOptions = { editable: true }
            this.pixelMap = await imageResource.createPixelMap(opts);

            let imageArray2 = await resourceManager.getMediaContent($r('app.media.sample10\_NV12\_fromJPG\_510X510'));
            let pixelBuffer2 = new Uint8Array(imageArray2).buffer as Object as ArrayBuffer;
            // The value 8 of the sourcePixelFormat parameter corresponds to NV21 format, and 9 corresponds to NV12 format; The sourceSize parameter needs to set the width and height (the width and height data of the original yuv image), and the width value cannot be odd.
            let sourceOptions2: image.SourceOptions =
              { sourceDensity: 120, sourcePixelFormat: 9, sourceSize: { width: 510, height: 510 } };
            let imageResource2 = image.createImageSource(pixelBuffer2, sourceOptions2);
            let opts2: image.DecodingOptions = { editable: true }
            this.pixelMap2 = await imageResource2.createPixelMap(opts2);
          })
        Image(this.pixelMap2)
          .width(200).height(200).margin(15)
      }
      .width('100%')
    }
    .height('100%')
  }
}
