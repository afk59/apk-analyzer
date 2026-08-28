# Notifying the Reading Progress

Upon page display, the page rendering information is returned through the page display callback API. The page rendering information contains the **domPos** and **resourceIndex** attributes. You can save the attributes to the database for reading progress navigation.

#### API Description

This function involves two APIs. See the following table for detailed API information.

| 
API

 | 

Description

 |
| :-- | :-- |
| 

[on('pageShow')](https://developer.huawei.com/consumer/en/doc/harmonyos-references/reader-read-core#section1657755491213)

 | 

Registers a callback for the chapter content pagination result.

 |
| 

[off('pageShow')](https://developer.huawei.com/consumer/en/doc/harmonyos-references/reader-read-core#section18368173691416)

 | 

Deregisters a callback for the chapter content pagination result. This API can be called when a page is destroyed.

 |

#### Preparations

Before listening to reading progress notifications, ensure that you have [built a reader](../../book-content-typesetting/building-a-reader/document.md).

#### Development Procedure

1.  Listen to the page display callback through **ReaderComponentController**.
    
    The typesetting engine calls the **on('pageShow')** API to return the page rendering information after rendering the page. The **domPos** and **resourceIndex** attributes in the page rendering information are used to identify the reading progress.
    
    You can save the reading progress to the database through the **on('pageShow')** API callback in real time, preventing progress loss if a user exits the reader unexpectedly. When the user returns to reading, you can pass the saved **domPos** and **resourceIndex** attributes to the [startPlay](https://developer.huawei.com/consumer/en/doc/harmonyos-references/reader-read-core#section3667128165411) API to restore the reading progress.
    
    aboutToAppear(): void {
      this.setOnPageShowListener();
    }
    
    private async setOnPageShowListener(){
      try {
          this.readerComponentController.on('pageShow', (data: readerCore.PageDataInfo): void => {
          // You can save the content pagination data here, and pass the **data.resourceIndex** and **data.startDomPos** values to the **startPlay** API to resume reading when required.
          hilog.info(0x0000, 'testTag', 'pageshow: data is: ' + JSON.stringify(data));
        });
      } catch (err) {
        hilog.error(0x0000, 'testTag', \`failed to init, Code is ${err.code}, message is ${err.message}\`);
      }
    }
    
2.  When a page is destroyed, call the API for deregistering page display.
    
    aboutToDisappear(): void {
      this.readerComponentController.off('pageShow');
    }
