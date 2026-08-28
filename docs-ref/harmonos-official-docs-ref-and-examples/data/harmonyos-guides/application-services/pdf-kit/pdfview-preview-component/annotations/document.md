# Annotations

You can enter the annotation mode to add highlighted, underlined, and strikethrough annotations.

#### API Description

| 
API Name

 | 

Description

 |
| :-- | :-- |
| 

[enableAnnotation](https://developer.huawei.com/consumer/en/doc/harmonyos-references/pdf-arkts-pdfviewmanage#section1771517381253)(annotationType: SupportedAnnotationType, color?: number): void

 | 

Switches between common operations and adds annotations.

 |

#### Sample Code

1.  Load the PDF document.
2.  Call the **PdfView** preview component to render the display.
3.  Call the **enableAnnotation** method to enter the annotation mode.

import { pdfService, pdfViewManager, PdfView } from '@kit.PDFKit';

@Entry
@Component
struct PdfPage {
  private pdfController = new pdfViewManager.PdfController();
  private context = this.getUIContext().getHostContext() as Context;

  aboutToAppear(): void {
    // Ensure that the **input.pdf** document exists in the sandbox directory.
    let filePath = this.context.filesDir + '/input.pdf';
    (async () => {
      let loadResult: pdfService.ParseResult = await this.pdfController.loadDocument(filePath);
      if (pdfService.ParseResult.PARSE\_SUCCESS === loadResult) {
        // Add a strikethrough annotation.
        this.pdfController.enableAnnotation(pdfViewManager.SupportedAnnotationType.STRIKETHROUGH, 0xAAEEEEEE);
      }
    })()
  }

  build() {
    Column() {
      // Load the PdfView component for preview.
      PdfView({
        controller: this.pdfController,
        pageFit: pdfService.PageFit.FIT\_WIDTH,
        showScroll: true
      })
        .id('pdfview\_app\_view')
        .layoutWeight(1);
    }
  }
}
