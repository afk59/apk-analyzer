# Adding and Deleting PDF Pages

Adds or deletes pages in a PDF document, including:

-   Adds one or more blank pages to a PDF document.
-   Deletes one or more specified pages from a PDF document.
-   Adds PDF pages from other documents to the current PDF document.

#### API Description

| 
API Name

 | 

Description

 |
| :-- | :-- |
| 

[insertBlankPage](https://developer.huawei.com/consumer/en/doc/harmonyos-references/pdf-arkts-pdfservice#section18418154319159)(index: number, width: number, height: number): PdfPage

 | 

Inserts a blank PDF page at a specified position.

 |
| 

[getPage](https://developer.huawei.com/consumer/en/doc/harmonyos-references/pdf-arkts-pdfservice#section1221013163209)(index: number): PdfPage

 | 

Obtains an object of the specified page.

 |
| 

[insertPageFromDocument](https://developer.huawei.com/consumer/en/doc/harmonyos-references/pdf-arkts-pdfservice#section7656515132015)(document: PdfDocument, fromIndex: number, pageCount: number, index: number): PdfPage

 | 

Adds a page of another document to the current document.

 |
| 

[deletePage](https://developer.huawei.com/consumer/en/doc/harmonyos-references/pdf-arkts-pdfservice#section1472716318565)(index: number, count: number): void

 | 

Deletes a specified PDF page.

 |

#### Sample Code

1.  Call the **loadDocument** method to load a PDF document.
2.  Call the **getPage** method to obtain the width and height of the current page.
3.  Call the **insertBlankPage** and **insertPageFromDocument** methods to implement the following functions:
    1.  Inserts a single blank page.
    2.  Inserts multiple blank pages.
    3.  Inserts pages with indexes 1, 2, and 3 of the **input2.pdf** document to the page with index 0 of the **input.pdf** document and save the document as a new document.
4.  Call the **deletePage** method to delete one or more index pages.

import { pdfService } from '@kit.PDFKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

@Entry
@Component
struct PdfPage {
  private pdfDocument: pdfService.PdfDocument = new pdfService.PdfDocument();
  private context = this.getUIContext().getHostContext() as Context;

  aboutToAppear(): void {
    // Ensure that the **input.pdf** document exists in the sandbox directory.
    let filePath = this.context.filesDir + '/input.pdf';
    this.pdfDocument.loadDocument(filePath);
  }

  build() {
    Column() {
      // Insert a single blank page.
      Button('insertBlankPage').onClick(async () => {
        let page: pdfService.PdfPage = this.pdfDocument.getPage(0);
        let page2: pdfService.PdfPage = this.pdfDocument.insertBlankPage(2, page.getWidth(), page.getHeight());
        let outPdfPath = this.context.filesDir + '/testInsertBlankPage.pdf';
        let result = this.pdfDocument.saveDocument(outPdfPath);
        hilog.info(0x0000, 'PdfPage', 'insertBlankPage %{public}s!', result ? 'success' : 'fail');
      })
      // Insert multiple blank pages.
      Button('insertSomeBlankPage').onClick(async () => {
        let page: pdfService.PdfPage = this.pdfDocument.getPage(0);
        for (let i = 0; i < 3; i++) {
          this.pdfDocument.insertBlankPage(2, page.getWidth(), page.getHeight());
        }
        let outPdfPath = this.context.filesDir + '/testInsertSomeBlankPage.pdf';
        let result = this.pdfDocument.saveDocument(outPdfPath);
        hilog.info(0x0000, 'PdfPage', 'insertSomeBlankPage %{public}s!', result ? 'success' : 'fail');
      })
      // Insert pages with indexes 1, 2, and 3 of the **input2.pdf** document to the page with index 0 of the **input.pdf** document and save the document as a new document.
      Button('insertPageFromDocument').onClick(async () => {
        let pdfDoc: pdfService.PdfDocument = new pdfService.PdfDocument();
        // Ensure that the **input2.pdf** document exists in the sandbox directory.
        pdfDoc.loadDocument(this.context.filesDir + '/input2.pdf');
        this.pdfDocument.insertPageFromDocument(pdfDoc, 1, 3, 0);
        let outPdfPath = this.context.filesDir + '/testInsertPageFromDocument.pdf';
        let result = this.pdfDocument.saveDocument(outPdfPath);
        hilog.info(0x0000, 'PdfPage', 'insertPageFromDocument %{public}s!', result ? 'success' : 'fail');
      })
      // Delete one or more index pages.
      Button('deletePage').onClick(async () => {
        this.pdfDocument.deletePage(2, 2);
        let outPdfPath = this.context.filesDir + '/testDeletePage.pdf';
        let result = this.pdfDocument.saveDocument(outPdfPath);
        hilog.info(0x0000, 'PdfPage', 'deletePage %{public}s!', result ? 'success' : 'fail');
      })      
    }
  }
}
