# @ohos.arkui.dragController (DragController)

This module provides APIs for initiating drag actions. When receiving a gesture event, such as a touch or long-press event, an application can initiate a drag action and carry drag information therein.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/23/v3/nANF23t3QueYQajjAe2lug/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062226Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=FAE4E2DCB4596A0A5B6ADBF975C37459C7665F549F1A66AE1B75005AFF54A7A1)

-   The initial APIs of this module are supported since API version 10. Newly added APIs will be marked with a superscript to indicate their earliest API version.
    
-   The functionality of this module depends on UI context. This means that the APIs of this module cannot be used where [the UI context is ambiguous](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-global-interface#ambiguous-ui-context). For details, see [UIContext](../ohos-arkui-uicontext-uicontext/class-uicontext/document.md).
    
-   You can preview how this component looks on a real device, but not in DevEco Studio Previewer.
    

#### Modules to Import

import { dragController } from '@kit.ArkUI';

#### dragController.executeDrag(deprecated)

executeDrag(custom: CustomBuilder | DragItemInfo, dragInfo: DragInfo,callback:AsyncCallback<DragEventParam>): void

Initiates a drag action, with the object to be dragged and the drag information passed in. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/36/v3/z66yffr1QRezVD5VBI17Ag/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062226Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7361FE2D5A8CA03FD7C1E6FC1591EC51B239A22F5128852B75BCCC794738DD1B)

