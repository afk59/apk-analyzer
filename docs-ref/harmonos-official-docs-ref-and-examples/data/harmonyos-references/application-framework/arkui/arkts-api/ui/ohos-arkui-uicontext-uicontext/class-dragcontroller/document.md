# Class (DragController)

Provides APIs for initiating drag actions. When receiving a gesture event, such as a touch or long-press event, an application can initiate a drag action and carry drag information therein.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/71/v3/GpmMn4vTSfu0CLTobHK7qQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062227Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6B6AD175B69807C5B12089B012C6C921A1115772F5820BE9247913112DB24DFB)

-   The initial APIs of this module are supported since API version 10. Newly added APIs will be marked with a superscript to indicate their earliest API version.
    
-   The initial APIs of this class are supported since API version 11.
    
-   In the following API examples, you must first use [getDragController()](../class-uicontext/document.md#getdragcontroller11) in **UIContext** to obtain a **DragController** instance, and then call the APIs using the obtained instance.
    

#### executeDrag11+

executeDrag(custom: CustomBuilder | DragItemInfo, dragInfo: dragController.DragInfo, callback: AsyncCallback<dragController.DragEventParam>): void

Initiates a drag action, with the object to be dragged and the drag information passed in. This API uses a callback to return the drag event result.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| custom | [CustomBuilder](../../../../arkts-components/common-definitions/basic-types/document.md#custombuilder8) | [DragItemInfo](../../../../arkts-components/universal-events/interaction-response-events/drag-event/document.md#dragiteminfo) | Yes | 
Object to be dragged.

**NOTE**

The global builder is not supported. If the [Image](../../../../arkts-components/images-and-videos/image/document.md) component is used in the builder, enable synchronous loading, that is, set the [syncLoad](../../../../arkts-components/images-and-videos/image/document.md#syncload8) attribute of the component to **true**. The builder is used only to generate the image displayed during the current dragging. If the root component of the builder has zero width or height, it will cause failure in drag image generation, which in turn breaks the entire drag operation. Changes to the builder, if any, apply to the next dragging, but not to the current dragging.

 |
| dragInfo | [dragController.DragInfo](../../ohos-arkui-dragcontroller-dragcontroller/document.md#draginfo) | Yes | Drag information. |
| callback | [AsyncCallback](../../../../../../system/basic-functions/basic-services-kit/arkts-apis/others/ohos-base-public-callback-information/document.md#asynccallback)<[dragController.DragEventParam](../../ohos-arkui-dragcontroller-dragcontroller/document.md#drageventparam12)\> | Yes | 

Callback used to return the result.

\- **event**: drag event information that includes only the drag result.

\- **extraParams**: extra information about the drag event.

 |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.Incorrect parameters types; 3. Parameter verification failed. |
| 100001 | Internal handling failed. |

**Example**

import { dragController } from '@kit.ArkUI';
import { unifiedDataChannel } from '@kit.ArkData';

class DragInfo {
  event: DragEvent | undefined = undefined;
  extraParams: string = '';
}

@Entry
@Component
struct DragControllerPage {
  @Builder
  DraggingBuilder() {
    Column() {
      Text("DraggingBuilder")
    }
    .width(100)
    .height(100)
    .backgroundColor(Color.Blue)
  }

  build() {
    Column() {
      Button('touch to execute drag')
        .onTouch((event?: TouchEvent) => {
          if (event) {
            if (event.type == TouchType.Down) {
              let text = new unifiedDataChannel.Text();
              let unifiedData = new unifiedDataChannel.UnifiedData(text);

              let dragInfo: dragController.DragInfo = {
                pointerId: 0,
                data: unifiedData,
                extraParams: ''
              };
              let eve: DragInfo = new DragInfo();
              this.getUIContext().getDragController().executeDrag(() => {
                this.DraggingBuilder()
              }, dragInfo, (err, eve) => {
                if (eve.event) {
                  if (eve.event.getResult() == DragResult.DRAG\_SUCCESSFUL) {
                    // ...
                  } else if (eve.event.getResult() == DragResult.DRAG\_FAILED) {
                    // ...
                  }
                }
              })
            }
          }
        })
    }
    .width('100%')
    .height('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c7/v3/uMT_jYonRBWKL1FzNNiCbA/en-us_image_0000002568765049.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062227Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F221F933310A1B367FA63D4F0C6A8F359451DD647BDA3C948F297558E8C44F4B)

#### executeDrag11+

executeDrag(custom: CustomBuilder | DragItemInfo, dragInfo: dragController.DragInfo): Promise<dragController.DragEventParam>

Initiates a drag action, with the object to be dragged and the drag information passed in. This API uses a promise to return the drag event result.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| custom | [CustomBuilder](../../../../arkts-components/common-definitions/basic-types/document.md#custombuilder8) | [DragItemInfo](../../../../arkts-components/universal-events/interaction-response-events/drag-event/document.md#dragiteminfo) | Yes | Object to be dragged. |
| dragInfo | [dragController.DragInfo](../../ohos-arkui-dragcontroller-dragcontroller/document.md#draginfo) | Yes | Drag information. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[dragController.DragEventParam](../../ohos-arkui-dragcontroller-dragcontroller/document.md#drageventparam12)\> | 
Callback used to return the result.

\- **event**: drag event information that includes only the drag result.

\- **extraParams**: extra information about the drag event.

 |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.Incorrect parameters types; 3. Parameter verification failed. |
| 100001 | Internal handling failed. |

**Example**

import { dragController } from '@kit.ArkUI';
import { image } from '@kit.ImageKit';
import { unifiedDataChannel } from '@kit.ArkData';

class DragInfo {
  event: DragEvent | undefined = undefined;
  extraParams: string = '';
}

@Entry
@Component
struct DragControllerPage {
  @State pixmap: image.PixelMap | null = null;

  @Builder
  DraggingBuilder() {
    Column() {
      Text("DraggingBuilder")
    }
    .width(100)
    .height(100)
    .backgroundColor(Color.Blue)
  }

  @Builder
  PixmapBuilder() {
    Column() {
      Text("PixmapBuilder")
    }
    .width(100)
    .height(100)
    .backgroundColor(Color.Blue)
  }

  build() {
    Column() {
      Button('touch to execute drag')
        .onTouch((event?: TouchEvent) => {
          if (event) {
            if (event.type == TouchType.Down) {
              let text = new unifiedDataChannel.Text();
              let unifiedData = new unifiedDataChannel.UnifiedData(text);

              let dragInfo: dragController.DragInfo = {
                pointerId: 0,
                data: unifiedData,
                extraParams: ''
              };
              let pb: CustomBuilder = (): void => {
                this.PixmapBuilder()
              };
              this.getUIContext().getComponentSnapshot().createFromBuilder(pb).then((pix: image.PixelMap) => {
                this.pixmap = pix;
                let dragItemInfo: DragItemInfo = {
                  pixelMap: this.pixmap,
                  builder: () => {
                    this.DraggingBuilder()
                  },
                  extraInfo: "DragItemInfoTest"
                };
                let eve: DragInfo = new DragInfo();
                this.getUIContext()
                  .getDragController()
                  .executeDrag(dragItemInfo, dragInfo)
                  .then((eve) => {
                    if (eve.event.getResult() == DragResult.DRAG\_SUCCESSFUL) {
                      // ...
                    } else if (eve.event.getResult() == DragResult.DRAG\_FAILED) {
                      // ...
                    }
                  })
                  .catch((err: Error) => {
                  })
              })
            }
          }
        })
    }
    .width('100%')
    .height('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5f/v3/PlziWs80T_2BVw9dTbNYqQ/en-us_image_0000002537765324.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062227Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=863478F2C5035E9856429143ADE562FC6A60B4D978520E7B83C0F24387D7A92C)

#### createDragAction11+

createDragAction(customArray: Array<CustomBuilder | DragItemInfo>, dragInfo: dragController.DragInfo): dragController.DragAction

Creates a drag action object for initiating drag and drop operations. You need to explicitly specify one or more drag previews, the drag data, and the drag handle point. If a drag operation initiated by an existing drag action object is not completed, no new object can be created, and calling the API will throw an exception. After the lifecycle of the drag action object ends, the callback functions registered on this object become invalid. Therefore, it is necessary to hold this object within a longer scope and replace the old value with a new object returned by **createDragAction** before each drag initiation.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/85/v3/k5IVNfycQbicDi81GVmjPg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062227Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=70FBF904DF6A5720129A34EBADC080AD1D152023FA39675BFB11A05CEAB44A1A)

For optimal drag and drop performance, limit the number of drag previews.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| customArray | Array<[CustomBuilder](../../../../arkts-components/common-definitions/basic-types/document.md#custombuilder8) | [DragItemInfo](../../../../arkts-components/universal-events/interaction-response-events/drag-event/document.md#dragiteminfo)\> | Yes | Object to be dragged. |
| dragInfo | [dragController.DragInfo](../../ohos-arkui-dragcontroller-dragcontroller/document.md#draginfo) | Yes | Drag information. |

**Return value**

| Type | Description |
| :-- | :-- |
| [dragController.DragAction](../../ohos-arkui-dragcontroller-dragcontroller/document.md#dragaction11) | **DragAction** object, which is used to subscribe to drag state changes and start the drag service. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.Incorrect parameters types; 3. Parameter verification failed. |
| 100001 | Internal handling failed. |

**Example**

1.  In the **EntryAbility.ets** file, obtain the UI context and save it to LocalStorage.

import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { window, UIContext } from '@kit.ArkUI';

let uiContext: UIContext;
let localStorage: LocalStorage = new LocalStorage('uiContext');

export default class EntryAbility extends UIAbility {
  storage: LocalStorage = localStorage;

  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
    hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onCreate');
  }

  onDestroy(): void {
    hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onDestroy');
  }

  onWindowStageCreate(windowStage: window.WindowStage): void {
    // Main window is created, set main page for this ability
    hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onWindowStageCreate');

    windowStage.loadContent('pages/Index', this.storage, (err, data) => {
      if (err.code) {
        hilog.error(0x0000, 'testTag', 'Failed to load the content. Cause: %{public}s', JSON.stringify(err) ?? '');
        return;
      }
      hilog.info(0x0000, 'testTag', 'Succeeded in loading the content. Data: %{public}s', JSON.stringify(data) ?? '');
      windowStage.getMainWindow((err, data) => {
        if (err.code) {
          console.error(\`Failed to obtain the main window. Cause:${err.message}\`);
          return;
        }
        let windowClass: window.Window = data;
        uiContext = windowClass.getUIContext();
        this.storage.setOrCreate<UIContext>('uiContext', uiContext);
        // Obtain a UIContext instance.
      });
    });
  }

  onWindowStageDestroy(): void {
    // Main window is destroyed, release UI related resources
    hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onWindowStageDestroy');
  }

  onForeground(): void {
    // Ability has brought to foreground
    hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onForeground');
  }

  onBackground(): void {
    // Ability has back to background
    hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onBackground');
  }
}

1.  Call **this.getUIContext().getSharedLocalStorage()** to obtain the UI context and then use the **DragController** object obtained to perform subsequent operations.

import { dragController, componentSnapshot, UIContext, DragController } from '@kit.ArkUI';
import { image } from '@kit.ImageKit';
import { unifiedDataChannel } from '@kit.ArkData';

@Entry()
@Component
struct DragControllerPage {
  @State pixmap: image.PixelMap | null = null;
  private dragAction: dragController.DragAction | null = null;
  customBuilders: Array<CustomBuilder | DragItemInfo> = new Array<CustomBuilder | DragItemInfo>();
  storages = this.getUIContext().getSharedLocalStorage();

  @Builder
  DraggingBuilder() {
    Column() {
      Text("DraggingBuilder")
    }
    .width(100)
    .height(100)
    .backgroundColor(Color.Blue)
  }

  build() {
    Column() {
      Button('Drag Multiple Objects').onTouch((event?: TouchEvent) => {
        if (event) {
          if (event.type == TouchType.Down) {
            console.info("multi drag Down by listener");
            this.customBuilders.push(() => {
              this.DraggingBuilder()
            });
            this.customBuilders.push(() => {
              this.DraggingBuilder()
            });
            this.customBuilders.push(() => {
              this.DraggingBuilder()
            });
            let text = new unifiedDataChannel.Text();
            let unifiedData = new unifiedDataChannel.UnifiedData(text);
            let dragInfo: dragController.DragInfo = {
              pointerId: 0,
              data: unifiedData,
              extraParams: ''
            };
            try {
              let uiContext: UIContext = this.storages?.get<UIContext>('uiContext') as UIContext;
              this.dragAction = uiContext.getDragController().createDragAction(this.customBuilders, dragInfo);
              if (!this.dragAction) {
                console.info("listener dragAction is null");
                return;
              }
              this.dragAction.on('statusChange', (dragAndDropInfo) => {
                if (dragAndDropInfo.status == dragController.DragStatus.STARTED) {
                  console.info("drag has start");
                } else if (dragAndDropInfo.status == dragController.DragStatus.ENDED) {
                  console.info("drag has end");
                  if (!this.dragAction) {
                    return;
                  }
                  this.customBuilders.splice(0, this.customBuilders.length);
                  this.dragAction.off('statusChange');
                }
              })
              this.dragAction.startDrag().then(() => {
              }).catch((err: Error) => {
                console.error(\`start drag Error:${err.message}\`);
              })
            } catch (err) {
              console.error(\`create dragAction Error:${err.message}\`);
            }
          }
        }
      }).margin({ top: 20 })
    }
    .width('100%')
    .height('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ec/v3/gPXFFcwtROeXcxuw8fo0LQ/en-us_image_0000002537925264.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062227Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C8EFAF07FEAE70B77DCCBC461FE670F5D81B69AA748EA9066FC55C68AD8EFA19)

#### getDragPreview11+

getDragPreview(): dragController.DragPreview

Obtains the **DragPreview** object, which represents the preview displayed during a drag operation.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Return value**

| Type | Description |
| :-- | :-- |
| [dragController.DragPreview](../../ohos-arkui-dragcontroller-dragcontroller/document.md#dragpreview11) | **DragPreview** object. It provides the API for setting the preview style. It does not work in the **OnDrop** and **OnDragEnd** callbacks. |

**Error codes**: For details about universal error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md).

**Example**

See the example for [animate](../../ohos-arkui-dragcontroller-dragcontroller/document.md#animate11).

#### setDragEventStrictReportingEnabled12+

setDragEventStrictReportingEnabled(enable: boolean): void

Sets whether the **onDragLeave** callback of the parent component is triggered when an item is dragged from the parent to the child component.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| enable | boolean | Yes | Whether the **onDragLeave** callback of the parent component is triggered when an item is dragged from the parent to the child component. The value **true** means the **onDragLeave** callback of the parent component is triggered, and **false** means the opposite. |

**Example**

import { UIAbility } from '@kit.AbilityKit';
import { window, UIContext } from '@kit.ArkUI';

 export default class EntryAbility extends UIAbility {
   onWindowStageCreate(windowStage: window.WindowStage): void {
       windowStage.loadContent('pages/Index', (err, data) => {
         if (err.code) {
         return;
       }
       windowStage.getMainWindow((err, data) => {
         if (err.code) {
           return;
         }
         let windowClass: window.Window = data;
         let uiContext: UIContext = windowClass.getUIContext();
         uiContext.getDragController().setDragEventStrictReportingEnabled(true);
     });
   });
 }
}

#### cancelDataLoading15+

cancelDataLoading(key: string): void

Cancels the data loading initiated by the [startDataLoading](../../../../arkts-components/universal-events/interaction-response-events/drag-event/document.md#startdataloading15) API. This API can be called only after the drag is released.

**Atomic service API**: This API can be used in atomic services since API version 15.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| key | string | Yes | Identifier for the drag data. It is used to distinguish between different drag operations. The key can be obtained through the **startDataLoading** API. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [Drag Event Error Codes](../../../../error-codes/ui/drag-event-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. |
| 190004 | Operation failed. |

#### notifyDragStartRequest18+

notifyDragStartRequest(requestStatus: dragController.DragStartRequestStatus): void

Controls whether the application can initiate a drag operation.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| requestStatus | [dragController.DragStartRequestStatus](../../ohos-arkui-dragcontroller-dragcontroller/document.md#dragstartrequeststatus18) | Yes | Whether the application can initiate a drag operation. |

**Example**

// xxx.ets
import { unifiedDataChannel } from '@kit.ArkData';
import { image } from '@kit.ImageKit';
import { dragController } from '@kit.ArkUI';

@Entry
@Component
struct NormalEts {
  @State finished: boolean = false;
  @State timeout1: number = 1;
  @State pixmap: image.PixelMap | undefined = undefined;
  @State unifiedData1: unifiedDataChannel.UnifiedData | undefined = undefined;
  @State previewData: DragItemInfo | undefined = undefined;

  loadData() {
    // Set a 4-second delay before initiating a drag action.
    let timeout = setTimeout(() => {
      this.getUIContext().getComponentSnapshot().get("image1", (error: Error, pixmap: image.PixelMap) => {
        this.pixmap = pixmap;
        this.previewData = {
          pixelMap: this.pixmap
        };
      });

      let data: unifiedDataChannel.Image = new unifiedDataChannel.Image();
      data.imageUri = "app.media.startIcon";
      let unifiedData = new unifiedDataChannel.UnifiedData(data);
      this.unifiedData1 = unifiedData;

      this.getUIContext().getDragController().notifyDragStartRequest(dragController.DragStartRequestStatus.READY);
    }, 4000);
    this.timeout1 = timeout;
  }

  build() {
    Column({ space: 20 }) {
      Image($r("app.media.startIcon"))
        .width(150)
        .height(150)
        .id("image1")
        .draggable(true)
        .dragPreview(this.previewData)
        .onPreDrag((status: PreDragStatus) => {
          if (status == PreDragStatus.PREPARING\_FOR\_DRAG\_DETECTION) {
            this.loadData();
          } else {
            clearTimeout(this.timeout1);
          }
        })
        .onDragStart((event: DragEvent) => {
          if (this.finished == false) {
            this.getUIContext()
              .getDragController()
              // In the application data preparation phase, a drag action cannot be initiated.
              .notifyDragStartRequest(dragController.DragStartRequestStatus.WAITING);
          } else {
            event.setData(this.unifiedData1);
          }
        })
        .onDragEnd(() => {
          this.finished = false;
        })
    }
    .width('100%')
    .height(400)
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/17/v3/UvpchlVQRXqIEGhdH2O5YQ/en-us_image_0000002568685041.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062227Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5EC4CC3F66B373C48F9B22147139EB153FB963437BCFC77452DD6C21A581FB1A)

#### enableDropDisallowedBadge20+

enableDropDisallowedBadge(enabled: boolean): void

Specifies whether to enable the display of a disallowed badge when dragged content is incompatible with a component's configured [allowDrop](../../../../arkts-components/universal-attributes/interaction-properties/drag-and-drop-control/document.md#allowdrop) types. When a component can accept or process dragged data or returns **DragBehavior.COPY** to indicate copy mode processing, the drag preview shows a plus icon with data count badge. When the component returns **DragBehavior.MOVE** to indicate cut mode processing, only the data count badge appears. When this feature is enabled, the system automatically displays a disallowed badge during drag operations if the dragged data types are incompatible with the target component's allowed drop types. This API currently does not support [UIExtension](../../ohos-arkui-uiextension-uiextension/document.md).

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| enabled | boolean | Yes | Whether to enable the display of a disallowed badge when dragged content is incompatible with a component's configured [allowDrop](../../../../arkts-components/universal-attributes/interaction-properties/drag-and-drop-control/document.md#allowdrop) types. The value **true** means to enable the display of a disallowed badge, and **false** means the opposite. The default value is **false**. |

**Example**

This example demonstrates how to use the **enableDropDisallowedBadge** API to enable the display of a disallowed badge when dragged content is incompatible with the target component's allowed drop types.

1.  Call the **enableDropDisallowedBadge** API in **EntryAbility.ets** and set the **enabled** parameter to **true**.
    
    import { UIAbility } from '@kit.AbilityKit';
    import { window, UIContext } from '@kit.ArkUI';
    
     export default class EntryAbility extends UIAbility {
       onWindowStageCreate(windowStage: window.WindowStage): void {
           windowStage.loadContent('pages/Index', (err, data) => {
             if (err.code) {
             return;
           }
           windowStage.getMainWindow((err, data) => {
             if (err.code) {
               return;
             }
             let windowClass: window.Window = data;
             let uiContext: UIContext = windowClass.getUIContext();
             uiContext.getDragController().enableDropDisallowedBadge(true);
         });
       });
     }
    }
    
2.  Drag the icon to the blank area below in **Index.ets**. The drag-disallowed badge is displayed.
    
    @Entry
    @Component
    struct Index {
      build() {
        Column({ space: 20 }) {
          // Replace $r('app.media.startIcon') with the image resource file you use.
          Image($r('app.media.startIcon'))
            .width(120)
            .height(120)
          Text ('Invalid drop zone.')
          Column()
            .width('100%')
            .layoutWeight(1)
            .allowDrop(null)
            .onDrop(() => {
            })
        }.width('100%')
      }
    }
    

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fc/v3/k2XCGYH2QcuuBBO3n9uvKw/en-us_image_0000002568765051.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062227Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6783D74F4EC1540B45C402F31B68590F76382CBE40F9D3B1E207E626948B3749)
