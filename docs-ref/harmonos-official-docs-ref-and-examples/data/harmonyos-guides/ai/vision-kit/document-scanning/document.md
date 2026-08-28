# Document Scanning

#### Use Cases

The document scanning control provides the service of taking photos of documents and converting them into high-definition scanned copies. Users can capture document photos, and these photos can be automatically cropped, optimized, and then saved or shared as images or PDF files. Users can also use this service to identify tables from photos just taken or in the gallery and generate table documents.

It can be widely used in education and office scenarios. Users can scan documents, bills, class presentations, and books, generate images or PDF files, and then send or archive them.

**Figure 1** Document scanning example  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f8/v3/z3I5c4GyRzSoKZZTZ_czjQ/en-us_image_0000002271471913.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062129Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=051D9285A97D32098C86A8D49D812A7B5DA499189997415089068C1A400E37A0 "Click to enlarge")

#### Restrictions

-   Supported languages: simplified Chinese and English
-   Currently, document scanning supports only phones and tablets.
-   This control should not be blocked by another component or window.

#### API Description

The following lists only some main APIs called in the demo. For details about all APIs, please refer to the [API Reference](https://developer.huawei.com/consumer/en/doc/harmonyos-references/vision-document-scanner).

| 
API

 | 

Description

 |
| :-- | :-- |
| 

[DocumentScanner](https://developer.huawei.com/consumer/en/doc/harmonyos-references/vision-document-scanner#section143611912403)

 | 

Document scanning control.

 |
| 

[DocumentScannerResultCallback](https://developer.huawei.com/consumer/en/doc/harmonyos-references/vision-document-scanner#section3361123418402)

 | 

Document scanning result.

 |

#### Development Procedure

1.  Add classes related to the document scanning control to a project.
    
    import { DocType, DocumentScanner, DocumentScannerConfig, SaveOption, FilterId, ShootingMode } from "@kit.VisionKit";
    
2.  Configure the layout, set the attributes of the document scanning control based on the service scenario, and obtain the returned document image URI list.
    
    import { hilog } from '@kit.PerformanceAnalysisKit';
    
    const TAG = 'DocumentScanner'
    
    @Entry
    @Component
    struct Index {
      private docScanConfig = new DocumentScannerConfig()
    
      aboutToAppear() {
        this.docScanConfig.supportType = \[DocType.DOC, DocType.SHEET\]
        this.docScanConfig.isGallerySupported = true
        this.docScanConfig.editTabs = \[\]
        this.docScanConfig.maxShotCount = 3
        this.docScanConfig.defaultFilterId = FilterId.ORIGINAL
        this.docScanConfig.defaultShootingMode = ShootingMode.MANUAL
        this.docScanConfig.isShareable = true
        this.docScanConfig.originalUris = \[\]
      }
    
      build() {
        Column() {
          DocumentScanner({
            scannerConfig: this.docScanConfig,
            onResult: (code: number, saveType: SaveOption, uris: string\[\]) => {
              hilog.info(0x0001, TAG, \`result code: ${code}, save: ${saveType}\`)
              uris.forEach(uriString => {
                hilog.info(0x0001, TAG, \`uri: ${uriString}\`)
              })
            }
          }).size({ width: '100%', height: '100%' })
        }
        .height('100%')
        .width('100%')
      }
    }
    

#### Development Example

## Index.ets

// The development example of document scanning is implemented on two screens. One is the entry screen, and the other is the implementation screen.
// The entry screen needs to introduce the implementation screen. In the following example, the implementation screen file name is **DocDemoPage**.
import { DocDemoPage } from './DocDemoPage'

@Entry
@Component
struct MainPage {
  @Provide('pathStack') pathStack: NavPathStack = new NavPathStack()

  @Builder
  PageMap(name: string) {
    if (name === 'documentScanner') {
      DocDemoPage()
    }
  }

  // Button on the document scanning entry screen.
  build() {
    Navigation(this.pathStack) {
      Button('DocumentScanner', { stateEffect: true, type: ButtonType.Capsule })
        .width('50%')
        .height(40)
        .onClick(() => {
          this.pathStack.pushPath({ name: 'documentScanner' })
        })
    }.title('Document scanning control demo').navDestination(this.PageMap)
    .mode(NavigationMode.Stack)
  }
}

## DocDemoPage.ets

// Document scanning implementation screen, and its file name is **DocDemoPage**. This screen needs to be introduced by the entry screen.
import {
  DocType,
  DocumentScanner,
  DocumentScannerConfig,
  SaveOption,
  FilterId,
  ShootingMode
} from "@kit.VisionKit"
import { hilog } from '@kit.PerformanceAnalysisKit';

const TAG: string = 'DocDemoPage'

// Document scanning screen, which is used to load **uiExtensionAbility**.
@Component
export struct DocDemoPage {
  @State docImageUris: string\[\] = \[\]
  @Consume('pathStack') pathStack: NavPathStack
  private docScanConfig = new DocumentScannerConfig()

  aboutToAppear() {
    this.docScanConfig.supportType = \[DocType.DOC, DocType.SHEET\]
    this.docScanConfig.isGallerySupported = true
    this.docScanConfig.editTabs = \[\]
    this.docScanConfig.maxShotCount = 3
    this.docScanConfig.defaultFilterId = FilterId.ORIGINAL
    this.docScanConfig.defaultShootingMode = ShootingMode.MANUAL
    this.docScanConfig.isShareable = true
    this.docScanConfig.originalUris = \[\]
  }

  build() {
    NavDestination() {
      Stack({ alignContent: Alignment.Top }) {
      // Display the document scanning result.
        List() {
          ForEach(this.docImageUris, (uri: string) => {
            ListItem() {
              Image(uri)
                .objectFit(ImageFit.Contain)
                .width(100)
                .height(100)
            }
          })
        }
        .listDirection(Axis.Vertical)
        .alignListItem(ListItemAlign.Center)
        .margin({
          top: 50
        })
        .width('80%')
        .height('80%')
        
        // Document scanning.
        DocumentScanner({
          scannerConfig: this.docScanConfig,
          onResult: (code: number, saveType: SaveOption, uris: string\[\]) => {
            hilog.info(0x0001, TAG, \`result code: ${code}, save: ${saveType}\`)
            if (code === -1) {
              this.pathStack.pop()
            }
            uris.forEach(uriString => {
              hilog.info(0x0001, TAG, \`uri: ${uriString}\`)
            })
            this.docImageUris = uris
          }
        })
          .size({ width: '100%', height: '100%' })
      }
      .width('100%')
      .height('100%')
    }
    .width('100%')
    .height('100%')
    .hideTitleBar(true)
  }
}