-   This API is supported since API version 10 and deprecated since API version 18. You are advised to use [executeDrag](../ohos-arkui-uicontext-uicontext/class-dragcontroller/document.md#executedrag11) instead. Before calling this API, you need to obtain the [DragController](../ohos-arkui-uicontext-uicontext/class-dragcontroller/document.md) instance using the [getDragController](../ohos-arkui-uicontext-uicontext/class-uicontext/document.md#getdragcontroller11) method in [UIContext](../ohos-arkui-uicontext-uicontext/class-uicontext/document.md).
    
-   Since API version 11, you can use the [getDragController](../ohos-arkui-uicontext-uicontext/class-uicontext/document.md#getdragcontroller11) API in [UIContext](../ohos-arkui-uicontext-uicontext/class-uicontext/document.md) to obtain the [DragController](../ohos-arkui-uicontext-uicontext/class-dragcontroller/document.md) object associated with the current UI context.
    

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| custom | [CustomBuilder](../../../arkts-components/common-definitions/basic-types/document.md#custombuilder8) | [DragItemInfo](../../../arkts-components/universal-events/interaction-response-events/drag-event/document.md#dragiteminfo) | Yes | 
Object to be dragged.

**NOTE**

The global builder is not supported. If the [Image](../../../arkts-components/images-and-videos/image/document.md) component is used in the builder, enable synchronous loading, that is, set the [syncLoad](../../../arkts-components/images-and-videos/image/document.md#syncload8) attribute of the component to **true**. The builder is used only to generate the image displayed during the current dragging. If the root component of the builder has zero width or height, it will cause failure in drag image generation, which in turn breaks the entire drag operation. Changes to the builder, if any, apply to the next dragging, but not to the current dragging.

 |
| dragInfo | [DragInfo](#draginfo) | Yes | Drag information. |
| callback | [AsyncCallback](../../../../../system/basic-functions/basic-services-kit/arkts-apis/others/ohos-base-public-callback-information/document.md#asynccallback)<[DragEventParam](#drageventparam12)\> | Yes | Callback function. If the operation is successful, **err** is **undefined** and **data** is the **DragEventParam** object obtained. Otherwise, **err** is an error object. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.Incorrect parameters types; 3. Parameter verification failed. |
| 100001 | Internal handling failed. |

**Example**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f/v3/wub8wnO1S5edA3O7iju2nw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062226Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=57C06652321B919550F298771B1793609546BA8AAFF4EA22F9C0046199667E91)

You are advised to use the [getDragController](../ohos-arkui-uicontext-uicontext/class-uicontext/document.md#getdragcontroller11) to obtain the **DragController** object associated with the current UI context.

import { dragController } from '@kit.ArkUI';
import { unifiedDataChannel } from '@kit.ArkData';

class DragInfo {
  event: DragEvent | undefined = undefined;
  extraParams: string = '';
}

@Entry
@Component
struct DragControllerPage {
  @State text: string = ''

  @Builder
  DraggingBuilder() {
    Column() {
      Text("DraggingBuilder")
        .fontColor(Color.White)
        .fontSize(12)
    }
    .width(100)
    .height(100)
    .backgroundColor(Color.Blue)
  }

  build() {
    Column() {
      Button('touch to execute drag')
        .margin(10)
        .onTouch((event?: TouchEvent) => {
          if (event) {
            if (event.type == TouchType.Down) {
              let text = new unifiedDataChannel.PlainText()
              text.textContent = 'drag text'
              text.abstract = 'abstract'
              let unifiedData = new unifiedDataChannel.UnifiedData(text)

              let dragInfo: dragController.DragInfo = {
                pointerId: 0,
                data: unifiedData,
                extraParams: ''
              }
              let eve: DragInfo = new DragInfo();
              this.getUIContext().getDragController().executeDrag(() => {
                this.DraggingBuilder()
              }, dragInfo, (err, eve) => { // You are advised to use this.getUIContext().getDragController().executeDrag().
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
      Text(this.text)
        .height(100)
        .width(150)
        .margin({ top: 20 })
        .border({ color: Color.Black, width: 1 })
        .onDrop((dragEvent?: DragEvent) => {
          if (dragEvent) {
            let records: Array<unifiedDataChannel.UnifiedRecord> = dragEvent.getData().getRecords();
            let plainText: unifiedDataChannel.PlainText = records\[0\] as unifiedDataChannel.PlainText;
            this.text = plainText.textContent;
          }
        })
    }
    .width('100%')
    .height('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c2/v3/U0udJ-kxRxiZX6MBrBT9HQ/en-us_image_0000002568685033.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062226Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=844B912E453448D8D47691FC187B9B35DFAA12943CFD19363E3514452F890365)

#### dragController.executeDrag(deprecated)

executeDrag(custom: CustomBuilder | DragItemInfo, dragInfo: DragInfo): Promise<DragEventParam>

Initiates a drag action, with the object to be dragged and the drag information passed in. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d1/v3/6yIBQlFATaGvzQ7p40wbuA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062226Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=77D932B6ECDEE56D05BD1CD4E609277C55B1F86DEBFF1F77FA40602D63174635)

-   This API is supported since API version 10 and deprecated since API version 18. You are advised to use [executeDrag](../ohos-arkui-uicontext-uicontext/class-dragcontroller/document.md#executedrag11-1) instead. Before calling this API, you need to obtain the [DragController](../ohos-arkui-uicontext-uicontext/class-dragcontroller/document.md) instance using the [getDragController](../ohos-arkui-uicontext-uicontext/class-uicontext/document.md#getdragcontroller11) method in [UIContext](../ohos-arkui-uicontext-uicontext/class-uicontext/document.md).
    
-   Since API version 11, you can use the [getDragController](../ohos-arkui-uicontext-uicontext/class-uicontext/document.md#getdragcontroller11) API in [UIContext](../ohos-arkui-uicontext-uicontext/class-uicontext/document.md) to obtain the [DragController](../ohos-arkui-uicontext-uicontext/class-dragcontroller/document.md) object associated with the current UI context.
    

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| custom | [CustomBuilder](../../../arkts-components/common-definitions/basic-types/document.md#custombuilder8) | [DragItemInfo](../../../arkts-components/universal-events/interaction-response-events/drag-event/document.md#dragiteminfo) | Yes | Object to be dragged. |
| dragInfo | [DragInfo](#draginfo) | Yes | Drag information. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[DragEventParam](#drageventparam12)\> | Promise used to return the result. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.Incorrect parameters types; 3. Parameter verification failed. |
| 100001 | Internal handling failed. |

**Example**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3d/v3/ZkSBWzJkSQWw7D1hEPVCRQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062226Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D875E41222096CA1C52C9E0EA30CBC21BDA48C2E6195F3A39315C5BE3B2BBC17)

You are advised to use the [getDragController](../ohos-arkui-uicontext-uicontext/class-uicontext/document.md#getdragcontroller11) to obtain the **DragController** object associated with the current UI context.

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
  @State pixmap: image.PixelMap | undefined = undefined
  @State text: string = ''

  @Builder
  DraggingBuilder() {
    Column() {
      Text("DraggingBuilder")
        .fontColor(Color.White)
    }
    .width(100)
    .height(100)
    .backgroundColor(Color.Blue)
  }

  @Builder
  PixmapBuilder() {
    Column() {
      Text("PixmapBuilder")
        .fontColor(Color.White)
        .fontSize(15)
    }
    .width(100)
    .height(100)
    .backgroundColor(Color.Blue)
  }

  aboutToAppear() {
    let pb: CustomBuilder = (): void => {
      this.PixmapBuilder()
    }
    this.getUIContext().getComponentSnapshot().createFromBuilder(pb).then((pix: image.PixelMap) => {
      this.pixmap = pix;
    })
  }

  build() {
    Column() {
      Button('touch to execute drag')
        .margin(10)
        .onTouch((event?: TouchEvent) => {
          if (event) {
            if (event.type == TouchType.Down) {
              let text = new unifiedDataChannel.PlainText()
              text.textContent = 'drag text'
              text.abstract = 'abstract'
              let unifiedData = new unifiedDataChannel.UnifiedData(text)

              let dragInfo: dragController.DragInfo = {
                pointerId: 0,
                data: unifiedData,
                extraParams: ''
              }
              let dragItemInfo: DragItemInfo = {
                pixelMap: this.pixmap,
                builder: () => {
                  this.DraggingBuilder()
                },
                extraInfo: "DragItemInfoTest"
              }
              let eve: DragInfo = new DragInfo();
              this.getUIContext()
                .getDragController()
                .executeDrag(dragItemInfo, dragInfo) // You are advised to use this.getUIContext().getDragController().executeDrag().
                .then((eve) => {
                  if (eve.event.getResult() == DragResult.DRAG\_SUCCESSFUL) {
                    // ...
                  } else if (eve.event.getResult() == DragResult.DRAG\_FAILED) {
                    // ...
                  }
                })
                .catch((err: Error) => {
                })
            }
          }
        })
      Text(this.text)
        .height(100)
        .width(150)
        .margin({ top: 20 })
        .border({ color: Color.Black, width: 1 })
        .onDrop((dragEvent?: DragEvent) => {
          if (dragEvent) {
            let records: Array<unifiedDataChannel.UnifiedRecord> = dragEvent.getData().getRecords();
            let plainText: unifiedDataChannel.PlainText = records\[0\] as unifiedDataChannel.PlainText;
            this.text = plainText.textContent;
          }
        })
    }
    .width('100%')
    .height('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d1/v3/XG6q5iQ9SamwIzc018eb6g/en-us_image_0000002568765043.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062226Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D55367166BB538FA9EF81283C63C858C4DD78DEBD9465B6E2D0F32B24A90CE16)

#### DragInfo

Defines the attributes required for initiating a drag action and information carried in the dragging process.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| pointerId | number | No | No | 
ID of the touch point on the screen when dragging is started. The value is an integer in the \[0, 9\] range.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| data | [unifiedDataChannel.UnifiedData](../../../../arkdata/arkts-apis/ohos-data-unifieddatachannel-unified-data-channel/document.md#unifieddata) | No | Yes | 

Data carried in the dragging process.

The default value is null.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| extraParams | string | No | Yes | 

Additional information about the drag action. Not supported currently.

The default value is null.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| touchPoint11+ | [TouchPoint](../../../arkts-components/common-definitions/basic-types/document.md#touchpoint11) | No | Yes | 

Coordinates of the touch point. If this parameter is not set, the touch point is centered horizontally and shifted downward by 20% from the top.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| previewOptions11+ | [DragPreviewOptions](../../../arkts-components/universal-attributes/interaction-properties/drag-and-drop-control/document.md#dragpreviewoptions11-1) | No | Yes | 

Processing mode of the drag preview and the display of the number badge during dragging.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| dataLoadParams20+ | [unifiedDataChannel.DataLoadParams](../../../../arkdata/arkts-apis/ohos-data-unifieddatachannel-unified-data-channel/document.md#dataloadparams20) | No | Yes | 

Parameters for deferred data loading from the drag source. This API provides data loading parameters to the system instead of directly providing complete data objects. When the user drops data on the target application, the system will use these parameters to request the actual data from the drag source. If set together with **data**, **dataLoadParams** takes effect.

The default value is null.

**Atomic service API**: This API can be used in atomic services since API version 20.

 |

#### dragController.createDragAction(deprecated)

createDragAction(customArray: Array<CustomBuilder | DragItemInfo>, dragInfo: DragInfo): DragAction

Creates a drag action object for initiating drag and drop operations. You need to explicitly specify one or more drag previews, the drag data, and the drag handle point. If a drag operation initiated by an existing drag action object is not completed, no new object can be created, and calling the API will throw an exception. After the lifecycle of the drag action object ends, the callback functions registered on this object become invalid. Therefore, it is necessary to hold this object within a longer scope and replace the old value with a new object returned by **createDragAction** before each drag initiation.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7e/v3/2YLo-QBKRxy3vwjAyXdTQQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062226Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4D878F3D32491EFE96A7D0CA6FD5E4BC9CB2FACC0E04D0A70B9F8CBD88049AB1)

-   This API is supported since API version 11 and deprecated since API version 18. You are advised to use [createDragAction](../ohos-arkui-uicontext-uicontext/class-dragcontroller/document.md#createdragaction11) instead. Before calling this API, you need to obtain the [DragController](../ohos-arkui-uicontext-uicontext/class-dragcontroller/document.md) instance using the [getDragController](../ohos-arkui-uicontext-uicontext/class-uicontext/document.md#getdragcontroller11) method in [UIContext](../ohos-arkui-uicontext-uicontext/class-uicontext/document.md).
    
-   Since API version 11, you can use the [getDragController](../ohos-arkui-uicontext-uicontext/class-uicontext/document.md#getdragcontroller11) API in [UIContext](../ohos-arkui-uicontext-uicontext/class-uicontext/document.md) to obtain the [DragController](../ohos-arkui-uicontext-uicontext/class-dragcontroller/document.md) object associated with the current UI context.
    
-   For optimal drag and drop performance, limit the number of drag previews.
    

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| customArray | Array<[CustomBuilder](../../../arkts-components/common-definitions/basic-types/document.md#custombuilder8) | [DragItemInfo](../../../arkts-components/universal-events/interaction-response-events/drag-event/document.md#dragiteminfo)\> | Yes | Object to be dragged. |
| dragInfo | [DragInfo](#draginfo) | Yes | Drag information. |

**Return value**

| Type | Description |
| :-- | :-- |
| [DragAction](#dragaction11) | **DragAction** object, which is used to subscribe to drag state changes and start the drag service. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.Incorrect parameters types; 3. Parameter verification failed. |
| 100001 | Internal handling failed. |

**Example**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bb/v3/j5EUoC78Q7CKBBRj8JiQlw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062226Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=DB1298DF02403FACCF0E0FCD424FB5AF593E1D43101D3590689F6C4E8EEC099B)

You are advised to use the [getDragController](../ohos-arkui-uicontext-uicontext/class-uicontext/document.md#getdragcontroller11) to obtain the **DragController** object associated with the current UI context.

import { dragController } from '@kit.ArkUI';
import { image } from '@kit.ImageKit';
import { unifiedDataChannel } from '@kit.ArkData';

@Entry
@Component
struct DragControllerPage {
  @State pixmap: image.PixelMap | null = null
  @State text: string = ''
  private dragAction: dragController.DragAction | null = null;
  customBuilders: Array<CustomBuilder | DragItemInfo> = new Array<CustomBuilder | DragItemInfo>();

  @Builder
  DraggingBuilder() {
    Column() {
      Text("DraggingBuilder")
        .fontColor(Color.White)
        .fontSize(12)
    }
    .width(100)
    .height(100)
    .backgroundColor(Color.Blue)
  }

  build() {
    Column() {

      Column() {
        Text(this.text)
          .width('100%')
          .height('100%')
          .fontColor(Color.White)
          .fontSize(18)
          .onDrop((dragEvent?: DragEvent) => {
            if (dragEvent) {
              let records: Array<unifiedDataChannel.UnifiedRecord> = dragEvent.getData().getRecords();
              let plainText: unifiedDataChannel.PlainText = records\[0\] as unifiedDataChannel.PlainText;
              this.text = plainText.textContent;
            }
          })
      }
      .width(100)
      .height(100)
      .backgroundColor(Color.Red)
      .margin(10)

      Button('Drag Multiple Objects').onTouch((event?: TouchEvent) => {
        if (event) {
          if (event.type == TouchType.Down) {
            console.info("multi drag Down by listener");
            this.customBuilders.splice(0, this.customBuilders.length);
            this.customBuilders.push(() => {
              this.DraggingBuilder()
            });
            this.customBuilders.push(() => {
              this.DraggingBuilder()
            });
            this.customBuilders.push(() => {
              this.DraggingBuilder()
            });
            let text = new unifiedDataChannel.PlainText()
            text.textContent = 'drag text'
            let unifiedData = new unifiedDataChannel.UnifiedData(text)
            let dragInfo: dragController.DragInfo = {
              pointerId: 0,
              data: unifiedData,
              extraParams: ''
            }
            try {
              this.dragAction = this.getUIContext()
                .getDragController()
                .createDragAction(this.customBuilders,
                  dragInfo) // You are advised to use this.getUIContext().getDragController().createDragAction().
              if (!this.dragAction) {
                console.info("listener dragAction is null");
                return
              }
              this.dragAction.on('statusChange', (dragAndDropInfo: dragController.DragAndDropInfo) => {
                if (dragAndDropInfo.status == dragController.DragStatus.STARTED) {
                  console.info("drag has start");
                } else if (dragAndDropInfo.status == dragController.DragStatus.ENDED) {
                  console.info("drag has end");
                  if (!this.dragAction) {
                    return
                  }
                  this.dragAction.off('statusChange')
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
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d2/v3/CQhBmd8oSO2v9MwKv0_c1g/en-us_image_0000002537765318.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062226Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1292E0107269AAEF27CFB86291CB23B20FF03B34902B342D5093A6CD90C95A82)

#### DragAction11+

Implements a **DragAction** object to subscribe to drag state changes and start the drag service.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

#### \[h2\]startDrag11+

startDrag(): Promise<void>

Starts the drag service. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

| ID | Error Message |
| :-- | :-- |
| 100001 | Internal handling failed. |

**Example 1**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/27/v3/8lvq1qpDRzStXWxDQyL96Q/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062226Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9F8D8036F64511497A1F1B079AAAC542310B7EF386B8FC6F36E4DE28900A246F)

You are advised to use the [getDragController](../ohos-arkui-uicontext-uicontext/class-uicontext/document.md#getdragcontroller11) to obtain the **DragController** object associated with the current UI context.

import { dragController } from '@kit.ArkUI';
import { unifiedDataChannel } from '@kit.ArkData';

@Entry
@Component
struct DragControllerPage {
  private dragAction: dragController.DragAction | null = null;
  customBuilders: Array<CustomBuilder | DragItemInfo> = new Array<CustomBuilder | DragItemInfo>();

  @Builder
  DraggingBuilder() {
    Column() {
      Text("DraggingBuilder")
        .fontColor(Color.White)
        .fontSize(12)
    }
    .width(100)
    .height(100)
    .backgroundColor(Color.Blue)
  }

  build() {
    Column() {
      Button('touch to execute drag').onTouch((event?: TouchEvent) => {
        if (event) {
          if (event.type == TouchType.Down) {
            this.customBuilders.splice(0, this.customBuilders.length);
            this.customBuilders.push(() => {
              this.DraggingBuilder()
            });
            let text = new unifiedDataChannel.PlainText()
            text.textContent = 'drag text'
            let unifiedData = new unifiedDataChannel.UnifiedData(text)
            let dragInfo: dragController.DragInfo = {
              pointerId: 0,
              data: unifiedData,
              extraParams: ''
            }
            try {
              this.dragAction = this.getUIContext()
                .getDragController()
                .createDragAction(this.customBuilders,
                  dragInfo) // You are advised to use this.getUIContext().getDragController().createDragAction().
              if (!this.dragAction) {
                console.info("listener dragAction is null");
                return;
              }
              this.dragAction.startDrag().then(() => {
              }).catch((err: Error) => {
                console.error(\`start drag Error: ${err.message}\`);
              })
            } catch (err) {
              console.error(\`create dragAction Error: ${err.message}\`);
            }
          }
        }
      }).margin({ top: 20 })
    }
  }
}

**Example 2**

Since API version 20, you can configure **dataLoadParams** in [DragInfo](#draginfo) to enable deferred data loading from the drag source.

import { unifiedDataChannel, uniformTypeDescriptor, uniformDataStruct } from '@kit.ArkData';
import { fileUri, fileIo as fs } from '@kit.CoreFileKit';
import { common } from '@kit.AbilityKit';
import { dragController } from '@kit.ArkUI';

@Entry
@Component
struct ImageExample {
  private dragAction: dragController.DragAction | null = null;
  customBuilders: Array<CustomBuilder | DragItemInfo> = new Array<CustomBuilder | DragItemInfo>();
  @State uri: string = "";
  @State blockArr: string\[\] = \[\];
  uiContext = this.getUIContext();
  udKey: string = '';

  @Builder
  DraggingBuilder() {
    Video({ src: $rawfile('test1.mp4'), controller: new VideoController() })
      .width(100)
      .height(100)
  }

  build() {
    Column() {
      Flex({ direction: FlexDirection.Row, alignItems: ItemAlign.Center, justifyContent: FlexAlign.SpaceAround }) {
        Button('touch to execute drag')
          .margin(10)
          .onTouch((event?: TouchEvent) => {
            if (event) {
              if (event.type == TouchType.Down) {
                this.customBuilders.splice(0, this.customBuilders.length);
                this.customBuilders.push(() => {
                  this.DraggingBuilder()
                });
                const context: Context | undefined = this.uiContext.getHostContext();
                if (context) {
                  let loadHandler: unifiedDataChannel.DataLoadHandler = () => {
                    let data =
                      context.resourceManager.getRawFdSync('test1.mp4');
                    let filePath = context.filesDir + '/test1.mp4';
                    let file = fs.openSync(filePath, fs.OpenMode.CREATE | fs.OpenMode.READ\_WRITE);
                    let bufferSize = data.length as number;
                    let buf = new ArrayBuffer(bufferSize);
                    fs.readSync(data.fd, buf, { offset: data.offset, length: bufferSize });
                    fs.writeSync(file.fd, buf, { offset: 0, length: bufferSize });
                    fs.closeSync(file.fd);
                    context.resourceManager.closeRawFdSync('test1.mp4')
                    this.uri = fileUri.getUriFromPath(filePath);
                    let videoMp: uniformDataStruct.FileUri = {
                      uniformDataType: 'general.file-uri',
                      oriUri: this.uri,
                      fileType: 'general.video',
                    }
                    let unifiedRecord = new unifiedDataChannel.UnifiedRecord();
                    let unifiedData = new unifiedDataChannel.UnifiedData();
                    unifiedRecord.addEntry(uniformTypeDescriptor.UniformDataType.FILE\_URI, videoMp);
                    unifiedData.addRecord(unifiedRecord);
                    return unifiedData;
                  }

                  let dragInfo: dragController.DragInfo = {
                    pointerId: 0,
                    extraParams: '',
                    dataLoadParams: {
                      loadHandler: loadHandler,
                      dataLoadInfo: { types: new Set(\[uniformTypeDescriptor.UniformDataType.VIDEO\]), recordCount: 1 }
                    }
                  }

                  let func = (dragAndDropInfo: dragController.DragAndDropInfo) => {
                    console.info(\`ndq Register to listen on drag status ${JSON.stringify(dragAndDropInfo)}\`);
                  }
                  try {
                    this.dragAction = this.getUIContext()
                      .getDragController()
                      .createDragAction(this.customBuilders,
                        dragInfo)
                    if (!this.dragAction) {
                      console.info("listener dragAction is null");
                      return;
                    }
                    this.dragAction.on('statusChange', func);
                    this.dragAction.startDrag().then(() => {
                    }).catch((err: Error) => {
                      console.error(\`start drag Error: ${err.message}\`);
                    })
                  } catch (err) {
                    console.error(\`create dragAction Error: ${err.message}\`);
                  }
                }
              }
            }
          })
      }
      .margin({ bottom: 20 })

      Row() {
        Column() {
          Text('Valid drop target')
            .fontSize('15dp')
            .height('10%')
          List() {
            ForEach(this.blockArr, (item: string, index) => {
              ListItem() {
                Video({ src: item, controller: new VideoController() })
                  .width(100)
                  .height(100)
                  .border({ width: 1 })
              }
              .margin({ left: 30, top: 30 })
            }, (item: string) => item)
          }
          .border({ width: 1 })
          .height('90%')
          .width('100%')
          .allowDrop(\[uniformTypeDescriptor.UniformDataType.VIDEO\])
          .onDrop((event?: DragEvent, extraParams?: string) => {
            let context = this.uiContext.getHostContext() as common.UIAbilityContext;
            let pathDir: string = context.distributedFilesDir;
            let destUri = fileUri.getUriFromPath(pathDir);
            let progressListener: unifiedDataChannel.DataProgressListener =
              (progress: unifiedDataChannel.ProgressInfo, dragData: UnifiedData | null) => {
                if (dragData != null) {
                  let arr: Array<unifiedDataChannel.UnifiedRecord> = dragData.getRecords();
                  if (arr.length > 0) {
                    if (arr\[0\].getType() === uniformTypeDescriptor.UniformDataType.VIDEO) {
                      this.blockArr.splice(JSON.parse(extraParams as string).insertIndex, 0, this.uri);
                    }
                  } else {
                    console.info('dragData arr is null');
                  }
                } else {
                  console.info('dragData is undefined');
                }
                console.info(\`percentage: ${progress.progress}\`);
              };
            let options: DataSyncOptions = {
              destUri: destUri,
              fileConflictOptions: unifiedDataChannel.FileConflictOptions.OVERWRITE,
              progressIndicator: unifiedDataChannel.ProgressIndicator.DEFAULT,
              dataProgressListener: progressListener,
            }
            try {
              this.udKey = (event as DragEvent).startDataLoading(options);
              console.info('udKey: ', this.udKey);
            } catch (e) {
              console.error(\`startDataLoading errorCode: ${e.code}, errorMessage: ${e.message}\`);
            }
          }, { disableDataPrefetch: true })
        }
        .height("50%")
        .width("90%")
        .border({ width: 1 })
      }

      Button('Cancel Data Transfer')
        .onClick(() => {
          try {
            this.getUIContext().getDragController().cancelDataLoading(this.udKey);
          } catch (e) {
            console.error(\`cancelDataLoading errorCode: ${e.code}, errorMessage: ${e.message}\`);
          }
        })
        .margin({ top: 10 })
    }.width('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/93/v3/Gt_4snWKTheEy7Uul2qLbQ/en-us_image_0000002537925258.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062226Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1D88259648A6DB47740559AF662D9E74AFF9025B7E95147804D19FDD74534DF1)

#### \[h2\]on('statusChange')11+

on(type: 'statusChange', callback: Callback<[DragAndDropInfo](#draganddropinfo11)\>): void

Subscribes to drag state changes.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The value is fixed at **'statusChange'**, which indicates the drag state change event. |
| callback | Callback<[DragAndDropInfo](#draganddropinfo11)\> | Yes | Callback used to return a [DragAndDropInfo](#draganddropinfo11) instance. |

**Example**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bb/v3/kCCkyvizT6mhcjWYd7wKgg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062226Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=AC5CFBDBFB0025CCC60CF5361720E002422C254CF88308907C50FEFC43478BD2)

You are advised to use the [getDragController](../ohos-arkui-uicontext-uicontext/class-uicontext/document.md#getdragcontroller11) to obtain the **DragController** object associated with the current UI context.

import { dragController } from '@kit.ArkUI';
import { unifiedDataChannel } from '@kit.ArkData';

@Entry
@Component
struct DragControllerPage {
  private dragAction: dragController.DragAction | null = null;
  customBuilders: Array<CustomBuilder | DragItemInfo> = new Array<CustomBuilder | DragItemInfo>();

  @Builder
  DraggingBuilder() {
    Column() {
      Text("DraggingBuilder")
        .fontColor(Color.White)
        .fontSize(12)
    }
    .width(100)
    .height(100)
    .backgroundColor(Color.Blue)
  }

  build() {
    Column() {
      Button('touch to execute drag').onTouch((event?: TouchEvent) => {
        if (event) {
          if (event.type == TouchType.Down) {
            this.customBuilders.splice(0, this.customBuilders.length);
            this.customBuilders.push(() => {
              this.DraggingBuilder()
            });
            let text = new unifiedDataChannel.PlainText()
            text.textContent = 'drag text'
            let unifiedData = new unifiedDataChannel.UnifiedData(text)
            let dragInfo: dragController.DragInfo = {
              pointerId: 0,
              data: unifiedData,
              extraParams: ''
            }
            let func = (dragAndDropInfo: dragController.DragAndDropInfo) => {
              console.info(\`Register to listen on drag status ${JSON.stringify(dragAndDropInfo)}\`);
            }
            try {
              this.dragAction = this.getUIContext()
                .getDragController()
                .createDragAction(this.customBuilders,
                  dragInfo) // You are advised to use this.getUIContext().getDragController().createDragAction().
              if (!this.dragAction) {
                console.info("listener dragAction is null");
                return;
              }
              // Subscribe to drag state changes. The information in func will be logged once a change is detected.
              this.dragAction.on('statusChange', func);
              this.dragAction.startDrag().then(() => {
              }).catch((err: Error) => {
                console.error(\`start drag Error: ${err.message}\`);
              })
            } catch (err) {
              console.error(\`create dragAction Error: ${err.message}\`);
            }
          }
        }
      }).margin({ top: 20 })
    }
  }
}

#### \[h2\]off('statusChange')11+

off(type: 'statusChange', callback?: Callback<[DragAndDropInfo](#draganddropinfo11)\>): void

Unsubscribes from drag state changes.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The value is fixed at **'statusChange'**, which indicates the drag state change event. |
| callback | Callback<[DragAndDropInfo](#draganddropinfo11)\> | No | Callback used to return a [DragAndDropInfo](#draganddropinfo11) instance. |

**Example**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/db/v3/eC042SWWQ3CWLCYEwCFnvA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062226Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=612B100CA26044F76317B8315C24B179A9881D4020FAD569E7C4447801BE31F1)

You are advised to use the [getDragController](../ohos-arkui-uicontext-uicontext/class-uicontext/document.md#getdragcontroller11) to obtain the **DragController** object associated with the current UI context.

import { dragController } from '@kit.ArkUI';
import { unifiedDataChannel } from '@kit.ArkData';

@Entry
@Component
struct DragControllerPage {
  private dragAction: dragController.DragAction | null = null;
  customBuilders: Array<CustomBuilder | DragItemInfo> = new Array<CustomBuilder | DragItemInfo>();

  @Builder
  DraggingBuilder() {
    Column() {
      Text("DraggingBuilder")
        .fontColor(Color.White)
        .fontSize(12)
    }
    .width(100)
    .height(100)
    .backgroundColor(Color.Blue)
  }

  build() {
    Column() {
      Button('touch to execute drag').onTouch((event?: TouchEvent) => {
        if (event) {
          if (event.type == TouchType.Down) {
            this.customBuilders.splice(0, this.customBuilders.length);
            this.customBuilders.push(() => {
              this.DraggingBuilder()
            });
            let text = new unifiedDataChannel.PlainText()
            text.textContent = 'drag text'
            let unifiedData = new unifiedDataChannel.UnifiedData(text)
            let dragInfo: dragController.DragInfo = {
              pointerId: 0,
              data: unifiedData,
              extraParams: ''
            }
            let func = (dragAndDropInfo: dragController.DragAndDropInfo) => {
              console.info(\`Register to listen on drag status ${JSON.stringify(dragAndDropInfo)}\`);
            }
            this.dragAction = this.getUIContext()
              .getDragController()
              .createDragAction(this.customBuilders,
                dragInfo) // You are advised to use this.getUIContext().getDragController().createDragAction().
            if (!this.dragAction) {
              console.info("listener dragAction is null");
              return;
            }
            this.dragAction.on('statusChange', func);
            // Unsubscribe from drag state changes. The information in func will not be logged after a drag operation starts.
            this.dragAction.off('statusChange', func);
            this.dragAction.startDrag().then(() => {
            }).catch((err: Error) => {
              console.error(\`start drag Error: ${err.message}\`);
            })
          }
        }
      }).margin({ top: 20 })
    }
  }
}

#### DragAndDropInfo11+

Provides the data reported when the state changes during dragging.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| status | [DragStatus](#dragstatus11) | No | No | Current dragging state (started or ended). |
| event | [DragEvent](../../../arkts-components/universal-events/interaction-response-events/drag-event/document.md#dragevent7) | No | No | Drag event corresponding to the current state. The drag event initiated by **dragController** only supports the APIs for obtaining the result and behavior, and is used exclusively for the dragging end state. |
| extraParams | string | No | Yes | Additional information about the drag action. Not supported currently. The default value is null. |

#### DragStatus11+

Describes the dragging start and end states.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Value | Description |
| :-- | :-- | :-- |
| STARTED | 0 | Dragging is started. |
| ENDED | 1 | Dragging ends. |

#### AnimationOptions11+

Defines parameters related to drag-and-drop animation effects.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| duration | number | No | Yes | 
Animation duration, in ms.

Default value: **1000**

**NOTE**

\- If this parameter is set to a value less than 0, the value **0** is used.

\- Floating-point values will be rounded down to integers. For example, if the value set is 1.2, **1** will be used.

 |
| curve | [Curve](../../../arkts-components/common-definitions/enums/document.md#curve) | [ICurve](../ohos-curves-interpolation-calculation/document.md#icurve9) | No | Yes | 

Animation curve.

Default value: **Curve.EaseInOut**

 |

#### DragEventParam12+

Callback used to return the result.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| event10+ | [DragEvent](../../../arkts-components/universal-events/interaction-response-events/drag-event/document.md#dragevent7) | No | No | Drag event information that includes only the drag result. |
| extraParams10+ | string | No | No | Additional information about the drag event. |

#### dragController.getDragPreview(deprecated)

getDragPreview(): DragPreview

Obtains the **DragPreview** object, which represents the preview displayed during a drag operation.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/85/v3/uAkIImH1TluJvkoqs_-73g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062226Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=41BAEBD5C092375CEE236F792191DE2F4332718D6481D4AD716C83B32C409E1C)

-   This API is supported since API version 11 and deprecated since API version 18. You are advised to use [getDragPreview](../ohos-arkui-uicontext-uicontext/class-dragcontroller/document.md#getdragpreview11) instead. Before calling this API, you need to obtain the [DragController](../ohos-arkui-uicontext-uicontext/class-dragcontroller/document.md) instance using the [getDragController](../ohos-arkui-uicontext-uicontext/class-uicontext/document.md#getdragcontroller11) method in [UIContext](../ohos-arkui-uicontext-uicontext/class-uicontext/document.md).
    
-   Since API version 11, you can use the [getDragController](../ohos-arkui-uicontext-uicontext/class-uicontext/document.md#getdragcontroller11) API in [UIContext](../ohos-arkui-uicontext-uicontext/class-uicontext/document.md) to obtain the [DragController](../ohos-arkui-uicontext-uicontext/class-dragcontroller/document.md) object associated with the current UI context.
    

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Return value**

| Type | Description |
| :-- | :-- |
| [DragPreview](#dragpreview11) | **DragPreview** object. It provides the API for setting the preview style. It does not work in the **OnDrop** and **OnDragEnd** callbacks. |

**Example**

For details, see [animate](#animate11).

#### DragPreview11+

Implements a **DragPreview** object. This API does not work in the **OnDrop** and **OnDragEnd** callbacks.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

#### \[h2\]setForegroundColor11+

setForegroundColor(color: ResourceColor): void

Sets the foreground color of the drag preview. This API does not work in the **OnDrop** and **OnDragEnd** callbacks. It can only be used on the object obtained through the [getDragPreview()](../ohos-arkui-uicontext-uicontext/class-dragcontroller/document.md#getdragpreview11) API.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| color | [ResourceColor](../../../arkts-components/common-definitions/basic-types/document.md#resourcecolor) | Yes | Foreground color of the drag preview. |

**Example**

For details, see [animate](#animate11).

#### \[h2\]animate11+

animate(options: AnimationOptions, handler: () => void): void

Applies a foreground color animation to the drag preview. This API does not work in the **OnDrop** and **OnDragEnd** callbacks. It can only be used on the object obtained through the [getDragPreview()](../ohos-arkui-uicontext-uicontext/class-dragcontroller/document.md#getdragpreview11) API.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| options | [AnimationOptions](#animationoptions11) | Yes | Animation settings. |
| handler | () => void | Yes | Callback used to change attributes such as the background mask color. |

**Example**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/89/v3/E2N0I5nKSsqXR79ttW2Q_g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062226Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=DC393567ACAA9408B215F920863530F9889AC9BDFF3D6AD5DE577B200558FABC)

You are advised to use the [getDragController](../ohos-arkui-uicontext-uicontext/class-uicontext/document.md#getdragcontroller11) to obtain the **DragController** object associated with the current UI context.

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
        hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onWindowStageCreate');
    
        windowStage.loadContent('pages/Index', this.storage, (err, data) => {
          if (err.code) {
            hilog.error(0x0000, 'testTag', 'Failed to load the content. Cause: %{public}s',
              \`Code is ${err.code}, message is ${err.message}\`);
            return;
          }
          hilog.info(0x0000, 'testTag', 'Succeeded in loading the content. Data: %{public}s',
            \`Code is ${err.code}, message is ${err.message}\`);
          windowStage.getMainWindow((err, data) => {
            if (err.code) {
              hilog.error(0x0000, \`Failed to obtain the main window. Cause: ${err.message}\`, '');
              return;
            }
            uiContext = data.getUIContext();
            this.storage.setOrCreate<UIContext>('uiContext', uiContext);
          })
        });
      }
    }
    
2.  In the **Index.ets** file, call **this.getUIContext().getSharedLocalStorage()** to obtain the UI context and then use the **DragController** object obtained to perform subsequent operations.
    
    import { unifiedDataChannel } from '@kit.ArkData';
    import { hilog } from '@kit.PerformanceAnalysisKit';
    import { dragController, curves, promptAction, UIContext } from '@kit.ArkUI';
    import { image } from '@kit.ImageKit';
    import { BusinessError } from '@kit.BasicServicesKit';
    
    class DragInfo {
      event: DragEvent | undefined = undefined;
      extraParams: string = '';
    }
    
    @Entry()
    @Component
    struct DragControllerPage {
      @State pixmap: image.PixelMap | null = null;
      storages = this.getUIContext().getSharedLocalStorage();
    
      @Builder
      DraggingBuilder() {
        Column() {
          Text("DraggingBuilder")
            .fontColor(Color.White)
            .fontSize(12)
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
          Button('Drop Here')
            .margin(10)
            .onDragEnter(() => {
              try {
                let uiContext: UIContext = this.storages?.get<UIContext>('uiContext') as UIContext;
                let previewObj: dragController.DragPreview = uiContext.getDragController().getDragPreview();
                let foregroundColor: ResourceColor = Color.Green;
    
                let previewAnimation: dragController.AnimationOptions = {
                  curve: curves.cubicBezierCurve(0.2, 0, 0, 1),
                }
                previewObj.animate(previewAnimation, () => {
                  previewObj.setForegroundColor(foregroundColor);
                });
              } catch (error) {
                let msg = (error as BusinessError).message;
                let code = (error as BusinessError).code;
                hilog.error(0x0000, \`show error code is ${code}, message is ${msg}\`, '');
              }
            })
            .onDrop(() => {
              this.getUIContext().getPromptAction().showToast({ duration: 100, message: 'Drag Success', bottom: 400 })
            })
          Button('Drag').onTouch((event?: TouchEvent) => {
            if (event) {
              if (event.type == TouchType.Down) {
                let text = new unifiedDataChannel.Text()
                let unifiedData = new unifiedDataChannel.UnifiedData(text)
                let dragInfo: dragController.DragInfo = {
                  pointerId: 0,
                  data: unifiedData,
                  extraParams: ''
                }
                let eve: DragInfo = new DragInfo();
                this.getUIContext()
                  .getDragController()
                  .executeDrag(() => { // You are advised to use this.getUIContext().getDragController().executeDrag().
                    this.DraggingBuilder()
                  }, dragInfo, (err, eve) => {
                    hilog.info(0x0000, \`${JSON.stringify(err)}\`, '')
                    if (eve && eve.event) {
                      if (eve.event.getResult() == DragResult.DRAG\_SUCCESSFUL) {
                        hilog.info(0x0000, 'success', '');
                      } else if (eve.event.getResult() == DragResult.DRAG\_FAILED) {
                        hilog.info(0x0000, 'failed', '');
                      }
                    }
                  })
              }
            }
          }).margin({ top: 100 })
        }
        .width('100%')
        .height('100%')
      }
    }
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/62/v3/Uy4HHuxkSsWZazGihtOb4A/en-us_image_0000002568685035.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062226Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0D2F315B516E8CE8BCAA22535B11B3CC6B358D13D531337C9115F2CBCE03E43E)

#### DragStartRequestStatus18+

Enumerates the states defining whether an application can initiate a drag operation. This API is effective only when [onDragStart](../../../arkts-components/universal-events/interaction-response-events/drag-event/document.md#ondragstart) is called.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Value | Description |
| :-- | :-- | :-- |
| WAITING | 0 | The application is preparing data and cannot initiate a drag operation yet. |
| READY | 1 | The application has completed data preparation and is ready to initiate a drag operation. |

#### DragSpringLoadingState20+

Enumerates hover detection states during drag operations.

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Value | Description |
| :-- | :-- | :-- |
| BEGIN | \- | Initial state when a dragged item enters the component boundary and remains stationary for the specified duration. This state enables preparation operations. |
| UPDATE | \- | Periodic notification state during sustained hover detection. In this state, periodic updates refresh UI effects to highlight the hover state. |
| END | \- | Final state indicating completion of the hover detection cycle, which is triggered when the dragged item remains stationary after the last update notification. Hover detection will only restart after the dragged item exits and re-enters the component boundary or enters a child component. In this state, the application can perform cleanup, navigation, or view switching operations. |
| CANCEL | \- | Interruption state of hover detection triggered by termination events, which include the following: finger or mouse release, window switching, screen off, exiting the component boundary, entering child components, or exceeding the movement threshold within the component. The application will restore the UI style and cancel pending navigation and view switching operations. |

#### DragSpringLoadingConfiguration20+

Defines the configuration parameters for drag hover detection. The default settings typically suffice. These settings can be customized through [onDragSpringLoading](../../../arkts-components/universal-events/interaction-response-events/drag-event/document.md#ondragspringloading20) binding or dynamically updated during BEGIN state using [updateConfiguration](#updateconfiguration20).

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| stillTimeLimit | number | No | Yes | Time (in ms) required to remain stationary to enter the BEGIN state of hover detection. Value range: integer in the \[0, 231\-1\] range. Floating-point number inputs will be truncated to integers. Invalid values (negative numbers, **null**, **undefined**, **NaN**) are treated as the default value **500**. |
| updateInterval | number | No | Yes | Time interval (in ms) at which update notifications are sent after hover detection enters the UPDATE state. Value range: integer in the \[0, 231\-1\] range. Floating-point number inputs will be truncated to integers. Invalid values (negative numbers, **null**, **undefined**, **NaN**) are treated as the default value **100**. |
| updateNotifyCount | number | No | Yes | Maximum number of update notifications after hover detection enters the UPDATE state. Value range: integer in the \[0, 231\-1\] range. Floating-point number inputs will be truncated to integers. Invalid values (negative numbers, **null**, **undefined**, **NaN**) are treated as the default value **3**. |
| updateToFinishInterval | number | No | Yes | Maximum waiting time (in ms) from the UPDATE state to the END state. Value range: integer in the \[0, 231\-1\] range. Floating-point number inputs will be truncated to integers. Invalid values (negative numbers, **null**, **undefined**, **NaN**) are treated as the default value **100**. |

#### SpringLoadingDragInfos20+

Defines the drag event information when hover detection is triggered. This API provides drag data summaries and additional drag event information, allowing applications to decide whether to respond to hover detection callbacks.

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| dataSummary | [unifiedDataChannel.Summary](../../../../arkdata/arkts-apis/ohos-data-unifieddatachannel-unified-data-channel/document.md#summary) | No | Yes | Summary of the dragged data. The default value is null. |
| extraInfos | string | No | Yes | Additional information about the drag event. The default value is an empty string. |

#### SpringLoadingContext20+

Defines callback context information passed to applications during hover detection. It enables access to drag states, dynamic UI effect updates, and drag data for operation handling decisions.

#### \[h2\]Properties

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| state | [DragSpringLoadingState](#dragspringloadingstate20) | No | No | Current state of hover detection. |
| currentNotifySequence | number | No | No | Callback notification sequence number in the current hover detection cycle. The value is zero-based. |
| dragInfos | [SpringLoadingDragInfos](#springloadingdraginfos20) | No | Yes | Drag information. Omitted in CANCEL state; uses the [SpringLoadingDragInfos](#springloadingdraginfos20) default value when **undefined**. |
| currentConfig | [DragSpringLoadingConfiguration](#dragspringloadingconfiguration20) | No | Yes | Configuration information in the current callback. Omitted in CANCEL state; uses the [DragSpringLoadingConfiguration](#dragspringloadingconfiguration20) default value when **undefined**. |

#### \[h2\]abort20+

abort(): void

Terminates subsequent hover detection. This API does not trigger CANCEL state notifications, and the application needs to perform state cleanup when executing this API.

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

#### \[h2\]updateConfiguration20+

updateConfiguration(config: DragSpringLoadingConfiguration): void

Updates the hover detection configuration. This API is effective only when the hover detection state is BEGIN. Applications typically set the hover detection configuration when binding [onDragSpringLoading](../../../arkts-components/universal-events/interaction-response-events/drag-event/document.md#ondragspringloading20) or use the default configuration. This API does not modify the original configuration set during binding, but updates dynamic configuration information for subsequent hover detection. Use this API with caution, as different drag data types may require different UX timing.

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| config | [DragSpringLoadingConfiguration](#dragspringloadingconfiguration20) | Yes | New configuration for hover detection. |
