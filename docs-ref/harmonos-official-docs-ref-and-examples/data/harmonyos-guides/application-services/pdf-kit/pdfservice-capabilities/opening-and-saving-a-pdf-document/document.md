# Opening and Saving a PDF Document

You need to open a PDF document before you can [add content](../text-images-and-annotations-on-pdf-pages/document.md), [headers and footers](../adding-and-deleting-headers-and-footers/document.md), [watermarks](../adding-and-deleting-watermarks/document.md), [backgrounds](../adding-and-deleting-backgrounds/document.md), or [bookmarks](../adding-and-deleting-bookmarks/document.md) to the document. After you finish the operations, save the PDF document.

Both pdfService and PdfView can be used to open and save documents, while they have differences in the application scenarios:

-   It is recommended that you open and save PDF documents using pdfService during document editing.
-   If you wish to preview documents, search for keywords, listen to PDF document callback, or add annotations, PdfView is recommended.

#### API Description

| 
API Name

 | 

Description

 |
| :-- | :-- |
| 

[loadDocument](https://developer.huawei.com/consumer/en/doc/harmonyos-references/pdf-arkts-pdfservice#section167288392229)(path: string, password?: string, onProgress?: Callback<number>): ParseResult

 | 

Loads the document with the specified document path.

 |
| 

[saveDocument](https://developer.huawei.com/consumer/en/doc/harmonyos-references/pdf-arkts-pdfservice#section660833016157)(path: string, onProgress?: Callback<number>): boolean

 | 

Saves a document.

 |

#### Sample Code

1.  Call the **loadDocument** method to load a PDF document.
2.  Call the **saveDocument** method in the **Save As** and **Save** buttons to save the document as a PDF document and overwrite the source PDF document.

import { pdfService } from '@kit.PDFKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { fileIo } from '@kit.CoreFileKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct PdfPage {
  private pdfDocument: pdfService.PdfDocument = new pdfService.PdfDocument();
  private context = this.getUIContext().getHostContext() as Context;
  private filePath = '';
  @State saveEnable: boolean = false;

  aboutToAppear(): void {
    this.filePath = this.context.filesDir + '/input.pdf';
    try {
      let res = fileIo.accessSync(this.filePath);
      if(!res) {
      // Ensure that the **input.pdf** document exists in the **src/main/resources/rawfile** project directory.
        let content: Uint8Array = this.context.resourceManager.getRawFileContentSync('rawfile/input.pdf');
        let fdSand =
          fileIo.openSync(this.filePath, fileIo.OpenMode.WRITE\_ONLY | fileIo.OpenMode.CREATE | fileIo.OpenMode.TRUNC);
        fileIo.writeSync(fdSand.fd, content.buffer);
        fileIo.closeSync(fdSand.fd);
      }
      this.pdfDocument.loadDocument(this.filePath);
    } catch (e) {
      let error: BusinessError = e as BusinessError;
      console.error(\`Failed to loadDocument. Code: ${error.code}, message: ${error.message} \`);
    }
  }

  build() {
    Column() {
      // Save as a new PDF document.
      Button('Save As').onClick(() => {
        // Add headers, footers, watermarks, or backgrounds to the PDF document, and save the document as a new document.
        let outPdfPath = this.context.filesDir + '/testSaveAsPdf.pdf';
        let result = this.pdfDocument.saveDocument(outPdfPath);
        this.saveEnable = true;
        hilog.info(0x0000, 'PdfPage', 'saveAsPdf %{public}s!', result ? 'success' : 'fail');
      })
      // Save the PDF document by overwriting the source document.
      Button('Save').enabled(this.saveEnable).onClick(() => {
        // Add headers, footers, watermarks, or backgrounds to the PDF document, and save the document.
        let tempDir = this.context.tempDir;
        let tempFilePath = tempDir + \`/temp${Math.random()}.pdf\`;
        try {
          fileIo.copyFileSync(this.filePath, tempFilePath);
        } catch (e) {
          let error: BusinessError = e as BusinessError;
          console.error(\`Failed to copyFileSync. Code: ${error.code}, message: ${error.message} \`);
        }
        let pdfDocument: pdfService.PdfDocument = new pdfService.PdfDocument();
        // Load the temporary document.
        let loadResult = pdfDocument.loadDocument(tempFilePath, '');
        if (loadResult === pdfService.ParseResult.PARSE\_SUCCESS) {
          let result = pdfDocument.saveDocument(this.filePath);
          hilog.info(0x0000, 'PdfPage', 'savePdf %{public}s!', result ? 'success' : 'fail');
        }
      })
    }
  }
}
