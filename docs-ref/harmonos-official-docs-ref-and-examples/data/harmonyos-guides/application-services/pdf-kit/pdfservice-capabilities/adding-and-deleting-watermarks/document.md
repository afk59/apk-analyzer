# Adding and Deleting Watermarks

You can add text or image watermarks to a specified page.

-   Set attributes such as font, size, rotation, and position of the text watermark.
-   Set attributes such as scaling, rotation, opacity, and position for image watermarks.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b4/v3/8MNCTFpTS42rk8b_P1Uc-g/en-us_image_0000002533821275.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062115Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0F70451B3F89D93F9306E51C23B1B43E82CA607DF9EF64A5436F1BEFFAA94013)

#### API Description

| 
API Name

 | 

Description

 |
| :-- | :-- |
| 

[addWatermark](https://developer.huawei.com/consumer/en/doc/harmonyos-references/pdf-arkts-pdfservice#section206080386472)(info: WatermarkInfo, startIndex: number, endIndex: number, oddPages: boolean, evenPages: boolean): void

 | 

Inserts a watermark to a PDF document. To insert an image, see [ImageFormat](https://developer.huawei.com/consumer/en/doc/harmonyos-references/pdf-arkts-pdfservice#section1713111745313) for the supported image formats. There is no restriction on text characters.

 |
| 

[removeWatermark](https://developer.huawei.com/consumer/en/doc/harmonyos-references/pdf-arkts-pdfservice#section18585132044815)(): boolean

 | 

Removes a watermark from a PDF document.

 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c3/v3/Fd-MNGyGTl2x4klxrIWSwA/caution_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062115Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E95AF9AD318D185420A3CAAF09A58DA27AEF0F91C52A1DDF69EF26CD07187B2D)

The [addWatermark](https://developer.huawei.com/consumer/en/doc/harmonyos-references/pdf-arkts-pdfservice#section206080386472) method is time-consuming as it involves iterating through each page to add watermarks. For documents with many pages, it is recommended that you process them in a thread.

#### Sample Code

## Adding/Deleting a Text Watermark

**Adding a text watermark**:

1.  Call the **loadDocument** method to load a PDF document.
2.  Instantiate the **TextWatermarkInfo** class and set related attributes, including the font, size, rotation, and position.
3.  Call the **addWatermark** method to add a text watermark.
4.  Save the PDF document to the app sandbox.

**Deleting a text watermark**:

1.  Call the **loadDocument** method to load a PDF document.
2.  Call the **removeWatermark** method to delete a text watermark.
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
      Button('addTextWatermark').onClick(async () => {
        // Ensure that the **input.pdf** document exists in the sandbox directory.
        let filePath = this.context.filesDir + '/input.pdf';
        let res = this.pdfDocument.loadDocument(filePath);
        if (res === pdfService.ParseResult.PARSE\_SUCCESS) {
          let wminfo: pdfService.TextWatermarkInfo = new pdfService.TextWatermarkInfo();
          wminfo.watermarkType = pdfService.WatermarkType.WATERMARK\_TEXT;
          wminfo.content = 'This is Watermark';
          wminfo.textSize = 30;
          wminfo.textColor = 200;
          wminfo.fontInfo = new pdfService.FontInfo();
// Ensure that the font path exists.
          let font: Font = new Font()
          wminfo.fontInfo.fontPath = font.getFontByName('HarmonyOS Sans').path;
          wminfo.opacity = 0.5;
          wminfo.isOnTop = true;
          wminfo.rotation = 45;
          wminfo.scale = 1.5;
          wminfo.opacity = 0.5;
          wminfo.verticalAlignment = pdfService.WatermarkAlignment.WATERMARK\_ALIGNMENT\_TOP;
          wminfo.horizontalAlignment = pdfService.WatermarkAlignment.WATERMARK\_ALIGNMENT\_LEFT;
          wminfo.horizontalSpace = 1.0;
          wminfo.verticalSpace = 1.0;
          this.pdfDocument.addWatermark(wminfo, 0, 5, true, true);
          let outPdfPath = this.context.filesDir + '/testTextWatermark.pdf';
          let result = this.pdfDocument.saveDocument(outPdfPath);
          hilog.info(0x0000, 'PdfPage', 'addTextWatermark %{public}s!', result ? 'success' : 'fail');
        }
        this.pdfDocument.releaseDocument();
      })
      Button('removeTextWatermark').onClick(async () => {
        let filePath = this.context.filesDir + '/testTextWatermark.pdf';
        let res = this.pdfDocument.loadDocument(filePath);
        if (res === pdfService.ParseResult.PARSE\_SUCCESS && this.pdfDocument.hasWatermark()) {
          let removeResult = this.pdfDocument.removeWatermark();
          if (removeResult) {
            let outPdfPath = this.context.filesDir + '/removeWatermark.pdf';
            let result = this.pdfDocument.saveDocument(outPdfPath);
            hilog.info(0x0000, 'PdfPage', 'removeWatermark %{public}s!', result ? 'success' : 'fail');
          }
        }
        this.pdfDocument.releaseDocument();
      })
    }
  }
}

