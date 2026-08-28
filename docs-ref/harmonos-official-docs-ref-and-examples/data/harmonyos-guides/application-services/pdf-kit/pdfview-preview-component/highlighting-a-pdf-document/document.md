# Highlighting a PDF Document

When previewing a PDF document, you can highlight the rectangular area or text on the page and customize the highlight color.

Use [setHighlightText](https://developer.huawei.com/consumer/en/doc/harmonyos-references/pdf-arkts-pdfviewmanage#section475716341213) to highlight multiple different text blocks at the same time.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2c/v3/sxwlqRNRQFmhvLBIAvIXUQ/en-us_image_0000002533661317.jpg?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062115Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1457291EF73DFE33656E688820FB25F6A774791D0D946D40C92E669F75A606C3)

#### API Description

| 
API Name

 | 

Description

 |
| :-- | :-- |
| 

[setHighlightText](https://developer.huawei.com/consumer/en/doc/harmonyos-references/pdf-arkts-pdfviewmanage#section475716341213)(pageIndex: number, textArray: string\[\], color: number): void

 | 

Highlights the specified text.

 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2f/v3/N1zCWg3uRlyziBy5AGEaBA/caution_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062115Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8134905C3D5C0795E91A74D087BB0949CE32C7DFFF0FB94115FF5F1EE64D4645)

The [setHighlightText](https://developer.huawei.com/consumer/en/doc/harmonyos-references/pdf-arkts-pdfviewmanage#section475716341213) and [searchKey](https://developer.huawei.com/consumer/en/doc/harmonyos-references/pdf-arkts-pdfviewmanage#section117864247160) functions are mutually exclusive.

#### Sample Code

1.  Load the PDF document.
2.  Call the PdfView preview component to render the display.
3.  Call the **setHighlightText** method via the **setHighlightText** button, to set one or more text blocks to be highlighted.

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
    })()
  }

  build() {
    Column() {
      Row() {
// Set the highlight style of the text.
        Button('setHighlightText').onClick(async () => {
          if (this.loadResult === pdfService.ParseResult.PARSE\_SUCCESS) {            
            this.controller.setHighlightText(0, \['White Paper'\], 0xAAF9CC00);
          }
        })
      }

      // Load the PdfView component for preview.
      PdfView({
        controller: this.controller,
        pageFit: pdfService.PageFit.FIT\_WIDTH,
        showScroll: true
      })
        .id('pdfview\_app\_view')
        .layoutWeight(1);
    }
    .width('100%').height('100%')
  }
}
