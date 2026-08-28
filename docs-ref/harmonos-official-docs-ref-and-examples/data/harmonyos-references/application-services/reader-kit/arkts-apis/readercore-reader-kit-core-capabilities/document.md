# readerCore (Reader Kit Core Capabilities)

This module provides core capabilities of Reader Kit, including the page data base class, page status, content pagination information, page typesetting attributes, and component controller.

**Start version**: 5.0.4(16)

#### Module Import

import { readerCore } from '@kit.ReaderKit';

#### PageDatabaseBean

Page data base class.

**Atomic service API**: This API can be used in atomic services since API version 5.0.4(16).

**System capability**: SystemCapability.Reader.ReaderService.ReaderCore

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

nodeType

 | 

string

 | 

No

 | 

No

 | 

Node type. The value is fixed at **ReaderCoreIdentity**, indicating the reader node.

 |
| 

dataId

 | 

string

 | 

No

 | 

No

 | 

Node ID, which is automatically generated based on the resource index and page offset.

 |

#### \[h2\]constructor

constructor(nodeType: string, nodeDataId: string)

Page data constructor.

**Atomic service API**: This API can be used in atomic services since API version 5.0.4(16).

**System capability**: SystemCapability.Reader.ReaderService.ReaderCore

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

nodeType

 | 

string

 | 

Yes

 | 

Node type. The value is fixed at **ReaderCoreIdentity**, indicating the reader node.

 |
| 

nodeDataId

 | 

string

 | 

Yes

 | 

