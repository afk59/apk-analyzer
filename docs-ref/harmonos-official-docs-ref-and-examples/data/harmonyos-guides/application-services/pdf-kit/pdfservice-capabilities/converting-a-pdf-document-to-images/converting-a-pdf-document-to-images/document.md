# Converting a PDF Document to Images

#### Use Cases

Converts an entire PDF document into images. Each page is converted into an image, and all images are stored in the same folder.

For details about the supported image formats, see [ImageFormat](https://developer.huawei.com/consumer/en/doc/harmonyos-references/pdf-arkts-pdfservice#section1713111745313).

#### API Description

| 
API Name

 | 

Description

 |
| :-- | :-- |
| 

[convertToImage](https://developer.huawei.com/consumer/en/doc/harmonyos-references/pdf-arkts-pdfservice#section1029783924311)(path: string, format: ImageFormat, onProgress?: Callback<number>): boolean

 | 

Converts a PDF document to images.

 |

#### Sample Code

1.  Call the **loadDocument** method to load a PDF document.
2.  Set the folder where the output images are to be stored. Call the **convertToImage** method to convert all pages of the PDF document to images.

import { fileIo as fs } from '@kit.CoreFileKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { pdfService } from '@kit.PDFKit';

@Entry
@Component
struct PdfPage {
  private pdfDocument: pdfService.PdfDocument = new pdfService.PdfDocument();
  private context = this.getUIContext().getHostContext() as Context;
  private loadResult: pdfService.ParseResult = pdfService.ParseResult.PARSE\_ERROR\_FORMAT;

  aboutToAppear(): void {
    // Ensure that the **input.pdf** document exists in the sandbox directory.
    let filePath = this.context.filesDir + '/input.pdf';
    this.loadResult = this.pdfDocument.loadDocument(filePath);
  }

  build() {
    Column() {
      // Obtain it as an image and save it to the app sandbox.
      Button('convertToImage').onClick(async () => {
        if (this.loadResult === pdfService.ParseResult.PARSE\_SUCCESS) {
          let outputPath = this.getUIContext().getHostContext()?.filesDir + '/output/';
          // Convert all pages into PNG images and save them to the **output** folder. Ensure that the **output** folder exists.
          let res = this.pdfDocument.convertToImage(outputPath, pdfService.ImageFormat.PNG);
          hilog.info(0x0000, 'PdfPage', 'convertToImage %{public}s!', res ? 'success' : 'fail');
        }
      })
    }
  }
}
