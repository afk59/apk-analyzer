# Opening and Saving a PDF Document

#### Use Cases

Loads a PDF document from a local path to preview the PDF document. You can save a PDF document that contains annotations.

The capabilities are the same as those of pdfService. For details about the differences, see the use cases of [Opening and Saving a PDF Document](../../pdfservice-capabilities/opening-and-saving-a-pdf-document/document.md) of pdfService.

#### API Description

| 
API Name

 | 

Description

 |
| :-- | :-- |
| 

[loadDocument](https://developer.huawei.com/consumer/en/doc/harmonyos-references/pdf-arkts-pdfviewmanage#section073321844615)(path: string, password?: string, initPageIndex?: number, onProgress?: Callback<number>): Promise<ParseResult>

 | 

Load the PDF document.

 |
| 

[saveDocument](https://developer.huawei.com/consumer/en/doc/harmonyos-references/pdf-arkts-pdfviewmanage#section1641615224414)(path: string, onProgress?: Callback<number>): Promise<number>

 | 

Saves a PDF document. This API returns the result asynchronously through a promise.

 |

#### Sample Code

1.  Load the PDF document in the **aboutToAppear** function.
2.  Call the PdfView preview component to render the display.
3.  Call the **saveDocument** method via the **savePdfDocument** button to save the PDF document as a new one.

import { pdfService, PdfView, pdfViewManager } from '@kit.PDFKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

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

  build() {
    Column() {    
      // Save the PDF document.
      Button('savePdfDocument').onClick(async () => {
        if (this.loadResult === pdfService.ParseResult.PARSE\_SUCCESS) {
          let savePath = this.context.filesDir + '/savePdfDocument.pdf';
          let result = await this.controller.saveDocument(savePath);
          hilog.info(0x0000, 'PdfPage', 'savePdfDocument %{public}s!', result ? 'success' : 'fail');
        }
      })
      PdfView({
        controller: this.controller,
        pageFit: pdfService.PageFit.FIT\_WIDTH,
        showScroll: true
      })
        .id('pdfview\_app\_view')
        .layoutWeight(1);
    }
    .width('100%')
    .height('100%')
  }
}
