# bookParser (Book Parsing Capability)

This module provides the book parsing capability, with support for TXT, EPUB, MOBI, AZW, and AZW3 file formats. It can initialize [BookParserHandler](#section59035422210) for book files in the [app sandbox directory](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/app-sandbox-directory) to obtain the basic book information, [spine item list](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/reader-introduction#section2215512152119), catalog item list, and chapter content.

**Start version**: 5.0.4(16)

#### Module Import

import { bookParser } from '@kit.ReaderKit';

#### BookInfo

Basic book information.

**Atomic service API**: This API can be used in atomic services since API version 5.0.4(16).

**System capability**: SystemCapability.Reader.ReaderService.BookParser

**Start version**: 5.0.4(16)

| 
**Name**

 | 

**Type**

 | 

Read-Only

 | 

Optional

 | 

**Description**

 |
| :-- | :-- | :-- | :-- | :-- |
| 

bookTitle

 | 

string

 | 

No

 | 

No

 | 

Book title.

 |
| 

bookCreator

 | 

string

 | 

No

 | 

Yes

 | 

Author.

 |
| 

bookPublishDate

 | 

string

 | 

No

 | 

Yes

 | 

Publication date. (This parameter is reserved.)

 |
| 

bookLanguage

 | 

string

 | 

No

 | 

Yes

 | 

Book language.

-   **zh\_HK**: traditional Chinese, including traditional Chinese (Taiwan, China) and traditional Chinese (Hong Kong, China)
-   **zh\_CN**: simplified Chinese
-   **zh**: Chinese (**zh** is used as the default value for unsupported or invalid languages.)
-   **en\_US**: English

 |
| 

bookCoverImage

 | 

string

 | 

No

 | 

Yes

 | 

Path of a book cover image. Example: **OEBPS/images/coverpage.jpg**.

 |
| 

bookCharset

 | 

string

 | 

No

 | 

Yes

 | 

Character set of the book content, which is determined by the book encoding format, for example, **utf-8**. For details about the supported encoding formats, please refer to [TextEncoder](../../../../application-framework/arkts/arkts-apis/ohos-util-util/document.md#textencoder). (This parameter is reserved.)

 |
| 

bookType

 | 

string

 | 

No

 | 

Yes

 | 

Book format, which can be **txt**, **epub**, **mobi**, **azw**, or **azw3**.

 |
| 

isRtl

 | 

boolean

 | 

No

 | 

Yes

 | 

Indicates whether the text direction is right-to-left (RTL). (This parameter is reserved.)

-   **true**: RTL
-   **false**: left-to-right (LTR)

 |
| 

renditionLayout

 | 

string

 | 

No

 | 

Yes

 | 

Book layout. (This parameter is reserved.)

-   **reflowable**: reflowable layout
-   **pre-paginated**: fixed layout

 |
| 

renditionOrientation

 | 

string

 | 

No

 | 

Yes

 | 

Orientation. (This parameter is reserved.)

-   **landscape**
-   **portrait**
-   **auto**: auto-adaptive

 |
| 

renditionSpread

 | 

string

 | 

No

 | 

Yes

 | 

Scenario for merging the left and right pages of the spine. (This parameter is reserved.)

-   **none**: The left and right pages of the spine are not merged.
-   **landscape**: The left and right pages of the spine are merged in landscape orientation.
-   **portrait**: The left and right pages of the spine are merged in portrait orientation.
-   **auto**: Spine page merging is auto-adaptive.

 |

#### SpineItem

Spine item, which identifies a readable content resource, for example, **chapter1.xhtml**.

**Atomic service API**: This API can be used in atomic services since API version 5.0.4(16).

**System capability**: SystemCapability.Reader.ReaderService.BookParser

**Start version**: 5.0.4(16)

| 
**Name**

 | 

**Type**

 | 

Read-Only

 | 

Optional

 | 

**Description**

 |
| :-- | :-- | :-- | :-- | :-- |
| 

idRef

 | 

string

 | 

No

 | 

No

 | 

Content resource ID, which uniquely identifies a body content file.

 |
| 

index

 | 

number

 | 

No

 | 

No

 | 

Content resource index, starting from **0**.

 |
| 

href

 | 

string

 | 

No

 | 

No

 | 

Reference path of a content resource in a book. Example: **/OEBPS/Txt/chapter01.xhtml**.

 |
| 

properties

 | 

string

 | 

No

 | 

No

 | 

Content display mode for two-page view. (This parameter is reserved.)

-   **page-spread-left**: Content is displayed on the left of the screen.
-   **page-spread-right**: Content is displayed on the right of the screen.

 |

#### CatalogItem

Book catalog item, which can be used for displaying the catalog.

**Atomic service API**: This API can be used in atomic services since API version 5.0.4(16).

**System capability**: SystemCapability.Reader.ReaderService.BookParser

**Start version**: 5.0.4(16)

| 
**Name**

 | 

**Type**

 | 

Read-Only

 | 

Optional

 | 

**Description**

 |
| :-- | :-- | :-- | :-- | :-- |
| 

catalogId

 | 

number

 | 

No

 | 

No

 | 

Catalog item ID, starting from **0**.

 |
| 

catalogName

 | 

string

 | 

No

 | 

No

 | 

Catalog item name.

 |
| 

catalogLevel

 | 

number

 | 

No

 | 

Yes

 | 

Catalog item level.

For example, the catalog level of Chapter 1 is 0. If there are subchapters below it, the catalog level of the subchapters is incremented by 1, resulting in 1. If there are further subchapters below those subchapters, the level continues to be incremented by 1, resulting in 2.

You can identify the hierarchical relationships between catalog items based on their order and level.

 |
| 

playOrder

 | 

number

 | 

No

 | 

Yes

 | 

Catalog item reading order, starting from **0**. (This parameter is reserved.)

 |
| 

idRef

 | 

string

 | 

No

 | 

Yes

 | 

ID of the content resource corresponding to a catalog item. (This parameter is reserved.)

 |
| 

href

 | 

string

 | 

No

 | 

Yes

 | 

Content resource path of a catalog item, with an anchor.

 |
| 

resourceFile

 | 

string

 | 

No

 | 

Yes

 | 

Content resource path of a catalog item, without an anchor.

Take an EPUB book as an example. This parameter indicates the relative path of a resource in the root directory **/OEBPS**.

 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/39/v3/yFOiQEUyQxmiauU4DtDngQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062519Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=54403B5E5E7CB8D21C1C5B579CF52824E22107E5212867C794210EEDFC313E59)

A **CatalogItem** value specifies a catalog item, and a **SpineItem** value specifies a content resource file. The two items are not necessarily in a one-to-one mapping. For example, if a chapter in an EPUB book has three subchapters, there are four catalog items. However, the four catalog items may map only one content resource file specified by **SpineItem** based on **CatalogItem.resourceFile** and **SpineItem.href**.

#### CallbackRes

type CallbackRes<T, V> = (data: T) => V

Callback API for book resource requests, which is called when the typesetting engine renders the page. This API must be used together with the **ReaderComponentController**'s registration API [on('resourceRequest')](../readercore-reader-kit-core-capabilities/document.md#section169541417131914). If there are custom background and font resources, these resources need to be returned through this API.

**Atomic service API**: This API can be used in atomic services since API version 5.0.4(16).

**System capability**: SystemCapability.Reader.ReaderService.BookParser

**Start version**: 5.0.4(16)

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

data

 | 

T

 | 

Yes

 | 

Parameter of the resource request API. For example, when the API obtains a custom font, this parameter indicates the name of the font to be obtained.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

V

 | 

Return value type of the resource request API. For example, when the API obtains a custom font, the return value indicates the binary data stream of the font file.

 |

**Example**:

import { bookParser, readerCore, ReadPageComponent } from '@kit.ReaderKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { common } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Reader {
  private readerComponentController: readerCore.ReaderComponentController = new readerCore.ReaderComponentController();
  private selectFontPath = 'fonts/SourceHanSerifCN-VF.ttf';

  aboutToAppear(): void {
    this.registerListener();
  }

  private async registerListener(){
    try {
      let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
      await this.readerComponentController.init(context)
      this.readerComponentController.on('resourceRequest', this.resourceRequest);
    } catch (err) {
      hilog.error(0x0000, 'testTag', \`failed to registerListener, Code is ${err.code}, message is ${err.message}\`);
    }
  }

  private resourceRequest: bookParser.CallbackRes<string,ArrayBuffer> = (fileName: string): ArrayBuffer => {
    if (this.isFont(fileName)) {
      let res = $rawfile(this.selectFontPath);
      let context = this.getUIContext().getHostContext();
      if (res && context) {
        try {
        // Obtain the font data in the resource path.
          let value: Uint8Array = context.resourceManager.getRawFileContentSync(this.selectFontPath);
          hilog.info(0x0000, 'testTag', 'resourceRequest : get success');
          return value.buffer as ArrayBuffer;
        } catch (error) {
          let code = (error as BusinessError).code;
          let message = (error as BusinessError).message;
          hilog.error(0x0000, 'testTag', \`callback getRawFileContent failed, error code: ${code}, message: ${message}.\`);
        }
      }
    }
    return new ArrayBuffer(0);
  }

  private isFont(filePath: string): boolean {
    let options = \[".ttf", ".woff2", ".otf"\];
    let path = filePath.toLowerCase();
    let result = path.indexOf(options\[0\]) != -1 || path.indexOf(options\[1\]) != -1 || path.indexOf(options\[2\]) != -1;
    hilog.info(0x0000, 'testTag', 'isFont = ' + result);
    return result;
  }

  build() {
    Stack() {
      ReadPageComponent({
        controller: this.readerComponentController,
        readerCallback: (err: BusinessError, data: readerCore.ReaderComponentController) => {
          this.readerComponentController = data;
        }
      })
    }.width('100%').height('100%')
  }
}

#### getDefaultHandler

getDefaultHandler(path: string): Promise<BookParserHandler>

Obtains the default book parser. This API returns the result through a promise.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8a/v3/Bdorz5PARASn2fTovA9sFA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062519Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=199B754550A421781885A6B13A8CB8580356EACD1F54DA4A4B8FC92B678BC2A8)

The **getDefaultHandler** API cannot be called concurrently for book files in the same path.

**Atomic service API**: This API can be used in atomic services since API version 5.0.4(16).

**System capability**: SystemCapability.Reader.ReaderService.BookParser

**Start version**: 5.0.4(16)

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

path

 | 

string

 | 

Yes

 | 

Local book file path (only the [sandbox path](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/app-sandbox-directory) of the current app is supported).

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<[BookParserHandler](#section59035422210)\>

 | 

**BookParserHandler** class.

 |

**Error codes**:

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

[401](../../../../api-reference-overview/universal-error-codes/document.md#section401-parameter-check-failed)

 | 

Parameter error.

 |
| 

[1017000999](../../arkts-api-error-codes/document.md#section31031138161116)

 | 

Other error.

 |
| 

[1017010003](../../arkts-api-error-codes/document.md#section1855956131312)

 | 

Book file format is unexpected.

 |
| 

[1017010004](../../arkts-api-error-codes/document.md#section692725412147)

 | 

File is not exist.

 |

**Example**:

import { bookParser } from '@kit.ReaderKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { common } from '@kit.AbilityKit';

@Entry
@Component
struct Reader {
  aboutToAppear(): void {
    this.initBookParser();
  }

  private async initBookParser() {
    try {
      // Initialize the book parser for the book file that has been imported to the [app sandbox directory](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/app-sandbox-directory).
      let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
      let filePath: string = \`${context.filesDir}/abc.epub\`;
      let bookParserHandler: bookParser.BookParserHandler = await bookParser.getDefaultHandler(filePath);
      hilog.info(0x0000, 'testTag', \`getDefaultHandler succeeded\`);
    } catch (err) {
      hilog.error(0x0000, 'testTag', \`failed to initBookParser, Code is ${err.code}, message is ${err.message}\`);
    }
  }

  build() {
    // Implement the page layout based on your service needs.
  }
}

#### BookParserHandler

Book parsing API class.

**Atomic service API**: This API can be used in atomic services since API version 5.0.4(16).

**System capability**: SystemCapability.Reader.ReaderService.BookParser

**Start version**: 5.0.4(16)

#### \[h2\]getBookInfo

getBookInfo(): BookInfo

Obtains book information.

**Atomic service API**: This API can be used in atomic services since API version 5.0.4(16).

**System capability**: SystemCapability.Reader.ReaderService.BookParser

**Start version**: 5.0.4(16)

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

[BookInfo](#section38181821125613)

 | 

Basic book information.

 |

**Error codes**:

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

[1017000001](../../arkts-api-error-codes/document.md#section1427915529104)

 | 

Book parser is not initialized.

 |
| 

[1017000999](../../arkts-api-error-codes/document.md#section31031138161116)

 | 

Other error.

 |
| 

[1017010002](../../arkts-api-error-codes/document.md#section1115195931210)

 | 

Invalid request.

 |

**Example**:

import { bookParser } from '@kit.ReaderKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { common } from '@kit.AbilityKit';

@Entry
@Component
struct Reader {
  aboutToAppear(): void {
    this.getBookInfo();
  }

  private async getBookInfo() {
    try {
      // Initialize the book parser for the book file that has been imported to the [app sandbox directory](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/app-sandbox-directory).
      let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
      let filePath: string = \`${context.filesDir}/abc.epub\`;
      let bookParserHandler: bookParser.BookParserHandler = await bookParser.getDefaultHandler(filePath);
      let bookInfo: bookParser.BookInfo = bookParserHandler.getBookInfo();
      hilog.info(0x0000, 'testTag', \`getBookInfo succeeded, bookInfo:\` + JSON.stringify(bookInfo));
    } catch (err) {
      hilog.error(0x0000, 'testTag', \`failed to getBookInfo, Code is ${err.code}, message is ${err.message}\`);
    }
  }

  build() {
    // Implement the page layout based on your service needs.
  }
}

#### \[h2\]getCatalogList

getCatalogList(): CatalogItem\[\]

Obtains the catalog item list.

**Atomic service API**: This API can be used in atomic services since API version 5.0.4(16).

**System capability**: SystemCapability.Reader.ReaderService.BookParser

**Start version**: 5.0.4(16)

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

[CatalogItem](#section12325515195)\[\]

 | 

Catalog item list.

 |

**Error codes**:

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

[1017000001](../../arkts-api-error-codes/document.md#section1427915529104)

 | 

Book parser is not initialized

 |
| 

[1017000999](../../arkts-api-error-codes/document.md#section31031138161116)

 | 

Other error

 |
| 

[1017010002](../../arkts-api-error-codes/document.md#section1115195931210)

 | 

Invalid request

 |

**Example**:

import { bookParser } from '@kit.ReaderKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { common } from '@kit.AbilityKit';

@Entry
@Component
struct Reader {
  aboutToAppear(): void {
    this.getCatalogList();
  }

  private async getCatalogList(){
    try {
      // Initialize the book parser for the book file that has been imported to the [app sandbox directory](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/app-sandbox-directory).
      let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
      let filePath: string = \`${context.filesDir}/abc.epub\`;
      let bookParserHandler: bookParser.BookParserHandler = await bookParser.getDefaultHandler(filePath);
      let catalogList: bookParser.CatalogItem\[\] = bookParserHandler.getCatalogList();
      hilog.info(0x0000, 'testTag', \`getCatalogList succeeded, catalogList:\` + JSON.stringify(catalogList));
    } catch(err) {
      hilog.error(0x0000, 'testTag', \`failed to getCatalogList, Code is ${err.code}, message is ${err.message}\`);
    }
  }

  build() {
    // Implement the page layout based on your service needs.
  }
}

#### \[h2\]getSpineList

getSpineList(): SpineItem\[\]

Obtains the spine item list.

**Atomic service API**: This API can be used in atomic services since API version 5.0.4(16).

**System capability**: SystemCapability.Reader.ReaderService.BookParser

**Start version**: 5.0.4(16)

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

[SpineItem](#section1029864651619)\[\]

 | 

Spine item list.

 |

**Error codes**:

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

[1017000001](../../arkts-api-error-codes/document.md#section1427915529104)

 | 

Book parser is not initialized.

 |
| 

[1017000999](../../arkts-api-error-codes/document.md#section31031138161116)

 | 

Other error.

 |
| 

[1017010002](../../arkts-api-error-codes/document.md#section1115195931210)

 | 

Invalid request.

 |

**Example**:

import { bookParser } from '@kit.ReaderKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { common } from '@kit.AbilityKit';

@Entry
@Component
struct Reader {
  aboutToAppear(): void {
    this.getSpineList();
  }

  private async getSpineList(){
    try {
      // Initialize the book parser for the book file that has been imported to the [app sandbox directory](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/app-sandbox-directory).
      let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
      let filePath: string = \`${context.filesDir}/abc.epub\`;
      let bookParserHandler: bookParser.BookParserHandler = await bookParser.getDefaultHandler(filePath);
      let spineList: bookParser.SpineItem\[\] = bookParserHandler.getSpineList();
      hilog.info(0x0000, 'testTag', \`getSpineList succeeded, spineList:\` + JSON.stringify(spineList));
    } catch(err) {
      hilog.error(0x0000, 'testTag', \`failed to getSpineList, Code is ${err.code}, message is ${err.message}\`);
    }
  }

  build() {
    // Implement the page layout based on your service needs.
  }
}

#### \[h2\]getSpineItemContent

getSpineItemContent(spineIndex: number): Promise<string>

Obtains the resource content of a single spine item. This API is called when the typesetting engine obtains the content of a resource file. If you do not need to customize the typesetting engine, you can ignore this API.

**Atomic service API**: This API can be used in atomic services since API version 5.0.4(16).

**System capability**: SystemCapability.Reader.ReaderService.BookParser

**Start version**: 5.0.4(16)

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

spineIndex

 | 

number

 | 

Yes

 | 

Content resource index ([SpineItem](#section1029864651619).index).

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<string>

 | 

Content string of a spine item.

 |

**Error codes**:

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

[401](../../../../api-reference-overview/universal-error-codes/document.md#section401-parameter-check-failed)

 | 

Parameter error. Possible causes: 1. Incorrect parameter types; 2. Parameter out of range.

 |
| 

[1017000001](../../arkts-api-error-codes/document.md#section1427915529104)

 | 

Book parser is not initialized.

 |
| 

[1017000999](../../arkts-api-error-codes/document.md#section31031138161116)

 | 

Other error.

 |
| 

[1017010001](../../arkts-api-error-codes/document.md#section19552151617126)

 | 

Invalid spine item.

 |
| 

[1017010002](../../arkts-api-error-codes/document.md#section1115195931210)

 | 

Invalid request.

 |

**Example**:

import { bookParser } from '@kit.ReaderKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { common } from '@kit.AbilityKit';

@Entry
@Component
struct Reader {
  aboutToAppear(): void {
    this.getSpineItemContent();
  }

  private async getSpineItemContent(){
    try {
      // Initialize the book parser for the book file that has been imported to the [app sandbox directory](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/app-sandbox-directory).
      let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
      let filePath: string = \`${context.filesDir}/abc.epub\`;
      let bookParserHandler: bookParser.BookParserHandler = await bookParser.getDefaultHandler(filePath);
      let spineList: bookParser.SpineItem\[\] = bookParserHandler.getSpineList();
      let spineItemContent: string = await bookParserHandler.getSpineItemContent(spineList\[0\].index);
      hilog.info(0x0000, 'testTag', \`getSpineItemContent succeeded, spineItemContent:\` + JSON.stringify(spineItemContent));
    } catch(err) {
      hilog.error(0x0000, 'testTag', \`failed to getSpineItemContent, Code is ${err.code}, message is ${err.message}\`);
    }
  }

  build() {
    // Implement the page layout based on your service needs.
  }
}

#### \[h2\]getResourceContent

getResourceContent(spineIndex: number, filePath: string): ArrayBuffer

Obtains book content resources.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bf/v3/dYLvpgZHSnCuMYeu3C2ZwQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062519Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8C6D209AF3D1E6350294F671C11395C2932F974661FEA11D39A36AC2F8EAD034)

You can use this API to obtain book cover resources. The typesetting engine preferentially calls this API to obtain resources such as images in a book. If the resources cannot be obtained, it will proceed to call [on('resourceRequest')](../readercore-reader-kit-core-capabilities/document.md#section169541417131914).

**Atomic service API**: This API can be used in atomic services since API version 5.0.4(16).

**System capability**: SystemCapability.Reader.ReaderService.BookParser

**Start version**: 5.0.4(16)

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

spineIndex

 | 

number

 | 

Yes

 | 

Content resource index ([SpineItem](#section1029864651619).index). If a negative number, for example, **\-1**, is passed, the book cover is obtained.

 |
| 

filePath

 | 

string

 | 

Yes

 | 

Path of a resource in a book.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

ArrayBuffer

 | 

Binary data of a file.

 |

**Error codes**:

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

[401](../../../../api-reference-overview/universal-error-codes/document.md#section401-parameter-check-failed)

 | 

Parameter error. Possible causes: 1. Incorrect parameter types; 2. Parameter out of range.

 |
| 

[1017000001](../../arkts-api-error-codes/document.md#section1427915529104)

 | 

Book parser is not initialized.

 |
| 

[1017000999](../../arkts-api-error-codes/document.md#section31031138161116)

 | 

Other error.

 |
| 

[1017010001](../../arkts-api-error-codes/document.md#section19552151617126)

 | 

Invalid spine item.

 |
| 

[1017010002](../../arkts-api-error-codes/document.md#section1115195931210)

 | 

Invalid request.

 |

**Example**:

import { bookParser } from '@kit.ReaderKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { common } from '@kit.AbilityKit';

@Entry
@Component
struct Reader {
  aboutToAppear(): void {
    this.getResourceContent();
  }

  private async getResourceContent() {
    try {
      // Initialize the book parser for the book file that has been imported to the [app sandbox directory](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/app-sandbox-directory).
      let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
      let filePath: string = \`${context.filesDir}/abc.epub\`;
      let bookParserHandler: bookParser.BookParserHandler = await bookParser.getDefaultHandler(filePath);
      // Replace the value with an actual image name in the book file.
      let imagePath = './2188093923226426261\_image001.jpg'
      let spineList: bookParser.SpineItem\[\] = bookParserHandler.getSpineList();
      let resourceContent: ArrayBuffer = bookParserHandler.getResourceContent(spineList\[0\].index, imagePath);
      hilog.info(0x0000, 'testTag', \`getResourceContent succeeded, resourceContentByteLength:\` + resourceContent.byteLength);
    } catch (err) {
      hilog.error(0x0000, 'testTag', \`failed to getResourceContent, Code is ${err.code}, message is ${err.message}\`);
    }
  }

  build() {
    // Implement the page layout based on your service needs.
  }
}

#### \[h2\]getDomPosByCatalogHref

getDomPosByCatalogHref(href: string): string

Obtains the reading start position **domPos**, which can be used to identify the reading progress, facilitating navigation to a specified reading position.

**Atomic service API**: This API can be used in atomic services since API version 5.0.4(16).

**System capability**: SystemCapability.Reader.ReaderService.BookParser

**Start version**: 5.0.4(16)

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

href

 | 

string

 | 

Yes

 | 

Content resource path of a catalog item ([CatalogItem](#section12325515195).href), with an anchor.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

string

 | 

**domPos** information of a chapter.

 |

**Error codes**:

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

[401](../../../../api-reference-overview/universal-error-codes/document.md#section401-parameter-check-failed)

 | 

Parameter error. Possible causes: 1. Incorrect parameter types; 2. Parameter out of range.

 |
| 

[1017000001](../../arkts-api-error-codes/document.md#section1427915529104)

 | 

Book parser is not initialized.

 |
| 

[1017000999](../../arkts-api-error-codes/document.md#section31031138161116)

 | 

Other error.

 |
| 

[1017010002](../../arkts-api-error-codes/document.md#section1115195931210)

 | 

Invalid request.

 |

**Example**:

import { bookParser } from '@kit.ReaderKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { common } from '@kit.AbilityKit';

@Entry
@Component
struct Reader {
  aboutToAppear(): void {
    this.getDomPosByCatalogHref();
  }

  private async getDomPosByCatalogHref(){
    try {
      // Initialize the book parser for the book file that has been imported to the [app sandbox directory](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/app-sandbox-directory).
      let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
      let filePath: string = \`${context.filesDir}/abc.epub\`;
      let bookParserHandler: bookParser.BookParserHandler = await bookParser.getDefaultHandler(filePath);
      let catalogList: bookParser.CatalogItem\[\] = bookParserHandler.getCatalogList();
      let href = catalogList\[1\]?.href || '';
      let domPos: string = bookParserHandler.getDomPosByCatalogHref(href);
      hilog.info(0x0000, 'testTag', \`getDomPosByCatalogHref succeeded, domPos:\` + domPos);
    } catch(err) {
      hilog.error(0x0000, 'testTag', \`failed to getDomPosByCatalogHref, Code is ${err.code}, message is ${err.message}\`);
    }
  }

  build() {
    // Implement the page layout based on your service needs.
  }
}

#### \[h2\]getAbsoluteResourcePath

getAbsoluteResourcePath(spineIndex: number): string

Obtains the absolute file path of a resource.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c7/v3/GaGAOVasS-yh8l0YD86LGQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062519Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=004F5D066A0EB386CC41BFE344247B78C510FC038CD53F28298536A1420EDA06)

This API is typically called when the typesetting engine renders a resource. If typesetting engine customization is not required, you can ignore this API.

**Atomic service API**: This API can be used in atomic services since API version 5.0.4(16).

**System capability**: SystemCapability.Reader.ReaderService.BookParser

**Start version**: 5.0.4(16)

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

spineIndex

 | 

number

 | 

Yes

 | 

Content resource index ([SpineItem](#section1029864651619).index).

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

string

 | 

Absolute resource path.

 |

**Error codes**:

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

[401](../../../../api-reference-overview/universal-error-codes/document.md#section401-parameter-check-failed)

 | 

Parameter error. Possible causes: 1. Incorrect parameter types; 2. Parameter out of range.

 |
| 

[1017000001](../../arkts-api-error-codes/document.md#section1427915529104)

 | 

Book parser is not initialized.

 |
| 

[1017000999](../../arkts-api-error-codes/document.md#section31031138161116)

 | 

Other error.

 |
| 

[1017010002](../../arkts-api-error-codes/document.md#section1115195931210)

 | 

Invalid request.

 |
| 

[1017010004](../../arkts-api-error-codes/document.md#section692725412147)

 | 

File is not exist.

 |

**Example**:

import { bookParser } from '@kit.ReaderKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { common } from '@kit.AbilityKit';

@Entry
@Component
struct Reader {
  aboutToAppear(): void {
    this.getAbsoluteResourcePath();
  }

  private async getAbsoluteResourcePath(){
    try {
      // Initialize the book parser for the book file that has been imported to the [app sandbox directory](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/app-sandbox-directory).
      let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
      let filePath: string = \`${context.filesDir}/abc.epub\`;
      let bookParserHandler: bookParser.BookParserHandler = await bookParser.getDefaultHandler(filePath);
      let spineList: bookParser.SpineItem\[\] = bookParserHandler.getSpineList();
      let resourcePath: string = bookParserHandler.getAbsoluteResourcePath(spineList\[0\].index);
      hilog.info(0x0000, 'testTag', \`getAbsoluteResourcePath succeeded, resourcePath:\` + resourcePath);
    } catch(err) {
      hilog.error(0x0000, 'testTag', \`failed to getAbsoluteResourcePath, Code is ${err.code}, message is ${err.message}\`);
    }
  }

  build() {
    // Implement the page layout based on your service needs.
  }
}
