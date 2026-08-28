# Adding and Deleting Headers and Footers

PDF Kit allows you to add or delete a header and a footer of a specified page. The header and footer contain text, date, and page number. You can set the font size, color, and spacing. For details, see [HeaderFooterInfo](https://developer.huawei.com/consumer/en/doc/harmonyos-references/pdf-arkts-pdfservice#section3237995481). The following figure is an example.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/68/v3/OBNH7hPNQquElk8YE1_DLw/en-us_image_0000002533821277.jpg?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062115Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E9168913E4B367C21BEE9104283E43FE6DB849449B422F0FF8D31B8AC4977A66 "Click to enlarge")

#### API Description

| 
API Name

 | 

Description

 |
| :-- | :-- |
| 

[addHeaderFooter](https://developer.huawei.com/consumer/en/doc/harmonyos-references/pdf-arkts-pdfservice#section4211341401)(info: HeaderFooterInfo, startIndex: number, endIndex: number, oddPages: boolean, evenPages: boolean): void

 | 

Inserts a header and a footer to a PDF document.

 |
| 

[removeHeaderFooter](https://developer.huawei.com/consumer/en/doc/harmonyos-references/pdf-arkts-pdfservice#section19996123722218)(): boolean

 | 

Removes a header and a footer from a PDF document.

 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fa/v3/r8xJ4WcDQHWZ936RhzoJfg/caution_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062115Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=28C4AD941A8CCC48457E2A22C8B63F046B0E3E3184A9F861669AC99ED196D182)

The [addHeaderFooter](https://developer.huawei.com/consumer/en/doc/harmonyos-references/pdf-arkts-pdfservice#section4211341401) method is time-consuming as it involves iterating through each page to add headers and footers. For documents with many pages, it is recommended that you process them in a thread.

#### Sample Code

**Adding a header and a footer**:

1.  Call the **loadDocument** method to load a PDF document.
2.  Instantiate the **HeaderFooterInfo** class and set related attributes, including the font size, color, and spacing.
3.  Call the **addHeaderFooter** method to add a header and a footer to the page.
4.  Save the PDF document to the app sandbox.

**Deleting a header and a footer**:

1.  Call the **loadDocument** method to load a PDF document.
2.  Call the **removeHeaderFooter** method to delete a header and a footer.
3.  Save the PDF document to the app sandbox.

import { pdfService } from '@kit.PDFKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { Font } from '@kit.ArkUI';

@Entry
@Component
struct PdfPage {
  private pdfDocument: pdfService.PdfDocument = new pdfService.PdfDocument();
  private context = this.getUIContext().getHostContext() as Context;

  build() {
    Column() {
      Button('addHeaderFooter').onClick(async () => {
        // Ensure that the **input.pdf** document exists in the sandbox directory.
        let filePath = this.context.filesDir + '/input.pdf';
        let res = this.pdfDocument.loadDocument(filePath);
        if (res === pdfService.ParseResult.PARSE\_SUCCESS) {
          let hfInfo: pdfService.HeaderFooterInfo = new pdfService.HeaderFooterInfo();
          hfInfo.fontInfo = new pdfService.FontInfo();
          // Ensure that the font path exists.
          let font: Font = new Font()
          hfInfo.fontInfo.fontPath = font.getFontByName('HarmonyOS Sans')?.path;
          // If you don't know the specific name of the font, leave it blank.
          hfInfo.fontInfo.fontName = '';
          hfInfo.textSize = 10;
          hfInfo.charset = pdfService.CharsetType.PDF\_FONT\_DEFAULT\_CHARSET;
          hfInfo.underline = false;
          hfInfo.textColor = 0x00000000;
          hfInfo.leftMargin = 1.0;
          hfInfo.topMargin = 40.0;
          hfInfo.rightMargin = 1.0;
          hfInfo.bottomMargin = 40.0;
          hfInfo.headerLeftText = 'left H <<dd.mm.yyyy>> <<1/n>>';
          hfInfo.headerCenterText = 'center H <<m/d/yyyy>> <<1/n>>';
          hfInfo.headerRightText = 'right H <<m/d>><<1>>';
          hfInfo.footerLeftText = 'left F <<m/d>><<1>>';
          hfInfo.footerCenterText = 'center F <<m/d>><<1>>';
          hfInfo.footerRightText = 'right F <<dd.mm.yyyy>><<1>>';
          this.pdfDocument.addHeaderFooter(hfInfo, 1, 5, true, true);
          let outPdfPath = this.context.filesDir + '/testAddHeaderFooter.pdf';
          let result = this.pdfDocument.saveDocument(outPdfPath);
          hilog.info(0x0000, 'PdfPage', 'addHeaderFooter %{public}s!', result ? 'success' : 'fail');
        }
        this.pdfDocument.releaseDocument();
      })
      Button('removeHeaderFooter').onClick(async () => {
        let filePath = this.context.filesDir + '/testAddHeaderFooter.pdf';
        let res = this.pdfDocument.loadDocument(filePath);
        if (res === pdfService.ParseResult.PARSE\_SUCCESS && this.pdfDocument.hasHeaderFooter()) {
          let removeResult = this.pdfDocument.removeHeaderFooter();
          if (removeResult) {
            let outPdfPath = this.context.filesDir + '/removeHeaderFooter.pdf';
            let result = this.pdfDocument.saveDocument(outPdfPath);
            hilog.info(0x0000, 'PdfPage', 'removeHeaderFooter %{public}s!', result ? 'success' : 'fail');
          }
        }
        this.pdfDocument.releaseDocument();
      })
    }
  }
}
