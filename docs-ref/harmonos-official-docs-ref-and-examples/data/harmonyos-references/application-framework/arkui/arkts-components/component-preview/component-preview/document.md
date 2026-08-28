# Component Preview

Component preview enables you to preview the UI effect of individual custom components.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ae/v3/Y_NvLv9XT1Sm4yZRzt5CFA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062249Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=34E13DA132B122282870CB7A088963777DE30A287C00C1689F556318E04DFA6A)

The initial APIs of this module are supported since API version 7. Newly added APIs will be marked with a superscript to indicate their earliest API version.

For details about usage, see [Component Preview](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/ui-ide-previewer#component-preview).

#### @Preview Decorator

The @Preview decorator decorates custom components for preview.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cd/v3/goHHRAAjQuuq2mVfkVgunw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062249Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D25034F0D4735BC2357BCCFD6EED174DD357F6DF95BA9303C6847F16D34D915B)

This API is supported in ArkTS widgets, though component preview itself is not supported in ArkTS widgets.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

#### PreviewParams9+

Implements a configuration object for @Preview parameters.

Defines preview device attributes such as device type and screen state.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| title | string | No | Yes | Name of the component module to preview. Default value: custom component name. |
| width | number | No | Yes | Width of the preview device, in px. Default value: **1080**. |
| height | number | No | Yes | Height of the preview device, in px. Default value: **2340**. |
| locale | string | No | Yes | Device language (for example, **zh\_CN** and **en\_US**). Default value: **zh\_CN**. |
| colorMode | string | No | Yes | Color mode of the preview device. The default value is **light** for non-TV devices (only **light** supported) and **dark** for TV devices (only **dark** supported). |
| deviceType | string | No | Yes | Device type for preview rendering. Default value: **Phone**. |
| dpi | number | No | Yes | DPI of the preview device. Default value: **480**. |
| orientation | string | No | Yes | Screen orientation of the preview device. Options: **portrait** (default), **landscape**. |
| roundScreen | boolean | No | Yes | Whether the preview screen is circular. Default value: **false**. **true**: circular. **false**: non-circular. |

#### Example.

This example demonstrates @Preview usage with and without parameters.

@Entry
@Preview
@Component
struct Index {
  @State message: string = 'default Preview';

  build() {
    RelativeContainer() {
      Text(this.message)
        .fontSize(50)
        .fontWeight(FontWeight.Bold)
    }
    .height('100%')
    .width('100%')
  }
}

@Preview({
  title: 'PreviewParams',
  width: 540,
  height: 1170
})
@Component
struct Test {
  @State message: string = 'PreviewParams';

  build() {
    RelativeContainer() {
      Text(this.message)
        .fontSize(40)
        .fontWeight(FontWeight.Bold)
    }
    .height('100%')
    .width('100%')
  }
}
