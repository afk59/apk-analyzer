# Setting the PDF Document Preview Effects

pdfViewManager provides rich preview features for PDF documents.

-   Single- or dual-page layout, continuous scrolling preview, and page adaptation mode.
-   Page redirection, for example, redirection to the previous page, next page, or a specified page.
-   Page zoom.

**Figure 1**: Provides the dual-page preview layout, page width adaptation, and continuous scrolling preview mode.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/62/v3/fVKSIy61QmqbRf75Lbi5cA/en-us_image_0000002533661319.jpg?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062115Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E0AA1FB969E602508D95CA94F05233A44EB18579D5680AEDEFD02D3A38D09915 "Click to enlarge")

#### API Description

| 
API Name

 | 

Description

 |
| :-- | :-- |
| 

[setPageLayout](https://developer.huawei.com/consumer/en/doc/harmonyos-references/pdf-arkts-pdfviewmanage#section113581457158)(columnCount: PageLayout): void

 | 

Sets the page layout mode. The values of **columnCount** are as follows:

-   1: Single-page layout
-   2: Dual-page layout

 |
| 

[setPageContinuous](https://developer.huawei.com/consumer/en/doc/harmonyos-references/pdf-arkts-pdfviewmanage#section32161930132611)(isContinuous: boolean): void

 | 

Sets whether the page is scrolled continuously.

 |
| 

[setPageFit](https://developer.huawei.com/consumer/en/doc/harmonyos-references/pdf-arkts-pdfviewmanage#section347455378)(pageFit: PageFit): void

 | 

Sets the page fit mode.

 |
| 

[goToPage](https://developer.huawei.com/consumer/en/doc/harmonyos-references/pdf-arkts-pdfviewmanage#section9554132275317)(pageIndex: number): void

 | 

Redirects to a specified page.

 |
| 

[setPageZoom](https://developer.huawei.com/consumer/en/doc/harmonyos-references/pdf-arkts-pdfviewmanage#section2693181014192)(zoom: number): void

 | 

Sets the zoom ratio.

 |

#### Sample Code

1.  Load the PDF document.
2.  Call the PdfView preview component to render the display.
3.  Call the **setPageLayout** and **setPageContinuous** methods via the **setPreviewMode** button to set the document preview effect.
4.  Call the **goToPage** method via the **goTopage** button to set page redirection.
5.  Call the **setPageZoom** method via the **zoomPage2** button to zoom in the page by two times.

import { pdfService, PdfView, pdfViewManager } from '@kit.PDFKit';

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
      // Note: The document is just loaded. Do not set the preview mode of the PDF document immediately.
    })()
  }

  build() {
    Column() {
      Row() {
        // Set the preview mode.
        Button('setPreviewMode').onClick(() => {
          if (this.loadResult === pdfService.ParseResult.PARSE\_SUCCESS) {
            // Single-page layout.
            this.controller.setPageLayout(pdfService.PageLayout.LAYOUT\_SINGLE);
            // Whether to continuously scroll the pages.
            this.controller.setPageContinuous(true);
            // Preview mode of the adaptation page.
            this.controller.setPageFit(pdfService.PageFit.FIT\_PAGE);
          }
        })
        // Go to page 11.
        Button('goTopage').onClick(() => {
          if (this.loadResult === pdfService.ParseResult.PARSE\_SUCCESS) {
            this.controller.goToPage(10);
          }
        })
        // Zoom in the page by 2 times.
        Button('zoomPage2').onClick(() => {
          if (this.loadResult === pdfService.ParseResult.PARSE\_SUCCESS) {
            this.controller.setPageZoom(2);
          }
        })
      }

      PdfView({
        controller: this.controller,
        pageFit: pdfService.PageFit.FIT\_WIDTH,
        showScroll: true
      })
        .id('pdfview\_app\_view')
        .layoutWeight(1);
    }
  }
}
