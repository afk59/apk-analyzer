# Text, Images, and Annotations on PDF Pages

You can edit PDF page content, including:

-   Add or delete text.
-   Add or delete images.
-   Add, modify, or delete annotations.
    
    You can add annotations to a PDF page and set the position, font, and border of the annotations on the page. 13 annotation styles are provided, including [TextAnnotationInfo](https://developer.huawei.com/consumer/en/doc/harmonyos-references/pdf-arkts-pdfservice#section31971811203120), [LineAnnotationInfo](https://developer.huawei.com/consumer/en/doc/harmonyos-references/pdf-arkts-pdfservice#section19125125519345), [HighlightAnnotationInfo](https://developer.huawei.com/consumer/en/doc/harmonyos-references/pdf-arkts-pdfservice#section42937218352), and [StrikethroughAnnotationInfo](https://developer.huawei.com/consumer/en/doc/harmonyos-references/pdf-arkts-pdfservice#section1079774919358).
    

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3e/v3/aabs25CiTa2j9A7Pcov5NA/en-us_image_0000002501901424.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062115Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C913812D853BE8D370CAD858796E805F8098472DE966A52D9D299754B6326609 "Click to enlarge")

#### API Description

| 
API Name

 | 

Description

 |
| :-- | :-- |
| 

[addTextObject](https://developer.huawei.com/consumer/en/doc/harmonyos-references/pdf-arkts-pdfservice#section67811517143913)(text: string, x: number, y: number, style: TextStyle): void

 | 

Adds text content only by line.

 |
| 

[addImageObject](https://developer.huawei.com/consumer/en/doc/harmonyos-references/pdf-arkts-pdfservice#section699712112399)(path: string, x: number, y: number, width: number, height: number): void

 | 

Adds an image to a page of a PDF document.

 |
| 

[deleteGraphicsObject](https://developer.huawei.com/consumer/en/doc/harmonyos-references/pdf-arkts-pdfservice#section5391931153910)(object: GraphicsObject): void

 | 

Deletes a specified **GraphicsObject**.

 |
| 

[addAnnotation](https://developer.huawei.com/consumer/en/doc/harmonyos-references/pdf-arkts-pdfservice#section8253013193814)(annotationInfo: PdfAnnotationInfo): PdfAnnotation

 | 

Adds an annotation to the current page.

 |

#### Adding Text and Images

1.  Call the **loadDocument** method to load a PDF document.
2.  Call the **addTextObject** method via the **addText** button to insert text.
3.  Call the **deleteGraphicsObject** method via the **delText** button to delete the corresponding text on the page.
4.  Call the **addImageObject** method via the **addImage** button to insert an image.

import { pdfService } from '@kit.PDFKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { Font } from '@kit.ArkUI';

@Entry
@Component
struct PdfPage {
  private pdfDocument: pdfService.PdfDocument = new pdfService.PdfDocument();
  private context = this.getUIContext().getHostContext() as Context;

  aboutToAppear(): void {
    // Ensure that the **input.pdf** document exists in the sandbox directory.
    let filePath = this.context.filesDir + '/input.pdf';
    this.pdfDocument.loadDocument(filePath);
  }

  build() {
    Column() {
      // Add text.
      Button('addText').onClick(async () => {
        let page: pdfService.PdfPage = this.pdfDocument.getPage(0);
        let str = 'This is add text object!';
        let fontInfo = new pdfService.FontInfo();
        // Ensure that the font path exists.
        let font: Font = new Font()
        fontInfo.fontPath = font.getFontByName('HarmonyOS Sans')?.path;
        fontInfo.fontName = '';
        let style: pdfService.TextStyle = { textColor: 0x000000, textSize: 30, fontInfo: fontInfo };
        page.addTextObject(str, 10, 10, style);
        let outPdfPath = this.context.filesDir + '/testAddText.pdf';
        let result = this.pdfDocument.saveDocument(outPdfPath);
        hilog.info(0x0000, 'PdfPage', 'addText %{public}s!', result ? 'success' : 'fail');
      })
      // Delete text.
      Button('delText').onClick(async () => {
        let page: pdfService.PdfPage = this.pdfDocument.getPage(0);
        let graphicsObjects = page.getGraphicsObjects();
        // Find the first text block to be deleted.
        let index = graphicsObjects.findIndex(item => item.type === pdfService.GraphicsObjectType.OBJECT\_TEXT);
        if (index > -1) {
          // Delete the first text block.
          page.deleteGraphicsObject(graphicsObjects\[index\]);
        }
        let outPdfPath = this.context.filesDir + '/testDelText.pdf';
        let result = this.pdfDocument.saveDocument(outPdfPath);
        hilog.info(0x0000, 'PdfPage', 'delText %{public}s!', result ? 'success' : 'fail');
      })
      // Add an image.
      Button('addImage').onClick(async () => {
        let page: pdfService.PdfPage = this.pdfDocument.getPage(0);
        // Insert an image. Ensure that the **img.jpg** image exists in the sandbox directory.
        let imagePath = this.context.filesDir + '/img.jpg';
        page.addImageObject(imagePath, 100, 100, 100, 120);
        let outPdfPath = this.context.filesDir + '/testAddImage.pdf';
        let result = this.pdfDocument.saveDocument(outPdfPath);
        hilog.info(0x0000, 'PdfPage', 'addImage %{public}s!', result ? 'success' : 'fail');
      })
    }
  }
}

#### Adding a Text Annotation

1.  Call the **loadDocument** method to load a PDF document.
2.  Call the **getPage** method to obtain a specified page.
3.  Instantiate the **TextAnnotationInfo** text annotation and set related attributes.
4.  Call the **addAnnotation** or **setAnnotation** method to add or edit an annotation.
5.  Call the **removeAnnotation** method to delete an annotation.

import { pdfService } from '@kit.PDFKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

@Entry
@Component
struct PdfPage {
  private pdfDocument: pdfService.PdfDocument = new pdfService.PdfDocument();
  private context = this.getUIContext().getHostContext() as Context;

  build() {
    Column() {
      // Add an annotation.
      Button('addTextAnnotation').onClick(async () => {
        // Ensure that the **input.pdf** document exists in the sandbox directory.
        let filePath = this.context.filesDir + '/input.pdf';
        this.pdfDocument.loadDocument(filePath);
        let page: pdfService.PdfPage = this.pdfDocument.getPage(0);
        let aInfo = new pdfService.TextAnnotationInfo();
        aInfo.iconName = 'cument Format';
        aInfo.content = 'this is a content';
        aInfo.subject = 'Annotation';
        aInfo.title = 'this is a title';
        aInfo.state = pdfService.TextAnnotationState.MARKED;
        aInfo.x = 200;
        aInfo.y = 200;
        aInfo.color = 0xf9b1b1;
        aInfo.flag = pdfService.AnnotationFlag.PRINTED;
        let annotation: pdfService.PdfAnnotation = page.addAnnotation(aInfo);
        let outPdfPath = this.context.filesDir + '/testAddTextAnnotation.pdf';
        let result = this.pdfDocument.saveDocument(outPdfPath);
        this.pdfDocument.releaseDocument();
        hilog.info(0x0000, 'PdfPage', 'addTextAnnotation %{public}s!', result ? 'success' : 'fail');
      })
      // Edit an annotation.
      Button('setAnnotation').onClick(async () => {
        let filePath = this.context.filesDir + '/testAddTextAnnotation.pdf';
        let result = this.pdfDocument.loadDocument(filePath);
        if (result === pdfService.ParseResult.PARSE\_SUCCESS) {
          let page: pdfService.PdfPage = this.pdfDocument.getPage(0);
          let annotations = page.getAnnotations();
          if (annotations.length > 0 && annotations\[0\].type === pdfService.AnnotationType.TEXT) {
            let newAnno = annotations\[0\];
            page.removeAnnotation(newAnno);
            let annotation = page.addAnnotation(newAnno);
            let newInfo = new pdfService.TextAnnotationInfo();
            newInfo.title = "new Title";
            newInfo.content = "new Info";
            newInfo.state = pdfService.TextAnnotationState.MARKED;
            newInfo.x = 100;
            newInfo.y = 100;
            page.setAnnotation(annotation, newInfo);
            let outPdfPath = this.context.filesDir + '/testSetAnnotation.pdf';
            let result = this.pdfDocument.saveDocument(outPdfPath);
            this.pdfDocument.releaseDocument();
            hilog.info(0x0000, 'PdfPage', 'setAnnotation %{public}s!', result ? 'success' : 'fail');
          }
        }
      })
      // Delete an annotation.
      Button('removeAnnotation').onClick(async () => {
        let filePath = this.context.filesDir + '/testAddTextAnnotation.pdf';
        let result = this.pdfDocument.loadDocument(filePath);
        if (result === pdfService.ParseResult.PARSE\_SUCCESS) {
          let page: pdfService.PdfPage = this.pdfDocument.getPage(0);
          let annotations = page.getAnnotations();
          if (annotations.length > 0 && annotations\[0\].type === pdfService.AnnotationType.TEXT) {
            page.removeAnnotation(annotations\[0\]);
            let outPdfPath = this.context.filesDir + '/testRemoveAnnotation.pdf';
            let result = this.pdfDocument.saveDocument(outPdfPath);
            this.pdfDocument.releaseDocument();
            hilog.info(0x0000, 'PdfPage', 'removeAnnotation %{public}s!', result ? 'success' : 'fail');
          }
        }
      })
    }
  }
}
