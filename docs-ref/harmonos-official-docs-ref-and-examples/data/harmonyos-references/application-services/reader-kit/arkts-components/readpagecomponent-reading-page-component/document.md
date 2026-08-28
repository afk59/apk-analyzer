# ReadPageComponent (Reading Page Component)

This module provides **ReadPageComponent**. HarmonyOS apps can integrate this component to quickly build book reading capabilities.

**Start version**: 5.0.4(16)

#### Module Import

import { ReadPageComponent } from '@kit.ReaderKit';

#### ReadPageComponent

The reading page component supports the display of book content, offers a variety of page-turning interactions and animations, and provides the progress and behavior perception capabilities required by the reader during the page-turning process.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bb/v3/KtymcSorQvetiWAeivyzPg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062519Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3AA765FDB9FED4356198115861365E24DEF86912585149A6C7AD649D49F857CF)

-   This component can typeset and render book content by page based on [ReaderSetting](../../arkts-apis/readercore-reader-kit-core-capabilities/document.md#section13615732174218).
-   This component can adapt to different screen sizes (phones, PCs/2-in-1 devices, and tablets, in both landscape and portrait orientations). It allows users to tap or swipe to interact with the reader, and supports page turning in simulated or horizontal swipe mode as well as page turning animation.
-   This component supports the typesetting result notification capability. It provides the page typesetting result [PageDataInfo](../../arkts-apis/readercore-reader-kit-core-capabilities/document.md#section1064382518239) by page after a book is opened or page turning is triggered.

**Decorator type**: @Component

**Atomic service API**: This API can be used in atomic services since API version 5.0.4(16).

**System capability**: SystemCapability.Reader.ReaderService.ReaderCore

**Start version**: 5.0.4(16)

**Parameters**:

| 
Parameter

 | 

Type

 | 

Decorator Type

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

controller

 | 

[ReaderComponentController](../../arkts-apis/readercore-reader-kit-core-capabilities/document.md#section1917812014110)

 | 

\_

 | 

**ReadPageComponent** controller.

 |
| 

readerCallback

 | 

AsyncCallback<readerCore.[ReaderComponentController](../../arkts-apis/readercore-reader-kit-core-capabilities/document.md#section1917812014110)\>

 | 

\_

 | 

Callback function.

 |

#### \[h2\]build

build(): void

Builder used to create a **ReadPageComponent** object.

**Atomic service API**: This API can be used in atomic services since API version 5.0.4(16).

**System capability**: SystemCapability.Reader.ReaderService.ReaderCore

**Start version**: 5.0.4(16)

**Example**:

import { bookParser, readerCore, ReadPageComponent } from '@kit.ReaderKit';
import { common } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Reader {
  private readerComponentController: readerCore.ReaderComponentController = new readerCore.ReaderComponentController();

  aboutToAppear(): void {
    this.init();
  }

  private async init() {
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
      this.readerComponentController.startPlay(spineIndex || 0, domPos);
      hilog.info(0x0000, 'testTag', \`startPlay succeeded\`);
    } catch (err) {
      hilog.error(0x0000, 'testTag', \`failed to startPlay, Code is ${err.code}, message is ${err.message}\`);
    }
  }

  aboutToDisappear(): void {
    this.readerComponentController.releaseBook();
  }

  build() {
    Stack() {
      ReadPageComponent({
        controller: this.readerComponentController,
        readerCallback: (err: BusinessError, data: readerCore.ReaderComponentController) => {
          this.readerComponentController = data;
        }
      })
    }.width('100%').height('100%').onClick(() => {
      // Implement the function of displaying the menu after tapping.
    })
  }
}
