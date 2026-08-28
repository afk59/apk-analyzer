# pdfViewManager (PDF Preview)

This module provides the unified PDF preview capability for apps.

**System capability**: SystemCapability.OfficeService.PDFService.Core

**Start version**: 5.0.0(12)

#### Importing Modules

import { pdfViewManager } from '@kit.PDFKit';

#### PdfController

PDF file controller class.

**System capability**: SystemCapability.OfficeService.PDFService.Core

**Start version**: 5.0.0(12)

#### \[h2\]constructor

constructor()

Constructor.

**System capability**: SystemCapability.OfficeService.PDFService.Core

**Start version**: 5.0.0(12)

import { pdfViewManager } from '@kit.PDFKit';

let pdfController = new pdfViewManager.PdfController();

#### \[h2\]setViewOffset

setViewOffset(offsetX: number, offsetY: number, refreshView: boolean): void

Sets the X and Y coordinate offsets of the visible area.

**System capability**: SystemCapability.OfficeService.PDFService.Core

**Start version**: 5.0.0(12)

**Parameters:**

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

offsetX

 | 

number

 | 

Yes

 | 

X-coordinate offset. The value ranges from **0** to **1**, indicating a relative offset of 0% to 100% of the total width. For example, if the total width is 1000 px, set this parameter to **0.5** for a 500 px offset.

 |
| 

offsetY

 | 

number

 | 

Yes

 | 

Y-coordinate offset. The value ranges from **0** to **1**, indicating a relative offset of 0% to 100% of the total height. For example, if the total height is 1000 px, set this parameter to **0.5** for a 500 px offset.

 |
| 

refreshView

 | 

boolean

 | 

Yes

 | 

Indicates whether to refresh the visible area (**true**: the page is clear when users scroll) or not (**false**: the page is blurry when users scroll).

 |

**Example:**

import { pdfViewManager, pdfService } from '@kit.PDFKit';

