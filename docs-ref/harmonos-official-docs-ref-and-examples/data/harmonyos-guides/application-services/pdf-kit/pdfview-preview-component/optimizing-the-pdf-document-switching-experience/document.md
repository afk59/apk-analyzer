# Optimizing the PDF Document Switching Experience

#### Use Cases

When switching between multiple documents in an app, you are advised to use state management to control the rendering timing of PdfView, thereby providing a smoother and clearer visual experience.

By introducing the loading status, you can temporarily hide the PdfView preview component and display the loading animation during document loading. After asynchronous loading through **loadDocument** is complete and the page layout is ready, the clear document content is displayed. This method can effectively smooth out visual jumps during document switching and improve the interaction quality.

#### API Description

| 
API Name

 | 

Description

 |
| :-- | :-- |
| 

[loadDocument](https://developer.huawei.com/consumer/en/doc/harmonyos-references/pdf-arkts-pdfviewmanage#section073321844615)(path: string, password?: string, initPageIndex?: number, onProgress?: Callback<number>): Promise<pdfService.ParseResult>

 | 

Loads a PDF document.

 |
| 

[setPageFit](https://developer.huawei.com/consumer/en/doc/harmonyos-references/pdf-arkts-pdfviewmanage#section347455378)(pageFit: pdfService.PageFit): void

 | 

Sets the page fit mode.

 |

#### Sample Code

1.  Define the @State variable **isLoading** to indicate the loading status of a document and control the mounting and display of the PdfView component.
2.  Set **isLoading** to **true** to display the loading page. After asynchronous loading is successful, set **isLoading** to **false** to display the PDF view.
3.  Call **loadDocument** to load a different file path to switch to another PDF document.

import { pdfService, pdfViewManager, PdfView } from '@kit.PDFKit'
import { fileIo } from '@kit.CoreFileKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@ohos.base';

const DOMAIN: number = 0x0000;
const TAG: string = 'SwitchDocumentDemo';

@Entry
@Component
struct Index {
  private controller: pdfViewManager.PdfController = new pdfViewManager.PdfController();
  private filePath1: string = '';
  private filePath2: string = '';
  private switchFlag: boolean = true; // **true**: load the **pdf1** document; **false**: load the **pdf2** document.
  @State isLoading: boolean = false;

  private makeSureFileExist(filePath: string): void {
    let fileName: string = filePath.split('/').pop() || '';
    try {
      let context = this.getUIContext().getHostContext() as Context;
      let res = fileIo.accessSync(filePath);
      if (!res) {
        let content: Uint8Array = context.resourceManager.getRawFileContentSync(\`rawfile/${fileName}\`);
        let fdSand =
          fileIo.openSync(filePath, fileIo.OpenMode.WRITE\_ONLY | fileIo.OpenMode.CREATE | fileIo.OpenMode.TRUNC);
        fileIo.writeSync(fdSand.fd, content.buffer);
        fileIo.closeSync(fdSand.fd);
      }
    } catch (e) {
      let error: BusinessError = e as BusinessError;
      hilog.error(DOMAIN, TAG, \`Code: ${error.code}, message: ${error.message} \`);
    }
  }

  aboutToAppear(): void {
    let context = this.getUIContext().getHostContext() as Context;
    let dir: string = context.filesDir
    // Ensure that the **pdf1.pdf** and **pdf2.pdf** documents exist in the sandbox directory.
    this.filePath1 = dir + '/pdf1.pdf';
    this.filePath2 = dir + '/pdf2.pdf';
    this.makeSureFileExist(this.filePath1);
    this.makeSureFileExist(this.filePath2);

    (async () => {
      let filePath: string = this.switchFlag ? this.filePath1 : this.filePath2;
      this.isLoading = true;
      let loadResult: pdfService.ParseResult = await this.controller.loadDocument(filePath);
      this.isLoading = false;
      if (loadResult !== pdfService.ParseResult.PARSE\_SUCCESS) {
        hilog.error(DOMAIN, TAG, 'Controller load PDF failed');
        return;
      }
    })();
  }

  build() {
    Stack({ alignContent: Alignment.TopStart }) {
      if (!this.isLoading) {
        PdfView({
          controller: this.controller,
          pageFit: pdfService.PageFit.FIT\_WIDTH,
          showScroll: false
        })
          .width('100%')
          .height('100%')
      } else {
        //  You can customize the loading page.
      }
      Row() {
        Button('SwitchDocument')
          .onClick(async () => {
            this.switchFlag = !this.switchFlag;
            let filePath: string = this.switchFlag ? this.filePath1 : this.filePath2;
            this.controller.releaseDocument();
            this.isLoading = true;
		    let loadResult: pdfService.ParseResult = await this.controller.loadDocument(filePath);
		    this.isLoading = false;
            if (loadResult !== pdfService.ParseResult.PARSE\_SUCCESS) {
              hilog.error(DOMAIN, TAG, 'Controller load PDF failed');
              return;
            }
            this.controller.setPageFit(pdfService.PageFit.FIT\_WIDTH);
          })
      }
    }
    .height('100%')
    .width('100%')
  }
}
