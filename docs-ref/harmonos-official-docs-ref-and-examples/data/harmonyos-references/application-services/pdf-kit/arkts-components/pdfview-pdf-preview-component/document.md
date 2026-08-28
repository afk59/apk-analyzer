# PdfView (PDF Preview Component)

This module provides the PdfView component for HarmonyOS apps to preview PDF files.

**Start version**: 5.0.0(12)

#### Importing Modules

import { pdfService, pdfViewManager, PdfView } from '@kit.PDFKit';

#### PdfView

Displays the UI components for previewing PDF documents.

**Decorator type**: @Component

**System capability**: SystemCapability.OfficeService.PDFService.Core

**Start version**: 5.0.0(12)

| 
Parameter

 | 

**Type**

 | 

Read-Only

 | 

Optional

 | 

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

controller

 | 

pdfViewManager.[PdfController](../../arkts-api/pdfviewmanager-pdf-preview/document.md#section15202162183817)

 | 

No

 | 

No

 | 

**PdfView** component controller.

 |
| 

pageLayout

 | 

pdfService.[PageLayout](../../arkts-api/pdfservice-pdf-services/document.md#section1749384210523)

 | 

No

 | 

No

 | 

Page layout display mode.

 |
| 

isContinuous

 | 

boolean

 | 

No

 | 

No

 | 

Whether the preview is continuous (**true**) or not (**false**).

 |
| 

showScroll

 | 

boolean

 | 

No

 | 

No

 | 

Indicates whether to display the scrollbar (**true**) or not (**false**).

 |
| 

pageFit

 | 

pdfService.[PageFit](../../arkts-api/pdfservice-pdf-services/document.md#section655755325212)

 | 

No

 | 

No

 | 

Page fit mode.

 |

#### \[h2\]build

build(): void

Constructor used to create a [PdfView](#section724521414201) object.

**System capability**: SystemCapability.OfficeService.PDFService.Core

**Start version**: 5.0.0(12)

**Example:**

import { pdfService, pdfViewManager, PdfView } from '@kit.PDFKit'
import { fileIo } from '@kit.CoreFileKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

@Entry
@Component
struct Index {
  private controller: pdfViewManager.PdfController = new pdfViewManager.PdfController();

  aboutToAppear(): void {
    let context = this.getUIContext().getHostContext() as Context;
    let dir: string = context.filesDir
    // Ensure that the **input.pdf** document exists in the **src/main/resources/rawfile** project directory.
    let filePath: string = dir + '/input.pdf';
    let res = fileIo.accessSync(filePath);
    if (!res) {
      let content: Uint8Array = context.resourceManager.getRawFileContentSync('rawfile/input.pdf');
      let fdSand =
        fileIo.openSync(filePath, fileIo.OpenMode.WRITE\_ONLY | fileIo.OpenMode.CREATE | fileIo.OpenMode.TRUNC);
      fileIo.writeSync(fdSand.fd, content.buffer);
      fileIo.closeSync(fdSand.fd);
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
