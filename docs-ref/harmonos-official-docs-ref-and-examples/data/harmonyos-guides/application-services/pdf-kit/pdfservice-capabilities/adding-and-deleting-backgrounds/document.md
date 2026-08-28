# Adding and Deleting Backgrounds

You can add a background image or background color to a specified page and set attributes such as size, rotation, opacity, and position. The following image formats are supported: .png, .bmp, and .jpeg.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3c/v3/eWJKdgLMSfuVxRWpdkpGqQ/en-us_image_0000002501901428.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062115Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A3046965AB519AEEA1D0055AC395E7B91973EC386C21BE207444BA98AFE6E1D3)

#### API Description

| 
API Name

 | 

Description

 |
| :-- | :-- |
| 

[addBackground](https://developer.huawei.com/consumer/en/doc/harmonyos-references/pdf-arkts-pdfservice#section13641714101419)(info: BackgroundInfo, startIndex: number, endIndex: number, oddPages: boolean, evenPages: boolean): void

 | 

Adds background to a PDF document.

 |
| 

[removeBackground](https://developer.huawei.com/consumer/en/doc/harmonyos-references/pdf-arkts-pdfservice#section16476184082314)(): boolean

 | 

Removes the background of a PDF document.

 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9f/v3/HeAwOnRDTfKBIgd-74fnKQ/caution_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062115Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A8B4C8B98051C9680DDCA09F93274F593CC610CC0E0F439AF78F3CAD2929E0BF)

The [addBackground](https://developer.huawei.com/consumer/en/doc/harmonyos-references/pdf-arkts-pdfservice#section13641714101419) method is time-consuming as it involves iterating through each page to add backgrounds. For documents with many pages, it is recommended that you process them in a thread.

#### Sample Code

**Adding a background**:

1.  Call the **loadDocument** method to load a PDF document.
2.  Instantiate the **BackgroundInfo** class and set related attributes, including size, rotation, opacity, and position.
3.  Call the **addBackground** method to add a background.
4.  Save the PDF document to the app sandbox.

**Deleting a background**:

1.  Call the **loadDocument** method to load a PDF document.
2.  Call the **removeBackground** method to delete a background.
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
      Button('addBackground').onClick(async () => {
        // Ensure that the **input.pdf** document exists in the sandbox directory.
        let filePath = this.context.filesDir + '/input.pdf';
        let res = this.pdfDocument.loadDocument(filePath);
        if (res === pdfService.ParseResult.PARSE\_SUCCESS) {
          let bginfo: pdfService.BackgroundInfo = new pdfService.BackgroundInfo();
          // Ensure that the **img.jpg** document exists in the sandbox directory.
          bginfo.imagePath = this.context.filesDir + '/img.jpg';
          bginfo.backgroundColor = 50;
          bginfo.isOnTop = true;
          bginfo.rotation = 45;
          bginfo.scale = 0.5;
          bginfo.opacity = 0.3;
          bginfo.verticalAlignment = pdfService.BackgroundAlignment.BACKGROUND\_ALIGNMENT\_TOP;
          bginfo.horizontalAlignment = pdfService.BackgroundAlignment.BACKGROUND\_ALIGNMENT\_LEFT;
          bginfo.horizontalSpace = 1.0;
          bginfo.verticalSpace = 1.0;
          this.pdfDocument.addBackground(bginfo, 0, 2, true, true);
          let outPdfPath = this.context.filesDir + '/testAddBackground.pdf';
          let result = this.pdfDocument.saveDocument(outPdfPath);
          hilog.info(0x0000, 'PdfPage', 'addBackground %{public}s!', result ? 'success' : 'fail');
        }
        this.pdfDocument.releaseDocument();
      })
      Button('removeBackground').onClick(async () => {
        let filePath = this.context.filesDir + '/testAddBackground.pdf';
        let res = this.pdfDocument.loadDocument(filePath);
        if (res === pdfService.ParseResult.PARSE\_SUCCESS && this.pdfDocument.hasBackground()) {
          let removeResult = this.pdfDocument.removeBackground();
          if (removeResult) {
            let outPdfPath = this.context.filesDir + '/removeBackground.pdf';
            let result = this.pdfDocument.saveDocument(outPdfPath);
            hilog.info(0x0000, 'PdfPage', 'removeBackground %{public}s!', result ? 'success' : 'fail');
          }
        }
        this.pdfDocument.releaseDocument();
      })
    }
  }
}