Node ID, which is automatically generated based on the [PageDataInfo](#section1064382518239).resourceIndex and [PageDataInfo](#section1064382518239).pageOffset parameters.

 |

#### PageState

Page status.

**Atomic service API**: This API can be used in atomic services since API version 5.0.4(16).

**System capability**: SystemCapability.Reader.ReaderService.ReaderCore

**Start version**: 5.0.4(16)

| 
Name

 | 

Value

 | 

Description

 |
| :-- | :-- | :-- |
| 

PAGE\_WAITING

 | 

1

 | 

Waiting for loading.

 |
| 

PAGE\_LOADING

 | 

2

 | 

Loading…

 |
| 

PAGE\_ON\_SHOW

 | 

3

 | 

Loading successful.

 |
| 

OPEN\_BOOK\_FAIL

 | 

4

 | 

Loading failed.

 |

#### PageDataInfo

Content pagination information, which is inherited from [PageDatabaseBean](#section393123711811).

**Atomic service API**: This API can be used in atomic services since API version 5.0.4(16).

**System capability**: SystemCapability.Reader.ReaderService.ReaderCore

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

nodeType

 | 

string

 | 

No

 | 

No

 | 

Node type. The value is fixed at **ReaderCoreIdentity**, indicating the reader node.

 |
| 

dataId

 | 

string

 | 

No

 | 

No

 | 

Node ID, which is automatically generated based on the **resourceIndex** and **pageOffset** parameters.

 |
| 

pageHeaderContent

 | 

string

 | 

No

 | 

No

 | 

Page header text. (This parameter is reserved.)

 |
| 

pageFooterContent

 | 

string

 | 

No

 | 

No

 | 

Page footer text. (This parameter is reserved.)

 |
| 

startDomPos

 | 

string

 | 

No

 | 

No

 | 

Start position of the current page.

 |
| 

endDomPos

 | 

string

 | 

No

 | 

No

 | 

End position of the current page.

 |
| 

state

 | 

[PageState](#section143420551333)

 | 

No

 | 

No

 | 

Page status.

 |
| 

resourceIndex

 | 

number

 | 

No

 | 

No

 | 

Spine item index ([SpineItem](../bookparser-book-parsing-capability/document.md#section1029864651619).index).

 |
| 

pageOffset

 | 

number

 | 

No

 | 

No

 | 

Page number offset, starting from **0**.

For example, if a content resource file contains 50 pages, the value ranges from 0 to 49.

 |

#### \[h2\]constructor

constructor(nodeType: string, nodeId: string)

Constructor of content pagination information.

**Atomic service API**: This API can be used in atomic services since API version 5.0.4(16).

**System capability**: SystemCapability.Reader.ReaderService.ReaderCore

**Start version**: 5.0.4(16)

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

nodeType

 | 

string

 | 

Yes

 | 

Node type. The value is fixed at **ReaderCoreIdentity**.

 |
| 

nodeId

 | 

string

 | 

Yes

 | 

Node ID, which is automatically generated based on the [PageDataInfo](#section1064382518239).resourceIndex and [PageDataInfo](#section1064382518239).pageOffset parameters.

 |

#### ReaderSetting

Page typesetting attributes.

**Atomic service API**: This API can be used in atomic services since API version 5.0.4(16).

**System capability**: SystemCapability.Reader.ReaderService.ReaderCore

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

fontName

 | 

string

 | 

No

 | 

No

 | 

Font name.

 |
| 

fontSize

 | 

number

 | 

No

 | 

No

 | 

Font size, in pixels.

 |
| 

fontWeight

 | 

number

 | 

No

 | 

No

 | 

Font weight, which relies on whether the specified font file supports setting the text thickness. (This parameter is reserved.)

 |
| 

fontColor

 | 

string

 | 

No

 | 

No

 | 

Font color. Example: **#ffffff** or **rgba(248, 249, 250, 1)**.

CAUTION:

Font color value constraints:

-   For hexadecimal color values, only the 6-digit format is supported, and transparency setting is not supported.
-   For RGBA color values, the transparency value must be **1**.

 |
| 

fontPath

 | 

string

 | 

No

 | 

No

 | 

Local path of a font file.

The following storage paths are supported:

-   **resources/rawfile** in the project directory
-   [App sandbox directory](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/app-sandbox-directory)

 |
| 

lineHeight

 | 

number

 | 

No

 | 

No

 | 

Line height coefficient. The actual display height of a line of text equals **fontSize** x **lineHeight**.

 |
| 

nightMode

 | 

boolean

 | 

No

 | 

No

 | 

Indicates whether to use the dark mode. You need to manually set the parameter when detecting switch between dark and light modes.

It is used for drawing the back theme color in simulated page turning.

-   **true**: dark mode.
-   **false**: light mode. The default value is **false**.

 |
| 

themeColor

 | 

string

 | 

No

 | 

No

 | 

Theme background color. Example: **#ffffff** or **rgba(248, 249, 250, 1)**.

If a background image is set, this parameter is used to draw the back theme color in simulated page turning.

If no background image is set, this parameter is used to render the background color of the reading page.

CAUTION:

Background color value constraints:

-   For hexadecimal color values, only the 6-digit format is supported, and transparency setting is not supported.
-   For RGBA color values, the transparency value must be **1**.

 |
| 

themeBgImg

 | 

string

 | 

No

 | 

No

 | 

Theme background image path, which is used for drawing the reading page background.

The following storage paths are supported:

-   **resources/rawfile** in the project directory
-   [App sandbox directory](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/app-sandbox-directory)

 |
| 

flipMode

 | 

string

 | 

No

 | 

No

 | 

Page turning mode.

-   **0**: simulated page turning
-   **1**: horizontal swipe

The default value is **0**.

 |
| 

scaledDensity

 | 

number

 | 

No

 | 

No

 | 

Scaling factor of the displayed text. The value is obtained from [display.getDefaultDisplaySync().scaledDensity](../../../../application-framework/arkui/arkts-api/display-management/ohos-display-display/document.md#displaygetdefaultdisplaysync9).

When the text scaling factor changes in scenarios such as Multi-Window, you need to call the [setPageConfig](#section6297758718) API of **ReaderComponentController** to update the attribute.

 |
| 

viewPortWidth

 | 

number

 | 

No

 | 

No

 | 

Viewport width, in pixels.

 |
| 

viewPortHeight

 | 

number

 | 

No

 | 

No

 | 

Viewport height, in pixels.

 |

#### ReaderComponentController

[ReadPageComponent](../../arkts-components/readpagecomponent-reading-page-component/document.md#section3730195311450) controller, which must be used together with **ReadPageComponent**.

**Atomic service API**: This API can be used in atomic services since API version 5.0.4(16).

**System capability**: SystemCapability.Reader.ReaderService.ReaderCore

**Start version**: 5.0.4(16)

#### \[h2\]init

init(context: common.UIAbilityContext): Promise<void>

Initializes **ReaderComponentController**. This API returns the result asynchronously through a promise.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b5/v3/qhVWa1bGRViT_ljwTypUBw/caution_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062518Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1884875F40F9DB043D5F453735C6E5EA1373AA68A2125CF816C355A3F25CBEFA)

When integrating **ReaderComponentController**, the initialization API must be executed before other APIs of the controller.

**Atomic service API**: This API can be used in atomic services since API version 5.0.4(16).

**System capability**: SystemCapability.Reader.ReaderService.ReaderCore

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

context

 | 

common.[UIAbilityContext](../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/uiabilitycontext/document.md)

 | 

Yes

 | 

App context.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<void>

 | 

Promise object. No result is returned.

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

[1016910004](../../arkts-api-error-codes/document.md#section11556619102)

 | 

Invalid caller.

 |

**Example**:

import { readerCore, ReadPageComponent } from '@kit.ReaderKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { common } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Reader {
  private readerComponentController: readerCore.ReaderComponentController = new readerCore.ReaderComponentController();

  aboutToAppear(): void {
    this.init();
  }

  private async init(){
    try {
      let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
      await this.readerComponentController.init(context);
      hilog.info(0x0000, 'testTag', \`init succeeded\`);
    } catch (err) {
      hilog.error(0x0000, 'testTag', \`failed to init, Code is ${err.code}, message is ${err.message}\`);
    }
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

#### \[h2\]registerBookParser

registerBookParser(bookParserHandler: bookParser.BookParserHandler): void

Registers a book parser.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9f/v3/Lz_GSMlpSSmds7tHDnnRSA/caution_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062518Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=AFCEDF4A2D09DA326E67ADCFEDD741350843D5BF99106D2AAEA6F16860BEB3BA)

The **registerBookParser** API must be called before the [startPlay](#section3667128165411) API. Otherwise, an error will be reported.

**Atomic service API**: This API can be used in atomic services since API version 5.0.4(16).

**System capability**: SystemCapability.Reader.ReaderService.ReaderCore

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

bookParserHandler

 | 

bookParser.[BookParserHandler](../bookparser-book-parsing-capability/document.md#section59035422210)

 | 

Yes

 | 

Book parser.

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

[1016900002](../../arkts-api-error-codes/document.md#section174762013118)

 | 

Read Page Component is not initialized.

 |
| 

[1016900003](../../arkts-api-error-codes/document.md#section16343120935)

 | 

Invalid request.

 |
| 

[1016900999](../../arkts-api-error-codes/document.md#section14689171516514)

 | 

Other error.

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

  aboutToAppear(): void {
    this.registerBookParser();
  }

  private async registerBookParser(){
    try {
      // Initialize the book parser for the book file that has been imported to the [app sandbox directory](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/app-sandbox-directory).
      let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
      let filePath: string = \`${context.filesDir}/abc.epub\`;
      let bookParserHandler: bookParser.BookParserHandler = await bookParser.getDefaultHandler(filePath);
      await this.readerComponentController.init(context);
      this.readerComponentController.registerBookParser(bookParserHandler);
      hilog.info(0x0000, 'testTag', \`registerBookParser succeeded\`);
    } catch (err) {
      hilog.error(0x0000, 'testTag', \`failed to registerBookParser, Code is ${err.code}, message is ${err.message}\`);
    }
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

#### \[h2\]setPageConfig

setPageConfig(pageConfig: ReaderSetting): void

Sets or modifies page typesetting attributes.

**Atomic service API**: This API can be used in atomic services since API version 5.0.4(16).

**System capability**: SystemCapability.Reader.ReaderService.ReaderCore

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

pageConfig

 | 

[ReaderSetting](#section13615732174218)

 | 

Yes

 | 

Page typesetting attributes.

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

[1016900002](../../arkts-api-error-codes/document.md#section174762013118)

 | 

Read Page Component is not initialized.

 |
| 

[1016900003](../../arkts-api-error-codes/document.md#section16343120935)

 | 

Invalid request.

 |
| 

[1016900999](../../arkts-api-error-codes/document.md#section14689171516514)

 | 

Other error.

 |

**Example**:

import { readerCore, ReadPageComponent } from '@kit.ReaderKit';
import { common } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { display } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Reader {
  private readerComponentController: readerCore.ReaderComponentController = new readerCore.ReaderComponentController();

  aboutToAppear(): void {
    this.setPageConfig();
  }

  private async setPageConfig(){
    try {
      let readerSetting: readerCore.ReaderSetting = {
      fontName: 'System font',
        fontPath: '',
        fontSize: 18,
        fontColor: '#000000',
        fontWeight: 400,
        lineHeight: 1.9,
        nightMode: false,
        themeColor: 'rgba(248, 249, 250, 1)',
        themeBgImg: '',
        flipMode: '0',
        scaledDensity: display.getDefaultDisplaySync().scaledDensity > 0 ? display.getDefaultDisplaySync().scaledDensity :
          1,
        viewPortWidth: 1260, // Viewport width. Obtain it based on the actual device characteristics. Otherwise, the reading page may have display issues.
        viewPortHeight: 2720, // Viewport height. Obtain it based on the actual device characteristics. Otherwise, the reading page may have display issues.
      };

      let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
      await this.readerComponentController.init(context);
      this.readerComponentController.setPageConfig(readerSetting);
      hilog.info(0x0000, 'testTag', \`setPageConfig succeeded\`);
    } catch (err) {
      hilog.error(0x0000, 'testTag', \`failed to setPageConfig, Code is ${err.code}, message is ${err.message}\`);
    }
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

#### \[h2\]startPlay

startPlay(spineIndex: number, domPos: string): Promise<void>

Opens a book at a specified reading progress. This API returns the result asynchronously through a promise.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4c/v3/qv5Mgc0FRj6LA5x2ujnmJw/caution_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062518Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=AB1757E6BF967451C8DB8BA8BB5119D4AAB6269944AEA6400949B2B0DCE30B32)

The **startPlay** API can be called only after the [registerBookParser](#section181215815104) event is triggered.

**Atomic service API**: This API can be used in atomic services since API version 5.0.4(16).

**System capability**: SystemCapability.Reader.ReaderService.ReaderCore

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

Content resource index ([SpineItem](../bookparser-book-parsing-capability/document.md#section1029864651619).index).

 |
| 

domPos

 | 

string

 | 

Yes

 | 

Last reading progress of a user.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<void>

 | 

Promise object. No result is returned.

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

[1016900002](../../arkts-api-error-codes/document.md#section174762013118)

 | 

Read Page Component is not initialized.

 |
| 

[1016900003](../../arkts-api-error-codes/document.md#section16343120935)

 | 

Invalid request.

 |
| 

[1016900999](../../arkts-api-error-codes/document.md#section14689171516514)

 | 

Other error.

 |
| 

[1016910001](../../arkts-api-error-codes/document.md#section13763141364)

 | 

Invalid spine item.

 |
| 

[1016910002](../../arkts-api-error-codes/document.md#section15116730175)

 | 

Unexpected spine item resource data.

 |
| 

[1016910003](../../arkts-api-error-codes/document.md#section216871194)

 | 

Spine item resource data out of range.

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

  aboutToAppear(): void {
    this.startPlay();
  }

  private async startPlay() {
    try {
      // Initialize the book parser for the book file that has been imported to the [app sandbox directory](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/app-sandbox-directory).
      let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
      let filePath: string = \`${context.filesDir}/abc.epub\`;
      let bookParserHandler: bookParser.BookParserHandler = await bookParser.getDefaultHandler(filePath);
      let spineList: bookParser.SpineItem\[\] = bookParserHandler.getSpineList();
      let spineIndex: number = spineList\[0\].index;
      let domPos: string = '';

      await this.readerComponentController.init(context);
      this.readerComponentController.registerBookParser(bookParserHandler);
    // Call the **startPlay** API to initialize the book content display.
      this.readerComponentController.startPlay(spineIndex || 0, domPos);
      hilog.info(0x0000, 'testTag', \`startPlay succeeded\`);
    } catch (err) {
      hilog.error(0x0000, 'testTag', \`failed to startPlay, Code is ${err.code}, message is ${err.message}\`);
    }
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

#### \[h2\]flipPage

flipPage(isNext: boolean): void

Triggers [ReadPageComponent](../../arkts-components/readpagecomponent-reading-page-component/document.md#section3730195311450) to turn pages.

**Atomic service API**: This API can be used in atomic services since API version 5.0.4(16).

**System capability**: SystemCapability.Reader.ReaderService.ReaderCore

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

isNext

 | 

boolean

 | 

Yes

 | 

Indicates whether to turn to the next page.

**true**: Turn to the next page.

**false**: Turn to the previous page.

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

[1016900002](../../arkts-api-error-codes/document.md#section174762013118)

 | 

Read Page Component is not initialized.

 |
| 

[1016900003](../../arkts-api-error-codes/document.md#section16343120935)

 | 

Invalid request.

 |
| 

[1016900999](../../arkts-api-error-codes/document.md#section14689171516514)

 | 

Other error.

 |

**Example**:

import { readerCore, ReadPageComponent } from '@kit.ReaderKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { common } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Reader {
  private readerComponentController: readerCore.ReaderComponentController = new readerCore.ReaderComponentController();

  aboutToAppear(): void {
    this.flipPage();
  }

  private async flipPage(){
    try {
      let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
      await this.readerComponentController.init(context);
    // Turn to the next page.
      this.readerComponentController.flipPage(true);
      hilog.info(0x0000, 'testTag', \`flipPage succeeded\`);
    } catch (err) {
      hilog.error(0x0000, 'testTag', \`failed to flipPage, Code is ${err.code}, message is ${err.message}\`);
    }
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

#### \[h2\]releaseBook

releaseBook(): void

Releases book resources, used in scenarios such as exiting a reader.

**Atomic service API**: This API can be used in atomic services since API version 5.0.4(16).

**System capability**: SystemCapability.Reader.ReaderService.ReaderCore

**Start version**: 5.0.4(16)

**Example**:

import { readerCore, ReadPageComponent } from '@kit.ReaderKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { common } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Reader {
  private readerComponentController: readerCore.ReaderComponentController = new readerCore.ReaderComponentController();

  aboutToAppear(): void {
    this.releaseBook();
  }

  private async releaseBook(){
    try {
      let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
      await this.readerComponentController.init(context);
    // Release the resources used for loading the book.
      this.readerComponentController.releaseBook();
      hilog.info(0x0000, 'testTag', \`releaseBook succeeded\`);
    } catch (err) {
      hilog.error(0x0000, 'testTag', \`failed to releaseBook, Code is ${err.code}, message is ${err.message}\`);
    }
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

#### \[h2\]on('pageShow')

on(type: 'pageShow', callback: Callback<PageDataInfo>): void

Registers a callback for the chapter content pagination display result.

**Atomic service API**: This API can be used in atomic services since API version 5.0.4(16).

**System capability**: SystemCapability.Reader.ReaderService.ReaderCore

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

type

 | 

string

 | 

Yes

 | 

Event type, which is **pageShow** in this case.

 |
| 

callback

 | 

Callback<[PageDataInfo](#section1064382518239)\>

 | 

Yes

 | 

Callback function, which returns the content pagination layout information.

 |

**Example**:

import { readerCore, ReadPageComponent } from '@kit.ReaderKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { common } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Reader {
  private readerComponentController: readerCore.ReaderComponentController = new readerCore.ReaderComponentController();

  aboutToAppear(): void {
    this.registerListener();
  }

  private async registerListener(){
    try {
      let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
      await this.readerComponentController.init(context)
      // This is only a sample method call. To actually trigger the callback, you must use the **startPlay** API.
      this.readerComponentController.on('pageShow', (data: readerCore.PageDataInfo): void => {
      // You can save the content pagination layout data here, and use **data.resourceIndex** and **data.startDomPos** to call the **startPlay** API to open a book at a specified reading progress.
        hilog.info(0x0000, 'testTag', 'pageshow: data is: ' + JSON.stringify(data));
      });
    } catch (err) {
      hilog.error(0x0000, 'testTag', \`failed to registerListener, Code is ${err.code}, message is ${err.message}\`);
    }
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

#### \[h2\]off('pageShow')

off(type: 'pageShow', callback?: Callback<PageDataInfo>): void

Deregisters a callback for the chapter content pagination display result. This API can be called when a page is destroyed.

**Atomic service API**: This API can be used in atomic services since API version 5.0.4(16).

**System capability**: SystemCapability.Reader.ReaderService.ReaderCore

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

type

 | 

string

 | 

Yes

 | 

Event type, which is **pageShow** in this case.

 |
| 

callback

 | 

Callback<[PageDataInfo](#section1064382518239)\>

 | 

No

 | 

Callback function, which must be the same as that passed for **on('pageShow')**. If this parameter is not passed, all callback functions are deregistered.

 |

**Example**:

import { readerCore, ReadPageComponent } from '@kit.ReaderKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { common } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Reader {
  private readerComponentController: readerCore.ReaderComponentController = new readerCore.ReaderComponentController();

  aboutToAppear(): void {
    this.unregisterListener();
  }

  private async unregisterListener(){
    try {
      let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
      let readerComponentController: readerCore.ReaderComponentController = new readerCore.ReaderComponentController();
      await readerComponentController.init(context);
      readerComponentController.off('pageShow');
      hilog.info(0x0000, 'testTag', \`offPageShow succeeded\`);
    } catch (err) {
      hilog.error(0x0000, 'testTag', \`failed to unregisterListener, Code is ${err.code}, message is ${err.message}\`);
    }
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

#### \[h2\]on('resourceRequest')

on(type: 'resourceRequest', callback: bookParser.CallbackRes<string, ArrayBuffer>): void

Registers a resource request callback. If a custom background or font is set, the typesetting engine uses this API to obtain the resource **ArrayBuffer**.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/95/v3/Ju7y8hspT9uS8RFWnMuAuw/caution_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062518Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=05E1972E6C32554AEDFF024D2BE9A99E8FBC0ABB04A8215C3019A3AE5F81C755)

When multiple resource request callbacks are registered, only the last registered callback will take effect.

**Atomic service API**: This API can be used in atomic services since API version 5.0.4(16).

**System capability**: SystemCapability.Reader.ReaderService.ReaderCore

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

type

 | 

string

 | 

Yes

 | 

Event type, which is **resourceRequest** in this case.

 |
| 

callback

 | 

bookParser.[CallbackRes](../bookparser-book-parsing-capability/document.md#section174676520576)<string, ArrayBuffer>

 | 

Yes

 | 

Callback function (**string**: path of the requested resource; **ArrayBuffer**: binary data of the requested resource).

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
  // Replace the value with the path to the font file, including the file name.
  private selectFontPath = 'fonts/SourceHanSerifCN-VF.ttf';

  aboutToAppear(): void {
    this.registerListener();
  }

  private async registerListener(){
    try {
      let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
      await this.readerComponentController.init(context);
      // This is only a sample method call. To actually trigger the callback, you must use the **startPlay** API.
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

#### \[h2\]off('resourceRequest')

off(type: 'resourceRequest', callback?: bookParser.CallbackRes<string, ArrayBuffer>): void

Deregisters a resource request callback. This API can be called when a page is destroyed.

**Atomic service API**: This API can be used in atomic services since API version 5.0.4(16).

**System capability**: SystemCapability.Reader.ReaderService.ReaderCore

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

type

 | 

string

 | 

Yes

 | 

Event type, which is **resourceRequest** in this case.

 |
| 

callback

 | 

bookParser.[CallbackRes](../bookparser-book-parsing-capability/document.md#section174676520576)<string, ArrayBuffer>

 | 

No

 | 

Callback function, which must be the same as that passed for **on('resourceRequest')**. If this parameter is not passed, all callback functions are deregistered.

 |

**Example**:

import { readerCore, ReadPageComponent } from '@kit.ReaderKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { common } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Reader {
  private readerComponentController: readerCore.ReaderComponentController = new readerCore.ReaderComponentController();

  aboutToAppear(): void {
    this.unregisterListener();
  }

  private async unregisterListener(){
    try {
      let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
      await this.readerComponentController.init(context);
      this.readerComponentController.off('resourceRequest');
      hilog.info(0x0000, 'testTag', \`offResourceRequest succeeded\`);
    } catch (err) {
      hilog.error(0x0000, 'testTag', \`failed to unregisterListener, Code is ${err.code}, message is ${err.message}\`);
    }
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
