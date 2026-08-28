# Drag and Drop Control

Components provide attributes and APIs to configure their response to drag events and influence system handling of drag operations, including drag enablement settings and drag preview customization.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/50/v3/Dq8cbjsrRJiwpUn9N9cmag/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062235Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=CFD3BA169FE7422232B495AAA3E24782088F30BC1C6CC218E7AD8E89A0FBD946)

The initial APIs of this module are supported since API version 10. Updates will be marked with a superscript to indicate their earliest API version.

The ArkUI framework provides default drag and drop capabilities for the following components, allowing them to serve as the drag source (from which data can be dragged) or drop target (to which data can be dropped). You can further customize drag and drop behavior by implementing universal drag events.

-   The following component supports drag actions by default: [Search](../../../text-and-input/search/document.md), [TextInput](../../../text-and-input/textinput/document.md), [TextArea](../../../text-and-input/textarea/document.md), [RichEditor](../../../text-and-input/richeditor/document.md), [Text](../../../text-and-input/text/document.md), [Image](../../../images-and-videos/image/document.md), [Hyperlink](../../../text-and-input/hyperlink/document.md). You can control the default drag behavior by setting the [draggable](#draggable) attribute.
    
-   The following component supports drop actions by default: [Search](../../../text-and-input/search/document.md), [TextInput](../../../text-and-input/textinput/document.md), [TextArea](../../../text-and-input/textarea/document.md), [RichEditor](../../../text-and-input/richeditor/document.md). You can disable the default drag behavior by setting the [allowDrop](#allowdrop) attribute to **null**.
    
-   The following components do not support drag actions: [ArcScrollBar](../../../scroll-and-swipe/arcscrollbar/document.md), [MultiNavigation](../../../navigation-and-switching/multinavigation/document.md), [ToolBarItem](../../../navigation-and-switching/toolbaritem/document.md), [ArcSlider](../../../buttons-and-selections/arcslider/document.md), [Span](../../../text-and-input/span/document.md), [ImageSpan](../../../text-and-input/imagespan/document.md), [ContainerSpan](../../../text-and-input/containerspan/document.md), [SymbolSpan](../../../text-and-input/symbolspan/document.md), [ArcAlphabetIndexer](../../../information-display/arcalphabetindexer/document.md), [OffscreenCanvas](../../../canvas-drawing/offscreencanvas/document.md), [Menu](../../../menus/menu/document.md), [MenuItem](../../../menus/menuitem/document.md), [MenuItemGroup](../../../menus/menuitemgroup/document.md), [PasteButton](../../../security/pastebutton/document.md), [SaveButton](../../../security/savebutton/document.md), [WithTheme](../../../themes/withtheme/document.md), [NavPushPathHelper](../../../atomicservice/navpushpathhelper/document.md), [ContentSlot](../../../custom-placeholder-components/contentslot/document.md), [Chip](../../../system-preset-ui-component-library/chip/document.md), [ExceptionPrompt](../../../system-preset-ui-component-library/exceptionprompt/document.md), [Filter](../../../system-preset-ui-component-library/filter/document.md), [FormMenu](../../../system-preset-ui-component-library/formmenu/document.md), [Popup](../../../system-preset-ui-component-library/popup/document.md), [SelectionMenu](../../../system-preset-ui-component-library/selectionmenu/document.md), [SplitLayout](../../../system-preset-ui-component-library/splitlayout/document.md), and all popup window components.
    

The draggable attribute of the Text, TextInput, TextArea, Hyperlink, Image, RichEditor, and Web components is true by default, indicating that the component is draggable.

To enable drag and drop for other components, you need to set the **draggable** attribute to **true** and implement data transmission in APIs such as [onDragStart](../../../universal-events/interaction-response-events/drag-event/document.md#ondragstart).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/de/v3/kEjIx5zJQl6P6k2AXWJ3pg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062235Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E4A7EA281CEF5BBF62716AF8712B8D94D45F3D9849F9E27F8A320B4F9812670D)

When using the **Text** component, set [copyOption](../../../text-and-input/text/document.md#copyoption9) to **CopyOptions.InApp** or **CopyOptions.LocalDevice**.

#### allowDrop

allowDrop(value: Array<UniformDataType> | null): T

Sets the types of data that can be dropped to the component. If **allowDrop** is not set, the component accepts all data types by default.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | Array<[UniformDataType](#uniformdatatype)\> | null12+ | Yes | Types of data that can be dropped to the component. Since API version 12, this parameter can be set to **null** to make the component reject all data types. |

**Return value**

| Type | Description |
| :-- | :-- |
| T | Current component. |

#### draggable

draggable(value: boolean): T

Sets whether the component is draggable. By default, the component is not draggable.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | boolean | Yes | 
Whether the component is draggable.

**true**: The component is draggable.

**false**: The component is not draggable.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| T | Current component. |

#### dragPreview11+

dragPreview(value: CustomBuilder | DragItemInfo | string): T

Sets the preview image displayed during component drag operations.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [CustomBuilder](../../../common-definitions/basic-types/document.md#custombuilder8) | [DragItemInfo](../../../universal-events/interaction-response-events/drag-event/document.md#dragiteminfo) | string12+ | Yes | 
Preview image displayed during component drag operations. It only applies to [onDragStart](../../../universal-events/interaction-response-events/drag-event/document.md#ondragstart) drag mode.

If the component supports drag and drop and a preview is specified through [bindContextMenu](../../dialog-box-control/menu-control/document.md#bindcontextmenu8), that specified preview is displayed when the component is dragged. The priority of the background image returned in [onDragStart](../../../universal-events/interaction-response-events/drag-event/document.md#ondragstart) is lower than that of the preview set in [dragPreview](#dragpreview11). This means that, once set, the latter will be used in place of the former. Using [CustomBuilder](../../../common-definitions/basic-types/document.md#custombuilder8) requires offline rendering and may increase performance overhead and latency. In light of this, you are advised to use [PixelMap](../../../../../../media/image-kit/arkts-apis/ohos-multimedia-image-image-processing/interface-pixelmap/document.md) in [DragItemInfo](../../../universal-events/interaction-response-events/drag-event/document.md#dragiteminfo) instead.

When an ID of the string type is passed in, the snapshot of the component assigned the ID is used as the preview image. If the component assigned the ID cannot be found or its [Visibility](../../../common-definitions/enums/document.md#visibility) attribute is set to **None** or **Hidden**, a snapshot of the current component is used as the preview image. Currently, snapshots do not support visual effects, such as brightness, shadow, blur, and rotation.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| T | Current component. |

#### dragPreview15+

dragPreview(preview: CustomBuilder | DragItemInfo | string, config?: PreviewConfiguration):T

Sets the drag preview for the component. This API specifically configures or disables the lift animation effect.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fd/v3/BFavmkokTPy_ahf-oJ7L7A/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062235Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E81D1B8394ECDB033B180422978CEF1DEFED4EB0B8B3BB1934DE5B430B2EE2D6)

This API cannot be called within [attributeModifier](../../modifiers-and-custom-property/attribute-modifier/document.md#attributemodifier).

**Atomic service API**: This API can be used in atomic services since API version 15.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| preview | [CustomBuilder](../../../common-definitions/basic-types/document.md#custombuilder8) | [DragItemInfo](../../../universal-events/interaction-response-events/drag-event/document.md#dragiteminfo) | string | Yes | 
Preview image displayed during component drag operations. It only applies to [onDragStart](../../../universal-events/interaction-response-events/drag-event/document.md#ondragstart) drag mode.

If the component supports drag and drop and a preview is specified through [bindContextMenu](../../dialog-box-control/menu-control/document.md#bindcontextmenu8), that specified preview is displayed when the component is dragged. The priority of the background image returned in [onDragStart](../../../universal-events/interaction-response-events/drag-event/document.md#ondragstart) is lower than that of the preview set in [dragPreview](#dragpreview11). This means that, once set, the latter will be used in place of the former. Using [CustomBuilder](../../../common-definitions/basic-types/document.md#custombuilder8) requires offline rendering and may increase performance overhead and latency. In light of this, you are advised to use [PixelMap](../../../../../../media/image-kit/arkts-apis/ohos-multimedia-image-image-processing/interface-pixelmap/document.md) in [DragItemInfo](../../../universal-events/interaction-response-events/drag-event/document.md#dragiteminfo) instead.

When an ID of the string type is passed in, the snapshot of the component assigned the ID is used as the preview image. If the component assigned the ID cannot be found or its [Visibility](../../../common-definitions/enums/document.md#visibility) attribute is set to **None** or **Hidden**, a snapshot of the current component is used as the preview image. Currently, snapshots do not support visual effects, such as brightness, shadow, blur, and rotation.

 |
| config | [PreviewConfiguration](../../../universal-events/interaction-response-events/drag-event/document.md#previewconfiguration15) | No | 

Additional settings for the drag preview.

This parameter is effective only for previews set using [dragPreview](#dragpreview11).

 |

**Return value**

| Type | Description |
| :-- | :-- |
| T | Current component. |

#### dragPreviewOptions11+

dragPreviewOptions(value: DragPreviewOptions, options?: DragInteractionOptions): T

Sets the preview image processing mode, badge count, and interaction behavior during drag operations. The **onItemDragStart** drag mode is not supported.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f/v3/s3CPo1oyTxG2chrDGby6yQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062235Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=53EA7ECE7D3026824986C62FB59DF661D5F2C95ED0C5700D1E92482D49E87F4A)

This API can be called in [attributeModifier](../../modifiers-and-custom-property/attribute-modifier/document.md#attributemodifier) since API version 20.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [DragPreviewOptions](#dragpreviewoptions11-1)11+ | Yes | Preview image processing mode and badge count during dragging. |
| options12+ | [DragInteractionOptions](#draginteractionoptions12)12+ | No | 
Interaction behavior for the floating preview image.

Default value: empty

 |

**Return value**

| Type | Description |
| :-- | :-- |
| T | Current component. |

#### DragPreviewOptions11+

Preview image processing mode and badge count during dragging.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| mode | [DragPreviewMode](#dragpreviewmode11) | Array<[DragPreviewMode](#dragpreviewmode11)\>12+ | No | Yes | 
How the background image is processed when the component is dragged.

Default value: **DragPreviewMode.AUTO**

If **DragPreviewMode.AUTO** is set concurrently with other enumerated values, **DragPreviewMode.AUTO** takes precedence and the other values are ignored.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| numberBadge12+ | boolean | number | No | Yes | 

Whether to display the number badge or the number displayed on the badge. For a number badge, the value range is \[0, 231\-1\]. Values outside this range will be processed as the default state. If the value specified is a floating-point number, only the integer part is displayed.

**NOTE**

When multiple items are dragged, use this API to set the number of items dragged.

Default value: **true**

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| modifier12+ | [ImageModifier](#imagemodifier12) | No | Yes | 

Drag preview style modifier. It applies image component attributes and styles to configure preview appearance (see Example 6). Supported effects: opacity, shadow, background blur, and rounded corners. Text drag previews only support default styling.

1\. Opacity

Use [opacity](../../visual-effects/opacity-control/document.md#opacity). The value ranges from 0 to 1. If this parameter is set to **0** or left empty, the default opacity 0.95 is used. If this parameter is set to **1** or an abnormal value, the opacity is 1.

2\. Shadow

Use [shadow](../../visual-effects/image-effect/document.md#shadow).

3\. Background blur

Use [backgroundEffect](../../basic-attributes/background/document.md#backgroundeffect11) or [backgroundBlurStyle](../../basic-attributes/background/document.md#backgroundblurstyle9). If both are set, the latter setting takes precedence.

4\. Rounded corners

Use [border](../../layout-and-borders/border-styling/document.md#border) or [borderRadius](../../layout-and-borders/border-styling/document.md#borderradius). Modifier settings override mode settings.

Default value: empty (unmodifiable).

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| sizeChangeEffect19+ | [DraggingSizeChangeEffect](#draggingsizechangeeffect19)19+ | No | Yes | 

Transition effect between the floating image and drag preview.

Default value: **DraggingSizeChangeEffect.DEFAULT**.

**Atomic service API**: This API can be used in atomic services since API version 19.

 |

#### DragPreviewMode11+

Sets the display mode of the drag preview.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Value | Description |
| :-- | :-- | :-- |
| AUTO | 1 | 
Enables the system to automatically change the position of the dragged point based on the scenario and apply scaling transformations to the drag preview based on set rules.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| DISABLE\_SCALE | 2 | 

Disables the system's scaling behavior for the drag preview.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| ENABLE\_DEFAULT\_SHADOW12+ | 3 | 

Enables the default shadow effect for non-text components.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| ENABLE\_DEFAULT\_RADIUS12+ | 4 | 

Enables a unified rounded corner effect for non-text components, with the default value of 12 vp. If the custom rounded corner value set by the application is greater than the default value or the value set by **modifier**, the custom value is used.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| ENABLE\_DRAG\_ITEM\_GRAY\_EFFECT18+ | 5 | 

Enables the grayscale effect for the original drag item, which does not apply to text content dragging. When the user starts dragging, the original item displays a grayscale effect. When released, the original item returns to its original appearance. After enabling the default grayscale effect, avoid manually modifying the opacity after dragging starts. Otherwise, the grayscale effect will be overridden, and the original opacity will not be correctly restored when dragging ends.

**Atomic service API**: This API can be used in atomic services since API version 18.

 |
| ENABLE\_MULTI\_TILE\_EFFECT18+ | 6 | 

Enables multi-tile display for mouse-dragged multi-selected objects, with each drag preview maintaining its original relative position. Requires multi-select mode with **isMultiSelectionEnabled** set to **true**. Takes precedence over [dragPreview](#dragpreview11). Does not support secondary dragging, rounded corners, or scaling effects.

**Atomic service API**: This API can be used in atomic services since API version 18.

 |
| ENABLE\_TOUCH\_POINT\_CALCULATION\_BASED\_ON\_FINAL\_PREVIEW19+ | 7 | 

Enables touch point calculation based on the initial drag preview size. Used when the floating image differs from the drag preview. Incompatible with mouse dragging and **DragPreviewMode.ENABLE\_MULTI\_TILE\_EFFECT**.

**Atomic service API**: This API can be used in atomic services since API version 19.

 |

#### DraggingSizeChangeEffect19+

Enumerates the transition effects for switching between the floating image (set through [bindContextMenu](../../dialog-box-control/menu-control/document.md#bindcontextmenu12)) and the drag preview when both are configured on a component.

**Atomic service API**: This API can be used in atomic services since API version 19.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Value | Description |
| :-- | :-- | :-- |
| DEFAULT | 0 | Direct transition from the menu preview to the final drag preview image upon drag initiation. |
| SIZE\_TRANSITION | 1 | Smooth size transition from the menu preview to the final drag preview. Disabled when **DISABLE\_SCALE** is set in [DragPreviewMode](#dragpreviewmode11). Used when the floating preview matches the drag preview. |
| SIZE\_CONTENT\_TRANSITION | 2 | Gradual transition from the menu preview to the final drag preview with opacity and size animations. Disabled when **DISABLE\_SCALE** is set in [DragPreviewMode](#dragpreviewmode11). Suitable for significant visual differences between preview images. |

#### DragInteractionOptions12+

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| isMultiSelectionEnabled | boolean | No | Yes | 
Whether to enable multi-select clustering during drag operations. **true** to enable, **false** otherwise. This parameter takes effect only for the [grid items](../../../scroll-and-swipe/griditem/document.md) and [list items](../../../scroll-and-swipe/listitem/document.md) in the [Grid](../../../scroll-and-swipe/grid/document.md) and [List](../../../scroll-and-swipe/list/document.md) containers.

When this feature is enabled, child components cannot be dragged individually. Preview priority: string in [dragPreview](#dragpreview11) > PixelMap in **dragPreview** > component snapshot. Builder previews not supported.

This parameter is incompatible with bindContextMenu\](ts-universal-attributes-menu.md#bindcontextmenu12) using **isShown** parameter.

Default value: **false**

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| defaultAnimationBeforeLifting | boolean | No | Yes | 

Whether to enable the default press animation (scale-down) during long-press lift phase. **true** to enable, **false** otherwise.

Default value: **false**

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| isLiftingDisabled15+ | boolean | No | Yes | 

Whether to disable the lift animation effect during dragging.

**true**: Disable the lifting effect during dragging.

**false**: Enable the lifting effect during dragging.

With the value **true**, only the custom menu preview (set using [bindContextMenu](../../dialog-box-control/menu-control/document.md#bindcontextmenu8)), also known as the long-press preview, is displayed if both the long-press preview and drag preview are configured.

Default value: **false**

**Atomic service API**: This API can be used in atomic services since API version 15.

 |
| enableEdgeAutoScroll18+ | boolean | No | Yes | 

Whether to trigger automatic scrolling when users drag to the edges of a scrollable container.

**true**: Trigger automatic scrolling.

**false**: Do not trigger automatic scrolling.

Default value: **true**

**Atomic service API**: This API can be used in atomic services since API version 18.

 |
| enableHapticFeedback18+ | boolean | No | Yes | 

Whether to enable haptic feedback during dragging.

**true**: Enable haptic feedback during dragging.

**false**: Disable haptic feedback during dragging. This parameter is effective only for previews with masks (configured using [bindContextMenu](../../dialog-box-control/menu-control/document.md#bindcontextmenu12)).

Note: The settings take effect only when the application has the **ohos.permission.VIBRATE** permission and the user has enabled haptic feedback.

Default value: **false**

**Atomic service API**: This API can be used in atomic services since API version 18.

 |

#### UniformDataType

type UniformDataType = UniformDataType

Defines the uniform data type.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Type | Description |
| :-- | :-- |
| [UniformDataType](../../../../../arkdata/arkts-apis/ohos-data-uniformtypedescriptor-uniform-data-definition-and-description/document.md#uniformdatatype) | Uniform data type. |

#### ImageModifier12+

type ImageModifier = ImageModifier

Defines the image component modifier.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Type | Description |
| :-- | :-- |
| [ImageModifier](../../modifiers-and-custom-property/attribute-modifier/document.md) | Image component modifier. |

#### Example

## Example 1: Allowing Drag and Drop

This example demonstrates how to use [allowDrop](#allowdrop) to configure component drop targets and [draggable](#draggable) to enable component dragging.

// xxx.ets
import { unifiedDataChannel, uniformTypeDescriptor } from '@kit.ArkData';

@Entry
@Component
struct ImageExample {
  @State uri: string = "";
  @State aBlockArr: string\[\] = \[\];
  @State bBlockArr: string\[\] = \[\];
  @State AVisible: Visibility = Visibility.Visible;
  @State dragSuccess: Boolean = false;

  build() {
    Column() {
      Text('Image drag and drop')
        .fontSize('30dp')
      Flex({ direction: FlexDirection.Row, alignItems: ItemAlign.Center, justifyContent: FlexAlign.SpaceAround }) {
        // Replace $r('app.media.icon') with the image resource file you use.
        Image($r('app.media.icon'))
          .width(100)
          .height(100)
          .border({ width: 1 })
          .visibility(this.AVisible)
          .draggable(true)
          .onDragEnd((event: DragEvent) => {
            let ret = event.getResult();
            if (ret == 0) {
              console.info("enter ret == 0")
              this.AVisible = Visibility.Hidden;
            } else {
              console.info("enter ret != 0")
              this.AVisible = Visibility.Visible;
            }
          })
      }
      .margin({ bottom: 20 })

      Row() {
        Column() {
          Text('Invalid drop target')
            .fontSize('15dp')
            .height('10%')
          List() {
            ForEach(this.aBlockArr, (item: string, index) => {
              ListItem() {
                Image(item)
                  .width(100)
                  .height(100)
                  .border({ width: 1 })
              }
              .margin({ left: 30, top: 30 })
            }, (item: string) => item)
          }
          .height('90%')
          .width('100%')
          .allowDrop(\[uniformTypeDescriptor.UniformDataType.TEXT\])
          .onDrop((event?: DragEvent, extraParams?: string) => {
            this.uri = JSON.parse(extraParams as string)?.extraInfo;
            this.aBlockArr.splice(JSON.parse(extraParams as string)?.insertIndex, 0, this.uri);
            console.info("ondrop not udmf data");
          })
          .border({ width: 1 })
        }
        .height("50%")
        .width("45%")
        .border({ width: 1 })
        .margin({ left: 12 })

        Column() {
          Text('Valid drop target')
            .fontSize('15dp')
            .height('10%')
          List() {
            ForEach(this.bBlockArr, (item: string, index) => {
              ListItem() {
                Image(item)
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
          .allowDrop(\[uniformTypeDescriptor.UniformDataType.IMAGE\])
          .onDrop((event?: DragEvent, extraParams?: string) => {
            console.info("enter onDrop")
            let dragData: UnifiedData = (event as DragEvent).getData() as UnifiedData;
            if (dragData != undefined) {
              let arr: Array<unifiedDataChannel.UnifiedRecord> = dragData.getRecords();
              if (arr.length > 0) {
                let image = arr\[0\] as unifiedDataChannel.Image;
                this.uri = image.imageUri;
                this.bBlockArr.splice(JSON.parse(extraParams as string)?.insertIndex, 0, this.uri);
              } else {
                console.info(\`dragData arr is null\`)
              }
            } else {
              console.info(\`dragData  is undefined\`)
            }
            console.info("ondrop udmf data");
            this.dragSuccess = true
          })
        }
        .height("50%")
        .width("45%")
        .border({ width: 1 })
        .margin({ left: 12 })
      }
    }.width('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ba/v3/jEOWiSizT2-GJK01mLzdXQ/en-us_image_0000002537765448.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062235Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=FAC147DA370BBF0D7AE991CE8CB8C0853DB25D52C66E1381403D155AA7436098)

## Example 2: Setting the Drag Preview

This example demonstrates how to configure the preview displayed during the drag process using [dragPreview](#dragpreview11).

// xxx.ets
@Entry
@Component
struct DragPreviewDemo {
  @Builder
  dragPreviewBuilder() {
    Column() {
      Text("dragPreview")
        .width(150)
        .height(50)
        .fontSize(20)
        .borderRadius(10)
        .textAlign(TextAlign.Center)
        .fontColor(Color.Black)
        .backgroundColor(Color.Pink)
    }
  }

  @Builder
  MenuBuilder() {
    Flex({ direction: FlexDirection.Column, justifyContent: FlexAlign.Center, alignItems: ItemAlign.Center }) {
      Text("menu item 1")
        .fontSize(15)
        .width(100)
        .height(40)
        .textAlign(TextAlign.Center)
        .fontColor(Color.Black)
        .backgroundColor(Color.Pink)
      Divider()
        .height(5)
      Text("menu item 2")
        .fontSize(15)
        .width(100)
        .height(40)
        .textAlign(TextAlign.Center)
        .fontColor(Color.Black)
        .backgroundColor(Color.Pink)
    }
    .width(100)
  }

  build() {
    Row() {
      Column() {
        // Replace $r('app.media.image') with the image resource file you use.
        Image($r('app.media.image'))
          .width("30%")
          .draggable(true)
          .bindContextMenu(this.MenuBuilder, ResponseType.LongPress)
          .onDragStart(() => {
            console.info("Image onDragStart")
          })
          .dragPreview(this.dragPreviewBuilder)
      }
      .width("100%")
    }
    .height("100%")
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fe/v3/P77vwFKqS_Kya9ynmc53YA/en-us_image_0000002537925388.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062235Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2B30962A9D5FFF3C3517605DAACDEC338D02093843941827940FD080ED461ABB)

## Example 3: Setting the Drag Preview Style

This example demonstrates how to configure the drag preview style using [dragPreviewOptions](#dragpreviewoptions11). Set **ENABLE\_DEFAULT\_SHADOW** and **ENABLE\_DEFAULT\_RADIUS** for default shadow and unified rounded corner effects. Starting from API version 18, set [dragPreviewOptions](#dragpreviewoptions11) to **ENABLE\_DRAG\_ITEM\_GRAY\_EFFECT** to enable grayscale effects on the original drag item.

// xxx.ets
@Entry
@Component
struct dragPreviewOptionsDemo {
  build() {
    Row() {
      Column() {
        // Replace $r('app.media.image') with the image resource file you use.
        Image($r('app.media.image'))
          .margin({ top: 10 })
          .width("30%")
          .draggable(true)
          .dragPreviewOptions({ mode: DragPreviewMode.AUTO })
        // Replace $r('app.media.image') with the image resource file you use.
        Image($r('app.media.image'))
          .margin({ top: 10 })
          .width("30%")
          .border({
            radius: {
              topLeft: 1,
              topRight: 2,
              bottomLeft: 4,
              bottomRight: 8
            }
          })
          .draggable(true)
          .onDragStart(() => {
            console.info("Image onDragStart")
          })
          .dragPreviewOptions({
            mode: \[DragPreviewMode.ENABLE\_DEFAULT\_SHADOW, DragPreviewMode.ENABLE\_DEFAULT\_RADIUS,
              DragPreviewMode.ENABLE\_DRAG\_ITEM\_GRAY\_EFFECT\]
          })
      }
      .width("100%")
      .height("100%")
    }
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6e/v3/J99O9ectQeOXMdYPsOpFrA/en-us_image_0000002568685165.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062235Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=180B38A808C3B493B3B0FDC9F199E1F775656AE1F62F1B5145E47512E774B533)

## Example 4: Enabling the Multi-select Drag Functionality

This example demonstrates how to configure [isMultiSelectionEnabled](#draginteractionoptions12) to enable the multi-select drag functionality in the **Grid** component.

@Entry
@Component
struct Example {
  @State numbers: number\[\] = \[0, 1, 2, 3, 4, 5, 6, 7, 8\]

  build() {
    Column({ space: 5 }) {
      Grid() {
        ForEach(this.numbers, (item: number) => {
          GridItem() {
            Column()
              .backgroundColor(Color.Blue)
              .width('100%')
              .height('100%')
          }
          .width(90)
          .height(90)
          .selectable(true)
          .selected(true)
          .dragPreviewOptions({}, { isMultiSelectionEnabled: true })
          .onDragStart(() => {

          })
        }, (item: string) => item)
      }
      .columnsTemplate('1fr 1fr 1fr')
      .rowsTemplate('1fr 1fr 1fr')
      .height(300)
    }
    .width('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/75/v3/dl_IG5TpRuaB6vXSrpBuXA/en-us_image_0000002568765175.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062235Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=CE0571300126A5E09D46FB109FE0C14F5263B401B0DBCCF5447E0E4F04F4CBF1)

## Example 5: Enabling the Default Pressed State Animation

This example demonstrates configuring [defaultAnimationBeforeLifting](#draginteractionoptions12) to enable the default press animation effect in the **Grid** component.

@Entry
@Component
struct Example {
  @State numbers: number\[\] = \[0, 1, 2, 3, 4, 5, 6, 7, 8\]

  build() {
    Column({ space: 5 }) {
      Grid() {
        ForEach(this.numbers, (item: number) => {
          GridItem() {
            Column()
              .backgroundColor(Color.Blue)
              .width('100%')
              .height('100%')
          }
          .width(90)
          .height(90)
          .selectable(true)
          .selected(true)
          .dragPreviewOptions({}, { isMultiSelectionEnabled: true, defaultAnimationBeforeLifting: true })
          .onDragStart(() => {

          })
        }, (item: string) => item)
      }
      .columnsTemplate('1fr 1fr 1fr')
      .rowsTemplate('1fr 1fr 1fr')
      .height(300)
    }
    .width('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c4/v3/zhu54OMbRxqwAgFHsJudUA/en-us_image_0000002537765450.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062235Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6D73B0887926D506D734D393FD7C5BB2971D39F508DB8033A97325C51B812BA3)

## Example 6: Customizing the Preview Style

This example demonstrates customizing the **Image** component background by configuring [ImageModifier](#imagemodifier12).

// xxx.ets
import { ImageModifier } from '@kit.ArkUI';

@Entry
@Component
struct dragPreviewOptionsDemo {
  @State myModifier: ImageAttribute = new ImageModifier().opacity(0.5)
  @State vis: boolean = true
  @State changeValue: string = ''
  @State submitValue: string = ''
  @State positionInfo: CaretOffset = { index: 0, x: 0, y: 0 }
  controller: SearchController = new SearchController()
  @State OpacityIndex: number = 0
  @State OpacityList: (number | undefined | null)\[\] = \[
    0.3, 0.5, 0.7, 1, -50, 0, 10, undefined, null
  \]

  build() {
    Row() {
      Column() {
        Text(this.OpacityList\[this.OpacityIndex\] + "")
        Button("Opacity")
          .onClick(() => {
            this.OpacityIndex++
            if (this.OpacityIndex > this.OpacityList.length - 1) {
              this.OpacityIndex = 0
            }
          })
        // Replace $r('app.media.image') with the image resource file you use.
        Image($r('app.media.image'))
          .margin({ top: 10 })
          .width("100%")
          .draggable(true)
          .dragPreviewOptions({
            modifier: this.myModifier.opacity(this.OpacityList\[this.OpacityIndex\]) as ImageModifier
          })
      }
      .width("50%")
      .height("50%")
    }
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4/v3/2xGfpZ7WTFuEbGekWH-mpg/en-us_image_0000002537925390.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062235Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B242DC0C1BC03812936345BF8B919C3AE5DE325B3D2A74E6160D6DC7E97C9BD0)

## Example 7: Configuring Image Dragging Settings

This example demonstrates drag configuration for different image types (online resources, local resources, and PixelMap).

The **ohos.permission.INTERNET** permission is required for using online images. For details about how to apply for a permission, see [Declaring Permissions](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/declare-permissions).

// xxx.ets
import { uniformTypeDescriptor, unifiedDataChannel } from '@kit.ArkData';
import { image } from '@kit.ImageKit';
import { request } from '@kit.BasicServicesKit';
import { fileIo } from '@kit.CoreFileKit';
import { buffer } from '@kit.ArkTS';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct ImageDrag {
  @State targetImage1: string | PixelMap | null = null;
  @State targetImage2: string | PixelMap | null = null;
  @State targetImage3: string | PixelMap | null = null;
  context: Context | undefined = this.getUIContext().getHostContext();
  filesDir = this.context?.filesDir;

  public async createPixelMap(pixelMap: unifiedDataChannel.SystemDefinedPixelMap): Promise<image.PixelMap | null> {
    let mWidth: number = (pixelMap.details?.width ?? -1) as number;
    let mHeight: number = (pixelMap.details?.height ?? -1) as number;
    let mPixelFormat: image.PixelMapFormat =
      (pixelMap.details?.\['pixel-format'\] ?? image.PixelMapFormat.UNKNOWN) as image.PixelMapFormat;
    let mItemPixelMapData: Uint8Array = pixelMap.rawData;
    const opts: image.InitializationOptions = {
      editable: false, pixelFormat: mPixelFormat, size: {
        height: mHeight,
        width: mWidth
      }
    };
    const buffer: ArrayBuffer = mItemPixelMapData.buffer.slice(mItemPixelMapData.byteOffset,
      mItemPixelMapData.byteLength + mItemPixelMapData.byteOffset);
    try {
      let pixelMap: image.PixelMap = await image.createPixelMap(buffer, opts);
      return pixelMap;
    } catch (err) {
      console.error('dragtest--> getPixelMap', err);
      return null;
    }
  }

  build() {
    Column() {
      Flex({ direction: FlexDirection.Row, justifyContent: FlexAlign.Center }) {
        // Drag an online image.
        Column() {
          Text('Online Image').fontSize(14)
          Image('https://www.example.com/xxx.png')// Enter a specific online image URL.
            .objectFit(ImageFit.Contain)
            .draggable(true)
            .onDragStart(() => {
            })
            .width(100)
            .height(100)
        }
        .border({
          width: 2,
          color: Color.Gray,
          radius: 5,
          style: BorderStyle.Dotted
        })
        .alignItems(HorizontalAlign.Center).justifyContent(FlexAlign.Center)

        // Drag a local image.
        Column() {
          Text('Local Image').fontSize(14)
          // Replace $r('app.media.example') with the image resource file you use.
          Image($r('app.media.example'))
            .objectFit(ImageFit.Contain)
            .draggable(true)
            .onDragStart(() => {
            })
            .width(100)
            .height(100)
        }
        .border({
          width: 2,
          color: Color.Gray,
          radius: 5,
          style: BorderStyle.Dotted
        })
        .alignItems(HorizontalAlign.Center).justifyContent(FlexAlign.Center)

        // Drag a PixelMap object.
        Column() {
          Text('PixelMap').fontSize(14)
          // Replace $r('app.media.example') with the image resource file you use.
          Image(this.context?.resourceManager.getDrawableDescriptor($r('app.media.example').id).getPixelMap())
            .objectFit(ImageFit.Contain)
            .draggable(true)
            .onDragStart(() => {
            })
            .width(100)
            .height(100)
        }
        .border({
          width: 2,
          color: Color.Gray,
          radius: 5,
          style: BorderStyle.Dotted
        })
        .alignItems(HorizontalAlign.Center).justifyContent(FlexAlign.Center)
      }

      // Set the drop data type to Image.
      Text('Data type is Image').fontSize(14).margin({ top: 10 })
      Column() {
        Image(this.targetImage1)
          .objectFit(ImageFit.Contain)
          .width('70%')
          .height('70%')
          .allowDrop(\[uniformTypeDescriptor.UniformDataType.IMAGE\])
          .onDrop((event: DragEvent, extraParams: string) => {
            if (extraParams === null || extraParams === undefined) {
              return;
            }
            // Obtain the image through extraParams.
            let arr: Record<string, object> = JSON.parse(extraParams) as Record<string, object>;
            let uri = arr\['extraInfo'\];
            if (typeof uri == 'string') {
              this.targetImage1 = uri;
              try {
                request.downloadFile(this.context, {
                  url: uri,
                  filePath: this.filesDir + '/example.png'
                }).then((downloadTask: request.DownloadTask) => {
                  let file = fileIo.openSync(this.filesDir + '/example.png', fileIo.OpenMode.READ\_WRITE);
                  let arrayBuffer = new ArrayBuffer(1024);
                  let readLen = fileIo.readSync(file.fd, arrayBuffer);
                  let buf = buffer.from(arrayBuffer, 0, readLen);
                  console.info(\`The content of file: ${buf.toString()}\`);
                  fileIo.closeSync(file);
                })
              } catch (error) {
              }
            }
          })
      }
      .width('70%')
      .height('25%')
      .border({
        width: 2,
        color: Color.Gray,
        radius: 5,
        style: BorderStyle.Dotted
      })
      .alignItems(HorizontalAlign.Center)
      .justifyContent(FlexAlign.Center)

      Column() {
        Image(this.targetImage2)
          .objectFit(ImageFit.Contain)
          .width('70%')
          .height('70%')
          .allowDrop(\[uniformTypeDescriptor.UniformDataType.IMAGE\])
          .onDrop((event: DragEvent, extraParams: string) => {
            // Obtain the image through uniformTypeDescriptor.
            let data: UnifiedData = event.getData();
            let records: Array<unifiedDataChannel.UnifiedRecord> = data.getRecords();
            if (records\[0\].getType() === uniformTypeDescriptor.UniformDataType.IMAGE) {
              let image: unifiedDataChannel.Image = records\[0\] as unifiedDataChannel.Image;
              this.targetImage2 = image.imageUri;
            }
          })
      }
      .width('70%')
      .height('25%')
      .border({
        width: 2,
        color: Color.Gray,
        radius: 5,
        style: BorderStyle.Dotted
      })
      .alignItems(HorizontalAlign.Center)
      .justifyContent(FlexAlign.Center)

      // Set the drop data type to PixelMap.
      Text('Data type is PixelMap').fontSize(14).margin({ top: 10 })
      Column() {
        Image(this.targetImage3)
          .objectFit(ImageFit.Contain)
          .width('70%')
          .height('70%')
          .allowDrop(\[uniformTypeDescriptor.UniformDataType.OPENHARMONY\_PIXEL\_MAP\])
          .onDrop(async (event: DragEvent, extraParams: string) => {
            // Obtain the image through uniformTypeDescriptor.
            let data: UnifiedData = event.getData();
            let records: Array<unifiedDataChannel.UnifiedRecord> = data.getRecords();
            if (records\[0\].getType() === uniformTypeDescriptor.UniformDataType.OPENHARMONY\_PIXEL\_MAP) {
              let record: unifiedDataChannel.SystemDefinedPixelMap =
                records\[0\] as unifiedDataChannel.SystemDefinedPixelMap;
              this.targetImage3 = await this.createPixelMap(record);

              // Save data to local storage.
              const imagePackerApi = image.createImagePacker();
              let packOpts: image.PackingOption = { format: "image/jpeg", quality: 98 };
              const path: string = this.context?.cacheDir + "/pixel\_map.jpg";
              let file = fileIo.openSync(path, fileIo.OpenMode.CREATE | fileIo.OpenMode.READ\_WRITE);
              imagePackerApi.packToFile(this.targetImage3, file.fd, packOpts).then(() => {
                // Pack the image into the file.
              }).catch((error: BusinessError) => {
                console.error('Failed to pack the image. And the error is: ' + error);
              })
            }
          })
      }
      .width('70%')
      .height('25%')
      .border({
        width: 2,
        color: Color.Gray,
        radius: 5,
        style: BorderStyle.Dotted
      })
      .alignItems(HorizontalAlign.Center)
      .justifyContent(FlexAlign.Center)

    }.width('100%').height('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/51/v3/KZVvswYeQt6ap3riOWGAiQ/en-us_image_0000002568685167.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062235Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D02349940A8290ED36081118CA4421B4F485597B3D187B23D8CF578BAF559F5A)

## Example 8: Enabling Haptic Feedback for Dragging

This example demonstrates enabling haptic feedback during image drag operations by configuring [enableHapticFeedback](#draginteractionoptions12), supported since API version 18.

// xxx.ets
@Entry
@Component
struct DragPreviewDemo {
  @Builder
  MenuBuilder() {
    Flex({ direction: FlexDirection.Column, justifyContent: FlexAlign.Center, alignItems: ItemAlign.Center }) {
      Text("menu item 1")
        .fontSize(15)
        .width(100)
        .height(40)
        .textAlign(TextAlign.Center)
        .fontColor(Color.Black)
        .backgroundColor(Color.Pink)
      Divider()
        .height(5)
      Text("menu item 2")
        .fontSize(15)
        .width(100)
        .height(40)
        .textAlign(TextAlign.Center)
        .fontColor(Color.Black)
        .backgroundColor(Color.Pink)
    }
    .width(100)
  }

  build() {
    Row() {
      Column() {
        // Replace $r('app.media.app\_icon') with the image resource file you use.
        Image($r('app.media.app\_icon'))
          .width("30%")
          .draggable(true)
          .dragPreviewOptions({},
            { isMultiSelectionEnabled: true, defaultAnimationBeforeLifting: true, enableHapticFeedback: true })
          .bindContextMenu(this.MenuBuilder, ResponseType.LongPress)
          .onDragStart(() => {
            console.info("Image onDragStart")
          })
      }
      .width("100%")
    }
    .height("100%")
  }
}

## Example 9: Customizing the Drag Preview

Starting from API version 15, this example configures [onlyForLifting](../../../universal-events/interaction-response-events/drag-event/document.md#previewconfiguration15) to create a custom preview image exclusively for the lift animation effect, and [isLiftingDisabled](#draginteractionoptions12) to disable the lift animation effect.

// xxx.ets
@Entry
@Component
struct LiftingExampleDemo {
  @Builder
  dragPreviewBuilder() {
    Column() {
      Text("dragPreview builder")
        .width(150)
        .height(50)
        .fontSize(20)
        .borderRadius(10)
        .textAlign(TextAlign.Center)
        .fontColor(Color.Black)
        .backgroundColor(Color.Green)
    }
  }

  @Builder
  MenuBuilder() {
    Flex({ direction: FlexDirection.Column, justifyContent: FlexAlign.Center, alignItems: ItemAlign.Center }) {
      Text("menu 1")
        .fontSize(25)
        .width(200)
        .height(60)
        .textAlign(TextAlign.Center)
        .fontColor(Color.Black)
        .backgroundColor(Color.Green)
      Divider()
        .height(5)
      Text("menu 2")
        .fontSize(25)
        .width(200)
        .height(60)
        .textAlign(TextAlign.Center)
        .fontColor(Color.Black)
        .backgroundColor(Color.Green)
    }
    .width(100)
  }

  build() {
    Column() {
      Column() {
        Text("Lifting effect disabled")
          .fontSize(30)
          .height(30)
          .backgroundColor('#FFFFFF')
          .margin({ top: 30 })
        // Replace $r('app.media.startIcon') with the image resource file you use.
        Image($r('app.media.startIcon'))
          .width("40%")
          .draggable(true)
          .margin({ top: 15 })
          .bindContextMenu(this.MenuBuilder, ResponseType.LongPress)
          .onDragStart(() => {
          })
          .dragPreviewOptions({}, {
            isLiftingDisabled: true
          })
          .dragPreview(this.dragPreviewBuilder, {
            onlyForLifting: true,
            delayCreating: true
          })
      }.width("%")

      Column() {
        Text("Lifting effect only")
          .fontSize(30)
          .height(30)
          .backgroundColor('#FFFFFF')
          .margin({ top: 80 })
        // Replace $r('app.media.startIcon') with the image resource file you use.
        Image($r('app.media.startIcon'))
          .width("40%")
          .draggable(true)
          .margin({ top: 15 })
          .onDragStart(() => {
          })
          .dragPreviewOptions({}, {
            isLiftingDisabled: false
          })
          .dragPreview(this.dragPreviewBuilder, {
            onlyForLifting: true,
            delayCreating: true
          })
      }.width("100%")
    }.height("100%")
  }
}

Custom preview for the lifting effect only

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/65/v3/B8JaQeghR_OqFzcCOZyQZw/en-us_image_0000002568765177.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062235Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7D521E636FC4E83DB36C99BA6E6C4C241A746B3880220EC3749762413C0A661B)

Custom preview with the lifting effect disabled

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/77/v3/N93FqmxKQia8Z7bKPfEeHg/en-us_image_0000002537765452.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062235Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F33A2DCC9073A0FB1C3B0B1575A30F5F9390DF83A9166462BD034E4D77645C94)

## Example 10: Implementing Touch Point Calculation Based on Initial Drag Preview Size

This example configures [DragPreviewMode](#dragpreviewmode11) as **ENABLE\_TOUCH\_POINT\_CALCULATION\_BASED\_ON\_FINAL\_PREVIEW** to calculate touch point positions using the initial drag preview size, supported since API version 19. This setting has no effect when [DragPreviewMode](#dragpreviewmode11) is set to **ENABLE\_MULTI\_TILE\_EFFECT**.

@Entry
@Component
struct Index {
  // Replace $r('app.media.app\_icon') with the image resource file you use.
  private iconStr: ResourceStr = $r("app.media.app\_icon")

  @Builder
  MyPreview() {
    // Replace $r('app.media.image') with the image resource file you use.
    Image($r('app.media.image'))
      .width(100)
      .height(100)
  }

  @Builder
  MyMenuPreview() {
    Column() {
      // Replace $r('app.media.image') with the image resource file you use.
      Image($r('app.media.image'))
        .width(100)
        .height(100)
    }
    .backgroundColor(Color.Green)
    .width(300)
    .height(300)
  }

  @Builder
  MyMenu() {
    Menu() {
      MenuItem({ startIcon: this.iconStr, content: "Menu option" })
      MenuItem({ startIcon: this.iconStr, content: "Menu option" })
    }
  }

  @Builder
  SubMenu() {
    Menu() {
      MenuItem({ content: "Copy", labelInfo: "Ctrl+C" })
      MenuItem({ content: "Paste", labelInfo: "Ctrl+V" })
    }
  }

  build() {
    NavDestination() {
      Scroll() {
        Column() {
          Text("no ENABLE\_TOUCH\_POINT\_CALCULATION\_BASED\_ON\_FINAL\_PREVIEW")
          // Replace $r('app.media.image') with the image resource file you use.
          Image($r('app.media.image'))
            .width(200)
            .height(200)
            .bindContextMenu(this.MyMenu, ResponseType.LongPress, {
              preview: this.MyPreview
            })
            .dragPreview(this.MyMenuPreview)
            .draggable(true)

          Text("ENABLE\_TOUCH\_POINT\_CALCULATION\_BASED\_ON\_FINAL\_PREVIEW")
          // Replace $r('app.media.image') with the image resource file you use.
          Image($r('app.media.image'))
            .width(200)
            .height(200)
            .bindContextMenu(this.MyMenu, ResponseType.LongPress, {
              preview: this.MyPreview
            })
            .dragPreview(this.MyMenuPreview)
            .draggable(true)
            .dragPreviewOptions({
              mode: \[DragPreviewMode.ENABLE\_TOUCH\_POINT\_CALCULATION\_BASED\_ON\_FINAL\_PREVIEW\]
            })
        }.width('100%')
      }
    }
    .height('100%')
    .width('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d9/v3/6NYG48SMS8a_OvIaNfSfow/en-us_image_0000002537925392.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062235Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=71F33A17CCE02CABAD836540DB3F9FE944079A1EBD831B22AF8947C81C38F2F6)

## Example 11: Implementing Transition Effects Between Floating Images and Drag Previews

This example demonstrates how to implement different transition effects between floating images and drag previews by configuring [DraggingSizeChangeEffect](#draggingsizechangeeffect19), supported since API version 19.

@Entry
@Component
struct Index {
  // Replace $r('app.media.app\_icon') with the image resource file you use.
  private iconStr: ResourceStr = $r("app.media.app\_icon")

  @Builder
  MyPreview() {
    // Replace $r('app.media.image') with the image resource file you use.
    Image($r('app.media.image'))
      .width(200)
      .height(200)
  }

  @Builder
  MyMenuPreviewSame() {
    Column() {
      // Replace $r('app.media.image') with the image resource file you use.
      Image($r('app.media.image'))
        .width(300)
        .height(300)
    }
  }

  @Builder
  MyMenuPreview() {
    Column() {
      // Replace $r('app.media.startIcon') with the image resource file you use.
      Image($r('app.media.startIcon'))
        .width(300)
        .height(300)
    }
  }

  @Builder
  MyMenu() {
    Menu() {
      MenuItem({ startIcon: this.iconStr, content: "Menu option" })
      MenuItem({ startIcon: this.iconStr, content: "Menu option" })
    }
  }

  @Builder
  SubMenu() {
    Menu() {
      MenuItem({ content: "Copy", labelInfo: "Ctrl+C" })
      MenuItem({ content: "Paste", labelInfo: "Ctrl+V" })
    }
  }

  build() {
    Column() {
      Text("sizeChangeEffect: SIZE\_TRANSITION - Long press to open menu, and drag to transition from menu preview to drag preview with scaling effect (no overlay).")
        .margin({ top: 10 })
      // Replace $r('app.media.image') with the image resource file you use.
      Image($r('app.media.image'))
        .width(200)
        .height(200)
        .bindContextMenu(this.MyMenu, ResponseType.LongPress, {
          preview: this.MyMenuPreviewSame
        })
        .dragPreview(this.MyPreview)
        .dragPreviewOptions({
          sizeChangeEffect: DraggingSizeChangeEffect.SIZE\_TRANSITION
        })
        .draggable(true)

      Text("sizeChangeEffect: SIZE\_CONTENT\_TRANSITION - Long press to open menu, and drag to transition with two-layer overlay effect (menu preview and drag preview).")
        .margin({ top: 10 })
      // Replace $r('app.media.image') with the image resource file you use.
      Image($r('app.media.image'))
        .width(200)
        .height(200)
        .bindContextMenu(this.MyMenu, ResponseType.LongPress, {
          preview: this.MyMenuPreview
        })
        .dragPreview(this.MyPreview)
        .dragPreviewOptions({
          sizeChangeEffect: DraggingSizeChangeEffect.SIZE\_CONTENT\_TRANSITION
        })
        .draggable(true)
    }
    .height('100%')
    .width('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0a/v3/J1eF4gvXQeq4rj7B1xLJYg/en-us_image_0000002568685169.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062235Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=42B45F7FCC8279E4ED2A3E15A32E91198F782155966295E32144925C53802234)
