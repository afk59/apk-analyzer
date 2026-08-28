# Searching for Keywords

When previewing a PDF document, you can search for keywords (English character case insensitivity) on the page and highlight them. In addition, you can use the [setSearchIndex](https://developer.huawei.com/consumer/en/doc/harmonyos-references/pdf-arkts-pdfviewmanage#section7253141182617) method to highlight the specified search results.

You can use the [getSearchIndex](https://developer.huawei.com/consumer/en/doc/harmonyos-references/pdf-arkts-pdfviewmanage#section10557163718239) method to obtain the highlight index, and use the [clearSearch](https://developer.huawei.com/consumer/en/doc/harmonyos-references/pdf-arkts-pdfviewmanage#section773545002018) method to clear all search results.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3d/v3/H5Z0JYUmQM24BJ5vm3d4kA/en-us_image_0000002502061280.jpg?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062115Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=DF6D1E9740FE5A15808C2E86087D121887C5B9D88654ADDE188BB100A6EAC092 "Click to enlarge")

#### API Description

| 
API Name

 | 

Description

 |
| :-- | :-- |
| 

[searchKey](https://developer.huawei.com/consumer/en/doc/harmonyos-references/pdf-arkts-pdfviewmanage#section117864247160)(text: string, listener: Callback<number>): void

 | 

Searches for text and returns the total number of matches.

 |
| 

[clearSearch](https://developer.huawei.com/consumer/en/doc/harmonyos-references/pdf-arkts-pdfviewmanage#section773545002018)(): void

 | 

Cancels the highlight of the matched text. This operation is equivalent to searching for empty strings.

 |
| 

[setSearchIndex](https://developer.huawei.com/consumer/en/doc/harmonyos-references/pdf-arkts-pdfviewmanage#section7253141182617)(index: number): void

 | 

Sets the index of the matching search result. The page will jump to the corresponding search result.

 |
| 

[getSearchIndex](https://developer.huawei.com/consumer/en/doc/harmonyos-references/pdf-arkts-pdfviewmanage#section10557163718239)(): number

 | 

Obtains the index of the search result that matches the keyword. The default index after the search API is executed is **0**.

 |

#### Sample Code

1.  Load the PDF document.
2.  Call the PdfView preview component to render the display.
3.  Call the **searchKey** method via the **searchKey** button to search for a specified keyword.
4.  Click the previous or next search button to go to the corresponding result.
5.  Call the **getSearchIndex** method via the **getSearchIndex** button to obtain the current search result index.
6.  Call the **clearSearch** method via the **clearSearch** button to clear the search results.

import { pdfService, PdfView, pdfViewManager } from '@kit.PDFKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

@Entry
@Component
struct PdfPage {
  private controller: pdfViewManager.PdfController = new pdfViewManager.PdfController();
  private context = this.getUIContext().getHostContext() as Context;
  private loadResult: pdfService.ParseResult = pdfService.ParseResult.PARSE\_ERROR\_FORMAT;
  private searchIndex = 0;
  private charCount = 0;

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
        // Search for keywords.
        Button('searchKey').onClick(async () => {
          if (this.loadResult === pdfService.ParseResult.PARSE\_SUCCESS) {
            this.controller.searchKey('C++', (index: number) => {
              this.charCount = index;
              hilog.info(0x0000, 'PdfPage', 'searchKey %{public}s!', index + '');
            })
          }
        })
        // Previous one.
        Button('setSearchPrevIndex').onClick(async () => {
          if (this.loadResult === pdfService.ParseResult.PARSE\_SUCCESS) {
            if(this.searchIndex > 0) {
              this.controller.setSearchIndex(--this.searchIndex);
            }
          }
        })
        // Next one.
        Button('setSearchNextIndex').onClick(async () => {
          if (this.loadResult === pdfService.ParseResult.PARSE\_SUCCESS) {
            if(this.searchIndex < this.charCount) {
              this.controller.setSearchIndex(++this.searchIndex);
            }
          }
        })
        // Obtain the index of the current page.
        Button('getSearchIndex').onClick(async () => {
          if (this.loadResult === pdfService.ParseResult.PARSE\_SUCCESS) {
            let curSearchIndex = this.controller.getSearchIndex();
            hilog.info(0x0000, 'PdfPage', 'curSearchIndex %{public}s!', curSearchIndex + '');
          }
        })
        // Clear the highlight of the searched text.
        Button('clearSearch').onClick(async () => {
          if (this.loadResult === pdfService.ParseResult.PARSE\_SUCCESS) {
            this.controller.clearSearch();
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
