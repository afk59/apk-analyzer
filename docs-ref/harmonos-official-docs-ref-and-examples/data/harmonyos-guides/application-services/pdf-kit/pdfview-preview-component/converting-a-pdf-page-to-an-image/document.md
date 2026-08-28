# Converting a PDF Page to an Image

#### Use Cases

Call the [getPagePixelMap](https://developer.huawei.com/consumer/en/doc/harmonyos-references/pdf-arkts-pdfviewmanage#section858145014542) method to convert the specified PDF page into an image.

#### API Description

| 
API Name

 | 

Description

 |
| :-- | :-- |
| 

[getPagePixelMap](https://developer.huawei.com/consumer/en/doc/harmonyos-references/pdf-arkts-pdfviewmanage#section858145014542)(pageIndex: number, isSync?: boolean): Promise<image.PixelMap>

 | 

Obtains the thumbnail of the corresponding PDF page. This API returns the result asynchronously through a promise.

 |

#### Sample Code

1.  Call the **loadDocument** method to load a PDF document.
2.  Call the **getPagePixelMap** method to obtain the **image.PixelMap** object.
3.  Convert **image.PixelMap** into a binary image file and save it.

import { pdfService, pdfViewManager } from '@kit.PDFKit';
import { image } from '@kit.ImageKit';
import { fileIo as fs } from '@kit.CoreFileKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct PdfPage {
  private controller: pdfViewManager.PdfController = new pdfViewManager.PdfController();
  private context = this.getUIContext().getHostContext() as Context;
  private loadResult: pdfService.ParseResult = pdfService.ParseResult.PARSE\_ERROR\_FORMAT;

  aboutToAppear(): void {
    // Ensure that the **input.pdf** document exists in the sandbox directory.
    let filePath = this.context.filesDir + '/input.pdf';
    (async () => {
      this.loadResult = await this.controller.loadDocument(filePath);
    })()
  }

  // Convert **pixelMap** to the image format.
  pixelMap2Buffer(pixelMap: image.PixelMap): Promise<ArrayBuffer> {
    return new Promise((resolve, reject) => {
      /\*\*
       Set packaging parameters.
       format: image packaging format.
       quality: quality of the JPEG output image.
       \*/
      let packOpts: image.PackingOption = { format: 'image/jpeg', quality: 98 }
      // Create an **ImagePacker** instance.
      const imagePackerApi = image.createImagePacker()
      imagePackerApi.packToData(pixelMap, packOpts).then((buffer: ArrayBuffer) => {
        resolve(buffer)
      }).catch((err: BusinessError) => {
        reject()
      })
    })
  }

  build() {
    Column() {
      // Convert it into an image and save it to the app sandbox.
      Button('getPagePixelMap').onClick(async () => {
        if (this.loadResult === pdfService.ParseResult.PARSE\_SUCCESS) {
          let pixmap: image.PixelMap = await this.controller.getPagePixelMap(0, true);
          if (!pixmap) {
            return
          }
          const imgBuffer = await this.pixelMap2Buffer(pixmap)
          try {
            const file =
              fs.openSync(this.context.filesDir + \`/${Date.now()}.png\`, fs.OpenMode.READ\_WRITE | fs.OpenMode.CREATE);
            await fs.write(file.fd, imgBuffer);
          // Close the document.
            await fs.close(file.fd)
          } catch (e) {
            let error: BusinessError = e as BusinessError;
            console.error(\`Code: ${error.code}, message: ${error.message} \`);
          }
        }
      })
    }
  }
}