let context = this.getUIContext().getHostContext() as Context;
let dir = context.filesDir;
let filePath = dir + \`/input.pdf\`;
let pdfController = new pdfViewManager.PdfController();
let loadResult: pdfService.ParseResult = await pdfController.loadDocument(filePath);
if (pdfService.ParseResult.PARSE\_SUCCESS === loadResult) {
  pdfController.setViewOffset(0.5, 0.5, true);
}

#### \[h2\]getPagePixelMap

getPagePixelMap(pageIndex: number, isSync?: boolean): Promise<image.PixelMap>

Obtains the thumbnail of the corresponding PDF page. This API returns the result asynchronously through a promise.

**System capability**: SystemCapability.OfficeService.PDFService.Core

**Start version**: 5.0.0(12)

**Parameters:**

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

pageIndex

 | 

number

 | 

Yes

 | 

Page index. The value **0** indicates the start page.

 |
| 

isSync

 | 

boolean

 | 

No

 | 

Indicates whether to obtain the thumbnail of the PDF page (**true**) or not (**false**). The default value is **false**.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<[image.PixelMap](../../../../media/image-kit/arkts-apis/ohos-multimedia-image-image-processing/interface-pixelmap/document.md)\>

 | 

**image.PixelMap** object returned through a promise.

 |

**Example**:

import { pdfViewManager, pdfService } from '@kit.PDFKit';

let context = this.getUIContext().getHostContext() as Context;
let dir = context.filesDir;
let filePath = dir + \`/input.pdf\`;
let pdfController = new pdfViewManager.PdfController();
let loadResult: pdfService.ParseResult = await pdfController.loadDocument(filePath);
if (pdfService.ParseResult.PARSE\_SUCCESS === loadResult) {
  let image = await pdfController.getPagePixelMap(0, true);
}

#### \[h2\]registerScrollListener

registerScrollListener(listener: Callback<ScrollParam>): void

Registers a scrolling listener.

**System capability**: SystemCapability.OfficeService.PDFService.Core

**Start version**: 5.0.0(12)

**Parameters:**

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

listener

 | 

[Callback](../../../../system/basic-functions/basic-services-kit/arkts-apis/others/ohos-base-public-callback-information/document.md#callback)<[ScrollParam](#section132324279455)\>

 | 

Yes

 | 

Listens to page scrolling. The listener returns **ScrollParam** data.

 |

**Example**:

import { pdfViewManager } from '@kit.PDFKit';

let pdfController = new pdfViewManager.PdfController();
pdfController.registerScrollListener((scrollParam: pdfViewManager.ScrollParam) => { });

#### \[h2\]enablePageDrag

enablePageDrag(verticalEnabled: boolean, horizontalEnabled: boolean): void

Sets whether the page supports dragging.

**System capability**: SystemCapability.OfficeService.PDFService.Core

**Start version**: 5.0.0(12)

**Parameters:**

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

verticalEnabled

 | 

boolean

 | 

Yes

 | 

Indicates whether the page can be dragged vertically along the Y axis (**true**) or not (**false**).

 |
| 

horizontalEnabled

 | 

boolean

 | 

Yes

 | 

Indicates whether the page can be dragged horizontally along the X axis (**true**) or not (**false**).

 |

**Example:**

import { pdfViewManager, pdfService } from '@kit.PDFKit';

let context = this.getUIContext().getHostContext() as Context;
let dir = context.filesDir;
let filePath = dir + \`/input.pdf\`;
let pdfController = new pdfViewManager.PdfController();
let loadResult: pdfService.ParseResult = await pdfController.loadDocument(filePath);
if (pdfService.ParseResult.PARSE\_SUCCESS === loadResult) {
  pdfController.enablePageDrag(true, true);
}

#### \[h2\]loadDocument

loadDocument(path: string, password?: string, initPageIndex?: number, onProgress?: Callback<number>): Promise<pdfService.ParseResult>

Loads a file and displays it on a specified page. This API returns the result asynchronously through a promise. Repeated **loadDocument** calls are not supported. Before any subsequent call, you must use **releaseDocument** to release the loaded document. This ensures that resources are properly released and prevents potential conflicts or exceptions.

**System capability**: SystemCapability.OfficeService.PDFService.Core

**Start version**: 5.0.0(12)

**Parameters:**

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

path

 | 

string

 | 

Yes

 | 

Document path.

 |
| 

password

 | 

string

 | 

No

 | 

Password. An empty character string is used by default.

 |
| 

initPageIndex

 | 

number

 | 

No

 | 

Index of the initial page of the document to be opened. The value **0** indicates the initial page. The default value is **0**.

 |
| 

onProgress

 | 

[Callback](../../../../system/basic-functions/basic-services-kit/arkts-apis/others/ohos-base-public-callback-information/document.md#callback)<number>

 | 

No

 | 

Callback for the document loading progress, which returns data of the number type. After this parameter is passed, the document loading progress is returned. If this parameter is not passed, no document loading progress will be returned.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<pdfService.[ParseResult](../pdfservice-pdf-services/document.md#section913412299528)\>

 | 

**ParseResult** data returned by a promise.

 |

**Example:**

import { pdfViewManager, pdfService } from '@kit.PDFKit';

let pdfController = new pdfViewManager.PdfController();
let context = this.getUIContext().getHostContext() as Context;
let dir = context.filesDir;
let tempFilePath = dir + '/test.pdf';
let loadResult: pdfService.ParseResult = await pdfController.loadDocument(tempFilePath);

#### \[h2\]releaseDocument

releaseDocument(): void

Releases loaded files.

**System capability**: SystemCapability.OfficeService.PDFService.Core

**Start version**: 5.0.0(12)

**Example:**

import { pdfViewManager, pdfService } from '@kit.PDFKit';

let pdfController = new pdfViewManager.PdfController();
let context = this.getUIContext().getHostContext() as Context;
let dir = context.filesDir;
let tempFilePath = dir + '/test.pdf';
let loadResult: pdfService.ParseResult = await pdfController.loadDocument(tempFilePath);
if (pdfService.ParseResult.PARSE\_SUCCESS === loadResult) {
  pdfController.releaseDocument();
}

#### \[h2\]setHighlightRects

setHighlightRects(rectArray: Array<PageRects>, color?: number): void

Sets a highlighted rectangular area at the UI layer using the PDF page's lower left corner (0,0) as the origin, measured in PDF points and extending upward.

**System capability**: SystemCapability.OfficeService.PDFService.Core

**Start version**: 5.0.0(12)

**Parameters:**

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

rectArray

 | 

Array<[PageRects](#section165811065495)\>

 | 

Yes

 | 

Rectangular area of a highlighted block on the page. The minimum value of **left** and **right** for the rectangular area is **0**, and their maximum value is the width of the PDF page. The minimum value of **top** and **bottom** is **0**, and their maximum value is the height of the PDF page.

 |
| 

color

 | 

number

 | 

No

 | 

Highlight color (ARGB). The value ranges from **0x00000000** to **0xFFFFFFFF**. The default value is **0x00000000**.

 |

**Example**:

import { pdfViewManager, pdfService } from '@kit.PDFKit'

let context = this.getUIContext().getHostContext() as Context;
let dir = context.filesDir;
let filePath = dir + \`/input.pdf\`;
let pdfController = new pdfViewManager.PdfController();
let loadResult: pdfService.ParseResult = await pdfController.loadDocument(filePath);
if (pdfService.ParseResult.PARSE\_SUCCESS === loadResult) {
  const highlightArray = new Array<pdfViewManager.PageRects>();
  const rectArray = new Array<pdfService.PdfRect>();
  const rect1: pdfService.PdfRect = { left: 20, top: 0, right: 120, bottom: 300 };
  rectArray.push(rect1);
  highlightArray.push(new pdfViewManager.PageRects(0, rectArray));
  pdfController.setHighlightRects(highlightArray, 0xAA666666);
}

#### \[h2\]setHighlightText

setHighlightText(pageIndex: number, textArray: string\[\], color: number): void

Highlight the selected text. Calling this API will interrupt the [searchKey](#section117864247160) command.

**System capability**: SystemCapability.OfficeService.PDFService.Core

**Start version**: 5.0.0(12)

**Parameters:**

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

pageIndex

 | 

number

 | 

Yes

 | 

Page index. The value **0** indicates the start page.

 |
| 

textArray

 | 

string\[\]

 | 

Yes

 | 

Selected text.

 |
| 

color

 | 

number

 | 

Yes

 | 

Highlight color (ARGB). The value ranges from **0x00000000** to **0xFFFFFFFF**.

 |

**Example:**

import { pdfViewManager, pdfService } from '@kit.PDFKit';

let context = this.getUIContext().getHostContext() as Context;
let dir = context.filesDir;
let filePath = dir + \`/input.pdf\`;
let pdfController = new pdfViewManager.PdfController();
let loadResult: pdfService.ParseResult = await pdfController.loadDocument(filePath);
if (pdfService.ParseResult.PARSE\_SUCCESS === loadResult) {
  pdfController.setHighlightText(1, \['1111', 'aaaa'\], 0x66666666);
}

#### \[h2\]setPageZoom

setPageZoom(zoom: number): void

Sets the zoom ratio.

**System capability**: SystemCapability.OfficeService.PDFService.Core

**Start version**: 5.0.0(12)

**Parameters:**

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

zoom

 | 

number

 | 

Yes

 | 

Zoom ratio (from **0.1** to **10**). (If the value is greater than 10, the value **10** is used. If the value is less than 0.1, the value **0.1** is used.)

 |

**Example**:

import { pdfViewManager, pdfService } from '@kit.PDFKit';

let context = this.getUIContext().getHostContext() as Context;
let dir = context.filesDir;
let filePath = dir + \`/input.pdf\`;
let pdfController = new pdfViewManager.PdfController();
let loadResult: pdfService.ParseResult = await pdfController.loadDocument(filePath);
if (pdfService.ParseResult.PARSE\_SUCCESS === loadResult) {
  pdfController.setPageZoom(2);
}

#### \[h2\]getPageZoom

getPageZoom(): number

Obtains the zoom ratio.

**System capability**: SystemCapability.OfficeService.PDFService.Core

**Start version**: 5.0.0(12)

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

number

 | 

Zoom ratio (from **0.1** to **10**).

 |

**Example:**

import { pdfViewManager, pdfService } from '@kit.PDFKit';

let context = this.getUIContext().getHostContext() as Context;
let dir = context.filesDir;
let filePath = dir + \`/input.pdf\`;
let pdfController = new pdfViewManager.PdfController();
let loadResult: pdfService.ParseResult = await pdfController.loadDocument(filePath);
if (pdfService.ParseResult.PARSE\_SUCCESS === loadResult) {
  let pageZoom = pdfController.getPageZoom();
}

#### \[h2\]setPageLayout

setPageLayout(columnCount: pdfService.PageLayout): void

Sets the page layout mode. The options are **1** (single-page) and **2** (dual-page).

**System capability**: SystemCapability.OfficeService.PDFService.Core

**Start version**: 5.0.0(12)

**Parameters:**

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

columnCount

 | 

pdfService.[PageLayout](../pdfservice-pdf-services/document.md#section1749384210523)

 | 

Yes

 | 

Page layout mode. The options are **1** (single-page) and **2** (dual-page).

 |

**Example**:

import { pdfService, pdfViewManager } from '@kit.PDFKit';

let context = this.getUIContext().getHostContext() as Context;
let dir = context.filesDir;
let filePath = dir + \`/input.pdf\`;
let pdfController = new pdfViewManager.PdfController();
let loadResult: pdfService.ParseResult = await pdfController.loadDocument(filePath);
if (pdfService.ParseResult.PARSE\_SUCCESS === loadResult) {
  pdfController.setPageLayout(pdfService.PageLayout.LAYOUT\_SINGLE);
}

#### \[h2\]getPageLayout

getPageLayout(): pdfService.PageLayout

Obtains the page layout mode.

**System capability**: SystemCapability.OfficeService.PDFService.Core

**Start version**: 5.0.0(12)

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

pdfService.[PageLayout](../pdfservice-pdf-services/document.md#section1749384210523)

 | 

Page layout mode. The options are **1** (single-page) and **2** (dual-page).

 |

**Example**:

import { pdfService, pdfViewManager } from '@kit.PDFKit';

let context = this.getUIContext().getHostContext() as Context;
let dir = context.filesDir;
let filePath = dir + \`/input.pdf\`;
let pdfController = new pdfViewManager.PdfController();
let loadResult: pdfService.ParseResult = await pdfController.loadDocument(filePath);
if (pdfService.ParseResult.PARSE\_SUCCESS === loadResult) {
  let pageLayout: pdfService.PageLayout = pdfController.getPageLayout();
}

#### \[h2\]setPageContinuous

setPageContinuous(isContinuous: boolean): void

Sets whether the page is scrolled continuously. Only vertical scrolling is supported.

**System capability**: SystemCapability.OfficeService.PDFService.Core

**Start version**: 5.0.0(12)

**Parameters:**

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

isContinuous

 | 

boolean

 | 

Yes

 | 

Indicates whether the scrolling is continuous (**true**) or not (**false**).

 |

**Example**:

import { pdfViewManager, pdfService } from '@kit.PDFKit';

let context = this.getUIContext().getHostContext() as Context;
let dir = context.filesDir;
let filePath = dir + \`/input.pdf\`;
let pdfController = new pdfViewManager.PdfController();
let loadResult: pdfService.ParseResult = await pdfController.loadDocument(filePath);
if (pdfService.ParseResult.PARSE\_SUCCESS === loadResult) {
  pdfController.setPageContinuous(true);
}

#### \[h2\]isPageContinuous

isPageContinuous(): boolean

Checks whether the page is scrolled continuously. Only vertical scrolling is supported.

**System capability**: SystemCapability.OfficeService.PDFService.Core

**Start version**: 5.0.0(12)

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

boolean

 | 

Whether the scrolling is continuous (**true**) or not (**false**).

 |

**Example**:

import { pdfViewManager, pdfService } from '@kit.PDFKit';

let context = this.getUIContext().getHostContext() as Context;
let dir = context.filesDir;
let filePath = dir + \`/input.pdf\`;
let pdfController = new pdfViewManager.PdfController();
let loadResult: pdfService.ParseResult = await pdfController.loadDocument(filePath);
if (pdfService.ParseResult.PARSE\_SUCCESS === loadResult) {  
  let pageContinuous: boolean = pdfController.isPageContinuous();
}

#### \[h2\]setPageFit

setPageFit(pageFit: pdfService.PageFit): void

Sets the page fit mode.

**System capability**: SystemCapability.OfficeService.PDFService.Core

**Start version**: 5.0.0(12)

**Parameters:**

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

pageFit

 | 

pdfService.[PageFit](../pdfservice-pdf-services/document.md#section655755325212)

 | 

Yes

 | 

Page fit mode.

 |

**Example**:

import { pdfService, pdfViewManager } from '@kit.PDFKit';

let context = this.getUIContext().getHostContext() as Context;
let dir = context.filesDir;
let filePath = dir + \`/input.pdf\`;
let pdfController = new pdfViewManager.PdfController();
let loadResult: pdfService.ParseResult = await pdfController.loadDocument(filePath);
if (pdfService.ParseResult.PARSE\_SUCCESS === loadResult) {
  pdfController.setPageFit(pdfService.PageFit.FIT\_NONE);
}

#### \[h2\]getPageFit

getPageFit(): pdfService.PageFit

Obtains the page fit mode.

**System capability**: SystemCapability.OfficeService.PDFService.Core

**Start version**: 5.0.0(12)

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

pdfService.[PageFit](../pdfservice-pdf-services/document.md#section655755325212)

 | 

Page fit mode.

 |

**Example:**

import { pdfService, pdfViewManager } from '@kit.PDFKit';

let context = this.getUIContext().getHostContext() as Context;
let dir = context.filesDir;
let filePath = dir + \`/input.pdf\`;
let pdfController = new pdfViewManager.PdfController();
let loadResult: pdfService.ParseResult = await pdfController.loadDocument(filePath);
if (pdfService.ParseResult.PARSE\_SUCCESS === loadResult) {
  let pageFitMode: pdfService.PageFit = pdfController.getPageFit();
}

#### \[h2\]setPageSpacing

setPageSpacing(horizontal: number, vertical?: number): void

Sets the line spacing and column spacing between pages.

**System capability**: SystemCapability.OfficeService.PDFService.Core

**Start version**: 5.0.0(12)

**Parameters:**

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

horizontal

 | 

number

 | 

Yes

 | 

Spacing between the left and right pages in dual-page mode, in vp. The value is greater than or equal to **0**.

 |
| 

vertical

 | 

number

 | 

No

 | 

Spacing between the upper and lower pages when the page is scrolled continuously, in vp. The value is greater than or equal to **0**. The default value is **10**.

 |

**Example:**

import { pdfViewManager, pdfService } from '@kit.PDFKit';

let context = this.getUIContext().getHostContext() as Context;
let dir = context.filesDir;
let filePath = dir + \`/input.pdf\`;
let pdfController = new pdfViewManager.PdfController();
let loadResult: pdfService.ParseResult = await pdfController.loadDocument(filePath);
if (pdfService.ParseResult.PARSE\_SUCCESS === loadResult) {
  pdfController.setPageSpacing(20, 20);
}

#### \[h2\]getPageHorizontalSpacing

getPageHorizontalSpacing(): number

Obtains the spacing between the left and right pages in dual-page mode.

**System capability**: SystemCapability.OfficeService.PDFService.Core

**Start version**: 5.0.0(12)

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

number

 | 

Spacing between the left and right pages, in vp.

 |

**Example**:

import { pdfViewManager, pdfService } from '@kit.PDFKit';

let context = this.getUIContext().getHostContext() as Context;
let dir = context.filesDir;
let filePath = dir + \`/input.pdf\`;
let pdfController = new pdfViewManager.PdfController();
let loadResult: pdfService.ParseResult = await pdfController.loadDocument(filePath);
if (pdfService.ParseResult.PARSE\_SUCCESS === loadResult) {
  let horSpacing = pdfController.getPageHorizontalSpacing();
}

#### \[h2\]getPageVerticalSpacing

getPageVerticalSpacing(): number

Obtains the spacing between the upper and lower pages.

**System capability**: SystemCapability.OfficeService.PDFService.Core

**Start version**: 5.0.0(12)

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

number

 | 

Spacing between the upper and lower pages, in vp.

 |

**Example**:

import { pdfViewManager, pdfService } from '@kit.PDFKit';

let context = this.getUIContext().getHostContext() as Context;
let dir = context.filesDir;
let filePath = dir + \`/input.pdf\`;
let pdfController = new pdfViewManager.PdfController();
let loadResult: pdfService.ParseResult = await pdfController.loadDocument(filePath);
if (pdfService.ParseResult.PARSE\_SUCCESS === loadResult) {
  let verSpacing = pdfController.getPageVerticalSpacing();
}

#### \[h2\]getPageCount

getPageCount(): number

Obtains the total page count of a PDF file.

**System capability**: SystemCapability.OfficeService.PDFService.Core

**Start version**: 5.0.0(12)

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

number

 | 

Total page count. The value is greater than or equal to **0**.

 |

**Example**:

import { pdfViewManager, pdfService } from '@kit.PDFKit';

let context = this.getUIContext().getHostContext() as Context;
let dir = context.filesDir;
let filePath = dir + \`/input.pdf\`;
let pdfController = new pdfViewManager.PdfController();
let loadResult: pdfService.ParseResult = await pdfController.loadDocument(filePath);
if (pdfService.ParseResult.PARSE\_SUCCESS === loadResult) {
  let pageCount = pdfController.getPageCount();
}

#### \[h2\]getPageIndex

getPageIndex(): number

Obtains the index of the current PDF page.

**System capability**: SystemCapability.OfficeService.PDFService.Core

**Start version**: 5.0.0(12)

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

number

 | 

Page index.

 |

**Example**:

import { pdfViewManager, pdfService } from '@kit.PDFKit';

let context = this.getUIContext().getHostContext() as Context;
let dir = context.filesDir;
let filePath = dir + \`/input.pdf\`;
let pdfController = new pdfViewManager.PdfController();
let loadResult: pdfService.ParseResult = await pdfController.loadDocument(filePath);
if (pdfService.ParseResult.PARSE\_SUCCESS === loadResult) {
  let pageIndex = pdfController.getPageIndex();
}

#### \[h2\]goToPage

goToPage(pageIndex: number): void

Redirects to a specified page.

**System capability**: SystemCapability.OfficeService.PDFService.Core

**Start version**: 5.0.0(12)

**Parameters:**

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

pageIndex

 | 

number

 | 

Yes

 | 

Index of a specified page, which is smaller than the total page count. The value **0** indicates the start page.

 |

**Example**:

import { pdfViewManager, pdfService } from '@kit.PDFKit';

let context = this.getUIContext().getHostContext() as Context;
let dir = context.filesDir;
let filePath = dir + \`/input.pdf\`;
let pdfController = new pdfViewManager.PdfController();
let loadResult: pdfService.ParseResult = await pdfController.loadDocument(filePath);
if (pdfService.ParseResult.PARSE\_SUCCESS === loadResult) {
  pdfController.goToPage(1);
}

#### \[h2\]setPageRotation

setPageRotation(pageIndex: number, angle: pdfService.RotationAngle): void

Rotates a specified page (only the display is rotated; the content remains unchanged) by 0, 90, 180, or 270 degrees.

**System capability**: SystemCapability.OfficeService.PDFService.Core

**Start version**: 5.0.0(12)

**Parameters:**

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

pageIndex

 | 

number

 | 

Yes

 | 

Index of a specified page, which is smaller than the total page count. The value **0** indicates the start page.

 |
| 

angle

 | 

pdfService.[RotationAngle](../pdfservice-pdf-services/document.md#section554915414532)

 | 

Yes

 | 

Rotation angle of a specified page.

 |

**Example**:

import { pdfService, pdfViewManager } from '@kit.PDFKit';

let context = this.getUIContext().getHostContext() as Context;
let dir = context.filesDir;
let filePath = dir + \`/input.pdf\`;
let pdfController = new pdfViewManager.PdfController();
let loadResult: pdfService.ParseResult = await pdfController.loadDocument(filePath);
if (pdfService.ParseResult.PARSE\_SUCCESS === loadResult) {
  pdfController.setPageRotation(1, pdfService.RotationAngle.ANGLE\_90);
}

#### \[h2\]getPageRotation

getPageRotation(pageIndex: number): pdfService.RotationAngle

Obtains the rotation degree of a specified page. The value can be **0**, **90**, **180**, or **270**.

**System capability**: SystemCapability.OfficeService.PDFService.Core

**Start version**: 5.0.0(12)

**Parameters:**

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

pageIndex

 | 

number

 | 

Yes

 | 

Index of a specified page, which is smaller than the total page count. The value **0** indicates the start page.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

pdfService.[RotationAngle](../pdfservice-pdf-services/document.md#section554915414532)

 | 

Rotation angle of a specified page.

 |

**Example**:

import { pdfService, pdfViewManager } from '@kit.PDFKit';

let context = this.getUIContext().getHostContext() as Context;
let dir = context.filesDir;
let filePath = dir + \`/input.pdf\`;
let pdfController = new pdfViewManager.PdfController();
let loadResult: pdfService.ParseResult = await pdfController.loadDocument(filePath);
if (pdfService.ParseResult.PARSE\_SUCCESS === loadResult) {
  let pageIndex: pdfService.RotationAngle = pdfController.getPageRotation(1);
}

#### \[h2\]enableAnnotation

enableAnnotation(annotationType: SupportedAnnotationType, color?: number): void

Switches between common operations and adds annotations. Currently, highlight, underline, and strikethrough are supported.

**System capability**: SystemCapability.OfficeService.PDFService.Core

**Start version**: 5.0.0(12)

**Parameters:**

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

annotationType

 | 

[SupportedAnnotationType](#section16111165319147)

 | 

Yes

 | 

Supported annotation types.

 |
| 

color

 | 

number

 | 

No

 | 

Color (ARGB). The value ranges from **0x00000000** to **0xFFFFFFFF**. The default value is **0xFFFFFFFF**.

 |

**Example**:

import { pdfViewManager, pdfService } from '@kit.PDFKit';

let context = this.getUIContext().getHostContext() as Context;
let dir = context.filesDir;
let filePath = dir + \`/input.pdf\`;
let pdfController = new pdfViewManager.PdfController();
let loadResult: pdfService.ParseResult = await pdfController.loadDocument(filePath);
if (pdfService.ParseResult.PARSE\_SUCCESS === loadResult) {
  pdfController.enableAnnotation(pdfViewManager.SupportedAnnotationType.STRIKETHROUGH, 0xAAEEEEEE);
}

#### \[h2\]addMarkupAnnotation

addMarkupAnnotation(annotationType: SupportedAnnotationType, selectedRects: Array<SelectedRects>, color: number): void

Adds a text annotation at the PDF annotation layer using the PDFView's upper left corner (0,0) as the origin, measured in pixels and extending downward. For example, the [registerAnnotationSelectedListener](#section2081318593516) callback can be used to highlight the text annotation.

**System capability**: SystemCapability.OfficeService.PDFService.Core

**Start version**: 5.0.0(12)

**Parameters**:

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

annotationType

 | 

[SupportedAnnotationType](#section16111165319147)

 | 

Yes

 | 

Annotation type.

 |
| 

selectedRects

 | 

Array<[SelectedRects](#section11370716427)\>

 | 

Yes

 | 

Highlighted rectangular area.

 |
| 

color

 | 

number

 | 

Yes

 | 

Color (ARGB). The value ranges from **0x00000000** to **0xFFFFFFFF**.

 |

**Example**:

import { pdfService, pdfViewManager } from '@kit.PDFKit';

let context = this.getUIContext().getHostContext() as Context;
let dir = context.filesDir;
let filePath = dir + \`/input.pdf\`;
let pdfController = new pdfViewManager.PdfController();
let loadResult: pdfService.ParseResult = await pdfController.loadDocument(filePath);
if (pdfService.ParseResult.PARSE\_SUCCESS === loadResult) {
  let rectArray: Array<pdfService.PdfRect> = \[{ left: 5, top: 5, right: 250, bottom: 250}\];
  let selectedRects: Array<pdfViewManager.SelectedRects> = \[new pdfViewManager.SelectedRects(0, rectArray, 0)\];
  pdfController.addMarkupAnnotation(pdfViewManager.SupportedAnnotationType.UNDERLINE, selectedRects, 0xAA666666);
}

#### \[h2\]disableAnnotation

disableAnnotation(): void

Disables annotations.

**System capability**: SystemCapability.OfficeService.PDFService.Core

**Start version**: 5.0.0(12)

**Example**:

import { pdfViewManager, pdfService } from '@kit.PDFKit';

let context = this.getUIContext().getHostContext() as Context;
let dir = context.filesDir;
let filePath = dir + \`/input.pdf\`;
let pdfController = new pdfViewManager.PdfController();
let loadResult: pdfService.ParseResult = await pdfController.loadDocument(filePath);
if (pdfService.ParseResult.PARSE\_SUCCESS === loadResult) {
  pdfController.disableAnnotation();
}

#### \[h2\]deleteSelectedAnnotation

deleteSelectedAnnotation(annotationIndex: number, pageIndex: number): void

Deletes a selected annotation.

**System capability**: SystemCapability.OfficeService.PDFService.Core

**Start version**: 5.0.0(12)

**Parameters:**

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

annotationIndex

 | 

number

 | 

Yes

 | 

Annotation index.

 |
| 

pageIndex

 | 

number

 | 

Yes

 | 

Page index.

 |

**Example**:

import { pdfViewManager, pdfService } from '@kit.PDFKit';

let context = this.getUIContext().getHostContext() as Context;
let dir = context.filesDir;
let filePath = dir + \`/input.pdf\`;
let pdfController = new pdfViewManager.PdfController();
let loadResult: pdfService.ParseResult = await pdfController.loadDocument(filePath);
if (pdfService.ParseResult.PARSE\_SUCCESS === loadResult) {
  // Verify that there is an annotation on the first page.
  pdfController.deleteSelectedAnnotation(0, 0);
}

#### \[h2\]updateMarkupAnnotation

updateMarkupAnnotation(annotationIndex: number, pageIndex: number, color: number): void

Changes the annotation color.

**System capability**: SystemCapability.OfficeService.PDFService.Core

**Start version**: 5.0.0(12)

**Parameters:**

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

annotationIndex

 | 

number

 | 

Yes

 | 

Annotation index.

 |
| 

pageIndex

 | 

number

 | 

Yes

 | 

Page index.

 |
| 

color

 | 

number

 | 

Yes

 | 

Color (ARGB). The value ranges from **0x00000000** to **0xFFFFFFFF**.

 |

**Example:**

import { pdfViewManager, pdfService } from '@kit.PDFKit';

let context = this.getUIContext().getHostContext() as Context;
let dir = context.filesDir;
let filePath = dir + \`/input.pdf\`;
let pdfController = new pdfViewManager.PdfController();
let loadResult: pdfService.ParseResult = await pdfController.loadDocument(filePath);
if (pdfService.ParseResult.PARSE\_SUCCESS === loadResult) {
  // Verify that there is an annotation on the first page.
  pdfController.updateMarkupAnnotation(0, 0, 0xAA000000);
}

#### \[h2\]saveDocument

saveDocument(path: string, onProgress?: Callback<number>): Promise<number>

Saves a PDF document. This API returns the result asynchronously through a promise.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7d/v3/UsbkLNEEQayQvBkQE4qNIw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062516Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3B68EBAA4D4F415A92F8DDAE62EE3605169F30903138029FB900CC84EEFBA12D)

As the document cannot be read and written at the same time, to replace the source document, you will need to create a temporary file by referring to the sample code below.

**System capability**: SystemCapability.OfficeService.PDFService.Core

**Start version**: 5.0.0(12)

**Parameters:**

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

path

 | 

string

 | 

Yes

 | 

Sandbox path of the document.

 |
| 

onProgress

 | 

[Callback](../../../../system/basic-functions/basic-services-kit/arkts-apis/others/ohos-base-public-callback-information/document.md#callback)<number>

 | 

No

 | 

Callback for the document saving progress, which returns data of the number type. After this parameter is passed, the document saving progress is returned. If this parameter is not passed, no document saving progress will be returned.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<number>

 | 

Number type value returned through a promise. The value can be **1** (success) or **0** (failure).

 |

**Example**:

import { pdfService, pdfViewManager } from '@kit.PDFKit';
import { fileIo as fs } from '@kit.CoreFileKit';

// Upload the test file to the app sandbox path.
let context = this.getUIContext().getHostContext() as Context;
let dir = context.filesDir;
let tempDir = context.tempDir;
// Make sure that your app has the permission to read and write the source document in the path.
let filePath = dir + \`/input.pdf\`;
let tempFilePath = tempDir + \`/temp${Math.random()}.pdf\`;
fs.copyFileSync(filePath, tempFilePath);
let pdfController = new pdfViewManager.PdfController();
// Load the temporary file.
let loadResult = await pdfController.loadDocument(tempFilePath, '');
if (pdfService.ParseResult.PARSE\_SUCCESS === loadResult) {
// Save the document by replacing the source document.
  let result = await pdfController.saveDocument(filePath);
}
pdfController.releaseDocument();

#### \[h2\]registerSelectedRectsChangedListener

registerSelectedRectsChangedListener(listener: Callback<Array<SelectedRects>>): void

Registers a listener for changes to the highlighted block when the selected text window is changed.

**System capability**: SystemCapability.OfficeService.PDFService.Core

**Start version**: 5.0.0(12)

**Parameters:**

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

listener

 | 

[Callback](../../../../system/basic-functions/basic-services-kit/arkts-apis/others/ohos-base-public-callback-information/document.md#callback)<Array<[SelectedRects](#section11370716427)\>>

 | 

Yes

 | 

Listener for changes to the selected text window when it is dragged, which returns data of the **SelectedRects** type.

 |

**Example**:

import { pdfViewManager } from '@kit.PDFKit';

let pdfController = new pdfViewManager.PdfController();
pdfController.registerSelectedRectsChangedListener((pageRects: Array<pdfViewManager.SelectedRects>) => {});

#### \[h2\]registerPageFitChangedListener

registerPageFitChangedListener(listener: Callback<pdfService.PageFit>): void

Registers a listener for when the page fit mode changes.

**System capability**: SystemCapability.OfficeService.PDFService.Core

**Start version**: 5.0.0(12)

**Parameters:**

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

listener

 | 

[Callback](../../../../system/basic-functions/basic-services-kit/arkts-apis/others/ohos-base-public-callback-information/document.md#callback)<pdfService.[PageFit](../pdfservice-pdf-services/document.md#section655755325212)\>

 | 

Yes

 | 

Listener for when the page fit mode changes, which returns data of the **PageFit** type.

 |

**Example**:

import { pdfViewManager, pdfService } from '@kit.PDFKit';

let pdfController = new pdfViewManager.PdfController();
pdfController.registerPageFitChangedListener((pageFit: pdfService.PageFit) => {});

#### \[h2\]registerPageChangedListener

registerPageChangedListener(listener: Callback<number>): void

Registers a listener for when the page index changes.

**System capability**: SystemCapability.OfficeService.PDFService.Core

**Start version**: 5.0.0(12)

**Parameters:**

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

listener

 | 

[Callback](../../../../system/basic-functions/basic-services-kit/arkts-apis/others/ohos-base-public-callback-information/document.md#callback)<number>

 | 

Yes

 | 

Listener for when the page index changes, which returns page index data of the number type.

 |

**Example**:

import { pdfViewManager } from '@kit.PDFKit';

let pdfController = new pdfViewManager.PdfController();
pdfController.registerPageChangedListener((pageIndex: number) => {});

#### \[h2\]registerScaleChangedListener

registerScaleChangedListener(listener: Callback<number>): void

Registers a listener for when the page scaling changes.

**System capability**: SystemCapability.OfficeService.PDFService.Core

**Start version**: 5.0.0(12)

**Parameters:**

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

listener

 | 

[Callback](../../../../system/basic-functions/basic-services-kit/arkts-apis/others/ohos-base-public-callback-information/document.md#callback)<number>

 | 

Yes

 | 

Listener for when the page scaling changes, which returns the scaling factor of the number type.

 |

**Example**:

import { pdfViewManager } from '@kit.PDFKit';

let pdfController = new pdfViewManager.PdfController();
pdfController.registerScaleChangedListener((scale: number) => {});

#### \[h2\]registerTextSelectedListener

registerTextSelectedListener(listener: Callback<TextSelectedParam>): void

Registers a listener for when text is selected.

**System capability**: SystemCapability.OfficeService.PDFService.Core

**Start version**: 5.0.0(12)

**Parameters:**

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

listener

 | 

[Callback](../../../../system/basic-functions/basic-services-kit/arkts-apis/others/ohos-base-public-callback-information/document.md#callback)<[TextSelectedParam](#section1783113168551)\>

 | 

Yes

 | 

Listener for when text is selected, which returns the selected text of the **TextSelectedParam** type.

 |

**Example**:

import { pdfViewManager } from '@kit.PDFKit';

let pdfController = new pdfViewManager.PdfController();
pdfController.registerTextSelectedListener((pageText: pdfViewManager.TextSelectedParam) => {});

#### \[h2\]registerAnnotationSelectedListener

registerAnnotationSelectedListener(listener: Callback<SelectedAnnotation>): void

Registers a listener for when an annotation is selected on the page.

**System capability**: SystemCapability.OfficeService.PDFService.Core

**Start version**: 5.0.0(12)

**Parameters:**

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

listener

 | 

[Callback](../../../../system/basic-functions/basic-services-kit/arkts-apis/others/ohos-base-public-callback-information/document.md#callback)<[SelectedAnnotation](#section11701105693313)\>

 | 

Yes

 | 

Listener for when an annotation is selected on the page, which returns the selected annotation of the **SelectedAnnotation** type.

 |

**Example**:

import { pdfViewManager } from '@kit.PDFKit';

let pdfController = new pdfViewManager.PdfController();
pdfController.registerAnnotationSelectedListener((pdfAnnotation: pdfViewManager.SelectedAnnotation) => {});

#### \[h2\]registerImageSelectedListener

registerImageSelectedListener(listener: Callback<ImageSelectedParam>): void

Registers a listener for when an image is selected on the page.

**System capability**: SystemCapability.OfficeService.PDFService.Core

**Start version**: 5.0.0(12)

**Parameters:**

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

listener

 | 

[Callback](../../../../system/basic-functions/basic-services-kit/arkts-apis/others/ohos-base-public-callback-information/document.md#callback)<[ImageSelectedParam](#section9756124685916)\>

 | 

Yes

 | 

Listener for when an image is selected on the page, which returns the selected image of the **ImageSelectedParam** type.

 |

**Example:**

import { pdfViewManager } from '@kit.PDFKit';

let pdfController = new pdfViewManager.PdfController();
pdfController.registerImageSelectedListener((image: pdfViewManager.ImageSelectedParam) => {});

#### \[h2\]registerActionClickListener

registerActionClickListener(listener: Callback<RedirectInfo>): void

Registers a listener for the click action. For example, when the listener obtains an address, it can start the browser and redirect to that address.

**System capability**: SystemCapability.OfficeService.PDFService.Core

**Start version**: 5.0.0(12)

**Parameters:**

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

listener

 | 

[Callback](../../../../system/basic-functions/basic-services-kit/arkts-apis/others/ohos-base-public-callback-information/document.md#callback)<[RedirectInfo](#section1890741412)\>

 | 

Yes

 | 

Listener for the click action, which returns data of the **RedirectInfo** type.

 |

**Example**:

import { pdfViewManager } from '@kit.PDFKit';

let pdfController = new pdfViewManager.PdfController();
pdfController.registerActionClickListener((redirectInfo: pdfViewManager.RedirectInfo) => {});

#### \[h2\]registerAnnotationChangedListener

registerAnnotationChangedListener(listener: Callback<AnnotationChangedParam>): void

Registers a listener for when the annotation changes.

**System capability**: SystemCapability.OfficeService.PDFService.Core

**Start version**: 5.0.0(12)

**Parameters:**

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

listener

 | 

[Callback](../../../../system/basic-functions/basic-services-kit/arkts-apis/others/ohos-base-public-callback-information/document.md#callback)<[AnnotationChangedParam](#section629771801812)\>

 | 

Yes

 | 

Listener for when the annotation changes, which returns data of the **AnnotationChangedParam** type.

 |

**Example**:

import { pdfViewManager } from '@kit.PDFKit';

let pdfController = new pdfViewManager.PdfController();
pdfController.registerAnnotationChangedListener((annotationChange: pdfViewManager.AnnotationChangedParam) => {});

#### \[h2\]registerPageCountChangedListener

registerPageCountChangedListener(listener: Callback<number>): void

Registers a listener for when the total page count changes. Note that you can only call this API before calling **loadDocument**.

**System capability**: SystemCapability.OfficeService.PDFService.Core

**Start version**: 5.0.0(12)

**Parameters:**

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

listener

 | 

[Callback](../../../../system/basic-functions/basic-services-kit/arkts-apis/others/ohos-base-public-callback-information/document.md#callback)<number>

 | 

Yes

 | 

Listener for when the total page count changes, which returns the total page count of the number type.

 |

**Example:**

import { pdfViewManager } from '@kit.PDFKit';

let pdfController = new pdfViewManager.PdfController();
pdfController.registerPageCountChangedListener((pageCount: number) => {});

#### \[h2\]searchKey

searchKey(text: string, listener: Callback<number>): void

Searches for text and returns the total number of matches. Calling this API invalidates the results from any previous [setHighlightText](#section475716341213) execution.

**System capability**: SystemCapability.OfficeService.PDFService.Core

**Start version**: 5.0.0(12)

**Parameters:**

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

text

 | 

string

 | 

Yes

 | 

Search text.

 |
| 

listener

 | 

[Callback](../../../../system/basic-functions/basic-services-kit/arkts-apis/others/ohos-base-public-callback-information/document.md#callback)<number>

 | 

Yes

 | 

Listener for text searching, which returns the total number of matches.

 |

**Example**:

import { pdfViewManager, pdfService } from '@kit.PDFKit';

let context = this.getUIContext().getHostContext() as Context;
let dir = context.filesDir;
let filePath = dir + \`/input.pdf\`;
let pdfController = new pdfViewManager.PdfController();
let loadResult: pdfService.ParseResult = await pdfController.loadDocument(filePath);
if (pdfService.ParseResult.PARSE\_SUCCESS === loadResult) {
  pdfController.searchKey('a', (index: number) => {});
}

#### \[h2\]clearSearch

clearSearch(): void

Cancels the highlight of the matched text. This operation is equivalent to searching for empty strings.

**System capability**: SystemCapability.OfficeService.PDFService.Core

**Start version**: 5.0.0(12)

**Example**:

import { pdfViewManager, pdfService } from '@kit.PDFKit';

let context = this.getUIContext().getHostContext() as Context;
let dir = context.filesDir;
let filePath = dir + \`/input.pdf\`;
let pdfController = new pdfViewManager.PdfController();
let loadResult: pdfService.ParseResult = await pdfController.loadDocument(filePath);
if (pdfService.ParseResult.PARSE\_SUCCESS === loadResult) {
  pdfController.clearSearch();
}

#### \[h2\]getSearchIndex

getSearchIndex(): number

Obtains the index of the search result that matches the keyword. The default index after the search API is executed is **0**.

**System capability**: SystemCapability.OfficeService.PDFService.Core

**Start version**: 5.0.0(12)

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

number

 | 

Index of the matching search result, which is greater than or equal to **0**.

 |

**Example**:

import { pdfViewManager, pdfService } from '@kit.PDFKit';

let context = this.getUIContext().getHostContext() as Context;
let dir = context.filesDir;
let filePath = dir + \`/input.pdf\`;
let pdfController = new pdfViewManager.PdfController();
let loadResult: pdfService.ParseResult = await pdfController.loadDocument(filePath);
if (pdfService.ParseResult.PARSE\_SUCCESS === loadResult) {
  let res = pdfController.getSearchIndex();
}

#### \[h2\]setSearchIndex

setSearchIndex(index: number): void

Sets the index of the matching search result. The page will jump to the corresponding search result.

**System capability**: SystemCapability.OfficeService.PDFService.Core

**Start version**: 5.0.0(12)

**Parameters:**

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

index

 | 

number

 | 

Yes

 | 

Search result index.

 |

**Example**:

import { pdfViewManager, pdfService } from '@kit.PDFKit';

let context = this.getUIContext().getHostContext() as Context;
let dir = context.filesDir;
let filePath = dir + \`/input.pdf\`;
let pdfController = new pdfViewManager.PdfController();
let loadResult: pdfService.ParseResult = await pdfController.loadDocument(filePath);
if (pdfService.ParseResult.PARSE\_SUCCESS === loadResult) {
  pdfController.setSearchIndex(1);
}

#### \[h2\]setDisplayDirection

setDisplayDirection(displayDirection: DisplayDirection): void

Sets the page turning direction of the document in non-continuous PDF mode.

**System capability**: SystemCapability.OfficeService.PDFService.Core

**Start version**: 6.0.0(20)

**Parameters:**

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

displayDirection

 | 

[DisplayDirection](#section1755014131618)

 | 

Yes

 | 

Page turning direction, which is vertical by default.

 |

**Example**:

import { pdfViewManager, pdfService } from '@kit.PDFKit';

let context = this.getUIContext().getHostContext() as Context;
let dir = context.filesDir;
let filePath = dir + \`/input.pdf\`;
let pdfController = new pdfViewManager.PdfController();
let loadResult: pdfService.ParseResult = await pdfController.loadDocument(filePath);
if (pdfService.ParseResult.PARSE\_SUCCESS === loadResult) {
  pdfController.setDisplayDirection(pdfViewManager.DisplayDirection.VERTICAL);
}

#### \[h2\]setNestedScroll

setNestedScroll(value: PdfNestedScrollOptions): void

Sets nested scrolling options. You can set the up, down, left, and right directions to implement scrolling linkage with the parent component.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/84/v3/8U__CUPzRWerfvkSSdXd3w/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062516Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=AFD70285689B04B54C5C3606AF23EC4D026CCC056389FBE3B0A616CD66777D6C)

If **PdfNestedScrollMode** in **PdfNestedScrollOptions** is set to **SELF\_FIRST**, the parent component will scroll only if the user releases and re-triggers the scroll gesture after reaching the edge.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.OfficeService.PDFService.Core

**Start version**: 6.0.2(22)

**Parameters:**

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

value

 | 

[PdfNestedScrollOptions](#section64102251111)

 | 

Yes

 | 

Nested scrolling options of a scrollable component, including **scrollUp**, **scrollDown**, **scrollLeft**, and **scrollRight**, with their default value being [PdfNestedScrollMode](#section11050104146).SELF\_ONLY.

 |

**Example:**

import { pdfViewManager, pdfService } from '@kit.PDFKit';
import { common } from '@kit.AbilityKit';

@Entry
@Component
struct PdfPage {
  private pdfController: pdfViewManager.PdfController = new pdfViewManager.PdfController();

  async aboutToAppear() {
    let context = getContext(this) as common.UIAbilityContext;
    let dir = context.filesDir;
    let filePath = dir + \`/input.pdf\`;

    let loadResult: pdfService.ParseResult = await this.pdfController.loadDocument(filePath);

    if (loadResult !== undefined && pdfService.ParseResult.PARSE\_SUCCESS === loadResult) {
      this.pdfController.setNestedScroll({
        scrollUp: pdfViewManager.PdfNestedScrollMode.SELF\_ONLY,
        scrollDown: pdfViewManager.PdfNestedScrollMode.SELF\_ONLY,
        scrollLeft: pdfViewManager.PdfNestedScrollMode.SELF\_ONLY,
        scrollRight: pdfViewManager.PdfNestedScrollMode.SELF\_ONLY
      });
    }
  }

  build() {
    Column() {
      // Component
    }
  }
}

#### RedirectInfo

PDF page redirection information class.

**System capability**: SystemCapability.OfficeService.PDFService.Core

**Start version**: 5.0.0(12)

## Attributes

| 
Name

 | 

Type

 | 

Read-Only

 | 

Optional

 | 

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

content

 | 

string

 | 

No

 | 

No

 | 

Redirection information.

 |
| 

actionType

 | 

[RedirectType](#section68484322217)

 | 

No

 | 

No

 | 

Redirection type.

 |

#### \[h2\]constructor

constructor(content: string, actionType: RedirectType)

Creates a PDF page redirection information object.

**System capability**: SystemCapability.OfficeService.PDFService.Core

**Start version**: 5.0.0(12)

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

content

 | 

string

 | 

Yes

 | 

Redirection information.

 |
| 

actionType

 | 

[RedirectType](#section68484322217)

 | 

Yes

 | 

Redirection type.

 |

**Example**:

import { pdfViewManager } from '@kit.PDFKit';

let redirectInfo = new pdfViewManager.RedirectInfo('https://www.test.com', pdfViewManager.RedirectType.URI);

#### SelectedAnnotation

Selected annotations in the PDF file.

**System capability**: SystemCapability.OfficeService.PDFService.Core

**Start version**: 5.0.0(12)

| 
Name

 | 

Type

 | 

Read-Only

 | 

Optional

 | 

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

annotationIndex

 | 

number

 | 

Yes

 | 

No

 | 

Annotation index.

 |
| 

pageIndex

 | 

number

 | 

Yes

 | 

No

 | 

Page index.

 |
| 

annotationType

 | 

[SupportedAnnotationType](#section16111165319147)

 | 

Yes

 | 

No

 | 

Annotation type.

 |
| 

color

 | 

number

 | 

Yes

 | 

No

 | 

Annotation color (ARGB). The value ranges from **0x00000000** to **0xFFFFFFFF**.

 |
| 

rect

 | 

Array<pdfService.[PdfRect](../pdfservice-pdf-services/document.md#section19829174815360)\>

 | 

Yes

 | 

Yes

 | 

Rectangular area of an annotation.

 |
| 

points

 | 

Array<pdfService.[PdfPoint](../pdfservice-pdf-services/document.md#section174855274363)\>

 | 

Yes

 | 

Yes

 | 

Annotation coordinates.

 |

#### PageRects

Class for rectangular areas on the page.

**System capability**: SystemCapability.OfficeService.PDFService.Core

**Start version**: 5.0.0(12)

## Attributes

| 
Name

 | 

Type

 | 

Read-Only

 | 

Optional

 | 

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

pageIndex

 | 

number

 | 

No

 | 

No

 | 

Page index.

 |
| 

rectArray

 | 

Array<pdfService.[PdfRect](../pdfservice-pdf-services/document.md#section19829174815360)\>

 | 

No

 | 

No

 | 

**PdfRect** array.

 |

#### \[h2\]constructor

constructor(pageIndex: number, rectArray: Array<pdfService.PdfRect>)

Creates a rectangular area object on a page.

**System capability**: SystemCapability.OfficeService.PDFService.Core

**Start version**: 5.0.0(12)

**Parameters:**

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

pageIndex

 | 

number

 | 

Yes

 | 

Page index.

 |
| 

rectArray

 | 

Array<pdfService.[PdfRect](../pdfservice-pdf-services/document.md#section19829174815360)\>

 | 

Yes

 | 

**PdfRect** array.

 |

#### SelectedRects

Class for the rectangular area of the selected text on a PDF page, which inherits from [PageRects](#section165811065495).

**System capability**: SystemCapability.OfficeService.PDFService.Core

**Start version**: 5.0.0(12)

## Attributes

| 
Name

 | 

Type

 | 

Read-Only

 | 

Optional

 | 

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

isRotated

 | 

number

 | 

No

 | 

No

 | 

Indicates whether rotation is supported. The options are **0** (no) and **1** (yes).

 |

#### \[h2\]constructor

constructor(pageIndex: number, rectArray: Array<pdfService.PdfRect>, isRotated: number)

Creates the rectangular area object of the selected text on a PDF page.

**System capability**: SystemCapability.OfficeService.PDFService.Core

**Start version**: 5.0.0(12)

**Parameters:**

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

pageIndex

 | 

number

 | 

Yes

 | 

Page index.

 |
| 

rectArray

 | 

Array<pdfService.[PdfRect](../pdfservice-pdf-services/document.md#section19829174815360)\>

 | 

Yes

 | 

**PdfRect** array.

 |
| 

isRotated

 | 

number

 | 

Yes

 | 

Indicates whether rotation is supported. The options are **0** (no) and **1** (yes).

 |

**Example**:

import { pdfService, pdfViewManager } from '@kit.PDFKit';

let rectArray: Array<pdfService.PdfRect> = new Array<pdfService.PdfRect>();
const rect1: pdfService.PdfRect = { left: 5, top: 5, right: 250, bottom: 250};
rectArray.push(rect1);
let selectedRects: pdfViewManager.SelectedRects = new pdfViewManager.SelectedRects(0, rectArray, 0);

#### ScrollParam

Callback parameter of **registerScrollListener**.

**System capability**: SystemCapability.OfficeService.PDFService.Core

**Start version**: 5.0.0(12)

| 
Name

 | 

Type

 | 

Read-Only

 | 

Optional

 | 

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

offsetX

 | 

number

 | 

No

 | 

No

 | 

Offset along the X axis. The value ranges from **0** to **1**, indicating from 0% to 100%.

 |
| 

offsetY

 | 

number

 | 

No

 | 

No

 | 

Offset along the Y axis. The value ranges from **0** to **1**, indicating from 0% to 100%.

 |
| 

pdfWidth

 | 

number

 | 

No

 | 

No

 | 

Total width of the PDF page after scaling, in px.

 |
| 

pdfHeight

 | 

number

 | 

No

 | 

No

 | 

Total height of the PDF page after scaling, in px.

 |
| 

viewWidth

 | 

number

 | 

No

 | 

No

 | 

Controller width, in px.

 |
| 

viewHeight

 | 

number

 | 

No

 | 

No

 | 

Controller height, in px.

 |

#### TextSelectedParam

Callback parameter of **registerTextSelectedListener**.

**System capability**: SystemCapability.OfficeService.PDFService.Core

**Start version**: 5.0.0(12)

| 
Name

 | 

Type

 | 

Read-Only

 | 

Optional

 | 

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

text

 | 

string

 | 

No

 | 

No

 | 

Selected text.

 |
| 

pdfRect

 | 

Array<[SelectedRects](#section11370716427)\>

 | 

No

 | 

No

 | 

Rectangular area of the selected text on a PDF page.

 |

#### ImageSelectedParam

Callback parameter of **registerImageSelectedListener**.

**System capability**: SystemCapability.OfficeService.PDFService.Core

**Start version**: 5.0.0(12)

| 
Name

 | 

Type

 | 

Read-Only

 | 

Optional

 | 

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

imageType

 | 

pdfService.[ImageFormat](../pdfservice-pdf-services/document.md#section1713111745313)

 | 

No

 | 

No

 | 

Type of the selected image.

 |
| 

buffer

 | 

ArrayBuffer

 | 

No

 | 

Yes

 | 

Image buffer. If the buffer is empty, the selection is canceled.

 |
| 

pdfRect

 | 

pdfService.[PdfRect](../pdfservice-pdf-services/document.md#section19829174815360)

 | 

No

 | 

Yes

 | 

Rectangular area of the selected image on a PDF page.

 |
| 

pageIndex

 | 

number

 | 

No

 | 

Yes

 | 

Page index.

 |

#### AnnotationChangedParam

Callback parameter of **registerAnnotationChangedListener**.

**System capability**: SystemCapability.OfficeService.PDFService.Core

**Start version**: 5.0.0(12)

| 
Name

 | 

Type

 | 

Read-Only

 | 

Optional

 | 

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

color

 | 

number

 | 

No

 | 

No

 | 

Color (ARGB). The value ranges from **0x00000000** to **0xFFFFFFFF**.

 |
| 

annotationType

 | 

[SupportedAnnotationType](#section16111165319147)

 | 

No

 | 

No

 | 

Annotation type.

 |
| 

pageIndexArray

 | 

Array<number>

 | 

No

 | 

No

 | 

Index list of annotations on a page.

 |
| 

controlType

 | 

[AnnotationEditType](#section38961531196)

 | 

No

 | 

No

 | 

Annotation operation type. The options are **0** (adding), **1** (modifying), and **2** (deleting).

 |

#### SupportedAnnotationType

Annotation types supported on the PDF page.

**System capability**: SystemCapability.OfficeService.PDFService.Core

**Start version**: 5.0.0(12)

| 
Name

 | 

Value

 | 

Description

 |
| :-- | :-- | :-- |
| 

UNKNOWN

 | 

0

 | 

Unknown type.

 |
| 

FREE\_TEXT

 | 

3

 | 

Free font.

 |
| 

LINE

 | 

4

 | 

Line.

 |
| 

SQUARE

 | 

5

 | 

Square, including rectangle.

 |
| 

OVAL

 | 

6

 | 

Oval, including circle.

 |
| 

POLYGON

 | 

7

 | 

Polygon.

 |
| 

HIGHLIGHT

 | 

9

 | 

Highlight.

 |
| 

UNDERLINE

 | 

10

 | 

Underline.

 |
| 

STRIKETHROUGH

 | 

12

 | 

Strikethrough.

 |

#### AnnotationEditType

Types of annotation operation supported on a PDF page.

**System capability**: SystemCapability.OfficeService.PDFService.Core

**Start version**: 5.0.0(12)

| 
Name

 | 

Value

 | 

Description

 |
| :-- | :-- | :-- |
| 

ADD

 | 

0

 | 

Adding.

 |
| 

MODIFY

 | 

1

 | 

Modifying.

 |
| 

DELETE

 | 

2

 | 

Deleting.

 |

#### RedirectType

**ActionType** for redirection.

**System capability**: SystemCapability.OfficeService.PDFService.Core

**Start version**: 5.0.0(12)

| 
Name

 | 

Value

 | 

Description

 |
| :-- | :-- | :-- |
| 

URI

 | 

6

 | 

URI.

 |
| 

LAUNCH

 | 

4

 | 

Local file path.

 |

#### DisplayDirection

Page turning direction in non-continuous mode.

**System capability**: SystemCapability.OfficeService.PDFService.Core

**Start version**: 6.0.0(20)

| 
Name

 | 

Value

 | 

Description

 |
| :-- | :-- | :-- |
| 

VERTICAL

 | 

0

 | 

Vertical page turning.

 |
| 

HORIZONTAL

 | 

1

 | 

Horizontal page turning.

 |

#### PdfNestedScrollOptions

Sets the nested scrolling rules for the up, down, left, and right directions.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.OfficeService.PDFService.Core

**Start version**: 6.0.2(22)

| 
Name

 | 

Type

 | 

Read-Only

 | 

Optional

 | 

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

scrollUp

 | 

[PdfNestedScrollMode](#section11050104146)

 | 

No

 | 

Yes

 | 

Nested scrolling rule when the component scrolls up.

The default value is **PdfNestedScrollMode.SELF\_ONLY**.

 |
| 

scrollDown

 | 

[PdfNestedScrollMode](#section11050104146)

 | 

No

 | 

Yes

 | 

Nested scrolling rule when the component scrolls down.

The default value is **PdfNestedScrollMode.SELF\_ONLY**.

 |
| 

scrollLeft

 | 

[PdfNestedScrollMode](#section11050104146)

 | 

No

 | 

Yes

 | 

Nested scrolling rule when the component scrolls left.

The default value is **PdfNestedScrollMode.SELF\_ONLY**.

 |
| 

scrollRight

 | 

[PdfNestedScrollMode](#section11050104146)

 | 

No

 | 

Yes

 | 

Nested scrolling rule when the component scrolls right.

The default value is **PdfNestedScrollMode.SELF\_ONLY**.

 |

#### PdfNestedScrollMode

Defines the nested scrolling mode of the component.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.OfficeService.PDFService.Core

**Start version**: 6.0.2(22)

| 
Name

 | 

Value

 | 

Description

 |
| :-- | :-- | :-- |
| 

SELF\_ONLY

 | 

0

 | 

The scrolling is contained within the component, and no scroll chaining occurs, that is, the parent component does not scroll when the component scrolling reaches the boundary.

 |
| 

SELF\_FIRST

 | 

1

 | 

The component scrolls first, and when it hits the boundary, the parent component scrolls. When the parent component hits the boundary, its edge effect is displayed. If no edge effect is specified for the parent component, the edge effect of the child component is displayed instead.

 |
