# Adding and Deleting Bookmarks

PDF Kit allows you to add and delete bookmarks for PDF documents.

When adding a bookmark, you can set the title, color, whether the bookmark is in bold or italic, and redirection information.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7b/v3/RKE8ekPlT2qhtc0N8_-i_g/en-us_image_0000002502061282.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062115Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=195D7B04BB8E3D6AF8156971A9F76C69EB49D51162E1BC16125E779AF9F4E969)

#### API Description

| 
API Name

 | 

Description

 |
| :-- | :-- |
| 

[createBookmark](https://developer.huawei.com/consumer/en/doc/harmonyos-references/pdf-arkts-pdfservice#section112600294114)(): Bookmark

 | 

Creates a bookmark for a PDF document.

 |
| 

[getRootBookmark](https://developer.huawei.com/consumer/en/doc/harmonyos-references/pdf-arkts-pdfservice#section191632714298)(): Bookmark

 | 

Obtains the first root bookmark of a PDF document.

 |
| 

[insertBookmark](https://developer.huawei.com/consumer/en/doc/harmonyos-references/pdf-arkts-pdfservice#section79471310105314)(bookmark: Bookmark, parent: Bookmark, position: number): boolean

 | 

Inserts a bookmark to a PDF document.

 |
| 

[setBookmarkInfo](https://developer.huawei.com/consumer/en/doc/harmonyos-references/pdf-arkts-pdfservice#section121011619472)(info: BookmarkInfo): void

 | 

Sets bookmark information.

 |
| 

[removeBookmark](https://developer.huawei.com/consumer/en/doc/harmonyos-references/pdf-arkts-pdfservice#section1601141912472)(bookmark: Bookmark): boolean

 | 

Removes a bookmark from a PDF document.

 |
| 

[setDestInfo](https://developer.huawei.com/consumer/en/doc/harmonyos-references/pdf-arkts-pdfservice#section96293491468)(info: DestInfo): void

 | 

Sets the bookmark redirection information.

 |
| 

[getBookmarkInfo](https://developer.huawei.com/consumer/en/doc/harmonyos-references/pdf-arkts-pdfservice#section17533902477)(): BookmarkInfo

 | 

Obtains bookmark information.

 |

#### Sample Code

**Adding a bookmark**:

1.  Call the **loadDocument** method to load a PDF document.
2.  Call the **createBookmark** method to create a bookmark.
3.  Call the **setDestInfo** method to set the bookmark redirection information.
4.  Call the **getBookmarkInfo** method to obtain bookmark information.
5.  Call the **setBookmarkInfo** method to set the bookmark content and style.
6.  Set the sandbox path for saving the document and save the settings.

**Deleting a bookmark**:

1.  Call the **loadDocument** method to load a PDF document.
2.  Call the **getRootBookmark** method to obtain the first root bookmark of the document.
3.  Call the **removeBookmark** method to delete a bookmark.
4.  Set the sandbox path for saving the document and save the settings.

import { pdfService } from '@kit.PDFKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

@Entry
@Component
struct PdfPage {
  private pdfDocument: pdfService.PdfDocument = new pdfService.PdfDocument();
  private context = this.getUIContext().getHostContext() as Context;

  build() {
    Column() {
      // Add a bookmark.
      Button('addBookmark').onClick(async () => {
        // Ensure that the **input.pdf** document exists in the sandbox directory.
        let filePath = this.context.filesDir + '/input.pdf';
        this.pdfDocument.loadDocument(filePath);
        // Create a bookmark.
        let mark1: pdfService.Bookmark = this.pdfDocument.createBookmark();
        let mark2: pdfService.Bookmark = this.pdfDocument.createBookmark();
        // Set the bookmark redirection information.
        let destInfo: pdfService.DestInfo = mark1.getDestInfo();
        destInfo.fitMode = pdfService.FitMode.FIT\_MODE\_XYZ;
        destInfo.pageIndex = 1;
        destInfo.left = 20;
        destInfo.top = 30;
        destInfo.zoom = 1.5;
        mark1.setDestInfo(destInfo);
        // Set the bookmark content and style.
        let bookInfo: pdfService.BookmarkInfo = mark1.getBookmarkInfo();
        bookInfo.title = 'Bookmark for going to the first page';
        bookInfo.titleColor = 12;
        bookInfo.isBold = true;
        bookInfo.isItalic = true;
        mark1.setBookmarkInfo(bookInfo);
        // Insert the created bookmark to the PDF page.
        this.pdfDocument.insertBookmark(mark1, null, 1);
        this.pdfDocument.insertBookmark(mark2, mark1, 1);
        // Set the sandbox path for saving the document and save the settings.
        let outPdfPath = this.context.filesDir + '/testAddBookmark.pdf';
        let result = this.pdfDocument.saveDocument(outPdfPath);
        hilog.info(0x0000, 'PdfPage', 'saveAddBookmark %{public}s!', result ? 'success' : 'fail');
      })
      // Delete the bookmark.
      Button('removeBookmark').onClick(async () => {
        // Ensure that the **testAddBookmark.pdf** document exists in the sandbox directory.
        this.pdfDocument.loadDocument(this.context.filesDir + '/testAddBookmark.pdf');
        let bookmarks: pdfService.Bookmark = this.pdfDocument.getRootBookmark();
        if (bookmarks.isRootBookmark()) {
          let hasRemoveBookmark: boolean = this.pdfDocument.removeBookmark(bookmarks);
          hilog.info(0x0000, 'PdfPage', 'removeBookmark %{public}s!', hasRemoveBookmark ? 'success' : 'fail');
          let outPdfPath = this.context.filesDir + '/testRemoveBookmark.pdf';
          let result = this.pdfDocument.saveDocument(outPdfPath);
          hilog.info(0x0000, 'PdfPage', 'saveRemoveBookmark %{public}s!', result ? 'success' : 'fail');
        }
      })
    }
  }
}