## Adding/Deleting an Image Watermark

**Adding an image watermark**:

1.  Call the **loadDocument** method to load a PDF document.
2.  Instantiate the **ImageWatermarkInfo** class and set related attributes, including scaling, rotation, opacity, and position.
3.  Call the **addWatermark** method to add an image watermark.
4.  Save the PDF document to the app sandbox.

**Deleting an image watermark**:

1.  Call the **loadDocument** method to load a PDF document.
2.  Call the **removeWatermark** method to delete an image watermark.
3.  Save the PDF document to the app sandbox.

import { pdfService } from '@kit.PDFKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

@Entry
@Component
struct PdfPage {
  private pdfDocument: pdfService.PdfDocument = new pdfService.PdfDocument();
  private context = this.getUIContext().getHostContext() as Context;

  build() {
    Column() {
      Button('addImageWatermark').onClick(async () => {
        let filePath = this.context.filesDir + '/input.pdf';
        let res = this.pdfDocument.loadDocument(filePath);
        if (res === pdfService.ParseResult.PARSE\_SUCCESS) {
          let wminfo: pdfService.ImageWatermarkInfo = new pdfService.ImageWatermarkInfo();
          wminfo.watermarkType = pdfService.WatermarkType.WATERMARK\_IMAGE;
          // Ensure that the **img.jpg** document exists in the sandbox directory.
          wminfo.imagePath = this.context.filesDir + '/img.jpg';
          wminfo.opacity = 0.5;
          wminfo.isOnTop = true;
          wminfo.rotation = 45;
          wminfo.scale = 0.5;
          wminfo.opacity = 0.5;
          wminfo.verticalAlignment = pdfService.WatermarkAlignment.WATERMARK\_ALIGNMENT\_TOP;
          wminfo.horizontalAlignment = pdfService.WatermarkAlignment.WATERMARK\_ALIGNMENT\_LEFT;
          wminfo.horizontalSpace = 1.0;
          wminfo.verticalSpace = 1.0;
          this.pdfDocument.addWatermark(wminfo, 0, 5, true, true);
          let outPdfPath = this.context.filesDir + '/testImageWatermark.pdf';
          let result = this.pdfDocument.saveDocument(outPdfPath);
          hilog.info(0x0000, 'PdfPage', 'addImageWatermark %{public}s!', result ? 'success' : 'fail');
        }
        this.pdfDocument.releaseDocument();
      })
      Button('removeImageWatermark').onClick(async () => {
        let filePath = this.context.filesDir + '/testImageWatermark.pdf';
        let res = this.pdfDocument.loadDocument(filePath);
        if (res === pdfService.ParseResult.PARSE\_SUCCESS && this.pdfDocument.hasWatermark()) {
          let removeResult = this.pdfDocument.removeWatermark();
          if (removeResult) {
            let outPdfPath = this.context.filesDir + '/removeImageWatermark.pdf';
            let result = this.pdfDocument.saveDocument(outPdfPath);
            hilog.info(0x0000, 'PdfPage', 'removeImageWatermark %{public}s!', result ? 'success' : 'fail');
          }
        }
        this.pdfDocument.releaseDocument();
      })
    }
  }
}
