# Previewing a PDF Document

PDF Kit provides various PDF document preview capabilities, such as:

-   Page redirection
-   Page zoom
-   Single- or dual-page display
-   Page adaptation
-   Preview in scrolling view mode

For details, see the [PdfView](https://developer.huawei.com/consumer/en/doc/harmonyos-references/pdf-arkts-pdfview-component#section724521414201) component.

#### Sample Code

1.  Import required modules.
2.  In the following sample code, the **input.pdf** document is used as an example. Ensure that the **input.pdf** document exists in the **src/main/resources/rawfile** project directory and is copied to the sandbox directory.
3.  Call the **loadDocument** method to load a PDF document.
4.  Call the PdfView preview component to render the display.

import { pdfService, pdfViewManager, PdfView } from '@kit.PDFKit'
import { fileIo } from '@kit.CoreFileKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Index {
  private controller: pdfViewManager.PdfController = new pdfViewManager.PdfController();

  aboutToAppear(): void {
    let context = this.getUIContext().getHostContext() as Context;
    let dir: string = context.filesDir
    // Ensure that the **input.pdf** document exists in the **src/main/resources/rawfile** project directory.
    let filePath: string = dir + '/input.pdf';
    try {
      let res = fileIo.accessSync(filePath);
      if (!res) {
        let content: Uint8Array = context.resourceManager.getRawFileContentSync('rawfile/input.pdf');
        let fdSand =
          fileIo.openSync(filePath, fileIo.OpenMode.WRITE\_ONLY | fileIo.OpenMode.CREATE | fileIo.OpenMode.TRUNC);
        fileIo.writeSync(fdSand.fd, content.buffer);
        fileIo.closeSync(fdSand.fd);
      }
    } catch (e) {
      let error: BusinessError = e as BusinessError;
      console.error(\`Code: ${error.code}, message: ${error.message} \`);
    }
    (async () => {
      // This listening method can be called only once before the document is loaded.
      this.controller.registerPageCountChangedListener((pageCount: number) => {
        hilog.info(0x0000, 'registerPageCountChanged-', pageCount.toString());
      });
      let loadResult1: pdfService.ParseResult = await this.controller.loadDocument(filePath);
      // Note: The document is just loaded. Do not set the preview mode of the PDF document immediately.
    })()
  }

  build() {
    Row() {
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
