# pdfService (PDF Services)

This module provides apps with the capability of managing the header, footer, watermark, and background of PDF pages, multiple annotation styles of documents, and bookmarks in a unified manner.

**Note**: The unit of attributes related to dimensions and coordinates is point. One inch is equal to 72 points.

**System capability**: SystemCapability.OfficeService.PDFService.Core

**Start version**: 5.0.0(12)

#### Importing Modules

import { pdfService } from '@kit.PDFKit';

#### Precautions

After editing a PDF document, you need to call the [saveDocument](#section660833016157) API to save the PDF document for the edits to take effect.

#### PdfDocument

PDF document class.

**System capability**: SystemCapability.OfficeService.PDFService.Core

**Start version**: 5.0.0(12)

#### \[h2\]constructor

constructor()

Constructor.

**System capability**: SystemCapability.OfficeService.PDFService.Core

**Start version**: 5.0.0(12)

import { pdfService } from '@kit.PDFKit';

let pdfDocument = new pdfService.PdfDocument();

#### \[h2\]loadDocument

loadDocument(path: string, password?: string, onProgress?: (progress: number) => number): ParseResult

Loads the document with the specified document path. Repeated **loadDocument** calls are not supported. Before any subsequent call, you must use **releaseDocument** to release the loaded document. This ensures that resources are properly released and prevents potential conflicts or exceptions.

**System capability**: SystemCapability.OfficeService.PDFService.Core

**Start version**: 5.0.0(12)

**Parameters:**

| 
**Parameter**

 | 

**Type**

 | 

**Mandatory**

 | 

**Description**

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

Document encryption password. An empty character string is used by default.

 |
| 

onProgress

 | 

(progress: number) => number

 | 

No

 | 

Callback for progress. After this parameter is passed, the document loading progress is returned. If this parameter is not passed, no document loading progress will be returned.

 |

**Returns**:

| 
**Type**

 | 

**Description**

 |
| :-- | :-- |
| 

[ParseResult](#section913412299528)

 | 

ParseResult enum.

 |

**Example**:

import { pdfService } from '@kit.PDFKit';

// Upload the test file to the app sandbox path.
let tempFilePath = '/data/storage/el2/base/temp/test.pdf';
let pdfDocument: pdfService.PdfDocument = new pdfService.PdfDocument();
// Load the temporary file.
let loadResult = pdfDocument.loadDocument(tempFilePath, '');

#### \[h2\]releaseDocument

releaseDocument(): void

Releases a PDF document.

**System capability**: SystemCapability.OfficeService.PDFService.Core

**Start version**: 5.0.0(12)

**Example**:

import { pdfService } from '@kit.PDFKit';

let pdfDocument = new pdfService.PdfDocument();
// Upload the test file to the app sandbox path.
let tempFilePath = '/data/storage/el2/base/temp/test.pdf';
// Load the temporary file.
let loadResult = pdfDocument.loadDocument(tempFilePath, '');
if(pdfService.ParseResult.PARSE\_SUCCESS === loadResult) {
  pdfDocument.releaseDocument();
}

#### \[h2\]saveDocument

saveDocument(path: string, onProgress?: (progress: number) => number): boolean

Saves a document.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f4/v3/lkD3aWxRSFW1A4zH4FPF7w/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062516Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E7FC90CF974F274ED363B37E0F78D87578CA45FBE23A673EB131A244C59CC5F2)

As the document cannot be read and written at the same time, to replace the source document, you will need to create a temporary file by referring to the sample code below.

**System capability**: SystemCapability.OfficeService.PDFService.Core

**Start version**: 5.0.0(12)

**Parameters:**

| 
**Parameter**

 | 

**Type**

 | 

**Mandatory**

 | 

**Description**

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

(progress: number) => number

 | 

No

 | 

Callback for progress. After this parameter is passed, the document saving progress is returned. If this parameter is not passed, no document saving progress will be returned.

 |

**Returns**:

| 
**Type**

 | 

**Description**

 |
| :-- | :-- |
| 

boolean

 | 

If the document is saved successfully, **true** is returned. Otherwise, **false** is returned.

 |

**Example**:

import { fileIo as fs } from '@kit.CoreFileKit';
import { pdfService } from '@kit.PDFKit';
import { Font } from '@kit.ArkUI';

// Upload the test file to the app sandbox path.
let context = this.getUIContext().getHostContext() as Context;
let dir = context.filesDir;
let tempDir = context.tempDir;
// Make sure that your app has the permission to read and write the source document in the path.
let filePath = dir + \`/input.pdf\`;
let tempFilePath = tempDir + \`/temp${Math.random()}.pdf\`;
fs.copyFileSync(filePath, tempFilePath);
let pdfDocument: pdfService.PdfDocument = new pdfService.PdfDocument();
// Load the temporary file.
let loadResult = pdfDocument.loadDocument(tempFilePath, '');
// Add watermarks to the document.
if (pdfService.ParseResult.PARSE\_SUCCESS === loadResult) {      
  let wminfo: pdfService.TextWatermarkInfo = new pdfService.TextWatermarkInfo();
  wminfo.watermarkType = pdfService.WatermarkType.WATERMARK\_TEXT;
  wminfo.content = "This is Watermark";
  wminfo.textSize = 30;
  wminfo.textColor = 200;
  wminfo.fontInfo = new pdfService.FontInfo();
  let font: Font = new Font()
  wminfo.fontInfo.fontPath = font.getFontByName("HarmonyOS Sans").path;
  wminfo.opacity = 0.5;
  wminfo.isOnTop = true;
  wminfo.rotation = 45;
  wminfo.scale = 1.5;
  wminfo.verticalAlignment = pdfService.WatermarkAlignment.WATERMARK\_ALIGNMENT\_TOP;
  wminfo.horizontalAlignment = pdfService.WatermarkAlignment.WATERMARK\_ALIGNMENT\_LEFT;
  wminfo.horizontalSpace = 1.0;
  wminfo.verticalSpace = 1.0;
  pdfDocument.addWatermark(wminfo, 0, 1, true, true);
// Save the document by replacing the source document.
  let result = pdfDocument.saveDocument(filePath);
}

#### \[h2\]createDocument

createDocument(width: number, height: number): boolean

Creates a blank document.

**System capability**: SystemCapability.OfficeService.PDFService.Core

**Start version**: 5.0.0(12)

**Parameters:**

| 
**Parameter**

 | 

**Type**

 | 

**Mandatory**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- |
| 

width

 | 

number

 | 

Yes

 | 

Document width, in points (one inch equals 72 points). The value must be greater than **0**.

 |
| 

height

 | 

number

 | 

Yes

 | 

Document height, in points (one inch equals 72 points). The value must be greater than **0**.

 |

**Returns**:

| 
**Type**

 | 

**Description**

 |
| :-- | :-- |
| 

boolean

 | 

If the document is successfully created, **true** is returned. Otherwise, **false** is returned.

 |

**Example**:

import { pdfService } from '@kit.PDFKit';

let pdfDocument = new pdfService.PdfDocument();
pdfDocument.createDocument(600, 900);

#### \[h2\]isEncrypted

isEncrypted(path: string): boolean

Indicates whether the document is encrypted.

**System capability**: SystemCapability.OfficeService.PDFService.Core

**Start version**: 5.0.0(12)

**Parameters:**

| 
**Parameter**

 | 

**Type**

 | 

**Mandatory**

 | 

**Description**

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

**Returns**:

| 
**Type**

 | 

**Description**

 |
| :-- | :-- |
| 

boolean

 | 

Indicates whether the document is encrypted (**true**) or not (**false**).

 |

**Example**:

import { pdfService } from '@kit.PDFKit';

// Upload the test file to the app sandbox path.
let tempFilePath = '/data/storage/el2/base/temp/test.pdf';
let pdfDocument = new pdfService.PdfDocument();
let loadResult = pdfDocument.loadDocument(tempFilePath, '');
if (pdfService.ParseResult.PARSE\_SUCCESS === loadResult) {
  let isEncrypted = pdfDocument.isEncrypted(tempFilePath);
}

#### \[h2\]removeSecurity

removeSecurity(): boolean

Removes document security lock.

**System capability**: SystemCapability.OfficeService.PDFService.Core

**Start version**: 5.0.0(12)

**Returns**:

| 
**Type**

 | 

**Description**

 |
| :-- | :-- |
| 

boolean

 | 

If the document security lock is successfully removed, **true** is returned. Otherwise, **false** is returned.

 |

**Example**:

import { pdfService } from '@kit.PDFKit';

// Upload the test file to the app sandbox path.
let tempFilePath = '/data/storage/el2/base/temp/test.pdf';
let pdfDocument = new pdfService.PdfDocument();
let loadResult = pdfDocument.loadDocument(tempFilePath, '');
if (pdfService.ParseResult.PARSE\_SUCCESS === loadResult) {
  let result = pdfDocument.removeSecurity();
}

#### \[h2\]getPageCount

getPageCount(): number

Obtains the page count of a document.

**System capability**: SystemCapability.OfficeService.PDFService.Core

**Start version**: 5.0.0(12)

**Returns**:

| 
**Type**

 | 

**Description**

 |
| :-- | :-- |
| 

number

 | 

Page count of a document. The value must be greater than **0**.

 |

**Example**:

import { pdfService } from '@kit.PDFKit';

// Upload the test file to the app sandbox path.
let tempFilePath = '/data/storage/el2/base/temp/test.pdf';
let pdfDocument = new pdfService.PdfDocument();
let loadResult = pdfDocument.loadDocument(tempFilePath, '');
if (pdfService.ParseResult.PARSE\_SUCCESS === loadResult) {
  let pageCount = pdfDocument.getPageCount();
}

#### \[h2\]getPage

getPage(index: number): PdfPage

Obtains an object of the specified page.

**System capability**: SystemCapability.OfficeService.PDFService.Core

**Start version**: 5.0.0(12)

**Parameters:**

| 
**Parameter**

 | 

**Type**

 | 

**Mandatory**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- |
| 

index

 | 

number

 | 

Yes

 | 

Index of the page object to be obtained. The value must be greater than or equal to **0** and less than the total page count. The value **0** indicates the start page.

 |

**Returns**:

| 
**Type**

 | 

**Description**

 |
| :-- | :-- |
| 

[PdfPage](#section1643717123816)

 | 

Object of the specified page.

 |

**Example**:

import { pdfService } from '@kit.PDFKit';

// Upload the test file to the app sandbox path.
let tempFilePath = '/data/storage/el2/base/temp/test.pdf';
let pdfDocument = new pdfService.PdfDocument();
// Load the temporary file.
let loadResult = pdfDocument.loadDocument(tempFilePath, '');
if (pdfService.ParseResult.PARSE\_SUCCESS === loadResult) {
  let pdfPage = pdfDocument.getPage(0);
}

#### \[h2\]insertBlankPage

insertBlankPage(index: number, width: number, height: number): PdfPage

Inserts a PDF page at a specified position.

**System capability**: SystemCapability.OfficeService.PDFService.Core

**Start version**: 5.0.0(12)

**Parameters:**

| 
**Parameter**

 | 

**Type**

 | 

**Mandatory**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- |
| 

index

 | 

number

 | 

Yes

 | 

Index of the page where a PDF page is to be inserted. The value must be greater than or equal to **0** and less than the total page count. The value **0** indicates the start page.

 |
| 

width

 | 

number

 | 

Yes

 | 

Width of the PDF page to be inserted, in points (one inch equals 72 points). The value must be greater than **0**.

 |
| 

height

 | 

number

 | 

Yes

 | 

Height of the PDF page to be inserted, in points (one inch equals 72 points). The value must be greater than **0**.

 |

**Returns**:

| 
**Type**

 | 

**Description**

 |
| :-- | :-- |
| 

[PdfPage](#section1643717123816)

 | 

Inserted PDF page.

 |

**Example**:

import { pdfService } from '@kit.PDFKit';

// Upload the test file to the app sandbox path.
let tempFilePath = '/data/storage/el2/base/temp/test.pdf';
let pdfDocument = new pdfService.PdfDocument();
// Load the temporary file.
let loadResult = pdfDocument.loadDocument(tempFilePath, '');
if (pdfService.ParseResult.PARSE\_SUCCESS === loadResult) {
  let pdfPage = pdfDocument.insertBlankPage(1, 600, 900);
}

#### \[h2\]insertPageFromDocument

insertPageFromDocument(document: PdfDocument, fromIndex: number, pageCount: number, index: number): PdfPage

Inserts a page of another document to the current document. Annotations on the page cannot be inserted to the current document.

**System capability**: SystemCapability.OfficeService.PDFService.Core

**Start version**: 5.0.0(12)

**Parameters:**

| 
**Parameter**

 | 

**Type**

 | 

**Mandatory**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- |
| 

document

 | 

[PdfDocument](#section1319183318231)

 | 

Yes

 | 

**PdfDocument** object.

 |
| 

fromIndex

 | 

number

 | 

Yes

 | 

Index of the start page to be inserted from another document. The value must be greater than **0**. The value **0** indicates the start page.

 |
| 

pageCount

 | 

number

 | 

Yes

 | 

Count of inserted pages. The value must be greater than **0** and less than or equal to the total page count.

 |
| 

index

 | 

number

 | 

Yes

 | 

Index of the start page to be inserted to the current document. The value must be greater than or equal to **0** and less than the total page count. The value **0** indicates the start page.

 |

**Returns**:

| 
**Type**

 | 

**Description**

 |
| :-- | :-- |
| 

[PdfPage](#section1643717123816)

 | 

Last page of the inserted PDF pages.

 |

**Example**:

import { pdfService } from '@kit.PDFKit';

// Upload the test file to the app sandbox path.
let tempFilePath1 = '/data/storage/el2/base/temp/test1.pdf';
let document: pdfService.PdfDocument = new pdfService.PdfDocument();
let loadResult1 = document.loadDocument(tempFilePath1, '');
if(pdfService.ParseResult.PARSE\_SUCCESS === loadResult1) {      
  // Upload the test file to the app sandbox path.
  let tempFilePath2 = '/data/storage/el2/base/temp/test2.pdf';
  let pdfDocument2 = new pdfService.PdfDocument();
// Load the temporary file.
  let loadResult2 = pdfDocument2.loadDocument(tempFilePath2, '');
  if(pdfService.ParseResult.PARSE\_SUCCESS === loadResult2) {
    let page = pdfDocument2.insertPageFromDocument(document, 1, 2, 3);        
  }  
}

#### \[h2\]deletePage

deletePage(index: number, count: number): void

Deletes a PDF page.

**System capability**: SystemCapability.OfficeService.PDFService.Core

**Start version**: 5.0.0(12)

**Parameters:**

| 
**Parameter**

 | 

**Type**

 | 

**Mandatory**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- |
| 

index

 | 

number

 | 

Yes

 | 

Index of the start page to be deleted from the current document. The value must be greater than **0** and less than or equal to the total page count. The value **0** indicates the start page.

 |
| 

count

 | 

number

 | 

Yes

 | 

Count of PDF pages to be deleted. The value must be greater than **0** and less than or equal to the total page count.

 |

**Example**:

import { pdfService } from '@kit.PDFKit';

// Upload the test file to the app sandbox path.
let tempFilePath = '/data/storage/el2/base/temp/test.pdf';
let pdfDocument = new pdfService.PdfDocument();
// Load the temporary file.
let loadResult = pdfDocument.loadDocument(tempFilePath, '');
if(pdfService.ParseResult.PARSE\_SUCCESS === loadResult) {      
  pdfDocument.deletePage(1, 2);
}

#### \[h2\]movePage

movePage(index: number, dest: number): boolean

Moves a page to the index position.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9f/v3/EhMsqMkpRoqoKAjhreiMRA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062516Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F40E104684E39D841A9D256ED6BCAC181F657B02A7D28DE369BB5859D4357221)

Assume that there are a total of five pages. Moving a page from index 2 (page 3) to index 3 (page 4) by calling **movePage(2, 3)** will fail, because this method can only move page 3 to behind page 4, meaning page 3 becomes page 5. In this case, the correct method should be **movePage(2, 4)**, which changes the sequence from \[0, 1, 2, 3, 4\] to \[0, 1, 3, 2, 4\].

Calling **movePage (3, 2)** changes the sequence to \[0, 1, 3, 2, 4\].

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8d/v3/yI2WCmdqRKyPd8zq4xwrzA/en-us_image_0000002501901426.jpg?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062516Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E3E00249A82161FE8D8FAEEB7929938649FB28A5E4DA3EE2CFA1F439D21FF8A9)

**System capability**: SystemCapability.OfficeService.PDFService.Core

**Start version**: 5.0.0(12)

**Parameters:**

| 
**Parameter**

 | 

**Type**

 | 

**Mandatory**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- |
| 

index

 | 

number

 | 

Yes

 | 

Index of the page to be moved. The value must be greater than or equal to **0** and less than the total page count. The value **0** indicates the start page.

 |
| 

dest

 | 

number

 | 

Yes

 | 

Index of the destination page. The value must be greater than or equal to **0** and less than or equal to the total page count. The value **0** indicates the start page.

 |

**Returns**:

| 
**Type**

 | 

**Description**

 |
| :-- | :-- |
| 

boolean

 | 

If the specified page is successfully moved to the index position, **true** is returned. Otherwise, **false** is returned.

 |

**Example**:

import { pdfService } from '@kit.PDFKit';

// Upload the test file to the app sandbox path.
let tempFilePath = '/data/storage/el2/base/temp/test.pdf';
let pdfDocument = new pdfService.PdfDocument();
// Load the temporary file.
let loadResult = pdfDocument.loadDocument(tempFilePath, '');
if(pdfService.ParseResult.PARSE\_SUCCESS === loadResult) {
  pdfDocument.movePage(2, 4);
}

#### \[h2\]getFontWeight

getFontWeight(): number

Obtains font weight.

**System capability**: SystemCapability.OfficeService.PDFService.Core

**Start version**: 5.0.0(12)

**Returns**:

| 
**Type**

 | 

**Description**

 |
| :-- | :-- |
| 

number

 | 

Font weight, in points (one inch equals 72 points). The value must be greater than **0**.

 |

**Example**:

import { pdfService } from '@kit.PDFKit';

// Upload the test file to the app sandbox path.
let tempFilePath = '/data/storage/el2/base/temp/test.pdf';
let pdfDocument = new pdfService.PdfDocument();
// Load the temporary file.
let loadResult = pdfDocument.loadDocument(tempFilePath, '');
if(pdfService.ParseResult.PARSE\_SUCCESS === loadResult) {
  let weight = pdfDocument.getFontWeight();
}

#### \[h2\]setFontWeight

setFontWeight(weight: number): void

Sets font weight.

**System capability**: SystemCapability.OfficeService.PDFService.Core

**Start version**: 5.0.0(12)

**Parameters:**

| 
**Parameter**

 | 

**Type**

 | 

**Mandatory**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- |
| 

weight

 | 

number

 | 

Yes

 | 

Font weight, in points (one inch equals 72 points). The value must be greater than **0**.

 |

**Example**:

import { pdfService } from '@kit.PDFKit';

// Upload the test file to the app sandbox path.
let tempFilePath = '/data/storage/el2/base/temp/test.pdf';
let pdfDocument = new pdfService.PdfDocument();
// Load the temporary file.
let loadResult = pdfDocument.loadDocument(tempFilePath, '');
if(pdfService.ParseResult.PARSE\_SUCCESS === loadResult) {
  let weight = pdfDocument.setFontWeight(10);
}

#### \[h2\]getMetadata

getMetadata(): Metadata

Obtains PDF metadata, including the author, creator, and date of creation.

**System capability**: SystemCapability.OfficeService.PDFService.Core

**Start version**: 5.0.0(12)

**Returns**:

| 
**Type**

 | 

**Description**

 |
| :-- | :-- |
| 

[Metadata](#section183223109272)

 | 

PDF metadata.

 |

**Example**:

import { pdfService } from '@kit.PDFKit';

// Upload the test file to the app sandbox path.
let tempFilePath = '/data/storage/el2/base/temp/test.pdf';
let pdfDocument = new pdfService.PdfDocument();
// Load the temporary file.
let loadResult = pdfDocument.loadDocument(tempFilePath, '');
if(pdfService.ParseResult.PARSE\_SUCCESS === loadResult) {
  pdfDocument.getMetadata();
}

#### \[h2\]convertToImage

convertToImage(path: string, format: ImageFormat, onProgress?: (progress: number) => number): boolean

Converts a PDF document to images.

**System capability**: SystemCapability.OfficeService.PDFService.Core

**Start version**: 5.0.0(12)

**Parameters:**

| 
**Parameter**

 | 

**Type**

 | 

**Mandatory**

 | 

**Description**

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

format

 | 

[ImageFormat](#section1713111745313)

 | 

Yes

 | 

Image format enum.

 |
| 

onProgress

 | 

(progress: number) => number

 | 

No

 | 

Image conversion progress. After this parameter is passed, the image conversion progress is returned. If this parameter is not passed, no image conversion progress will be returned.

 |

**Returns**:

| 
**Type**

 | 

**Description**

 |
| :-- | :-- |
| 

boolean

 | 

If the document is successfully converted to images, **true** is returned. Otherwise, **false** is returned.

 |

**Example**:

import { pdfService } from '@kit.PDFKit';
import { fileIo } from '@kit.CoreFileKit';

// Upload the test file to the app sandbox path.
let tempFilePath = '/data/storage/el2/base/temp/test.pdf';
let pdfDocument = new pdfService.PdfDocument();
// Load the temporary file.
let loadResult = pdfDocument.loadDocument(tempFilePath, '');
if(pdfService.ParseResult.PARSE\_SUCCESS === loadResult) {
  let context = this.getUIContext().getHostContext() as Context;
  let dir = context.filesDir + '/output/';
  fileIo.mkdir(dir);
  let result = pdfDocument.convertToImage(dir, pdfService.ImageFormat.PNG);
}

#### \[h2\]getRootBookmark

getRootBookmark(): Bookmark

Obtains the first root bookmark of a PDF document.

**System capability**: SystemCapability.OfficeService.PDFService.Core

**Start version**: 5.0.0(12)

**Returns**:

| 
**Type**

 | 

**Description**

 |
| :-- | :-- |
| 

[Bookmark](#section1435010204319)

 | 

First root bookmark.

 |

**Example**:

import { pdfService } from '@kit.PDFKit';

// Upload the test file to the app sandbox path.
let tempFilePath = '/data/storage/el2/base/temp/test.pdf';
let pdfDocument = new pdfService.PdfDocument();
// Load the temporary file.
let loadResult = pdfDocument.loadDocument(tempFilePath, '');
if(pdfService.ParseResult.PARSE\_SUCCESS === loadResult) {
  let rootBookmark = pdfDocument.getRootBookmark();
}

#### \[h2\]getRootBookmarks

getRootBookmarks(): Array<Bookmark>

Obtains the root bookmark of a PDF document.

**System capability**: SystemCapability.OfficeService.PDFService.Core

**Start version**: 5.0.0(12)

**Returns**:

| 
**Type**

 | 

**Description**

 |
| :-- | :-- |
| 

Array<[Bookmark](#section1435010204319)\>

 | 

Root bookmark.

 |

**Example**:

import { pdfService } from '@kit.PDFKit';

// Upload the test file to the app sandbox path.
let tempFilePath = '/data/storage/el2/base/temp/test.pdf';
let pdfDocument = new pdfService.PdfDocument();
// Load the temporary file.
let loadResult = pdfDocument.loadDocument(tempFilePath, '');
if(pdfService.ParseResult.PARSE\_SUCCESS === loadResult) {
  let rootBookmark = pdfDocument.getRootBookmarks();
}

#### \[h2\]createBookmark

createBookmark(): Bookmark

Creates a bookmark for a PDF document.

**System capability**: SystemCapability.OfficeService.PDFService.Core

**Start version**: 5.0.0(12)

**Returns**:

| 
**Type**

 | 

**Description**

 |
| :-- | :-- |
| 

[Bookmark](#section1435010204319)

 | 

If the bookmark is successfully created, the bookmark information is returned.

 |

**Example**:

import { pdfService } from '@kit.PDFKit';

// Upload the test file to the app sandbox path.
let tempFilePath = '/data/storage/el2/base/temp/test.pdf';
let pdfDocument = new pdfService.PdfDocument();
// Load the temporary file.
let loadResult = pdfDocument.loadDocument(tempFilePath, '');
if(pdfService.ParseResult.PARSE\_SUCCESS === loadResult) {
  let rootBookmark: pdfService.Bookmark = pdfDocument.createBookmark();
}

#### \[h2\]removeBookmark

removeBookmark(bookmark: Bookmark): boolean

Removes a bookmark from a PDF document.

**System capability**: SystemCapability.OfficeService.PDFService.Core

**Start version**: 5.0.0(12)

**Parameters:**

| 
**Parameter**

 | 

**Type**

 | 

**Mandatory**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- |
| 

bookmark

 | 

[Bookmark](#section1435010204319)

 | 

Yes

 | 

Bookmark type.

 |

**Returns**:

| 
**Type**

 | 

**Description**

 |
| :-- | :-- |
| 

boolean

 | 

If the bookmark is successfully removed, **true** is returned. Otherwise, **false** is returned.

 |

**Example**:

import { pdfService } from '@kit.PDFKit';

// Upload the test file to the app sandbox path.
let tempFilePath = '/data/storage/el2/base/temp/test.pdf';
let pdfDocument = new pdfService.PdfDocument();
// Load the temporary file.
let loadResult = pdfDocument.loadDocument(tempFilePath, '');
if(pdfService.ParseResult.PARSE\_SUCCESS === loadResult) {
  let bookmarks: Array<pdfService.Bookmark> = pdfDocument.getRootBookmarks();
  if (bookmarks.length && bookmarks\[0\].isRootBookmark()) {
    let rootBookmark: boolean = pdfDocument.removeBookmark(bookmarks\[0\]);
  }
}

#### \[h2\]insertBookmark

insertBookmark(bookmark: Bookmark, parent: Bookmark, position: number): boolean

Inserts a bookmark to a PDF document.

**System capability**: SystemCapability.OfficeService.PDFService.Core

**Start version**: 5.0.0(12)

**Parameters:**

| 
**Parameter**

 | 

**Type**

 | 

**Mandatory**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- |
| 

bookmark

 | 

[Bookmark](#section1435010204319)

 | 

Yes

 | 

Bookmark information.

 |
| 

parent

 | 

[Bookmark](#section1435010204319)

 | 

Yes

 | 

Parent bookmark information. The value can be **null**.

 |
| 

position

 | 

number

 | 

Yes

 | 

Position of a child bookmark. The system searches starting from 1 to find the child bookmark's position. If the position is found, the bookmark is inserted after it; if it is not found, the bookmark is inserted before the first child bookmark.

 |

**Returns**:

| 
**Type**

 | 

**Description**

 |
| :-- | :-- |
| 

boolean

 | 

If the bookmark is successfully inserted, **true** is returned. Otherwise, **false** is returned.

 |

**Example**:

import { pdfService } from '@kit.PDFKit';

// Upload the test file to the app sandbox path.
let tempFilePath = '/data/storage/el2/base/temp/test.pdf';
let pdfDocument = new pdfService.PdfDocument();
// Load the temporary file.
let loadResult = pdfDocument.loadDocument(tempFilePath, '');
if(pdfService.ParseResult.PARSE\_SUCCESS === loadResult) {
  let parentBookmark: pdfService.Bookmark = pdfDocument.createBookmark();
  let bookmark: pdfService.Bookmark = pdfDocument.createBookmark();
  pdfDocument.insertBookmark(bookmark, null, 1);
  pdfDocument.insertBookmark(bookmark, parentBookmark, 1);
  let bool1: boolean = parentBookmark.isRootBookmark();
  let bool2: boolean = bookmark.isRootBookmark();
}

#### \[h2\]addHeaderFooter

addHeaderFooter(info: HeaderFooterInfo, startIndex: number, endIndex: number, oddPages: boolean, evenPages: boolean): void

Inserts header or footer to a PDF document. This method is time-consuming as it involves iterating through each page to add headers and footers. For documents with many pages, it is recommended that you process them in a thread.

**System capability**: SystemCapability.OfficeService.PDFService.Core

**Start version**: 5.0.0(12)

**Parameters:**

| 
**Parameter**

 | 

**Type**

 | 

**Mandatory**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- |
| 

info

 | 

[HeaderFooterInfo](#section3237995481)

 | 

Yes

 | 

Header and footer information.

 |
| 

startIndex

 | 

number

 | 

Yes

 | 

Start page. The value must be greater than or equal to **0**. The value **0** indicates the start page.

 |
| 

endIndex

 | 

number

 | 

Yes

 | 

End page. The value must be less than the total page count.

 |
| 

oddPages

 | 

boolean

 | 

Yes

 | 

Indicates whether to add headers or footers to odd pages (**true**) or not (**false**).

 |
| 

evenPages

 | 

boolean

 | 

Yes

 | 

Indicates whether to add headers or footers to even pages (**true**) or not (**false**).

 |

**Example**:

import { pdfService } from '@kit.PDFKit';
import { Font } from '@kit.ArkUI';

let filePath = String.raw\`/data/storage/el2/base/haps/View/files/input.pdf\`;  
let document: pdfService.PdfDocument = new pdfService.PdfDocument();
let loadResult = document.loadDocument(filePath);
if(pdfService.ParseResult.PARSE\_SUCCESS === loadResult) {      
  let hfInfo: pdfService.HeaderFooterInfo = new pdfService.HeaderFooterInfo();
  hfInfo.fontInfo = new pdfService.FontInfo();
  let font: Font = new Font()
hfInfo.fontInfo.fontPath = font.getFontByName("HarmonyOS Sans")?.path; // Ensure that the font exists.
  hfInfo.fontInfo.fontName = '';
  hfInfo.textSize = 10;
  hfInfo.charset = pdfService.CharsetType.PDF\_FONT\_DEFAULT\_CHARSET;
  hfInfo.underline = false;
  hfInfo.textColor = 0x00000000;
  hfInfo.leftMargin = 1.0;
  hfInfo.topMargin = 40.0;
  hfInfo.rightMargin = 1.0;
  hfInfo.bottomMargin = 40.0;
  hfInfo.headerLeftText = "left H <<dd.mm.yyyy>><<1/n>>";
  hfInfo.headerCenterText = "center H <<m/d/yyyy>><<1>>";
  hfInfo.headerRightText = "right H <<m/d>><<1/n>>";
  hfInfo.footerLeftText = "left F <<m/d>><<1>>";
  hfInfo.footerCenterText = "center F <<m/d>><<1>>";
  hfInfo.footerRightText = "right F <<dd.mm.yyyy>><<1>>";
  document.addHeaderFooter(hfInfo, 1, 5, true, true);
}

#### \[h2\]getHeaderFooter

getHeaderFooter(): HeaderFooterInfo

Obtains the header or footer of a PDF document. If a PDF document does not have a header or footer, the default value of the **HeaderFooterInfo** attribute is obtained.

**System capability**: SystemCapability.OfficeService.PDFService.Core

**Start version**: 5.0.0(12)

**Returns**:

| 
**Type**

 | 

**Description**

 |
| :-- | :-- |
| 

[HeaderFooterInfo](#section3237995481)

 | 

Obtained header and footer information.

 |

**Example**:

import { pdfService } from '@kit.PDFKit';

let filePath = String.raw\`/data/storage/el2/base/haps/View/files/input.pdf\`;  
let pdfDocument = new pdfService.PdfDocument();
let loadResult = pdfDocument.loadDocument(filePath);
if(pdfService.ParseResult.PARSE\_SUCCESS === loadResult) {
  let headerFooterInfo = pdfDocument.getHeaderFooter();
}

#### \[h2\]hasHeaderFooter

hasHeaderFooter(): boolean

Indicates whether a PDF document has a header or footer.

**System capability**: SystemCapability.OfficeService.PDFService.Core

**Start version**: 5.0.0(12)

**Returns**:

| 
**Type**

 | 

**Description**

 |
| :-- | :-- |
| 

boolean

 | 

If a PDF document has a header or footer, **true** is returned. Otherwise, **false** is returned.

 |

**Example**:

import { pdfService } from '@kit.PDFKit';

let filePath = String.raw\`/data/storage/el2/base/haps/View/files/input.pdf\`;  
let pdfDocument: pdfService.PdfDocument = new pdfService.PdfDocument();
let loadResult = pdfDocument.loadDocument(filePath);
if(pdfService.ParseResult.PARSE\_SUCCESS === loadResult) {
  let hasHeaderFooter: boolean = pdfDocument.hasHeaderFooter();
}

#### \[h2\]removeHeaderFooter

removeHeaderFooter(): boolean

Removes the header or footer from a PDF document.

**System capability**: SystemCapability.OfficeService.PDFService.Core

**Start version**: 5.0.0(12)

**Returns**:

| 
**Type**

 | 

**Description**

 |
| :-- | :-- |
| 

boolean

 | 

If the header or footer is removed from a PDF document, **true** is returned. Otherwise, **false** is returned.

 |

**Example**:

import { pdfService } from '@kit.PDFKit';

let filePath = String.raw\`/data/storage/el2/base/haps/View/files/input.pdf\`;  
let pdfDocument = new pdfService.PdfDocument();
let loadResult = pdfDocument.loadDocument(filePath);
if(pdfService.ParseResult.PARSE\_SUCCESS === loadResult) {
  if (pdfDocument.hasHeaderFooter()) {
    let delHeaderFooter: boolean = pdfDocument.removeHeaderFooter();
  }
}

#### \[h2\]addWatermark

addWatermark(info: WatermarkInfo, startIndex: number, endIndex: number, oddPages: boolean, evenPages: boolean): void

Adds a watermark to a PDF document. This method is time-consuming as it involves iterating through each page to add watermarks. For documents with many pages, it is recommended that you process them in a thread.

**System capability**: SystemCapability.OfficeService.PDFService.Core

**Start version**: 5.0.0(12)

**Parameters:**

| 
**Parameter**

 | 

**Type**

 | 

**Mandatory**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- |
| 

info

 | 

[WatermarkInfo](#section4749820144811)

 | 

Yes

 | 

Watermark information.

 |
| 

startIndex

 | 

number

 | 

Yes

 | 

Start page. The value must be greater than or equal to **0**. The value **0** indicates the start page.

 |
| 

endIndex

 | 

number

 | 

Yes

 | 

End page. The value must be less than the total page count.

 |
| 

oddPages

 | 

boolean

 | 

Yes

 | 

Indicates whether to add watermarks to odd pages (**true**) or not (**false**).

 |
| 

evenPages

 | 

boolean

 | 

Yes

 | 

Indicates whether to add watermarks to even pages (**true**) or not (**false**).

 |

**Example**:

-   Add a text watermark.

import { pdfService } from '@kit.PDFKit';
import { Font } from '@kit.ArkUI';

let filePath = String.raw\`/data/storage/el2/base/haps/View/files/input.pdf\`;  
let pdfDocument: pdfService.PdfDocument = new pdfService.PdfDocument();
let loadResult = pdfDocument.loadDocument(filePath);
if(pdfService.ParseResult.PARSE\_SUCCESS === loadResult) {
  let wminfo: pdfService.TextWatermarkInfo = new pdfService.TextWatermarkInfo();
  wminfo.watermarkType = pdfService.WatermarkType.WATERMARK\_TEXT;
  wminfo.content = "This is watermark";
  wminfo.textSize = 30;
  wminfo.textColor = 200;
  wminfo.fontInfo = new pdfService.FontInfo();
  let font: Font = new Font()
  wminfo.fontInfo.fontPath = font.getFontByName("HarmonyOS Sans").path;
  wminfo.opacity = 0.5;
  wminfo.isOnTop = true;
  wminfo.rotation = 45;
  wminfo.scale = 1.5;
  wminfo.verticalAlignment = pdfService.WatermarkAlignment.WATERMARK\_ALIGNMENT\_TOP;
  wminfo.horizontalAlignment = pdfService.WatermarkAlignment.WATERMARK\_ALIGNMENT\_LEFT;
  wminfo.horizontalSpace = 1.0;
  wminfo.verticalSpace = 1.0;
  pdfDocument.addWatermark(wminfo, 1, 18, true, true);
}

-   Add an image watermark.

import { pdfService } from '@kit.PDFKit';

let filePath = String.raw\`/data/storage/el2/base/haps/View/files/input.pdf\`;  
let pdfDocument: pdfService.PdfDocument = new pdfService.PdfDocument();
let loadResult = pdfDocument.loadDocument(filePath);
if(pdfService.ParseResult.PARSE\_SUCCESS === loadResult) {
  let wminfo: pdfService.ImageWatermarkInfo = new pdfService.ImageWatermarkInfo();
  wminfo.watermarkType = pdfService.WatermarkType.WATERMARK\_IMAGE;
  wminfo.imagePath = "/data/storage/el2/base/haps/View/files/img.jpg";
  wminfo.opacity = 0.5;
  wminfo.isOnTop = true;
  wminfo.rotation = 45;
  wminfo.scale = 1.5;
  wminfo.verticalAlignment = pdfService.WatermarkAlignment.WATERMARK\_ALIGNMENT\_TOP;
  wminfo.horizontalAlignment = pdfService.WatermarkAlignment.WATERMARK\_ALIGNMENT\_LEFT;
  wminfo.horizontalSpace = 1.0;
  wminfo.verticalSpace = 1.0;
  pdfDocument.addWatermark(wminfo, 1, 18, true, true);
}

#### \[h2\]getWatermark

getWatermark(): WatermarkInfo

Obtains the watermark of a PDF document. If a PDF document does not have a watermark, the default value of the **WatermarkInfo** attribute is obtained.

**System capability**: SystemCapability.OfficeService.PDFService.Core

**Start version**: 5.0.0(12)

**Returns**:

| 
**Type**

 | 

**Description**

 |
| :-- | :-- |
| 

[WatermarkInfo](#section4749820144811)

 | 

Obtained PDF document watermark information.

 |

**Example**:

import { pdfService } from '@kit.PDFKit';

let filePath = String.raw\`/data/storage/el2/base/haps/View/files/input.pdf\`;  
let pdfDocument: pdfService.PdfDocument = new pdfService.PdfDocument();
let loadResult = pdfDocument.loadDocument(filePath);
if(pdfService.ParseResult.PARSE\_SUCCESS === loadResult) {
  let watermarkInfo: pdfService.WatermarkInfo = pdfDocument.getWatermark();
}

#### \[h2\]hasWatermark

hasWatermark(): boolean

Checks whether a PDF document has a watermark.

**System capability**: SystemCapability.OfficeService.PDFService.Core

**Start version**: 5.0.0(12)

**Returns**:

| 
**Type**

 | 

**Description**

 |
| :-- | :-- |
| 

boolean

 | 

If a PDF document has a watermark, **true** is returned. Otherwise, **false** is returned.

 |

**Example**:

import { pdfService } from '@kit.PDFKit';

let filePath = String.raw\`/data/storage/el2/base/haps/View/files/input.pdf\`;  
let pdfDocument: pdfService.PdfDocument = new pdfService.PdfDocument();
let loadResult = pdfDocument.loadDocument(filePath);
if(pdfService.ParseResult.PARSE\_SUCCESS === loadResult) {
  let hasWatermark: boolean = pdfDocument.hasWatermark();
}

#### \[h2\]removeWatermark

removeWatermark(): boolean

Removes a watermark from a PDF document.

**System capability**: SystemCapability.OfficeService.PDFService.Core

**Start version**: 5.0.0(12)

**Returns**:

| 
**Type**

 | 

**Description**

 |
| :-- | :-- |
| 

boolean

 | 

If the watermark is removed successfully, **true** is returned. Otherwise, **false** is returned.

 |

**Example**:

import { pdfService } from '@kit.PDFKit';

let filePath = String.raw\`/data/storage/el2/base/haps/View/files/input.pdf\`;  
let pdfDocument: pdfService.PdfDocument = new pdfService.PdfDocument();
let loadResult = pdfDocument.loadDocument(filePath);
if(pdfService.ParseResult.PARSE\_SUCCESS === loadResult) {
  let hasWatermark: boolean = pdfDocument.hasWatermark();
  if (hasWatermark) {
    let hasRemoveWatermark = pdfDocument.removeWatermark();
  }
}

#### \[h2\]addBackground

addBackground(info: BackgroundInfo, startIndex: number, endIndex: number, oddPages: boolean, evenPages: boolean): void

Adds background to a PDF document. This method is time-consuming as it involves iterating through each page to add backgrounds. For documents with many pages, it is recommended that you process them in a thread.

**System capability**: SystemCapability.OfficeService.PDFService.Core

**Start version**: 5.0.0(12)

**Parameters:**

| 
**Parameter**

 | 

**Type**

 | 

**Mandatory**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- |
| 

info

 | 

[BackgroundInfo](#section165811065495)

 | 

Yes

 | 

Background information.

 |
| 

startIndex

 | 

number

 | 

Yes

 | 

Start page. The value must be greater than or equal to **0**. The value **0** indicates the start page.

 |
| 

endIndex

 | 

number

 | 

Yes

 | 

End page. The value must be less than the total page count.

 |
| 

oddPages

 | 

boolean

 | 

Yes

 | 

Indicates whether to add backgrounds to odd pages (**true**) or not (**false**).

 |
| 

evenPages

 | 

boolean

 | 

Yes

 | 

Indicates whether to add backgrounds to even pages (**true**) or not (**false**).

 |

**Example**:

import { pdfService } from '@kit.PDFKit';

let filePath = String.raw\`/data/storage/el2/base/haps/View/files/output.pdf\`;  
let pdfDocument: pdfService.PdfDocument = new pdfService.PdfDocument();
let loadResult = pdfDocument.loadDocument(filePath);
if(pdfService.ParseResult.PARSE\_SUCCESS === loadResult) {
  let bginfo: pdfService.BackgroundInfo = new pdfService.BackgroundInfo();
  bginfo.imagePath = "/data/storage/el2/base/haps/View/files/img.jpg";
  bginfo.backgroundColor = 50;
  bginfo.isOnTop = true;
  bginfo.rotation = 90;
  bginfo.scale = 0.5;
  bginfo.opacity = 0.3;
  bginfo.verticalAlignment = pdfService.BackgroundAlignment.BACKGROUND\_ALIGNMENT\_TOP;
  bginfo.horizontalAlignment = pdfService.BackgroundAlignment.BACKGROUND\_ALIGNMENT\_LEFT;
  bginfo.horizontalSpace = 1.0;
  bginfo.verticalSpace = 1.0;
  pdfDocument.addBackground(bginfo, 2, 18, true, true);
}

#### \[h2\]getBackground

getBackground(): BackgroundInfo

Obtains PDF document background information. If a PDF document does not have a background, the default value of the **BackgroundInfo** attribute is obtained.

**System capability**: SystemCapability.OfficeService.PDFService.Core

**Start version**: 5.0.0(12)

**Returns**:

| 
**Type**

 | 

**Description**

 |
| :-- | :-- |
| 

[BackgroundInfo](#section165811065495)

 | 

Obtains PDF document background information.

 |

**Example**:

import { pdfService } from '@kit.PDFKit';

let filePath = String.raw\`/data/storage/el2/base/haps/View/files/output.pdf\`;  
let pdfDocument: pdfService.PdfDocument = new pdfService.PdfDocument();
let loadResult = pdfDocument.loadDocument(filePath);
if(pdfService.ParseResult.PARSE\_SUCCESS === loadResult) {
  if (pdfDocument.hasBackground()) {
    let backgroundInfo: pdfService.BackgroundInfo = pdfDocument.getBackground();
  }
}

#### \[h2\]hasBackground

hasBackground(): boolean

Checks whether a PDF document has a background.

**System capability**: SystemCapability.OfficeService.PDFService.Core

**Start version**: 5.0.0(12)

**Returns**:

| 
**Type**

 | 

**Description**

 |
| :-- | :-- |
| 

boolean

 | 

If a PDF document has a background, **true** is returned. Otherwise, **false** is returned.

 |

**Example**:

import { pdfService } from '@kit.PDFKit';

let filePath = String.raw\`/data/storage/el2/base/haps/View/files/output.pdf\`;  
let pdfDocument: pdfService.PdfDocument = new pdfService.PdfDocument();
let loadResult = pdfDocument.loadDocument(filePath);
if(pdfService.ParseResult.PARSE\_SUCCESS === loadResult) {
  let hasBackground: boolean = pdfDocument.hasBackground();
}

#### \[h2\]removeBackground

removeBackground(): boolean

Removes the background of a PDF document.

**System capability**: SystemCapability.OfficeService.PDFService.Core

**Start version**: 5.0.0(12)

**Returns**:

| 
**Type**

 | 

**Description**

 |
| :-- | :-- |
| 

boolean

 | 

If the background is successfully removed, **true** is returned. Otherwise, **false** is returned.

 |

**Example**:

import { pdfService } from '@kit.PDFKit';

let filePath = String.raw\`/data/storage/el2/base/haps/View/files/output.pdf\`;  
let pdfDocument: pdfService.PdfDocument = new pdfService.PdfDocument();
let loadResult = pdfDocument.loadDocument(filePath);
if(pdfService.ParseResult.PARSE\_SUCCESS === loadResult) {
  if (pdfDocument.hasBackground()) {
    let delBackground: boolean = pdfDocument.removeBackground();
  }
}

#### \[h2\]setPdfPassword

setPdfPassword(password: string): boolean

Adds a password to a PDF document.

**System capability**: SystemCapability.OfficeService.PDFService.Core

**Start version**: 5.0.5(17)

**Parameters:**

| 
**Parameter**

 | 

**Type**

 | 

**Mandatory**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- |
| 

password

 | 

string

 | 

Yes

 | 

Password (only ASCII characters ranging from 0 to 127 are supported).

 |

**Returns**:

| 
**Type**

 | 

**Description**

 |
| :-- | :-- |
| 

boolean

 | 

Whether the password is added successfully.

-   **true**: Adding successful.
-   **false**: Adding failed.

 |

**Example**:

import { pdfService } from '@kit.PDFKit';

let filePath = String.raw\`/data/storage/el2/base/haps/View/files/output.pdf\`;  
let pdfDocument: pdfService.PdfDocument = new pdfService.PdfDocument();
let loadResult = pdfDocument.loadDocument(filePath);
if(pdfService.ParseResult.PARSE\_SUCCESS === loadResult) {
   let setPassword: boolean = pdfDocument.setPdfPassword('123456');
 }

#### \[h2\]searchKey

searchKey(text: string, listener: SearchKeyCallback, options?: SearchOptions): Promise<void>

Searches for a keyword in a PDF document. This API returns the result asynchronously through a promise.

**System capability**: SystemCapability.OfficeService.PDFService.Core

**Start version**: 6.0.1(21)

**Parameters:**

| 
**Parameter**

 | 

**Type**

 | 

**Mandatory**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- |
| 

text

 | 

string

 | 

Yes

 | 

Keyword to search for (strings across PDF pages are not supported).

 |
| 

listener

 | 

[SearchKeyCallback](#section38941941115812)

 | 

Yes

 | 

Callback function executed after each page is searched.

 |
| 

options

 | 

[SearchOptions](#section324683725416)

 | 

No

 | 

Search options.

 |

**Returns**:

| 
**Type**

 | 

**Description**

 |
| :-- | :-- |
| 

Promise<void>

 | 

Promise that returns no value.

 |

**Example**:

import { pdfService } from '@kit.PDFKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
const keyword: string = 'watermelon';
const options: pdfService.SearchOptions = {
  startIndex: 0,
  endIndex: 50,
  isMatchWholeWord: true,
  isMatchCase: true,
  contextStringLength: 80
}
const listener: pdfService.SearchKeyCallback = (results: pdfService.SearchResultData\[\]): boolean => {
  for (let i = 0; i < results.length; i++) {
    let contextString = results\[i\].contextString;
    hilog.info(0x0000, 'searchKey',\`Get context string: ${contextString}\`);
  }
  return false;
};
let doc: pdfService.PdfDocument | undefined = undefined;
doc = new pdfService.PdfDocument();
let loadResult = doc.loadDocument(filePath);
if (loadResult === pdfService.ParseResult.PARSE\_SUCCESS) {
  await doc.searchKey(keyword, listener, options);
}

#### SearchKeyCallback

SearchKeyCallback = (results: SearchResultData\[\]) => boolean;

Callback function for keyword search. The callback is triggered once for each page of content searched.

**System capability**: SystemCapability.OfficeService.PDFService.Core

**Start version**: 6.0.1(21)

**Parameters:**

| 
**Parameter**

 | 

**Type**

 | 

**Mandatory**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- |
| 

results

 | 

[SearchResultData](#section16681737115912)\[\]

 | 

Yes

 | 

Search results.

 |

**Returns**:

| 
**Type**

 | 

**Description**

 |
| :-- | :-- |
| 

boolean

 | 

Whether to stop a search task.

-   **true**: yes
-   **false**: no

 |

#### SearchOptions

Search options.

**System capability**: SystemCapability.OfficeService.PDFService.Core

**Start version**: 6.0.1(21)

| 
**Name**

 | 

**Type**

 | 

**Read-Only**

 | 

**Optional**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- | :-- |
| 

startIndex

 | 

number

 | 

No

 | 

Yes

 | 

Start page number for keyword search. The value must be greater than or equal to **0**. The default value is **0**.

 |
| 

endIndex

 | 

number

 | 

No

 | 

Yes

 | 

End page number for keyword search. The value must be greater than or equal to **0**. The value of **endIndex** must be greater than or equal to that of **startIndex**. The default value is the total number of PDF pages minus 1.

 |
| 

isMatchWholeWord

 | 

boolean

 | 

No

 | 

Yes

 | 

Indicates whether to use whole-word matching for keyword search (valid only for English).

**true**: yes

**false**: no

The default value is **false**.

 |
| 

isMatchCase

 | 

boolean

 | 

No

 | 

Yes

 | 

Indicates whether keyword search is case sensitive (valid only for English).

**true**: yes

**false**: no

The default value is **false**.

 |
| 

contextStringLength

 | 

number

 | 

No

 | 

Yes

 | 

Context string length of a search hit (each Chinese or English character is counted as one character). The value ranges from **0** to **200**. The default value is **80**.

 |

#### SearchResultData

Search result data.

**System capability**: SystemCapability.OfficeService.PDFService.Core

**Start version**: 6.0.1(21)

| 
**Name**

 | 

**Type**

 | 

**Read-Only**

 | 

**Optional**

 | 

**Description**

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

Page number of a search hit.

 |
| 

rects

 | 

[PdfRect](#section19829174815360)\[\]

 | 

No

 | 

No

 | 

Rectangle information of a search hit.

 |
| 

contextString

 | 

boolean

 | 

No

 | 

No

 | 

Context string of a search hit (cross-page context strings are not supported). When the string length is within that specified by **contextStringLength**, the original string is output.

 |

#### Metadata

PDF metadata type.

**System capability**: SystemCapability.OfficeService.PDFService.Core

**Start version**: 5.0.0(12)

| 
**Name**

 | 

**Type**

 | 

**Read-Only**

 | 

**Optional**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- | :-- |
| 

title

 | 

string

 | 

No

 | 

No

 | 

Title.

 |
| 

author

 | 

string

 | 

No

 | 

No

 | 

Author.

 |
| 

subject

 | 

string

 | 

No

 | 

No

 | 

Theme.

 |
| 

keywords

 | 

string

 | 

No

 | 

No

 | 

Keyword.

 |
| 

creator

 | 

string

 | 

No

 | 

No

 | 

Creator, or the name of the original program if the file is converted from another format to PDF.

 |
| 

producer

 | 

string

 | 

No

 | 

No

 | 

Convertor, or the name of the original program if the file is converted from another format to PDF.

 |
| 

creationDate

 | 

Date

 | 

No

 | 

No

 | 

Creation date.

 |
| 

modifiedDate

 | 

Date

 | 

No

 | 

No

 | 

Modification date.

 |

#### PdfAnnotation

PDF page annotation class.

**System capability**: SystemCapability.OfficeService.PDFService.Core

**Start version**: 5.0.0(12)

## Attributes

| 
**Name**

 | 

**Type**

 | 

**Read-Only**

 | 

**Optional**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- | :-- |
| 

type

 | 

[AnnotationType](#section5365193011530)

 | 

No

 | 

No

 | 

Annotation type.

 |
| 

uniqueId

 | 

string

 | 

No

 | 

No

 | 

Annotation ID.

 |

#### \[h2\]getPdfPage

getPdfPage(): PdfPage

Obtains a PDF page.

**System capability**: SystemCapability.OfficeService.PDFService.Core

**Start version**: 5.0.0(12)

**Returns**:

| 
**Type**

 | 

**Description**

 |
| :-- | :-- |
| 

[PdfPage](#section1643717123816)

 | 

PDF page data.

 |

**Example**:

import { pdfService } from '@kit.PDFKit';

let tempFilePath = '/data/storage/el2/base/temp/test.pdf';
let pdfDocument = new pdfService.PdfDocument();
let loadResult = pdfDocument.loadDocument(tempFilePath, '');
if(pdfService.ParseResult.PARSE\_SUCCESS === loadResult) {
  let page: pdfService.PdfPage = pdfDocument.getPage(0);
  let annotations: Array<pdfService.PdfAnnotation> = page.getAnnotations();
  let annot: pdfService.PdfAnnotation = annotations\[0\]; // Obtain annotations on the current page.
  let pdfPage: pdfService.PdfPage = annot.getPdfPage();
}

#### \[h2\]getAnnotationIndex

getAnnotationIndex(): number

Obtains the index of an annotation on a PDF page.

**System capability**: SystemCapability.OfficeService.PDFService.Core

**Start version**: 5.0.0(12)

**Returns**:

| 
**Type**

 | 

**Description**

 |
| :-- | :-- |
| 

number

 | 

Obtained annotation index.

 |

**Example**:

import { pdfService } from '@kit.PDFKit';

let tempFilePath = '/data/storage/el2/base/temp/test.pdf';
let pdfDocument = new pdfService.PdfDocument();
let loadResult = pdfDocument.loadDocument(tempFilePath, '');
if(pdfService.ParseResult.PARSE\_SUCCESS === loadResult) {
  let page: pdfService.PdfPage = pdfDocument.getPage(0);
  let annotations: Array<pdfService.PdfAnnotation> = page.getAnnotations();
  let annot: pdfService.PdfAnnotation = annotations\[0\]; // Obtain annotations on the current page.
  let annoIndex: number = annot.getAnnotationIndex(); // Return the annotation index on the current page.
}

#### \[h2\]getAnnotationInfo

getAnnotationInfo(): PdfAnnotationInfo

Obtains the annotation information on the current PDF page.

**System capability**: SystemCapability.OfficeService.PDFService.Core

**Start version**: 5.0.0(12)

**Returns**:

| 
**Type**

 | 

**Description**

 |
| :-- | :-- |
| 

[PdfAnnotationInfo](#section1463555133017)

 | 

An annotation on the PDF page.

 |

**Example**:

import { pdfService } from '@kit.PDFKit';

let tempFilePath = '/data/storage/el2/base/temp/test.pdf';
let pdfDocument = new pdfService.PdfDocument();
let loadResult = pdfDocument.loadDocument(tempFilePath, '');
if(pdfService.ParseResult.PARSE\_SUCCESS === loadResult) {
  let page: pdfService.PdfPage = pdfDocument.getPage(0);
  let annotations: Array<pdfService.PdfAnnotation> = page.getAnnotations();
  let annot: pdfService.PdfAnnotation = annotations\[0\]; // Obtain an annotation on the current page.
  let pdfPage: pdfService.PdfPage = annot.getPdfPage();
  let annoIndex: number = annot.getAnnotationIndex(); // Return the annotation index on the current page.
  let annotat: pdfService.TextAnnotationInfo = annot.getAnnotationInfo() as pdfService.TextAnnotationInfo;
  let annot1: pdfService.PdfAnnotation = annotations\[1\];
  let annot2: pdfService.PdfAnnotation = annotations\[2\];
  // If the second annotation on the page has an in-document redirection link
  let gotoAction = annot1.getAnnotationInfo().action as pdfService.PdfActionGoTo;
  // If the third annotation on the page has a hyperlink
  let hyperlinkAction = annot2.getAnnotationInfo().action as pdfService.PdfActionHyperlink;
}

#### \[h2\]moveTo

moveTo(x: number, y: number): void

Moves an annotation by x and y in total on a PDF page.

**System capability**: SystemCapability.OfficeService.PDFService.Core

**Start version**: 5.0.0(12)

**Parameters**:

| 
**Parameter**

 | 

**Type**

 | 

**Mandatory**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- |
| 

x

 | 

number

 | 

Yes

 | 

Total distance of an annotation moved along the X axis, in points (one inch equals 72 points).

 |
| 

y

 | 

number

 | 

Yes

 | 

Total distance of an annotation moved along the Y axis, in points (one inch equals 72 points).

 |

**Example**:

import { pdfService } from '@kit.PDFKit';

let tempFilePath = '/data/storage/el2/base/temp/test.pdf';
let pdfDocument = new pdfService.PdfDocument();
let loadResult = pdfDocument.loadDocument(tempFilePath, '');
if(pdfService.ParseResult.PARSE\_SUCCESS === loadResult) {
  let page: pdfService.PdfPage = pdfDocument.getPage(0);
  let annotations: Array<pdfService.PdfAnnotation> = page.getAnnotations();
  let annot: pdfService.PdfAnnotation = annotations\[0\]; // Obtain annotations on the current page.
  let pdfPage: pdfService.PdfPage = annot.getPdfPage();
  let annoIndex: number = annot.getAnnotationIndex(); // Return the index of the annotation on the current page.
  let annotat: pdfService.TextAnnotationInfo = annot.getAnnotationInfo() as pdfService.TextAnnotationInfo;
  annot.moveTo (50, 50);// Move the annotation on the current page to the position where x is 50 and y is 50.
  let isMarkupAnno: boolean = annot.isMarkup();
}

#### \[h2\]isMarkup

isMarkup(): boolean

Checks whether the current annotation is a markup annotation.

**System capability**: SystemCapability.OfficeService.PDFService.Core

**Start version**: 5.0.0(12)

**Returns**:

| 
**Type**

 | 

**Description**

 |
| :-- | :-- |
| 

boolean

 | 

If the current annotation is a markup annotation, **true** is returned. Otherwise, **false** is returned.

 |

**Example**:

import { pdfService } from '@kit.PDFKit';

let tempFilePath = '/data/storage/el2/base/temp/test.pdf';
let pdfDocument = new pdfService.PdfDocument();
let loadResult = pdfDocument.loadDocument(tempFilePath, '');
if(pdfService.ParseResult.PARSE\_SUCCESS === loadResult) {
  let page: pdfService.PdfPage = pdfDocument.getPage(0);
  let annotations: Array<pdfService.PdfAnnotation> = page.getAnnotations();
  let annot: pdfService.PdfAnnotation = annotations\[0\]; // Obtain annotations on the current page.
  let pdfPage: pdfService.PdfPage = annot.getPdfPage();
  let annoIndex: number = annot.getAnnotationIndex(); // Return the index of the annotation on the current page.
  let annotat: pdfService.TextAnnotationInfo = annot.getAnnotationInfo() as pdfService.TextAnnotationInfo;
  annot.moveTo (50, 50);// Move the annotation on the current page to the position where x is 50 and y is 50.
  let isMarkupAnno: boolean =  annot.isMarkup();
}

#### PdfAnnotationInfo

PDF page annotation information.

**System capability**: SystemCapability.OfficeService.PDFService.Core

**Start version**: 5.0.0(12)

| 
**Name**

 | 

**Type**

 | 

**Read-Only**

 | 

**Optional**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- | :-- |
| 

type

 | 

[AnnotationType](#section5365193011530)

 | 

No

 | 

No

 | 

Annotation type.

 |
| 

uniqueId

 | 

string

 | 

No

 | 

No

 | 

Annotation ID.

 |
| 

content

 | 

string

 | 

No

 | 

Yes

 | 

Annotation content.

 |
| 

modifiedTime

 | 

Date

 | 

No

 | 

Yes

 | 

Annotation modification time.

 |
| 

border

 | 

[PdfBorder](#section5949183733615)

 | 

No

 | 

Yes

 | 

Border type.

 |
| 

flag

 | 

[AnnotationFlag](#section266974511502)

 | 

No

 | 

Yes

 | 

Annotation flag.

 |
| 

title

 | 

string

 | 

No

 | 

Yes

 | 

Annotation title.

 |
| 

opacity

 | 

number

 | 

No

 | 

Yes

 | 

Opacity. The value ranges from **0** to **1**. The value **0** indicates completely transparent, and the value **1** indicates completely opaque.

 |
| 

subject

 | 

string

 | 

No

 | 

Yes

 | 

Annotation subject.

 |
| 

creationDate

 | 

Date

 | 

No

 | 

Yes

 | 

Date on which an annotation is created, for example, 2024-01-01.

 |
| 

action

 | 

[PdfAction](#section1136285384812)

 | 

No

 | 

Yes

 | 

Page link redirection. The PDF document jumps to the corresponding page or hyperlink (for example, a web page address). Currently, links can be obtained but cannot be added or edited.

**Start version**: 5.1.0(18)

 |

#### TextAnnotationInfo

PDF page text annotation class, which is inherited from [PdfAnnotationInfo](#section1463555133017).

**System capability**: SystemCapability.OfficeService.PDFService.Core

**Start version**: 5.0.0(12)

| 
**Name**

 | 

**Type**

 | 

**Read-Only**

 | 

**Optional**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- | :-- |
| 

iconName

 | 

string

 | 

No

 | 

No

 | 

Icon name of a text annotation.

 |
| 

state

 | 

[TextAnnotationState](#section3149139155118)

 | 

No

 | 

No

 | 

Text annotation status enum.

 |
| 

x

 | 

number

 | 

No

 | 

No

 | 

X coordinate, in points (one inch equals 72 points). The value must be greater than or equal to **0**.

 |
| 

y

 | 

number

 | 

No

 | 

No

 | 

Y coordinate, in points (one inch equals 72 points). The value must be greater than or equal to **0**.

Note: As the underlying layer has performed data processing, there will be deviations between the passed value and the returned value.

 |
| 

color

 | 

number

 | 

No

 | 

Yes

 | 

Annotation text color. The value ranges from **0x000000** to **0xFFFFFF**.

(For example, **0xFF0000** indicates blue, and **0x0000FF** indicates red.)

 |

#### LinkAnnotationInfo

PDF page link annotation class, which is inherited from [PdfAnnotationInfo](#section1463555133017).

**System capability**: SystemCapability.OfficeService.PDFService.Core

**Start version**: 5.0.0(12)

| 
**Name**

 | 

**Type**

 | 

**Read-Only**

 | 

**Optional**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- | :-- |
| 

left

 | 

number

 | 

No

 | 

No

 | 

Left margin, in points (one inch equals 72 points). The value must be greater than or equal to **0**.

 |
| 

bottom

 | 

number

 | 

No

 | 

No

 | 

Bottom margin, in points (one inch equals 72 points). The value must be greater than or equal to **0**.

 |
| 

right

 | 

number

 | 

No

 | 

No

 | 

Right margin, in points (one inch equals 72 points). The value must be greater than or equal to **0**.

 |
| 

top

 | 

number

 | 

No

 | 

No

 | 

Top margin, in points (one inch equals 72 points). The value must be greater than or equal to **0**.

 |
| 

highlightMode

 | 

[HighlightMode](#section1343075435110)

 | 

No

 | 

Yes

 | 

Highlight mode.

Note: Currently only form annotations are supported. The returned value is **\-1**.

 |
| 

color

 | 

number

 | 

No

 | 

Yes

 | 

Color. The value ranges from **0x000000** to **0xFFFFFF**.

(For example, **0xFF0000** indicates blue, and **0x0000FF** indicates red.)

 |

#### FreeTextAnnotationInfo

PDF page free text annotation class, which is inherited from [PdfAnnotationInfo](#section1463555133017).

**System capability**: SystemCapability.OfficeService.PDFService.Core

**Start version**: 5.0.0(12)

| 
**Name**

 | 

**Type**

 | 

**Read-Only**

 | 

**Optional**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- | :-- |
| 

x

 | 

number

 | 

No

 | 

No

 | 

X coordinate, in points (one inch equals 72 points). The value must be greater than or equal to **0**.

Note: As the underlying layer has performed data processing, there will be deviations between the passed value and the returned value.

 |
| 

y

 | 

number

 | 

No

 | 

No

 | 

Y coordinate, in points (one inch equals 72 points). The value must be greater than or equal to **0**.

Note: As the underlying layer has performed data processing, there will be deviations between the passed value and the returned value.

 |
| 

width

 | 

number

 | 

No

 | 

Yes

 | 

Width, in points (one inch equals 72 points). The value must be greater than **0**.

Note: As the underlying layer has performed data processing, there will be deviations between the passed value and the returned value.

 |
| 

fillColor

 | 

number

 | 

No

 | 

Yes

 | 

Fill color. The value ranges from **0x000000** to **0xFFFFFF**.

(For example, **0xFF0000** indicates blue, and **0x0000FF** indicates red.)

 |
| 

textStyle

 | 

[TextStyle](#section8549131255014)

 | 

No

 | 

Yes

 | 

Text type.

Note: There may be discrepancies between the passed and returned values. For instance, when a Boolean value is passed, **1** is returned for **true**, and **0** is returned for **false**. For font parameters, as there is more than one font file name, the returned font name may be different.

 |
| 

textAlignment

 | 

[AlignmentType](#section96379535210)

 | 

No

 | 

Yes

 | 

Alignment type.

 |

#### SquareAnnotationInfo

PDF page square annotation class, which is inherited from [PdfAnnotationInfo](#section1463555133017).

**System capability**: SystemCapability.OfficeService.PDFService.Core

**Start version**: 5.0.0(12)

| 
**Name**

 | 

**Type**

 | 

**Read-Only**

 | 

**Optional**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- | :-- |
| 

left

 | 

number

 | 

No

 | 

No

 | 

Left margin, in points (one inch equals 72 points). The value must be greater than or equal to **0**.

 |
| 

bottom

 | 

number

 | 

No

 | 

No

 | 

Bottom margin, in points (one inch equals 72 points). The value must be greater than or equal to **0**.

 |
| 

right

 | 

number

 | 

No

 | 

No

 | 

Right margin, in points (one inch equals 72 points). The value must be greater than or equal to **0**.

 |
| 

top

 | 

number

 | 

No

 | 

No

 | 

Top margin, in points (one inch equals 72 points). The value must be greater than or equal to **0**.

 |
| 

lineColor

 | 

number

 | 

No

 | 

Yes

 | 

Border color. The value ranges from **0x000000** to **0xFFFFFF**.

(For example, **0xFF0000** indicates blue, and **0x0000FF** indicates red.)

 |
| 

fillColor

 | 

number

 | 

No

 | 

Yes

 | 

Fill color. The value ranges from **0x000000** to **0xFFFFFF**.

(For example, **0xFF0000** indicates blue, and **0x0000FF** indicates red.)

 |

#### OvalAnnotationInfo

PDF page oval annotation class, which is inherited from [PdfAnnotationInfo](#section1463555133017).

**System capability**: SystemCapability.OfficeService.PDFService.Core

**Start version**: 5.0.0(12)

| 
**Name**

 | 

**Type**

 | 

**Read-Only**

 | 

**Optional**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- | :-- |
| 

left

 | 

number

 | 

No

 | 

No

 | 

Left margin, in points (one inch equals 72 points). The value must be greater than or equal to **0**.

 |
| 

bottom

 | 

number

 | 

No

 | 

No

 | 

Bottom margin, in points (one inch equals 72 points). The value must be greater than or equal to **0**.

 |
| 

right

 | 

number

 | 

No

 | 

No

 | 

Right margin, in points (one inch equals 72 points). The value must be greater than or equal to **0**.

 |
| 

top

 | 

number

 | 

No

 | 

No

 | 

Top margin, in points (one inch equals 72 points). The value must be greater than or equal to **0**.

 |
| 

lineColor

 | 

number

 | 

No

 | 

Yes

 | 

Border color. The value ranges from **0x000000** to **0xFFFFFF**.

(For example, **0xFF0000** indicates blue, and **0x0000FF** indicates red.)

 |
| 

fillColor

 | 

number

 | 

No

 | 

Yes

 | 

Fill color. The value ranges from **0x000000** to **0xFFFFFF**.

(For example, **0xFF0000** indicates blue, and **0x0000FF** indicates red.)

 |

#### PolygonAnnotationInfo

PDF page polygon annotation class, which is inherited from [PdfAnnotationInfo](#section1463555133017).

**System capability**: SystemCapability.OfficeService.PDFService.Core

**Start version**: 5.0.0(12)

| 
**Name**

 | 

**Type**

 | 

**Read-Only**

 | 

**Optional**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- | :-- |
| 

vertexes

 | 

Array<[PdfPoint](#section174855274363)\>

 | 

No

 | 

No

 | 

Array describing the PdfPoint of a polygon annotation in sequence.

 |
| 

lineColor

 | 

number

 | 

No

 | 

Yes

 | 

Border color. The value ranges from **0x000000** to **0xFFFFFF**.

(For example, **0xFF0000** indicates blue, and **0x0000FF** indicates red.)

 |
| 

fillColor

 | 

number

 | 

No

 | 

Yes

 | 

Fill color. The value ranges from **0x000000** to **0xFFFFFF**.

(For example, **0xFF0000** indicates blue, and **0x0000FF** indicates red.)

 |

#### LineAnnotationInfo

PDF page line annotation class, which is inherited from [PdfAnnotationInfo](#section1463555133017).

**System capability**: SystemCapability.OfficeService.PDFService.Core

**Start version**: 5.0.0(12)

| 
**Name**

 | 

**Type**

 | 

**Read-Only**

 | 

**Optional**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- | :-- |
| 

startX

 | 

number

 | 

No

 | 

No

 | 

X coordinate of the start point (distance to the left margin), in points (one inch equals 72 points).

Note: As the underlying layer has performed data processing, there will be deviations between the passed value and the returned value.

 |
| 

startY

 | 

number

 | 

No

 | 

No

 | 

Y coordinate of the start point (distance to the bottom margin), in points (one inch equals 72 points).

Note: As the underlying layer has performed data processing, there will be deviations between the passed value and the returned value.

 |
| 

endX

 | 

number

 | 

No

 | 

No

 | 

X coordinate of the end point (distance to the left margin), in points (one inch equals 72 points).

Note: As the underlying layer has performed data processing, there will be deviations between the passed value and the returned value.

 |
| 

endY

 | 

number

 | 

No

 | 

No

 | 

Y coordinate of the end point (distance to the bottom margin), in points (one inch equals 72 points).

Note: As the underlying layer has performed data processing, there will be deviations between the passed value and the returned value.

 |
| 

startPointStyle

 | 

[LineEndStyle](#section16189171745220)

 | 

No

 | 

No

 | 

Line style of the start point.

 |
| 

endPointStyle

 | 

[LineEndStyle](#section16189171745220)

 | 

No

 | 

No

 | 

Line style of the end point.

 |
| 

lineColor

 | 

number

 | 

No

 | 

Yes

 | 

Border color. The value ranges from **0x000000** to **0xFFFFFF**. (For example, **0xFF0000** indicates blue, and **0x0000FF** indicates red.)

 |

#### PolylineAnnotationInfo

PDF page polyline annotation class, which is inherited from [PdfAnnotationInfo](#section1463555133017).

**System capability**: SystemCapability.OfficeService.PDFService.Core

**Start version**: 5.0.0(12)

| 
**Name**

 | 

**Type**

 | 

**Read-Only**

 | 

**Optional**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- | :-- |
| 

vertexes

 | 

Array<[PdfPoint](#section174855274363)\>

 | 

No

 | 

No

 | 

Array describing the PdfPoint of a polyline annotation in sequence.

 |
| 

lineColor

 | 

number

 | 

No

 | 

Yes

 | 

Border color. The value ranges from **0x000000** to **0xFFFFFF**.

(For example, **0xFF0000** indicates blue, and **0x0000FF** indicates red.)

 |

#### HighlightAnnotationInfo

PDF page highlight annotation class, which is inherited from [PdfAnnotationInfo](#section1463555133017).

**System capability**: SystemCapability.OfficeService.PDFService.Core

**Start version**: 5.0.0(12)

| 
**Name**

 | 

**Type**

 | 

**Read-Only**

 | 

**Optional**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- | :-- |
| 

quadPoints

 | 

Array<[PdfPoint](#section174855274363)\>

 | 

No

 | 

No

 | 

PdfPoint array of the highlight area.

Each link annotation has 4 x n points. The four points in each group are:

First point: point in the upper left corner of the rectangle

Second point: point in the upper right corner of the rectangle

Third point: point in the lower left corner of the rectangle

Fourth point: point in the lower right corner of the rectangle

Note: As the underlying layer has performed data processing, there will be deviations between the passed value and the returned value.

 |
| 

color

 | 

number

 | 

No

 | 

Yes

 | 

RGB color of the highlight area. The value ranges from **0x000000** to **0xFFFFFF**.

(For example, **0xFF0000** indicates blue, and **0x0000FF** indicates red.)

 |

#### UnderlineAnnotationInfo

PDF page underline annotation class, which is inherited from [PdfAnnotationInfo](#section1463555133017).

**System capability**: SystemCapability.OfficeService.PDFService.Core

**Start version**: 5.0.0(12)

| 
**Name**

 | 

**Type**

 | 

**Read-Only**

 | 

**Optional**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- | :-- |
| 

quadPoints

 | 

Array<[PdfPoint](#section174855274363)\>

 | 

No

 | 

No

 | 

PdfPoint array of the underlined area.

Each link annotation has 4 x n points. The four points in each group are:

First point: point in the upper left corner of the rectangle

Second point: point in the upper right corner of the rectangle

Third point: point in the lower left corner of the rectangle

Fourth point: point in the lower right corner of the rectangle

Note: As the underlying layer has performed data processing, there will be deviations between the passed value and the returned value.

 |

#### StrikethroughAnnotationInfo

PDF page strikethrough annotation class, which is inherited from [PdfAnnotationInfo](#section1463555133017).

**System capability**: SystemCapability.OfficeService.PDFService.Core

**Start version**: 5.0.0(12)

| 
**Name**

 | 

**Type**

 | 

**Read-Only**

 | 

**Optional**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- | :-- |
| 

quadPoints

 | 

Array<[PdfPoint](#section174855274363)\>

 | 

No

 | 

No

 | 

PdfPoint array of the strikethrough area.

Each link annotation has 4 x n points. The four points in each group are:

First point: point in the upper left corner of the rectangle

Second point: point in the upper right corner of the rectangle

Third point: point in the lower left corner of the rectangle

Fourth point: point in the lower right corner of the rectangle

Note: As the underlying layer has performed data processing, there will be deviations between the passed value and the returned value.

 |

#### InkAnnotationInfo

PDF page ink annotation class, which is inherited from [PdfAnnotationInfo](#section1463555133017).

**System capability**: SystemCapability.OfficeService.PDFService.Core

**Start version**: 5.0.0(12)

| 
**Name**

 | 

**Type**

 | 

**Read-Only**

 | 

**Optional**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- | :-- |
| 

inkPoints

 | 

Array<[PdfPoint](#section174855274363)\>

 | 

No

 | 

No

 | 

Array describing the PdfPoint of an ink annotation in sequence.

Each link annotation has 4 x n points. The four points in each group are:

First point: point in the upper left corner of the rectangle

Second point: point in the upper right corner of the rectangle

Third point: point in the lower left corner of the rectangle

Fourth point: point in the lower right corner of the rectangle

 |
| 

lineColor

 | 

number

 | 

No

 | 

Yes

 | 

Line color. The value ranges from **0x000000** to **0xFFFFFF**. The default value is **0x000000**.

(For example, **0xFF0000** indicates blue, and **0x0000FF** indicates red.)

 |

#### StampAnnotationInfo

PDF page stamp annotation class, which is inherited from [PdfAnnotationInfo](#section1463555133017).

**System capability**: SystemCapability.OfficeService.PDFService.Core

**Start version**: 5.0.0(12)

| 
**Name**

 | 

**Type**

 | 

**Read-Only**

 | 

**Optional**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- | :-- |
| 

imagePath

 | 

string

 | 

No

 | 

No

 | 

The file path of the image.

 |
| 

left

 | 

number

 | 

No

 | 

No

 | 

Left margin, in points (one inch equals 72 points). The value must be greater than or equal to **0**.

 |
| 

bottom

 | 

number

 | 

No

 | 

No

 | 

Bottom margin, in points (one inch equals 72 points). The value must be greater than or equal to **0**.

 |
| 

right

 | 

number

 | 

No

 | 

No

 | 

Right margin, in points (one inch equals 72 points). The value must be greater than or equal to **0**.

 |
| 

top

 | 

number

 | 

No

 | 

No

 | 

Top margin, in points (one inch equals 72 points). The value must be greater than or equal to **0**.

 |

#### PdfPoint

PDF page point position class.

**System capability**: SystemCapability.OfficeService.PDFService.Core

**Start version**: 5.0.0(12)

## Attributes

| 
**Name**

 | 

**Type**

 | 

**Read-Only**

 | 

**Optional**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- | :-- |
| 

x

 | 

number

 | 

No

 | 

No

 | 

X coordinate, in points (one inch equals 72 points).

 |
| 

y

 | 

number

 | 

No

 | 

No

 | 

Y coordinate, in points (one inch equals 72 points).

 |

#### \[h2\]constructor

constructor()

Creates a point location object.

**System capability**: SystemCapability.OfficeService.PDFService.Core

**Start version**: 5.0.0(12)

#### PdfBorder

PDF page border class.

**System capability**: SystemCapability.OfficeService.PDFService.Core

**Start version**: 5.0.0(12)

## Attributes

| 
**Name**

 | 

**Type**

 | 

**Read-Only**

 | 

**Optional**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- | :-- |
| 

borderStyle

 | 

[BorderStyle](#section12517112715502)

 | 

No

 | 

No

 | 

Border type.

 |
| 

borderWidth

 | 

number

 | 

No

 | 

No

 | 

Border width, in points (one inch equals 72 points). The value must be greater than **0**.

 |
| 

borderColor

 | 

number

 | 

No

 | 

No

 | 

Border color. The value ranges from **0x000000** to **0xFFFFFF**.

(For example, **0xFF0000** indicates blue, and **0x0000FF** indicates red.)

 |

#### \[h2\]constructor

constructor()

Creates a border object.

**System capability**: SystemCapability.OfficeService.PDFService.Core

**Start version**: 5.0.0(12)

#### PdfRect

PDF page rectangle class.

**System capability**: SystemCapability.OfficeService.PDFService.Core

**Start version**: 5.0.0(12)

## Attributes

| 
**Name**

 | 

**Type**

 | 

**Read-Only**

 | 

**Optional**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- | :-- |
| 

left

 | 

number

 | 

No

 | 

No

 | 

Left margin, in points (one inch equals 72 points). The value must be greater than or equal to **0**.

 |
| 

top

 | 

number

 | 

No

 | 

No

 | 

Top margin, in points (one inch equals 72 points). The value must be greater than or equal to **0**.

 |
| 

right

 | 

number

 | 

No

 | 

No

 | 

Right margin, in points (one inch equals 72 points). The value must be greater than or equal to **0**.

 |
| 

bottom

 | 

number

 | 

No

 | 

No

 | 

Bottom margin, in points (one inch equals 72 points). The value must be greater than or equal to **0**.

 |

#### \[h2\]constructor

constructor()

Creates a rectangle object.

**System capability**: SystemCapability.OfficeService.PDFService.Core

**Start version**: 5.0.0(12)

#### PdfMatrix

Coordinate transformation matrix of a PDF page. The matrix includes the **x**, **y**, **width**, **height**, and **rotate** attributes, among which **x** and **y** specify the offset of the upper left corner of the image relative to the page, **width** and **height** specify the zoom ratio relative to the original page, and **rotate** specifies the rotation angle.

**System capability**: SystemCapability.OfficeService.PDFService.Core

**Start version**: 5.0.0(12)

## Attributes

| 
**Name**

 | 

**Type**

 | 

**Read-Only**

 | 

**Optional**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- | :-- |
| 

x

 | 

number

 | 

No

 | 

No

 | 

X coordinate, in points (one inch equals 72 points). The value must be greater than or equal to **0**. Horizontal offset of the upper left corner of the target page within the PDF page.

 |
| 

y

 | 

number

 | 

No

 | 

No

 | 

Y coordinate, in points (one inch equals 72 points). The value must be greater than or equal to **0**. Vertical offset of the upper left corner of the target page within the PDF page.

 |
| 

width

 | 

number

 | 

No

 | 

No

 | 

Width, in points (one inch equals 72 points). The value must be greater than **0**.

 |
| 

height

 | 

number

 | 

No

 | 

No

 | 

Height, in points (one inch equals 72 points). The value must be greater than **0**.

 |
| 

rotate

 | 

number

 | 

No

 | 

No

 | 

Rotation angle. One unit equals 90 degrees. The value cannot be **Infinity** or **\-Infinity**.

Values 1, 2, 3, and 4 indicate 90, 180, 270, and 360 degrees, respectively.

 |

#### \[h2\]constructor

constructor()

Creates a PDF matrix object for the rectangular area on the PDF page.

**System capability**: SystemCapability.OfficeService.PDFService.Core

**Start version**: 5.0.0(12)

#### PdfPage

PDF page class.

**System capability**: SystemCapability.OfficeService.PDFService.Core

**Start version**: 5.0.0(12)

#### \[h2\]getDocument

getDocument(): PdfDocument

Obtains a **PDFDocument** object.

**System capability**: SystemCapability.OfficeService.PDFService.Core

**Start version**: 5.0.0(12)

**Returns**:

| 
**Type**

 | 

**Description**

 |
| :-- | :-- |
| 

[PdfDocument](#section1319183318231)

 | 

**PdfDocument** object.

 |

**Example**:

import { pdfService } from '@kit.PDFKit';

let tempFilePath = '/data/storage/el2/base/temp/test.pdf';
let pdfDocument = new pdfService.PdfDocument();
let loadResult = pdfDocument.loadDocument(tempFilePath, '');
if(pdfService.ParseResult.PARSE\_SUCCESS === loadResult) {
  let page: pdfService.PdfPage = pdfDocument.getPage(0);
  let document:pdfService.PdfDocument = page.getDocument();
}

#### \[h2\]getAnnotations

getAnnotations(): Array<PdfAnnotation>

Obtains the annotations of a document.

**System capability**: SystemCapability.OfficeService.PDFService.Core

**Start version**: 5.0.0(12)

**Returns**:

| 
**Type**

 | 

**Description**

 |
| :-- | :-- |
| 

Array<[PdfAnnotation](#section7542143132912)\>

 | 

Document annotation array.

 |

**Example**:

import { pdfService } from '@kit.PDFKit';

let tempFilePath = '/data/storage/el2/base/temp/test.pdf';
let pdfDocument = new pdfService.PdfDocument();
let loadResult = pdfDocument.loadDocument(tempFilePath, '');
if(pdfService.ParseResult.PARSE\_SUCCESS === loadResult) {
  let page: pdfService.PdfPage = pdfDocument.getPage(0);
  let annotations: Array<pdfService.PdfAnnotation> = page.getAnnotations();
}

#### \[h2\]addAnnotation

addAnnotation(annotationInfo: PdfAnnotationInfo): PdfAnnotation

Adds an annotation to the current page.

**System capability**: SystemCapability.OfficeService.PDFService.Core

**Start version**: 5.0.0(12)

**Parameters**:

| 
**Parameter**

 | 

**Type**

 | 

**Mandatory**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- |
| 

annotationInfo

 | 

[PdfAnnotationInfo](#section1463555133017)

 | 

Yes

 | 

Document annotation class.

 |

**Returns**:

| 
**Type**

 | 

**Description**

 |
| :-- | :-- |
| 

[PdfAnnotation](#section7542143132912)

 | 

Document annotation.

 |

**Example**:

import { pdfService } from '@kit.PDFKit';

let tempFilePath = '/data/storage/el2/base/temp/test.pdf';
let pdfDocument = new pdfService.PdfDocument();
let loadResult = pdfDocument.loadDocument(tempFilePath, '');
if(pdfService.ParseResult.PARSE\_SUCCESS === loadResult) {
  let pdfPage: pdfService.PdfPage = pdfDocument.getPage(0);
  let aInfo = new pdfService.TextAnnotationInfo();
  aInfo.iconName = "test iconName";
  aInfo.x = 200;
  aInfo.y = 200;
  aInfo.state = pdfService.TextAnnotationState.MARKED;
  aInfo.flag = pdfService.AnnotationFlag.PRINTED;
  let doc = pdfPage.addAnnotation(aInfo);
}

#### \[h2\]setAnnotation

setAnnotation(annotation: PdfAnnotation, annotationInfo: PdfAnnotationInfo): void

Sets an annotation on the current page.

**System capability**: SystemCapability.OfficeService.PDFService.Core

**Start version**: 5.0.0(12)

**Parameters**:

| 
**Parameter**

 | 

**Type**

 | 

**Mandatory**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- |
| 

annotation

 | 

[PdfAnnotation](#section7542143132912)

 | 

Yes

 | 

Document annotation.

 |
| 

annotationInfo

 | 

[PdfAnnotationInfo](#section1463555133017)

 | 

Yes

 | 

Document annotation class.

 |

**Example**:

import { pdfService } from '@kit.PDFKit';

let tempFilePath = '/data/storage/el2/base/temp/test.pdf';
let pdfDocument = new pdfService.PdfDocument();
let loadResult = pdfDocument.loadDocument(tempFilePath, '');
if(pdfService.ParseResult.PARSE\_SUCCESS === loadResult) {
  let pdfPage: pdfService.PdfPage = pdfDocument.getPage(0);
  let aInfo = new pdfService.TextAnnotationInfo();
  // Text param
  aInfo.iconName = "test iconName";
  aInfo.state = pdfService.TextAnnotationState.UNMARKED;
  aInfo.x = 200;
  aInfo.y = 200;
  aInfo.state = pdfService.TextAnnotationState.MARKED;
  aInfo.flag = pdfService.AnnotationFlag.PRINTED;
  let annotation = pdfPage.addAnnotation(aInfo);
  let bInfo = new pdfService.TextAnnotationInfo();
  bInfo.iconName = "yet another test iconName";
  bInfo.state = pdfService.TextAnnotationState.MARKED;
  bInfo.x = 200;
  bInfo.y = 200;
  bInfo.subject = "this is a subject";
  bInfo.content = "this is a content";
  pdfPage.setAnnotation(annotation, bInfo);
}

#### \[h2\]removeAnnotation

removeAnnotation(annotation: PdfAnnotation): void

Removes annotations from the current page.

**System capability**: SystemCapability.OfficeService.PDFService.Core

**Start version**: 5.0.0(12)

**Parameters**:

| 
**Parameter**

 | 

**Type**

 | 

**Mandatory**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- |
| 

annotation

 | 

[PdfAnnotation](#section7542143132912)

 | 

Yes

 | 

Document annotation.

 |

**Example**:

import { pdfService } from '@kit.PDFKit';

let tempFilePath = '/data/storage/el2/base/temp/test.pdf';
let pdfDocument = new pdfService.PdfDocument();
let loadResult = pdfDocument.loadDocument(tempFilePath, '');
if(pdfService.ParseResult.PARSE\_SUCCESS === loadResult) {
  let pdfPage: pdfService.PdfPage = pdfDocument.getPage(0);
  let aInfo = new pdfService.TextAnnotationInfo();
  // Text param
  aInfo.iconName = "test iconName";
  aInfo.x = 200;
  aInfo.y = 200;
  aInfo.state = pdfService.TextAnnotationState.MARKED;
  aInfo.flag = pdfService.AnnotationFlag.PRINTED;
  let annotation = pdfPage.addAnnotation(aInfo);pdfPage.removeAnnotation(annotation);
}

#### \[h2\]getIndex

getIndex(): number

Obtains the index of the current page.

**System capability**: SystemCapability.OfficeService.PDFService.Core

**Start version**: 5.0.0(12)

**Returns**:

| 
**Type**

 | 

**Description**

 |
| :-- | :-- |
| 

number

 | 

Index. The value must be greater than or equal to 0 and less than the total page count.

 |

**Example**:

import { pdfService } from '@kit.PDFKit';

let tempFilePath = '/data/storage/el2/base/temp/test.pdf';
let pdfDocument = new pdfService.PdfDocument();
let loadResult = pdfDocument.loadDocument(tempFilePath, '');
if(pdfService.ParseResult.PARSE\_SUCCESS === loadResult) {
  let pdfPage: pdfService.PdfPage = pdfDocument.getPage(0);
  let index = pdfPage.getIndex();
}

#### \[h2\]getWidth

getWidth(): number

Obtains the width of the current page.

**System capability**: SystemCapability.OfficeService.PDFService.Core

**Start version**: 5.0.0(12)

**Returns**:

| 
**Type**

 | 

**Description**

 |
| :-- | :-- |
| 

number

 | 

Width, in points (one inch equals 72 points).

 |

**Example**:

import { pdfService } from '@kit.PDFKit';

let tempFilePath = '/data/storage/el2/base/temp/test.pdf';
let pdfDocument = new pdfService.PdfDocument();
let loadResult = pdfDocument.loadDocument(tempFilePath, '');
if(pdfService.ParseResult.PARSE\_SUCCESS === loadResult) {
  let pdfPage: pdfService.PdfPage = pdfDocument.getPage(0);
  let width = pdfPage.getWidth();
}

#### \[h2\]getHeight

getHeight(): number

Obtains the height of the current page.

**System capability**: SystemCapability.OfficeService.PDFService.Core

**Start version**: 5.0.0(12)

**Returns**:

| 
**Type**

 | 

**Description**

 |
| :-- | :-- |
| 

number

 | 

Height, in points (one inch equals 72 points).

 |

**Example**:

import { pdfService } from '@kit.PDFKit';

let tempFilePath = '/data/storage/el2/base/temp/test.pdf';
let pdfDocument = new pdfService.PdfDocument();
let loadResult = pdfDocument.loadDocument(tempFilePath, '');
if(pdfService.ParseResult.PARSE\_SUCCESS === loadResult) {
  let pdfPage: pdfService.PdfPage = pdfDocument.getPage(0);
  let height = pdfPage.getHeight();
}

#### \[h2\]setBox

setBox(boxtype: BoxType, rect: PdfRect): void

Sets the page box.

**System capability**: SystemCapability.OfficeService.PDFService.Core

**Start version**: 5.0.0(12)

**Parameters**:

| 
**Parameter**

 | 

**Type**

 | 

**Mandatory**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- |
| 

boxtype

 | 

[BoxType](#section8653184295318)

 | 

Yes

 | 

Page box.

 |
| 

rect

 | 

[PdfRect](#section19829174815360)

 | 

Yes

 | 

Rectangle.

 |

**Example**:

import { pdfService } from '@kit.PDFKit';

let tempFilePath = '/data/storage/el2/base/temp/test.pdf';
let pdfDocument = new pdfService.PdfDocument();
let loadResult = pdfDocument.loadDocument(tempFilePath, '');
if(pdfService.ParseResult.PARSE\_SUCCESS === loadResult) {
  let pdfPage: pdfService.PdfPage = pdfDocument.getPage(0);
  let pdfRect = new pdfService.PdfRect();
  pdfRect.left = 100;
  pdfRect.top = 100;
  pdfRect.right = 100;
  pdfRect.bottom = 100;
  pdfPage.setBox(pdfService.BoxType.BOX\_MEDIA , pdfRect);
}

#### \[h2\]getBox

getBox(boxtype: BoxType): PdfRect

Obtains the page box.

**System capability**: SystemCapability.OfficeService.PDFService.Core

**Start version**: 5.0.0(12)

**Parameters:**

| 
**Parameter**

 | 

**Type**

 | 

**Mandatory**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- |
| 

boxtype

 | 

[BoxType](#section8653184295318)

 | 

Yes

 | 

Page box.

 |

**Returns**:

| 
**Type**

 | 

**Description**

 |
| :-- | :-- |
| 

[PdfRect](#section19829174815360)

 | 

Page box rectangle.

 |

**Example**:

import { pdfService } from '@kit.PDFKit';

let tempFilePath = '/data/storage/el2/base/temp/test.pdf';
let pdfDocument = new pdfService.PdfDocument();
let loadResult = pdfDocument.loadDocument(tempFilePath, '');
if(pdfService.ParseResult.PARSE\_SUCCESS === loadResult) {
  let pdfPage: pdfService.PdfPage = pdfDocument.getPage(0);
  let box: pdfService.PdfRect = pdfPage.getBox(pdfService.BoxType.BOX\_MEDIA);
}

#### \[h2\]setRotation

setRotation(rotation: RotationAngle): void

Sets the rotation angle of a page.

**System capability**: SystemCapability.OfficeService.PDFService.Core

**Start version**: 5.0.0(12)

**Parameters:**

| 
**Parameter**

 | 

**Type**

 | 

**Mandatory**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- |
| 

rotation

 | 

[RotationAngle](#section554915414532)

 | 

Yes

 | 

Rotation angle enum.

 |

**Example**:

import { pdfService } from '@kit.PDFKit';

let tempFilePath = '/data/storage/el2/base/temp/test.pdf';
let pdfDocument = new pdfService.PdfDocument();
let loadResult = pdfDocument.loadDocument(tempFilePath, '');
if(pdfService.ParseResult.PARSE\_SUCCESS === loadResult) {
  let pdfPage: pdfService.PdfPage = pdfDocument.getPage(0);
  pdfPage.setRotation(pdfService.RotationAngle.ANGLE\_90);
}

#### \[h2\]getRotation

getRotation(): RotationAngle

Obtains the rotation angle of a page.

**System capability**: SystemCapability.OfficeService.PDFService.Core

**Start version**: 5.0.0(12)

**Returns**:

| 
**Type**

 | 

**Description**

 |
| :-- | :-- |
| 

[RotationAngle](#section554915414532)

 | 

Rotation angle.

 |

**Example**:

import { pdfService } from '@kit.PDFKit';

let tempFilePath = '/data/storage/el2/base/temp/test.pdf';
let pdfDocument = new pdfService.PdfDocument();
let loadResult = pdfDocument.loadDocument(tempFilePath, '');
if(pdfService.ParseResult.PARSE\_SUCCESS === loadResult) {
  let pdfPage: pdfService.PdfPage = pdfDocument.getPage(0);
  let rotation = pdfPage.getRotation();
}

#### \[h2\]getPagePixelMap

getPagePixelMap(): image.PixelMap

Obtains the image of the current page.

**System capability**: SystemCapability.OfficeService.PDFService.Core

**Start version**: 5.0.0(12)

**Returns**:

| 
**Type**

 | 

**Description**

 |
| :-- | :-- |
| 

[image.PixelMap](../../../../media/image-kit/arkts-apis/ohos-multimedia-image-image-processing/interface-pixelmap/document.md)

 | 

**image.PixelMap** type of the current page.

 |

**Example**:

import { pdfService } from '@kit.PDFKit';

let tempFilePath = '/data/storage/el2/base/temp/test.pdf';
let pdfDocument = new pdfService.PdfDocument();
let loadResult = pdfDocument.loadDocument(tempFilePath, '');
if(pdfService.ParseResult.PARSE\_SUCCESS === loadResult) {
  let pdfPage: pdfService.PdfPage = pdfDocument.getPage(0);
  let img = pdfPage.getPagePixelMap();
}

#### \[h2\]getCustomPagePixelMap

getCustomPagePixelMap(matrix: PdfMatrix, isGray: boolean, drawAnnotations: boolean): image.PixelMap

Obtains the image content between pages specified by **PdfPage**.

**System capability**: SystemCapability.OfficeService.PDFService.Core

**Start version**: 5.0.0(12)

**Parameters:**

| 
**Parameter**

 | 

**Type**

 | 

**Mandatory**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- |
| 

matrix

 | 

[PdfMatrix](#section113572873718)

 | 

Yes

 | 

Coordinate transformation matrix, which is used to scale, translate, and rotate page content during rendering.

 |
| 

isGray

 | 

boolean

 | 

Yes

 | 

Indicates whether to obtain only the black and white image (**true**) or not (**false**).

 |
| 

drawAnnotations

 | 

boolean

 | 

Yes

 | 

Indicates whether to draw annotations in the image (**true**) or not (**false**).

 |

**Returns**:

| 
**Type**

 | 

**Description**

 |
| :-- | :-- |
| 

[image.PixelMap](../../../../media/image-kit/arkts-apis/ohos-multimedia-image-image-processing/interface-pixelmap/document.md)

 | 

PixelMap image of the current page.

 |

**Example**:

import { pdfService } from '@kit.PDFKit';
import { image } from '@kit.ImageKit';

let tempFilePath = '/data/storage/el2/base/temp/test.pdf';
let pdfDocument = new pdfService.PdfDocument();
let loadResult = pdfDocument.loadDocument(tempFilePath, '');
if(pdfService.ParseResult.PARSE\_SUCCESS === loadResult) {
  let pdfPage: pdfService.PdfPage = pdfDocument.getPage(0);
  let pdfMatrix: pdfService.PdfMatrix = new pdfService.PdfMatrix();
  let pixelMap: image.PixelMap = pdfPage.getCustomPagePixelMap(pdfMatrix, true, true);
}

#### \[h2\]getAreaPixelMap

getAreaPixelMap(matrix: PdfMatrix, bitmapwidth: number, bitmapHeight: number, isGray: boolean, drawAnnotations: boolean): image.PixelMap

Renders a specified PDF page as a PixelMap image.

**System capability**: SystemCapability.OfficeService.PDFService.Core

**Start version**: 5.0.0(12)

**Parameters:**

| 
**Parameter**

 | 

**Type**

 | 

**Mandatory**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- |
| 

matrix

 | 

[PdfMatrix](#section113572873718)

 | 

Yes

 | 

Coordinate transformation matrix, which is used to scale, translate, and rotate page content during rendering.

 |
| 

bitmapwidth

 | 

number

 | 

Yes

 | 

Width of the rendered image. The value must be greater than **0**.

 |
| 

bitmapHeight

 | 

number

 | 

Yes

 | 

Height of the rendered image. The value must be greater than **0**.

 |
| 

isGray

 | 

boolean

 | 

Yes

 | 

Indicates whether to obtain the gray image (**true**) or not (**false**).

 |
| 

drawAnnotations

 | 

boolean

 | 

Yes

 | 

Indicates whether to render annotations (**true**) or not (**false**).

 |

**Returns**:

| 
**Type**

 | 

**Description**

 |
| :-- | :-- |
| 

[image.PixelMap](../../../../media/image-kit/arkts-apis/ohos-multimedia-image-image-processing/interface-pixelmap/document.md)

 | 

PixelMap image of the current page.

 |

**Example**:

import { pdfService } from '@kit.PDFKit';
import { image } from '@kit.ImageKit';

let tempFilePath = '/data/storage/el2/base/temp/test.pdf';
let pdfDocument = new pdfService.PdfDocument();
let loadResult = pdfDocument.loadDocument(tempFilePath, '');
if(pdfService.ParseResult.PARSE\_SUCCESS === loadResult) {
  let pdfPage: pdfService.PdfPage = pdfDocument.getPage(0);
  let pdfMatrix: pdfService.PdfMatrix = new pdfService.PdfMatrix();
  let pixelMap: image.PixelMap = pdfPage.getAreaPixelMap(pdfMatrix, 200, 300, true, true);
}

#### \[h2\]addTextObject

addTextObject(text: string, x: number, y: number, style: TextStyle): void

Adds text content only by line.

**System capability**: SystemCapability.OfficeService.PDFService.Core

**Start version**: 5.0.0(12)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2a/v3/QwdzXGJeR4a7kzPYj8IYkA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062516Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=26467E56FF9C6415D22893BDBBF0C6173923B732F4471143B1747A13F38DD1E6)

The system version must be 5.0.0.126 (SP8) or later.

**Parameters:**

| 
**Parameter**

 | 

**Type**

 | 

**Mandatory**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- |
| 

text

 | 

string

 | 

Yes

 | 

Text content.

 |
| 

x

 | 

number

 | 

Yes

 | 

X coordinate, in points (one inch equals 72 points). The value must be greater than or equal to **0**.

 |
| 

y

 | 

number

 | 

Yes

 | 

Y coordinate, in points (one inch equals 72 points). The value must be greater than or equal to **0**.

 |
| 

style

 | 

[TextStyle](#section8549131255014)

 | 

Yes

 | 

Text style.

 |

**Example**:

import { pdfService } from '@kit.PDFKit';

let tempFilePath = '/data/storage/el2/base/temp/test.pdf';
let pdfDocument = new pdfService.PdfDocument();
let loadResult = pdfDocument.loadDocument(tempFilePath, '');
if(pdfService.ParseResult.PARSE\_SUCCESS === loadResult) {
  let pdfPage: pdfService.PdfPage = pdfDocument.getPage(0);
  let textStyle = new pdfService.TextStyle();
  let fontInfo = new pdfService.FontInfo();
  fontInfo.fontPath = "/system/fonts/HarmonyOS\_Sans\_SC\_Black.ttf"
  textStyle.fontInfo = fontInfo;
  textStyle.textSize = 11;
  textStyle.textColor = 234;
  textStyle.isBold = true;
  textStyle.isItalic = false;
  textStyle.isUnderline = true;
  pdfPage.addTextObject('a', 20, 20, textStyle);
}

#### \[h2\]addImageObject

addImageObject(path: string, x: number, y: number, width: number, height: number): void

Adds an image to a page of a PDF document.

**System capability**: SystemCapability.OfficeService.PDFService.Core

**Start version**: 5.0.0(12)

**Parameters:**

| 
**Parameter**

 | 

**Type**

 | 

**Mandatory**

 | 

**Description**

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

x

 | 

number

 | 

Yes

 | 

X coordinate, in points (one inch equals 72 points). The value must be greater than or equal to **0**.

 |
| 

y

 | 

number

 | 

Yes

 | 

Y coordinate, in points (one inch equals 72 points). The value must be greater than or equal to **0**.

 |
| 

width

 | 

number

 | 

Yes

 | 

Width, in points (one inch equals 72 points). The value must be greater than **0**.

 |
| 

height

 | 

number

 | 

Yes

 | 

Height, in points (one inch equals 72 points). The value must be greater than **0**.

 |

**Example**:

import { pdfService } from '@kit.PDFKit';

let tempFilePath = '/data/storage/el2/base/temp/test.pdf';
let pdfDocument = new pdfService.PdfDocument();
let loadResult = pdfDocument.loadDocument(tempFilePath, '');
if(pdfService.ParseResult.PARSE\_SUCCESS === loadResult) {
  let pdfPage: pdfService.PdfPage = pdfDocument.getPage(0);
  let context = this.getUIContext().getHostContext() as Context;
  let dir = context.filesDir;
  let imgPath = dir + "/img.jpg";
  pdfPage.addImageObject(imgPath, 0, 0, 200, 200);
  pdfDocument.saveDocument("/data/storage/el2/base/haps/entry/files/testAddImageToDocument.pdf");
}

#### \[h2\]getGraphicsObjects

getGraphicsObjects(): Array<GraphicsObject>

Obtains all graphics objects, which are returned by position, for example, from left to right or from top to bottom.

**System capability**: SystemCapability.OfficeService.PDFService.Core

**Start version**: 5.0.0(12)

**Returns**:

| 
**Type**

 | 

**Description**

 |
| :-- | :-- |
| 

Array<[GraphicsObject](#section1251812324215)\>

 | 

Array of all graphic objects.

 |

**Example**:

import { pdfService } from '@kit.PDFKit';

let tempFilePath = '/data/storage/el2/base/temp/test.pdf';
let pdfDocument = new pdfService.PdfDocument();
let loadResult = pdfDocument.loadDocument(tempFilePath, '');
if(pdfService.ParseResult.PARSE\_SUCCESS === loadResult) {
  let pdfPage: pdfService.PdfPage = pdfDocument.getPage(0);
  let allImgObj = pdfPage.getGraphicsObjects();
}

#### \[h2\]deleteGraphicsObject

deleteGraphicsObject(object: GraphicsObject): void

Deletes a specified [GraphicsObject](#section1251812324215) object.

**System capability**: SystemCapability.OfficeService.PDFService.Core

**Start version**: 5.0.0(12)

**Parameters:**

| 
**Parameter**

 | 

**Type**

 | 

**Mandatory**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- |
| 

object

 | 

[GraphicsObject](#section1251812324215)

 | 

Yes

 | 

Graphics object.

 |

**Example**:

import { pdfService } from '@kit.PDFKit';

let tempFilePath = '/data/storage/el2/base/temp/test.pdf';
let pdfDocument = new pdfService.PdfDocument();
let loadResult = pdfDocument.loadDocument(tempFilePath, '');
if(pdfService.ParseResult.PARSE\_SUCCESS === loadResult) {
  let pdfPage: pdfService.PdfPage = pdfDocument.getPage(0);
  let graphs: Array<pdfService.GraphicsObject> = pdfPage.getGraphicsObjects();
  if (graphs.length > 0) {
    pdfPage.deleteGraphicsObject(graphs\[0\]);
  }
}
pdfDocument.releaseDocument();

#### \[h2\]release

release(): void

Release the loaded PDF page.

**System capability**: SystemCapability.OfficeService.PDFService.Core

**Start version**: 5.0.0(12)

**Example**:

import { pdfService } from '@kit.PDFKit';

let tempFilePath = '/data/storage/el2/base/temp/test.pdf';
let pdfDocument = new pdfService.PdfDocument();
let loadResult = pdfDocument.loadDocument(tempFilePath, '');
if(pdfService.ParseResult.PARSE\_SUCCESS === loadResult) {
  let pdfPage: pdfService.PdfPage = pdfDocument.getPage(0);
  pdfPage.release();
}

#### \[h2\]getAreaPixelMapWithOptions

getAreaPixelMapWithOptions(matrix:PdfMatrix,bitmapwidth:mumber,bitmapHeight:number,options?:PixelOptions):image.PixelMap

Obtains the PixelMap image of the current PDF page.

**System capability**: SystemCapability.OfficeService.PDFService.Core

**Start version**: 5.1.0(18)

**Parameters:**

| 
**Parameter**

 | 

**Type**

 | 

**Mandatory**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- |
| 

matrix

 | 

[PdfMatrix](#section113572873718)

 | 

Yes

 | 

Coordinate transformation matrix, which is used to scale, translate, and rotate page content during rendering.

 |
| 

bitmapwidth

 | 

number

 | 

Yes

 | 

Image width, in points (one inch equals 72 points). The value must be greater than **0**.

 |
| 

bitmapHeight

 | 

number

 | 

Yes

 | 

Image height, in points (one inch equals 72 points). The value must be greater than **0**.

 |
| 

options

 | 

[PixelOptions](#section820410147548)

 | 

No

 | 

Parameter for converting a PDF page to an image.

 |

**Returns**:

| 
**Type**

 | 

**Description**

 |
| :-- | :-- |
| 

[image.PixelMap](../../../../media/image-kit/arkts-apis/ohos-multimedia-image-image-processing/interface-pixelmap/document.md)

 | 

PixelMap image of the current page.

 |

**Example**:

import { pdfService } from '@kit.PDFKit';
import { image } from '@kit.ImageKit';

let tempFilePath = '/data/storage/el2/base/temp/test.pdf';
let pdfDocument = new pdfService.PdfDocument();
let loadResult = pdfDocument.loadDocument(tempFilePath, '');
if(pdfService.ParseResult.PARSE\_SUCCESS === loadResult) {
  let pdfPage: pdfService.PdfPage = pdfDocument.getPage(0);
  let pdfMatrix: pdfService.PdfMatrix = new pdfService.PdfMatrix();
  pdfMatrix.x = 0;
  pdfMatrix.y = 0;
  pdfMatrix.width = pdfPage.getWidth();
  pdfMatrix.height = pdfPage.getHeight();
  pdfMatrix.rotate = 0;
  let options: pdfService.PixelOptions = new pdfService.PixelOptions();
  options.isGray = false;
  options.drawAnnotations = true;
  options.isTransparent = false;
  let pixelMap: image.PixelMap = pdfPage.getAreaPixelMapWithOptions(pdfMatrix, 200, 300, options);
}

#### GraphicsObject

Graphics object type.

**System capability**: SystemCapability.OfficeService.PDFService.Core

**Start version**: 5.0.0(12)

| 
**Name**

 | 

**Type**

 | 

**Read-Only**

 | 

**Optional**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- | :-- |
| 

type

 | 

[GraphicsObjectType](#section1083715225311)

 | 

No

 | 

No

 | 

Type of the current graphics object, which is an enum.

 |
| 

x

 | 

number

 | 

No

 | 

No

 | 

Left margin of the current graphics object, in points (one inch equals 72 points). The value must be greater than or equal to **0**.

 |
| 

y

 | 

number

 | 

No

 | 

No

 | 

Bottom margin of the current graphics object, in points (one inch equals 72 points). The value must be greater than or equal to **0**.

 |
| 

clipRect

 | 

[PdfRect](#section19829174815360)

 | 

No

 | 

No

 | 

Clip rectangle information.

 |
| 

strokeColor

 | 

number

 | 

No

 | 

No

 | 

Stroke color (RGB). The value ranges from **0x000000** to **0xFFFFFF**.

 |
| 

strokeOpacity

 | 

number

 | 

No

 | 

No

 | 

Stroke opacity. The value ranges from **0** to **1**.

 |
| 

fillColor

 | 

number

 | 

No

 | 

No

 | 

Fill color (RGB). The value ranges from **0x000000** to **0xFFFFFF**.

 |
| 

fillOpacity

 | 

number

 | 

No

 | 

No

 | 

Fill opacity. The value ranges from **0** to **1**.

 |
| 

rotate

 | 

number

 | 

No

 | 

No

 | 

Rotation angle of the current graphics.

 |

#### TextObject

Text object type, which is inherited from [GraphicsObject](#section1251812324215).

**System capability**: SystemCapability.OfficeService.PDFService.Core

**Start version**: 5.0.0(12)

| 
**Name**

 | 

**Type**

 | 

**Read-Only**

 | 

**Optional**

 | 

**Description**

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

Text.

 |
| 

fontInfo

 | 

[FontInfo](#section6845112510495)

 | 

No

 | 

No

 | 

Font information.

 |
| 

textSize

 | 

number

 | 

No

 | 

No

 | 

Font size, in points (one inch equals 72 points). The value must be greater than **0**.

 |
| 

charspace

 | 

number

 | 

No

 | 

No

 | 

Character spacing, in points (one inch equals 72 points). The value must be greater than or equal to **0**.

 |
| 

wordspace

 | 

number

 | 

No

 | 

No

 | 

Word spacing, in points (one inch equals 72 points). The value must be greater than or equal to **0**.

 |
| 

charRects

 | 

Array<[PdfRect](#section19829174815360)\>

 | 

No

 | 

No

 | 

Character area.

 |
| 

charUnicodes

 | 

Array<number>

 | 

No

 | 

No

 | 

Character Unicode.

 |

#### ImageObject

Image object type, which is inherited from [GraphicsObject](#section1251812324215).

**System capability**: SystemCapability.OfficeService.PDFService.Core

**Start version**: 5.0.0(12)

| 
**Name**

 | 

**Type**

 | 

**Read-Only**

 | 

**Optional**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- | :-- |
| 

pixelMap

 | 

[image.PixelMap](../../../../media/image-kit/arkts-apis/ohos-multimedia-image-image-processing/interface-pixelmap/document.md)

 | 

No

 | 

No

 | 

A special syntax is used to represent small image data directly within the content stream.

 |
| 

width

 | 

number

 | 

No

 | 

No

 | 

Image width, in points (one inch equals 72 points). The value must be greater than **0**.

 |
| 

height

 | 

number

 | 

No

 | 

No

 | 

Image height, in points (one inch equals 72 points). The value must be greater than **0**.

 |

#### Bookmark

Methods related to the bookmark object.

**System capability**: SystemCapability.OfficeService.PDFService.Core

**Start version**: 5.0.0(12)

#### \[h2\]isRootBookmark

isRootBookmark(): boolean

Checks whether a bookmark is a root bookmark.

**System capability**: SystemCapability.OfficeService.PDFService.Core

**Start version**: 5.0.0(12)

**Returns**:

| 
**Type**

 | 

**Description**

 |
| :-- | :-- |
| 

boolean

 | 

If a bookmark is a root bookmark, **true** is returned. Otherwise, **false** is returned.

 |

**Example**:

import { pdfService } from '@kit.PDFKit';

let tempFilePath = '/data/storage/el2/base/temp/test.pdf';
let pdfDocument = new pdfService.PdfDocument();
let loadResult = pdfDocument.loadDocument(tempFilePath, '');
if(pdfService.ParseResult.PARSE\_SUCCESS === loadResult) {
  let mark1: pdfService.Bookmark = pdfDocument.createBookmark();
  let mark2: pdfService.Bookmark = pdfDocument.createBookmark();
  pdfDocument.insertBookmark(mark1, null, 1);
  pdfDocument.insertBookmark(mark2, mark1, 1);
  let isRootBookmark = mark1.isRootBookmark();
}

#### \[h2\]getParent

getParent(): Bookmark

Obtains information about the parent bookmark.

**System capability**: SystemCapability.OfficeService.PDFService.Core

**Start version**: 5.0.0(12)

**Returns**:

| 
**Type**

 | 

**Description**

 |
| :-- | :-- |
| 

[Bookmark](#section1435010204319)

 | 

Parent bookmark.

 |

**Example**:

import { pdfService } from '@kit.PDFKit';

let tempFilePath = '/data/storage/el2/base/temp/test.pdf';
let pdfDocument = new pdfService.PdfDocument();
let loadResult = pdfDocument.loadDocument(tempFilePath, '');
if(pdfService.ParseResult.PARSE\_SUCCESS === loadResult) {
  let mark1: pdfService.Bookmark = pdfDocument.createBookmark();
  let mark2: pdfService.Bookmark = pdfDocument.createBookmark();
  pdfDocument.insertBookmark(mark1, null, 1);
  pdfDocument.insertBookmark(mark2, mark1, 1);
  let parentBookmark = mark2.getParent();
}

#### \[h2\]hasChild

hasChild(): boolean

Checks whether there is a child bookmark.

**System capability**: SystemCapability.OfficeService.PDFService.Core

**Start version**: 5.0.0(12)

**Returns**:

| 
**Type**

 | 

**Description**

 |
| :-- | :-- |
| 

boolean

 | 

If there is a child bookmark, **true** is returned. Otherwise, **false** is returned.

 |

**Example**:

import { pdfService } from '@kit.PDFKit';

let tempFilePath = '/data/storage/el2/base/temp/test.pdf';
let pdfDocument = new pdfService.PdfDocument();
let loadResult = pdfDocument.loadDocument(tempFilePath, '');
if(pdfService.ParseResult.PARSE\_SUCCESS === loadResult) {
  let mark1: pdfService.Bookmark = pdfDocument.createBookmark();
  let mark2: pdfService.Bookmark = pdfDocument.createBookmark();
  pdfDocument.insertBookmark(mark1, null, 1);
  pdfDocument.insertBookmark(mark2, mark1, 1);
  let hasChildBookmark = mark1.hasChild();
}

#### \[h2\]getChildren

getChildren(): Array<Bookmark>

Obtains the child bookmark list.

**System capability**: SystemCapability.OfficeService.PDFService.Core

**Start version**: 5.0.0(12)

**Returns**:

| 
**Type**

 | 

**Description**

 |
| :-- | :-- |
| 

Array<[Bookmark](#section1435010204319)\>

 | 

Child bookmark list.

 |

**Example**:

import { pdfService } from '@kit.PDFKit';

let tempFilePath = '/data/storage/el2/base/temp/test.pdf';
let pdfDocument = new pdfService.PdfDocument();
let loadResult = pdfDocument.loadDocument(tempFilePath, '');
if(pdfService.ParseResult.PARSE\_SUCCESS === loadResult) {
  let mark1: pdfService.Bookmark = pdfDocument.createBookmark();
  let mark2: pdfService.Bookmark = pdfDocument.createBookmark();
  pdfDocument.insertBookmark(mark1, null, 1);
  pdfDocument.insertBookmark(mark2, mark1, 1);
  let childBookmark = mark1.getChildren();
}

#### \[h2\]getDestInfo

getDestInfo(): DestInfo

Obtains the bookmark redirection destination information.

**System capability**: SystemCapability.OfficeService.PDFService.Core

**Start version**: 5.0.0(12)

**Returns**:

| 
**Type**

 | 

**Description**

 |
| :-- | :-- |
| 

[DestInfo](#section1531112425499)

 | 

Bookmark redirection information.

 |

**Example**:

import { pdfService } from '@kit.PDFKit';

let tempFilePath = '/data/storage/el2/base/temp/test.pdf';
let pdfDocument = new pdfService.PdfDocument();
let loadResult = pdfDocument.loadDocument(tempFilePath, '');
if(pdfService.ParseResult.PARSE\_SUCCESS === loadResult) {
  let mark1: pdfService.Bookmark = pdfDocument.createBookmark();
  let mark2: pdfService.Bookmark = pdfDocument.createBookmark();
  pdfDocument.insertBookmark(mark1, null, 1);
  pdfDocument.insertBookmark(mark2, mark1, 1);
  let destInfo: pdfService.DestInfo = mark1.getDestInfo();
  destInfo.fitMode = pdfService.FitMode.FIT\_MODE\_XYZ;
  destInfo.pageIndex = 1;
  destInfo.left = 20;
  destInfo.top = 30;
  destInfo.zoom = 1.5;
  mark1.setDestInfo(destInfo);
  let bookInfo: pdfService.BookmarkInfo = mark1.getBookmarkInfo();
  bookInfo.title = "hh";
  bookInfo.titleColor = 12;
  bookInfo.isBold = true;
  bookInfo.isItalic = true;
  mark1.setBookmarkInfo(bookInfo);
}

#### \[h2\]setDestInfo

setDestInfo(info: DestInfo): void

Sets the bookmark redirection information.

**System capability**: SystemCapability.OfficeService.PDFService.Core

**Start version**: 5.0.0(12)

**Parameters:**

| 
**Parameter**

 | 

**Type**

 | 

**Mandatory**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- |
| 

info

 | 

[DestInfo](#section1531112425499)

 | 

Yes

 | 

Bookmark redirection information.

 |

**Example**:

import { pdfService } from '@kit.PDFKit';

let tempFilePath = '/data/storage/el2/base/temp/test.pdf';
let pdfDocument = new pdfService.PdfDocument();
let loadResult = pdfDocument.loadDocument(tempFilePath, '');
if(pdfService.ParseResult.PARSE\_SUCCESS === loadResult) {
  let mark1: pdfService.Bookmark = pdfDocument.createBookmark();
  let mark2: pdfService.Bookmark = pdfDocument.createBookmark();
  pdfDocument.insertBookmark(mark1, null, 1);
  pdfDocument.insertBookmark(mark2, mark1, 1);
  let destInfo: pdfService.DestInfo = mark1.getDestInfo();
  destInfo.fitMode = pdfService.FitMode.FIT\_MODE\_XYZ;
  destInfo.pageIndex = 1;
  destInfo.left = 20;
  destInfo.top = 30;
  destInfo.zoom = 1.5;
  mark1.setDestInfo(destInfo);
  let bookInfo: pdfService.BookmarkInfo = mark1.getBookmarkInfo();
  bookInfo.title = "hh";
  bookInfo.titleColor = 12;
  bookInfo.isBold = true;
  bookInfo.isItalic = true;
  mark1.setBookmarkInfo(bookInfo);
}

#### \[h2\]getBookmarkInfo

getBookmarkInfo(): BookmarkInfo

Obtains bookmark information.

**System capability**: SystemCapability.OfficeService.PDFService.Core

**Start version**: 5.0.0(12)

**Returns**:

| 
**Type**

 | 

**Description**

 |
| :-- | :-- |
| 

[BookmarkInfo](#section10885185510474)

 | 

Bookmark information.

 |

**Example**:

import { pdfService } from '@kit.PDFKit';

let tempFilePath = '/data/storage/el2/base/temp/test.pdf';
let pdfDocument = new pdfService.PdfDocument();
let loadResult = pdfDocument.loadDocument(tempFilePath, '');
if(pdfService.ParseResult.PARSE\_SUCCESS === loadResult) {
  let mark1: pdfService.Bookmark = pdfDocument.createBookmark();
  let mark2: pdfService.Bookmark = pdfDocument.createBookmark();
  pdfDocument.insertBookmark(mark1, null, 1);
  pdfDocument.insertBookmark(mark2, mark1, 1);
  let destInfo: pdfService.DestInfo = mark1.getDestInfo();
  destInfo.fitMode = pdfService.FitMode.FIT\_MODE\_XYZ;
  destInfo.pageIndex = 1;
  destInfo.left = 20;
  destInfo.top = 30;
  destInfo.zoom = 1.5;
  mark1.setDestInfo(destInfo);
  let bookInfo: pdfService.BookmarkInfo = mark1.getBookmarkInfo();
  bookInfo.title = "hh";
  bookInfo.titleColor = 12;
  bookInfo.isBold = true;
  bookInfo.isItalic = true;
  mark1.setBookmarkInfo(bookInfo);
}

#### \[h2\]setBookmarkInfo

setBookmarkInfo(info: BookmarkInfo): void

Sets bookmark information.

**System capability**: SystemCapability.OfficeService.PDFService.Core

**Start version**: 5.0.0(12)

**Parameters:**

| 
**Parameter**

 | 

**Type**

 | 

**Mandatory**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- |
| 

info

 | 

[BookmarkInfo](#section10885185510474)

 | 

Yes

 | 

Bookmark information.

 |

**Example**:

import { pdfService } from '@kit.PDFKit';

let tempFilePath = '/data/storage/el2/base/temp/test.pdf';
let pdfDocument = new pdfService.PdfDocument();
let loadResult = pdfDocument.loadDocument(tempFilePath, '');
if(pdfService.ParseResult.PARSE\_SUCCESS === loadResult) {
  let mark1: pdfService.Bookmark = pdfDocument.createBookmark();
  let mark2: pdfService.Bookmark = pdfDocument.createBookmark();
  pdfDocument.insertBookmark(mark1, null, 1);
  pdfDocument.insertBookmark(mark2, mark1, 1);
  let destInfo: pdfService.DestInfo = mark1.getDestInfo();
  destInfo.fitMode = pdfService.FitMode.FIT\_MODE\_XYZ;
  destInfo.pageIndex = 1;
  destInfo.left = 20;
  destInfo.top = 30;
  destInfo.zoom = 1.5;
  mark1.setDestInfo(destInfo);
  let bookInfo: pdfService.BookmarkInfo = mark1.getBookmarkInfo();
  bookInfo.title = "hh";
  bookInfo.titleColor = 12;
  bookInfo.isBold = true;
  bookInfo.isItalic = true;
  mark1.setBookmarkInfo(bookInfo);
}

#### BookmarkInfo

Attributes related to the bookmark class.

**System capability**: SystemCapability.OfficeService.PDFService.Core

**Start version**: 5.0.0(12)

## Attributes

| 
**Name**

 | 

**Type**

 | 

**Read-Only**

 | 

**Optional**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- | :-- |
| 

title

 | 

string

 | 

No

 | 

No

 | 

A special syntax is used to represent small image data directly within the content stream.

 |
| 

titleColor

 | 

number

 | 

No

 | 

Yes

 | 

Title color. The value ranges from **0x000000** to **0xFFFFFF**. The default value is **0x000000**.

(For example, **0xFF0000** indicates blue, and **0x0000FF** indicates red.)

 |
| 

isBold

 | 

boolean

 | 

No

 | 

Yes

 | 

Indicates whether the title is in bold (**true**) or not (**false**).

The default value is **false**.

 |
| 

isItalic

 | 

boolean

 | 

No

 | 

Yes

 | 

Indicates whether the title is in italics (**true**) or not (**false**). The default value is **false**.

 |

#### \[h2\]constructor

constructor()

Creates a bookmark object.

**System capability**: SystemCapability.OfficeService.PDFService.Core

**Start version**: 5.0.0(12)

#### HeaderFooterInfo

Attributes related to the header and footer class.

**System capability**: SystemCapability.OfficeService.PDFService.Core

**Start version**: 5.0.0(12)

## Attributes

| 
**Name**

 | 

**Type**

 | 

**Read-Only**

 | 

**Optional**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- | :-- |
| 

fontInfo

 | 

[FontInfo](#section6845112510495)

 | 

No

 | 

No

 | 

Font information.

 |
| 

textSize

 | 

number

 | 

No

 | 

No

 | 

Text size of the header and footer, in points (one inch equals 72 points). The value must be greater than **0**.

 |
| 

charset

 | 

[CharsetType](#section415817717544)

 | 

No

 | 

No

 | 

Character set.

 |
| 

underline

 | 

boolean

 | 

No

 | 

No

 | 

Indicates whether to add underlines (**true**) or not (**false**).

 |
| 

textColor

 | 

number

 | 

No

 | 

No

 | 

Text color. The value ranges from **0x000000** to **0xFFFFFF**.

(For example, **0xFF0000** indicates blue, and **0x0000FF** indicates red.)

 |
| 

leftMargin

 | 

number

 | 

No

 | 

No

 | 

Left margin of the header and footer, in points (one inch equals 72 points). The value must be greater than or equal to **0**.

 |
| 

topMargin

 | 

number

 | 

No

 | 

No

 | 

Top margin of the header and footer, in points (one inch equals 72 points). The value must be greater than or equal to **0**.

 |
| 

rightMargin

 | 

number

 | 

No

 | 

No

 | 

Right margin of the header and footer, in points (one inch equals 72 points). The value must be greater than or equal to **0**.

 |
| 

bottomMargin

 | 

number

 | 

No

 | 

No

 | 

Bottom margin of the header and footer, in points (one inch equals 72 points). The value must be greater than or equal to **0**.

 |
| 

headerLeftText

 | 

string

 | 

No

 | 

No

 | 

Text on the left of the header.

 |
| 

headerCenterText

 | 

string

 | 

No

 | 

No

 | 

Text in the center of the header.

 |
| 

headerRightText

 | 

string

 | 

No

 | 

No

 | 

Text on the right of the header.

 |
| 

footerLeftText

 | 

string

 | 

No

 | 

No

 | 

Text on the left of the footer.

 |
| 

footerCenterText

 | 

string

 | 

No

 | 

No

 | 

Text in the center of the footer.

 |
| 

footerRightText

 | 

string

 | 

No

 | 

No

 | 

Text on the right of the footer.

 |

#### \[h2\]constructor

constructor()

Creates a header and footer object.

**System capability**: SystemCapability.OfficeService.PDFService.Core

**Start version**: 5.0.0(12)

#### WatermarkInfo

Attributes related to the watermark class, a parent class.

**System capability**: SystemCapability.OfficeService.PDFService.Core

**Start version**: 5.0.0(12)

## Attributes

| 
**Name**

 | 

**Type**

 | 

**Read-Only**

 | 

**Optional**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- | :-- |
| 

watermarkType

 | 

[WatermarkType](#section990936155517)

 | 

No

 | 

No

 | 

Watermark type.

 |
| 

isOnTop

 | 

boolean

 | 

No

 | 

No

 | 

Indicates whether the background is pinned on top (**true**) or not (**false**).

 |
| 

scale

 | 

number

 | 

No

 | 

No

 | 

Scale. The value must be greater than **0** and less than or equal to **5**.

 |
| 

rotation

 | 

number

 | 

No

 | 

No

 | 

Rotation.

 |
| 

opacity

 | 

number

 | 

No

 | 

No

 | 

Opacity. The value ranges from **0** to **1**.

 |
| 

horizontalAlignment

 | 

[WatermarkAlignment](#section76861950135416)

 | 

No

 | 

No

 | 

Horizontal alignment.

 |
| 

horizontalSpace

 | 

number

 | 

No

 | 

No

 | 

Horizontal spacing. The value must be greater than or equal to **0**.

 |
| 

verticalAlignment

 | 

[WatermarkAlignment](#section76861950135416)

 | 

No

 | 

No

 | 

Vertical alignment.

 |
| 

verticalSpace

 | 

number

 | 

No

 | 

No

 | 

Vertical spacing. The value must be greater than or equal to **0**.

 |

#### \[h2\]constructor

constructor()

Creates a watermark object.

**System capability**: SystemCapability.OfficeService.PDFService.Core

**Start version**: 5.0.0(12)

#### TextWatermarkInfo

Attributes related to the text watermark class, which are inherited from [WatermarkInfo](#section4749820144811).

**System capability**: SystemCapability.OfficeService.PDFService.Core

**Start version**: 5.0.0(12)

| 
**Name**

 | 

**Type**

 | 

**Read-Only**

 | 

**Optional**

 | 

**Description**

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

Text watermark.

 |
| 

fontInfo

 | 

[FontInfo](#section6845112510495)

 | 

No

 | 

No

 | 

Font information.

 |
| 

textSize

 | 

number

 | 

No

 | 

No

 | 

Text size. The value must be greater than **0**.

 |
| 

textColor

 | 

number

 | 

No

 | 

No

 | 

Text color. The value ranges from **0x000000** to **0xFFFFFF**.

(For example, **0xFF0000** indicates blue, and **0x0000FF** indicates red.)

 |

#### ImageWatermarkInfo

Attributes related to the image watermark class, which are inherited from [WatermarkInfo](#section4749820144811).

**System capability**: SystemCapability.OfficeService.PDFService.Core

**Start version**: 5.0.0(12)

| 
**Name**

 | 

**Type**

 | 

**Read-Only**

 | 

**Optional**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- | :-- |
| 

imagePath

 | 

string

 | 

No

 | 

No

 | 

Image path.

 |

#### BackgroundInfo

Attributes related to the background class.

**System capability**: SystemCapability.OfficeService.PDFService.Core

**Start version**: 5.0.0(12)

## Attributes

| 
**Name**

 | 

**Type**

 | 

**Read-Only**

 | 

**Optional**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- | :-- |
| 

imagePath

 | 

string

 | 

No

 | 

No

 | 

Image path. (If the image path is left blank, the background color is mandatory.)

 |
| 

backgroundColor

 | 

number

 | 

No

 | 

No

 | 

Background color. (If the background color is left blank, the image path is mandatory.)

The value ranges from **0x000000** to **0xFFFFFF**.

(For example, **0xFF0000** indicates blue, and **0x0000FF** indicates red.)

 |
| 

isOnTop

 | 

boolean

 | 

No

 | 

No

 | 

Indicates whether the background is pinned on top (**true**) or not (**false**).

 |
| 

scale

 | 

number

 | 

No

 | 

No

 | 

Scale. The value must be greater than **0** and less than or equal to **5**.

 |
| 

rotation

 | 

number

 | 

No

 | 

No

 | 

Rotation.

 |
| 

opacity

 | 

number

 | 

No

 | 

No

 | 

Opacity. The value ranges from **0** to **1**.

 |
| 

horizontalAlignment

 | 

[BackgroundAlignment](#section4661112045519)

 | 

No

 | 

No

 | 

Horizontal alignment.

 |
| 

horizontalSpace

 | 

number

 | 

No

 | 

No

 | 

Horizontal spacing, in inches (one inch equals 72 points). The value must be greater than or equal to **0**.

 |
| 

verticalAlignment

 | 

[BackgroundAlignment](#section4661112045519)

 | 

No

 | 

No

 | 

Vertical alignment.

 |
| 

verticalSpace

 | 

number

 | 

No

 | 

No

 | 

Vertical spacing, in inches (one inch equals 72 points). The value must be greater than or equal to **0**.

 |

#### \[h2\]constructor

constructor()

Creates a background object.

**System capability**: SystemCapability.OfficeService.PDFService.Core

**Start version**: 5.0.0(12)

#### PdfAction

Annotation link redirection, which is a parent class.

**System capability**: SystemCapability.OfficeService.PDFService.Core

**Start version**: 5.1.0(18)

## Attributes

| 
**Name**

 | 

**Type**

 | 

**Read-Only**

 | 

**Optional**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- | :-- |
| 

type

 | 

[PdfActionType](#section238632825816)

 | 

No

 | 

No

 | 

Annotation link redirection type.

 |

#### \[h2\]constructor

constructor()

Creates an annotation link object.

**System capability**: SystemCapability.OfficeService.PDFService.Core

**Start version**: 5.1.0(18)

#### PdfActionGoTo

Indicates the redirection in the document. It inherits from [PdfAction](#section1136285384812).

**System capability**: SystemCapability.OfficeService.PDFService.Core

**Start version**: 5.1.0(18)

| 
**Name**

 | 

**Type**

 | 

**Read-Only**

 | 

**Optional**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- | :-- |
| 

destInfo

 | 

[DestInfo](#section1531112425499)

 | 

No

 | 

No

 | 

Redirection information.

 |

#### PdfActionHyperlink

Indicates hyperlink redirection. It inherits from [PdfAction](#section1136285384812).

**System capability**: SystemCapability.OfficeService.PDFService.Core

**Start version**: 5.1.0(18)

| 
**Name**

 | 

**Type**

 | 

**Read-Only**

 | 

**Optional**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- | :-- |
| 

hyperlink

 | 

string

 | 

No

 | 

No

 | 

Hyperlink redirection.

 |

#### PixelOptions

Defines the parameters for converting a PDF page to an image.

**System capability**: SystemCapability.OfficeService.PDFService.Core

**Start version**: 5.1.0(18)

## Attributes

| 
**Name**

 | 

**Type**

 | 

**Read-Only**

 | 

**Optional**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- | :-- |
| 

isGray

 | 

boolean

 | 

No

 | 

Yes

 | 

Indicates whether to obtain only the gray image (**true**) or not (**false**).

The default value is **true**.

 |
| 

drawAnnotations

 | 

boolean

 | 

No

 | 

Yes

 | 

Indicates whether to add annotations in the image (**true**) or not (**false**).

The default value is **true**.

 |
| 

isTransparent

 | 

boolean

 | 

No

 | 

Yes

 | 

Indicates whether to obtain the transparent image (**true**) or not (**false**).

The default value is **false**.

 |

#### \[h2\]constructor

constructor()

Creates an image parameter option object.

**System capability**: SystemCapability.OfficeService.PDFService.Core

**Start version**: 5.1.0(18)

#### FontInfo

Font class.

**System capability**: SystemCapability.OfficeService.PDFService.Core

**Start version**: 5.0.0(12)

## Attributes

| 
**Name**

 | 

**Type**

 | 

**Read-Only**

 | 

**Optional**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- | :-- |
| 

fontPath

 | 

string

 | 

No

 | 

Yes

 | 

Font path.

 |
| 

fontName

 | 

string

 | 

No

 | 

Yes

 | 

Font name.

 |

#### \[h2\]constructor

constructor()

Creates a font class.

**System capability**: SystemCapability.OfficeService.PDFService.Core

**Start version**: 5.0.0(12)

#### DestInfo

Bookmark redirection information.

**System capability**: SystemCapability.OfficeService.PDFService.Core

**Start version**: 5.0.0(12)

## Attributes

| 
**Name**

 | 

**Type**

 | 

**Read-Only**

 | 

**Optional**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- | :-- |
| 

fitMode

 | 

[FitMode](#section103491426145411)

 | 

No

 | 

No

 | 

Fit mode of the destination page.

 |
| 

pageIndex

 | 

number

 | 

No

 | 

No

 | 

Page index. The value must be greater than or equal to **0** and less than the total page count. The value **0** indicates the start page.

 |
| 

left

 | 

number

 | 

No

 | 

Yes

 | 

Left spacing, in points (one inch equals 72 points). The value must be greater than or equal to **0**. The default value is **0**.

 |
| 

top

 | 

number

 | 

No

 | 

Yes

 | 

Top spacing, in points (one inch equals 72 points). The value must be greater than or equal to **0**. The default value is **0**.

 |
| 

right

 | 

number

 | 

No

 | 

Yes

 | 

Right spacing, in points (one inch equals 72 points). The value must be greater than or equal to **0**. The default value is **0**.

 |
| 

bottom

 | 

number

 | 

No

 | 

Yes

 | 

Bottom spacing, in points (one inch equals 72 points). The value must be greater than or equal to **0**. The default value is **0**.

 |
| 

zoom

 | 

number

 | 

No

 | 

Yes

 | 

Scale. The value must be greater than **0** and less than or equal to **5**. The default value is **1**.

 |

#### \[h2\]constructor

constructor()

Creates a bookmark redirection object.

**System capability**: SystemCapability.OfficeService.PDFService.Core

**Start version**: 5.0.0(12)

#### TextStyle

Text style.

**System capability**: SystemCapability.OfficeService.PDFService.Core

**Start version**: 5.0.0(12)

| 
**Name**

 | 

**Type**

 | 

**Read-Only**

 | 

**Optional**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- | :-- |
| 

fontInfo

 | 

[FontInfo](#section6845112510495)

 | 

No

 | 

Yes

 | 

Font information. The default font is HarmonyOS\_Sans.

 |
| 

textSize

 | 

number

 | 

No

 | 

Yes

 | 

Font size. The value must be greater than **0**. The default value is **20**.

 |
| 

textColor

 | 

number

 | 

No

 | 

Yes

 | 

Font color. The value ranges from **0x000000** to **0xFFFFFF**. The default value is **0x000000**.

(For example, **0xFF0000** indicates blue, and **0x0000FF** indicates red.)

 |
| 

isBold

 | 

boolean

 | 

No

 | 

Yes

 | 

Indicates whether the text is in bold (**true**) or not (**false**). The default value is **false**.

 |
| 

isItalic

 | 

boolean

 | 

No

 | 

Yes

 | 

Indicates whether the text is in italics (**true**) or not (**false**). The default value is **false**.

 |
| 

isUnderline

 | 

boolean

 | 

No

 | 

Yes

 | 

Indicates whether there is an underline (**true**) or not (**false**). The default value is **false**.

 |
| 

isStrikethrough

 | 

boolean

 | 

No

 | 

Yes

 | 

Indicates whether there is a strikethrough (**true**) or not (**false**). The default value is **false**.

 |

#### BorderStyle

Border enum.

**System capability**: SystemCapability.OfficeService.PDFService.Core

**Start version**: 5.0.0(12)

| 
**Name**

 | 

**Value**

 | 

**Description**

 |
| :-- | :-- | :-- |
| 

NONE

 | 

0

 | 

No border.

 |
| 

SOLID

 | 

1

 | 

Solid border.

 |
| 

BEVELED

 | 

2

 | 

Beveled border.

 |
| 

INSET

 | 

3

 | 

Inserted border.

 |
| 

UNDERLINE

 | 

4

 | 

Underline border.

 |
| 

DASH

 | 

5

 | 

Dashed border.

 |

#### AnnotationFlag

Annotation flag enum.

**System capability**: SystemCapability.OfficeService.PDFService.Core

**Start version**: 5.0.0(12)

| 
**Name**

 | 

**Value**

 | 

**Description**

 |
| :-- | :-- | :-- |
| 

INVISIBLE

 | 

1

 | 

Invisible.

 |
| 

HIDDEN

 | 

2

 | 

Hidden.

 |
| 

PRINTED

 | 

4

 | 

Printed.

 |

#### TextAnnotationState

Text annotation status enum.

**System capability**: SystemCapability.OfficeService.PDFService.Core

**Start version**: 5.0.0(12)

| 
**Name**

 | 

**Value**

 | 

**Description**

 |
| :-- | :-- | :-- |
| 

UNMARKED

 | 

0

 | 

Marked by users.

 |
| 

MARKED

 | 

1

 | 

Not marked by users (default value).

 |

#### HighlightMode

Text highlight mode enum.

**System capability**: SystemCapability.OfficeService.PDFService.Core

**Start version**: 5.0.0(12)

| 
**Name**

 | 

**Value**

 | 

**Description**

 |
| :-- | :-- | :-- |
| 

HIGHLIGHT\_INVERT

 | 

1

 | 

Contents of accessories annotations.

 |
| 

HIGHLIGHT\_OUTLINE

 | 

2

 | 

Inverts annotation borders.

 |
| 

HIGHLIGHT\_PUSH

 | 

3

 | 

Pressed appearance for displaying annotations.

 |
| 

HIGHLIGHT\_TOGGLE

 | 

4

 | 

Toggle, only useful for widget annotations.

 |

#### AlignmentType

Text alignment type enum.

**System capability**: SystemCapability.OfficeService.PDFService.Core

**Start version**: 5.0.0(12)

| 
**Name**

 | 

**Value**

 | 

**Description**

 |
| :-- | :-- | :-- |
| 

LEFT

 | 

0

 | 

Distance to the left edge of the page.

 |
| 

MIDDLE

 | 

1

 | 

Distance to the center line of the page.

 |
| 

RIGHT

 | 

2

 | 

Distance to the right edge of the page.

 |

#### LineEndStyle

End point line style enum.

**System capability**: SystemCapability.OfficeService.PDFService.Core

**Start version**: 5.0.0(12)

| 
**Name**

 | 

**Value**

 | 

**Description**

 |
| :-- | :-- | :-- |
| 

STYLE\_NONE

 | 

0

 | 

Default style.

 |
| 

STYLE\_SQUARE

 | 

1

 | 

Square style.

 |
| 

STYLE\_CIRCLE

 | 

2

 | 

Circle style.

 |
| 

STYLE\_DIAMOND

 | 

3

 | 

Diamond style.

 |
| 

STYLE\_OPEN\_ARROW

 | 

4

 | 

Open arrow style.

 |
| 

STYLE\_CLOSED\_ARROW

 | 

5

 | 

Closed arrow style.

 |
| 

STYLE\_BUTT

 | 

6

 | 

Butt style.

 |
| 

STYLE\_R\_OPEN\_ARROW

 | 

7

 | 

Right open arrow style.

 |
| 

STYLE\_R\_CLOSED\_ARROW

 | 

8

 | 

Right closed arrow style.

 |
| 

STYLE\_SLASH

 | 

9

 | 

Slash style.

 |

#### ParseResult

Parse result enum.

**System capability**: SystemCapability.OfficeService.PDFService.Core

**Start version**: 5.0.0(12)

| 
**Name**

 | 

**Value**

 | 

**Description**

 |
| :-- | :-- | :-- |
| 

PARSE\_SUCCESS

 | 

0

 | 

Parsed successfully.

 |
| 

PARSE\_ERROR\_FILE

 | 

1

 | 

Invalid file.

 |
| 

PARSE\_ERROR\_FORMAT

 | 

2

 | 

Incorrect format.

 |
| 

PARSE\_ERROR\_PASSWORD

 | 

3

 | 

Password error.

 |
| 

PARSE\_ERROR\_HANDLER

 | 

4

 | 

An error occurred during program processing.

 |
| 

PARSE\_ERROR\_CERT

 | 

5

 | 

Certificate error.

 |

#### PageLayout

Page layout display mode enum.

**System capability**: SystemCapability.OfficeService.PDFService.Core

**Start version**: 5.0.0(12)

| 
**Name**

 | 

**Value**

 | 

**Description**

 |
| :-- | :-- | :-- |
| 

LAYOUT\_SINGLE

 | 

1

 | 

Single-page.

 |
| 

LAYOUT\_DOUBLE

 | 

2

 | 

Dual-page.

 |

#### PageFit

Page fit mode enum.

**System capability**: SystemCapability.OfficeService.PDFService.Core

**Start version**: 5.0.0(12)

| 
**Name**

 | 

**Value**

 | 

**Description**

 |
| :-- | :-- | :-- |
| 

FIT\_NONE

 | 

0

 | 

Actual size.

 |
| 

FIT\_PAGE

 | 

1

 | 

Zooming in or out by page.

 |
| 

FIT\_WIDTH

 | 

2

 | 

Zooming in or out by width.

 |
| 

FIT\_HEIGHT

 | 

3

 | 

Zooming in or out by height.

 |

#### RotationAngle

Rotation angle enum.

**System capability**: SystemCapability.OfficeService.PDFService.Core

**Start version**: 5.0.0(12)

| 
**Name**

 | 

**Value**

 | 

**Description**

 |
| :-- | :-- | :-- |
| 

ANGLE\_0

 | 

0

 | 

0 degrees.

 |
| 

ANGLE\_90

 | 

90

 | 

90 degrees.

 |
| 

ANGLE\_180

 | 

180

 | 

180 degrees.

 |
| 

ANGLE\_270

 | 

270

 | 

270 degrees.

 |

#### ImageFormat

Image format enum.

**System capability**: SystemCapability.OfficeService.PDFService.Core

**Start version**: 5.0.0(12)

| 
**Name**

 | 

**Value**

 | 

**Description**

 |
| :-- | :-- | :-- |
| 

PNG

 | 

0

 | 

PNG format.

 |
| 

BMP

 | 

1

 | 

BMP format.

 |
| 

JPEG

 | 

2

 | 

JPEG format.

 |

#### AnnotationType

Annotation type enum.

**System capability**: SystemCapability.OfficeService.PDFService.Core

**Start version**: 5.0.0(12)

| 
**Name**

 | 

**Value**

 | 

**Description**

 |
| :-- | :-- | :-- |
| 

UNKNOWN

 | 

0

 | 

Unknown text.

 |
| 

TEXT

 | 

1

 | 

Text.

 |
| 

LINK

 | 

2

 | 

Link.

 |
| 

FREETEXT

 | 

3

 | 

Free text.

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

POLYLINE

 | 

8

 | 

Polyline.

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
| 

STAMP

 | 

13

 | 

Stamp.

 |
| 

INK

 | 

15

 | 

Ink.

 |
| 

POPUP

 | 

16

 | 

Pop-up.

 |

#### BoxType

Page box enum.

**System capability**: SystemCapability.OfficeService.PDFService.Core

**Start version**: 5.0.0(12)

| 
**Name**

 | 

**Value**

 | 

**Description**

 |
| :-- | :-- | :-- |
| 

BOX\_MEDIA

 | 

0

 | 

Specifies the boundary of the physical medium for displaying or printing the page.

 |
| 

BOX\_CROP

 | 

1

 | 

Specifies the visible area in the default user space.

 |
| 

BOX\_BLEED

 | 

2

 | 

Specifies the area to which the page content should be cropped during output in the production environment.

 |
| 

BOX\_TRIM

 | 

3

 | 

Expected dimensions of the trimmed page.

 |
| 

BOX\_ART

 | 

4

 | 

Specifies the scope of meaningful content on the page that the page creator wants.

 |

#### GraphicsObjectType

Graphics object type enum.

**System capability**: SystemCapability.OfficeService.PDFService.Core

**Start version**: 5.0.0(12)

| 
**Name**

 | 

**Value**

 | 

**Description**

 |
| :-- | :-- | :-- |
| 

OBJECT\_TEXT

 | 

1

 | 

Text.

 |
| 

OBJECT\_PATH

 | 

2

 | 

Path.

 |
| 

OBJECT\_IMAGE

 | 

3

 | 

Image.

 |
| 

OBJECT\_SHADING

 | 

4

 | 

Shading.

 |
| 

OBJECT\_FORM

 | 

5

 | 

Form.

 |

#### CharsetType

Character set object type enum.

**System capability**: SystemCapability.OfficeService.PDFService.Core

**Start version**: 5.0.0(12)

| 
**Name**

 | 

**Value**

 | 

**Description**

 |
| :-- | :-- | :-- |
| 

PDF\_FONT\_CID\_FONT\_CHARSET

 | 

0x100000

 | 

CID.

 |
| 

PDF\_FONT\_ANSI\_CHARSET

 | 

0

 | 

ANSI.

 |
| 

PDF\_FONT\_DEFAULT\_CHARSET

 | 

1

 | 

Default.

 |
| 

PDF\_FONT\_SYMBOL\_CHARSET

 | 

2

 | 

Symbol.

 |
| 

PDF\_FONT\_SHIFT\_JIS\_CHARSET

 | 

128

 | 

Shift JIS.

 |
| 

PDF\_FONT\_HANGUL\_CHARSET

 | 

129

 | 

Hangul.

 |
| 

PDF\_FONT\_GB2312\_CHARSET

 | 

134

 | 

GB2312.

 |
| 

PDF\_FONT\_CHINESE\_BIG5\_CHARSET

 | 

136

 | 

Chinese BIG5.

 |
| 

PDF\_FONT\_THAI\_CHARSET

 | 

222

 | 

Thai.

 |
| 

PDF\_FONT\_EAST\_EUROPE\_CHARSET

 | 

238

 | 

East Europe.

 |
| 

PDF\_FONT\_RUSSIAN\_CHARSET

 | 

204

 | 

Russian.

 |
| 

PDF\_FONT\_GREEK\_CHARSET

 | 

161

 | 

Greek.

 |
| 

PDF\_FONT\_TURKISH\_CHARSET

 | 

162

 | 

Turkish.

 |
| 

PDF\_FONT\_VIETNAMESE\_CHARSET

 | 

163

 | 

Vietnamese.

 |
| 

PDF\_FONT\_HEBREW\_CHARSET

 | 

177

 | 

Hebrew.

 |
| 

PDF\_FONT\_ARABIC\_CHARSET

 | 

178

 | 

Arabic.

 |
| 

PDF\_FONT\_BALTIC\_CHARSET

 | 

186

 | 

Baltic.

 |

#### FitMode

Page fit mode enum.

**System capability**: SystemCapability.OfficeService.PDFService.Core

**Start version**: 5.0.0(12)

| 
**Name**

 | 

**Value**

 | 

**Description**

 |
| :-- | :-- | :-- |
| 

FIT\_MODE\_XYZ

 | 

1

 | 

Zooms in or out the page based on the zoom ratio from the point in the upper left corner of the page.

 |
| 

FIT\_MODE\_HORIZONTAL

 | 

2

 | 

Fits the page to the entire page width in the window.

 |
| 

FIT\_MODE\_VERTICAL

 | 

3

 | 

Fits the page to the entire page height in the window.

 |
| 

FIT\_MODE\_RECT

 | 

4

 | 

Fits the page into the page rectangle within the window.

 |

#### WatermarkType

Page watermark type enum.

**System capability**: SystemCapability.OfficeService.PDFService.Core

**Start version**: 5.0.0(12)

| 
**Name**

 | 

**Value**

 | 

**Description**

 |
| :-- | :-- | :-- |
| 

WATERMARK\_TEXT

 | 

1

 | 

Text watermark.

 |
| 

WATERMARK\_IMAGE

 | 

2

 | 

Image watermark.

 |

#### WatermarkAlignment

Watermark alignment type enum.

**System capability**: SystemCapability.OfficeService.PDFService.Core

**Start version**: 5.0.0(12)

| 
**Name**

 | 

**Value**

 | 

**Description**

 |
| :-- | :-- | :-- |
| 

WATERMARK\_ALIGNMENT\_TOP

 | 

0

 | 

Vertical top.

 |
| 

WATERMARK\_ALIGNMENT\_VCENTER

 | 

1

 | 

Vertical center.

 |
| 

WATERMARK\_ALIGNMENT\_BOTTOM

 | 

2

 | 

Vertical bottom.

 |
| 

WATERMARK\_ALIGNMENT\_LEFT

 | 

3

 | 

Horizontal left.

 |
| 

WATERMARK\_ALIGNMENT\_HCENTER

 | 

4

 | 

Horizontally centered.

 |
| 

WATERMARK\_ALIGNMENT\_RIGHT

 | 

5

 | 

Horizontal right.

 |

#### BackgroundAlignment

Background alignment type enum.

**System capability**: SystemCapability.OfficeService.PDFService.Core

**Start version**: 5.0.0(12)

| 
**Name**

 | 

**Value**

 | 

**Description**

 |
| :-- | :-- | :-- |
| 

BACKGROUND\_ALIGNMENT\_TOP

 | 

0

 | 

Vertical top.

 |
| 

BACKGROUND\_ALIGNMENT\_VCENTER

 | 

1

 | 

Vertical center.

 |
| 

BACKGROUND\_ALIGNMENT\_BOTTOM

 | 

2

 | 

Vertical bottom.

 |
| 

BACKGROUND\_ALIGNMENT\_LEFT

 | 

3

 | 

Horizontal left.

 |
| 

BACKGROUND\_ALIGNMENT\_HCENTER

 | 

4

 | 

Horizontally centered.

 |
| 

BACKGROUND\_ALIGNMENT\_RIGHT

 | 

5

 | 

Horizontal right.

 |

#### PdfActionType

Link redirection type.

**System capability**: SystemCapability.OfficeService.PDFService.Core

**Start version**: 5.1.0(18)

| 
**Name**

 | 

**Value**

 | 

**Description**

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

GOTO

 | 

1

 | 

In-document redirection link.

 |
| 

HYPERLINK

 | 

2

 | 

Hyperlink.

 |
