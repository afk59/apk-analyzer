# Obtaining Book Information

You can use [DocumentViewPicker](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-file-picker#documentviewpicker) to import a book file to the [app sandbox directory](../../../../application-framework/core-file-kit/application-files/application-sandbox/document.md). Then your app can import the book file to the bookshelf, use the parsing capability to obtain the book information including the book cover, book title, and author, and display the information on the bookshelf.

#### Service Process

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/55/v3/J7ruuqhOSIKC23MHvJQEWg/en-us_image_0000002227052488.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062118Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=CB0772A4AA76A8F2366CF19849968E947FD54BC849A1277757DAF0BA7AE2C174 "Click to enlarge")

#### API Description

This function involves three APIs. See the following table for detailed API information.

| 
API

 | 

Description

 |
| :-- | :-- |
| 

[getDefaultHandler](https://developer.huawei.com/consumer/en/doc/harmonyos-references/reader-book-parser#section896820167243)(path: string): Promise<BookParserHandler>

 | 

Obtains the default book parser.

 |
| 

[getBookInfo](https://developer.huawei.com/consumer/en/doc/harmonyos-references/reader-book-parser#section599065683812)(): BookInfo

 | 

Obtains book information.

 |
| 

[getResourceContent](https://developer.huawei.com/consumer/en/doc/harmonyos-references/reader-book-parser#section17546184255211)(spineIndex: number, filePath: string): ArrayBuffer

 | 

Obtains book content.

 |

#### Development Procedure

1.  Import required modules.
    
    import { common } from '@kit.AbilityKit';
    import { bookParser } from '@kit.ReaderKit';
    import { hilog } from '@kit.PerformanceAnalysisKit';
    import { image } from '@kit.ImageKit';
    
2.  Initialize the book parser for the book file that has been imported to the [app sandbox directory](../../../../application-framework/core-file-kit/application-files/application-sandbox/document.md).
    
    private defaultHandler: bookParser.BookParserHandler | null = null;
    
    aboutToAppear(): void {
      this.init().then(() => {
      });
    }
    
    private async init() {
      let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
      let path: string = \`${context.filesDir}/abc.epub\`;
      try {
        this.defaultHandler = await bookParser.getDefaultHandler(path);
      } catch (error) {
        hilog.error(0x0000, "testTAG", \`getDefaultHandler failed, Code: ${error.code}, message: ${error.message}\`);
      }
    }
    
3.  Obtain and display the book title, author, and cover.
    
    @State bookCover: PixelMap | null = null;
    @State bookTitle: string = '';
    @State author: string = '';
    
    aboutToAppear(): void {
      this.init().then(() => {
        this.getBookInfo();
      });
    }
    
    private async getBookInfo() {
      try {
        let bookInfo: bookParser.BookInfo | undefined = this.defaultHandler?.getBookInfo();
        if (bookInfo) {
          this.bookTitle = bookInfo.bookTitle || '';
          this.author = bookInfo?.bookCreator || '';
          // SpineIndex is not required for obtaining the book cover.
          let buffer = this.defaultHandler?.getResourceContent(-1, bookInfo.bookCoverImage);
          let imageSource: image.ImageSource = image.createImageSource(buffer);
          this.bookCover = await imageSource.createPixelMap();
          imageSource.release();
        }
        hilog.info(0x0000, 'testTAG', 'getBookInfo bookInfo is: ' + JSON.stringify(bookInfo));
      } catch (error) {
        hilog.error(0x0000, 'testTAG', \`getBookInfo failed, Code: ${error.code}, message: ${error.message}\`);
      }
    }
    
    build() {
      Column() {
        Text('Book title:' + this.bookTitle)
          .fontSize(20)
          .fontColor("#E6000000")
          .margin({ top: 50 })
        Text('Author:' + this.author)
          .fontSize(20)
          .fontColor("#E6000000")
          .margin({ top: 10 })
        Image(this.bookCover)
          .width(200)
          .aspectRatio(3 / 4)
          .borderRadius(5)
          .margin({ top: 10 })
      }
      .alignItems(HorizontalAlign.Start)
      .margin({ left: 10, right: 10 })
    }
