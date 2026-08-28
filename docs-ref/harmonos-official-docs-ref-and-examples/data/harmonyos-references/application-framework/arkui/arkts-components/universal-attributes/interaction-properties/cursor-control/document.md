# Cursor Control

You can control the display style of the mouse cursor.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f4/v3/s_mdKf8YQnS_WREq1563Cg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062235Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4DC7E8C9F1908980792FEEE371AA89E73BF9872028E2BD25DD12C76C81460EED)

This feature is supported since API version 11. Updates will be marked with a superscript to indicate their earliest API version.

#### cursorControl

#### \[h2\]setCursor

setCursor(value: PointerStyle): void

Sets the current mouse cursor style. This API can be used globally in method statements.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [PointerStyle](#pointerstyle) | All consistent | Cursor style. |

#### \[h2\]restoreDefault

restoreDefault(): void

Restores the mouse cursor to the default arrow style. This API can be used globally in method statements.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

#### PointerStyle

type PointerStyle = pointer.PointerStyle

Defines the pointer style.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Type | Description |
| :-- | :-- |
| [pointer.PointerStyle](../../../../../../system/basic-functions/input-kit/arkts-apis/ohos-multimodalinput-pointer-mouse-pointer/document.md#pointerstyle) | Pointer style. |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/83/v3/7HXsVMQ-QSqfRBqTM2OGjg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062235Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=44B60CDAAFA95A8C4BD857E5F20F6B0027945F20BE71884881957609595A6E82)

Directly using **cursorControl** can lead to the issue of [ambiguous UI context](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-global-interface#ambiguous-ui-context). To avoid this, obtain the [UIContext](../../../../arkts-api/ui/ohos-arkui-uicontext-uicontext/class-uicontext/document.md) object using the **getUIContext()** API and then obtain the **cursorControl** bound to the instance using the [getCursorController](../../../../arkts-api/ui/ohos-arkui-uicontext-uicontext/class-uicontext/document.md#getcursorcontroller12) API.

#### Example

This example demonstrates how to change the mouse cursor style using **setCursor**.

// xxx.ets
import { pointer } from '@kit.InputKit';

@Entry
@Component
struct CursorControlExample {
  @State text: string = '';
  controller: TextInputController = new TextInputController()

  build() {
    Column() {
      Row()
        .height(200)
        .width(200)
        .backgroundColor(Color.Green)
        .position({ x: 60, y: 70 })
        .onHover((flag) => {
          if (flag) {
            // You are advised to use this.getUIContext().getCursorController().setCursor().
            cursorControl.setCursor(pointer.PointerStyle.EAST)
          } else {
            // You are advised to use this.getUIContext().getCursorController().restoreDefault().
            cursorControl.restoreDefault()
          }
        })
      Row()
        .height(200)
        .width(200)
        .backgroundColor(Color.Blue)
        .position({ x: 130, y: 120 })
        .onHover((flag) => {
          if (flag) {
            // You are advised to use this.getUIContext().getCursorController().setCursor().
            cursorControl.setCursor(pointer.PointerStyle.WEST)
          } else {
            // You are advised to use this.getUIContext().getCursorController().restoreDefault().
            cursorControl.restoreDefault()
          }
        })
    }.width('100%')
  }
}

Diagrams:

When the mouse hovers over the blue area, it displays a west-pointing arrow cursor style.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9/v3/Sl5YEOVvTPOn99gybhC5Jg/en-us_image_0000002537765456.jpg?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062235Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1E402F350C6B96AB74BC555F8CB30899326B6607E63324F355EEA1EA2CACAC65)

When the mouse hovers over the green area, it displays an east-pointing arrow cursor style.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ef/v3/AZQ5B7Q2ShqqqF5P6kDJ5Q/en-us_image_0000002537925396.jpg?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062235Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=33595467404215A2F5847EC0DBE3BB5E8408B350B5C2D301A4BDA978BC500199)
