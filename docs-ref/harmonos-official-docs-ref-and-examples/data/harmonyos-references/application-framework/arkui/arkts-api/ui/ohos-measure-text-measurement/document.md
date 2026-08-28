# @ohos.measure (Text Measurement)

The **measure** module provides APIs for measuring text metrics, such as text height and width.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5f/v3/5Ogu9PGCT2iSaojgbOQgYg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062228Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=EDBCA6A010B7111496AEBF077F933E562DB618FF4ADCA1125546ED5E6195542D)

-   The initial APIs of this module are supported since API version 9. Newly added APIs will be marked with a superscript to indicate their earliest API version.
    
-   This module cannot be used in the file declaration of the [UIAbility](../../../../ability-kit/arkts-apis/stage-model/ohos-app-ability-uiability-ability-with-ui/document.md). In other words, the APIs of this module can be used only after a component instance is created; they cannot be called in the lifecycle of the UIAbility.
    
-   To perform more complex text measurements, you are advised to call the corresponding graphics measurement API, specifically [Paragraph](../../../../../graphics/arkgraphics-2d/arkts-apis/ohos-graphics-text-text/document.md#paragraph).
    
-   Avoid using [ApplicationContext.setFontSizeScale](../../../../ability-kit/arkts-apis/dependent-elements-and-definitions/application/applicationcontext-application-context/document.md#applicationcontextsetfontsizescale13) during text measurement API calls. To ensure timing consistency and the accuracy of measurement results, manually listen for font scale changes.
    
-   For measuring text after truncation, direct use of the string length for truncation may lead to inaccuracies. This is because certain Unicode characters (for example, emojis) have code points with a length greater than 1, and truncating by string length can split these multi-code-point characters, resulting in incorrect text display or measurement errors. As such, you are advised to perform iterative processing based on Unicode code points during truncation.
    

#### Modules to Import

import { MeasureText } from '@kit.ArkUI';

#### MeasureText.measureText(deprecated)

static measureText(options: MeasureOptions): number

Measures the single-line display width of the specified text. For multi-line text (separated by newline characters **\\n**), this API returns the width of the longest line.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/88/v3/EBojljFzT3uU543ze5wduQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062228Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3DAA4123C8D61BF011DCDA100B5095DB71623CE19546CB596CE84FA6D77C9BED)

-   This API is supported since API version 9 and deprecated since API version 18. You are advised to use [measureText](../ohos-arkui-uicontext-uicontext/class-measureutils/document.md#measuretext12) instead. Before calling this API, you need to obtain the [MeasureUtils](../ohos-arkui-uicontext-uicontext/class-measureutils/document.md) object using the [getMeasureUtils](../ohos-arkui-uicontext-uicontext/class-uicontext/document.md#getmeasureutils12) method in [UIContext](../ohos-arkui-uicontext-uicontext/class-uicontext/document.md). Directly using **measureText** can lead to the issue of [ambiguous UI context](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-global-interface#ambiguous-ui-context).
    
-   Since API version 12, you can use the [getMeasureUtils](../ohos-arkui-uicontext-uicontext/class-uicontext/document.md#getmeasureutils12) API in [UIContext](../ohos-arkui-uicontext-uicontext/class-uicontext/document.md) to obtain the [MeasureUtils](../ohos-arkui-uicontext-uicontext/class-measureutils/document.md) object associated with the current UI context.
    
-   **measureText** always measures single-line text width. Layout constraints in **options** (**constraintWidth**, **maxLines**, and more) do not affect results. For layout-constrained width measurement, use [measureTextSize](../ohos-arkui-uicontext-uicontext/class-measureutils/document.md#measuretextsize12).
    

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| options | [MeasureOptions](#measureoptions) | Yes | Information about the measured text. |

**Return value**

| Type | Description |
| :-- | :-- |
| number | 
Text width.

Unit: px

 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fe/v3/dj7w9mh4S6CDxi7CHqc7mg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062228Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=71516D844F537B86F83B81428F9ADC27EC7C754C170E1636AEDFC0F6ADCEFB8C)

Directly using **MeasureText** can lead to the issue of [ambiguous UI context](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-global-interface#ambiguous-ui-context). To avoid this, obtain the [MeasureUtils](../ohos-arkui-uicontext-uicontext/class-measureutils/document.md) object associated with the current UI context by using the [getMeasureUtils](../ohos-arkui-uicontext-uicontext/class-uicontext/document.md#getmeasureutils12) API in [UIContext](../ohos-arkui-uicontext-uicontext/class-uicontext/document.md).

**Example**

import { MeasureText } from '@kit.ArkUI';

@Entry
@Component
struct Index {
  @State textWidth: number = MeasureText.measureText({
    // You are advised to use this.getUIContext().getMeasureUtils().measureText().
    textContent: "Hello World",
    fontSize: '50px'
  });

  build() {
    Row() {
      Column() {
        Text(\`The width of 'Hello World': ${this.textWidth}\`)
      }
      .width('100%')
    }
    .height('100%')
  }
}

#### MeasureText.measureTextSize(deprecated)

static measureTextSize(options: MeasureOptions): SizeOptions

Measures the width and height of the given text.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/33/v3/tSlL68EKSRitWpMR3CSvvg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062228Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E73F3F2E07C1C590C66F7AC25B248B4BC2DF77EFC4222DD5050C1977B8762526)

-   This API is supported since API version 10 and deprecated since API version 18. You are advised to use [measureTextSize](../ohos-arkui-uicontext-uicontext/class-measureutils/document.md#measuretextsize12) instead. Before calling this API, you need to obtain the [MeasureUtils](../ohos-arkui-uicontext-uicontext/class-measureutils/document.md) object using the [getMeasureUtils](../ohos-arkui-uicontext-uicontext/class-uicontext/document.md#getmeasureutils12) method in [UIContext](../ohos-arkui-uicontext-uicontext/class-uicontext/document.md). Directly using **measureTextSize** can lead to the issue of [ambiguous UI context](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-global-interface#ambiguous-ui-context).
    
-   Since API version 12, you can use the [getMeasureUtils](../ohos-arkui-uicontext-uicontext/class-uicontext/document.md#getmeasureutils12) API in [UIContext](../ohos-arkui-uicontext-uicontext/class-uicontext/document.md) to obtain the [MeasureUtils](../ohos-arkui-uicontext-uicontext/class-measureutils/document.md) object associated with the current UI context.
    

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| options | [MeasureOptions](#measureoptions) | Yes | Information about the measured text. |

**Return value**

| Type | Description |
| :-- | :-- |
| [SizeOptions](../../../arkts-components/common-definitions/basic-types/document.md#sizeoptions) | 
Layout width and height occupied by the text.

**NOTE**

The return values for text width and height are both in px.

 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1a/v3/jrW9c1CJSPWU9xit83d1Yg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062228Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=73A4898EEADE0FBFACB528E4746A0D9C094E2A8A40DE6517A006970830B65CAA)

Directly using **MeasureText** can lead to the issue of [ambiguous UI context](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-global-interface#ambiguous-ui-context). To avoid this, obtain the [MeasureUtils](../ohos-arkui-uicontext-uicontext/class-measureutils/document.md) object associated with the current UI context by using the [getMeasureUtils](../ohos-arkui-uicontext-uicontext/class-uicontext/document.md#getmeasureutils12) API in [UIContext](../ohos-arkui-uicontext-uicontext/class-uicontext/document.md).

**Example**

import { MeasureText } from '@kit.ArkUI';

@Entry
@Component
struct Index {
  textSize: SizeOptions = MeasureText.measureTextSize({
    // You are advised to use this.getUIContext().getMeasureUtils().measureTextSize().
    textContent: "Hello World",
    fontSize: '50px'
  });

  build() {
    Row() {
      Column() {
        Text(\`The width of 'Hello World': ${this.textSize.width}\`)
        Text(\`The height of 'Hello World': ${this.textSize.height}\`)
      }
      .width('100%')
    }
    .height('100%')
  }
}

#### MeasureOptions

Provides attributes of the measured text.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| textContent | string | [Resource](../../../arkts-components/common-definitions/basic-types/document.md#resource) | No | No | Content of the measured text. |
| constraintWidth10+ | number | string | [Resource](../../../arkts-components/common-definitions/basic-types/document.md#resource) | No | Yes | 
Layout width of the measured text.

**NOTE**

The default unit is vp. The value cannot be a percentage. If this parameter is not set, the value of **SizeOptions** is the maximum width allowed for the single-line text.

 |
| fontSize | number | string | [Resource](../../../arkts-components/common-definitions/basic-types/document.md#resource) | No | Yes | 

Font size of the text to be measured. When **fontSize** is of the number type, the unit is vp.

Default value: **16**

**NOTE**

The value cannot be a percentage.

Since API version 12, the fp unit is used when **fontSize** is of the number type.

 |
| fontStyle | number | [FontStyle](../../../arkts-components/common-definitions/enums/document.md#fontstyle) | No | Yes | 

Font style of the measured text.

Default value: **FontStyle.Normal**

Value range for the number type: \[0, 1\], with intervals of 1, corresponding to the values in the **FontStyle** enum

 |
| fontWeight | number | string | [FontWeight](../../../arkts-components/common-definitions/enums/document.md#fontweight) | No | Yes | 

Font width of the measured text. For the number type, the value ranges from 100 to 900, at an interval of 100. A larger value indicates a heavier font weight. The default value is **400**. For the string type, only strings of the number type are supported, for example, **400**, **"bold"**, **"bolder"**, **"lighter"**, **"regular"**, and **"medium"**, which correspond to the enumerated values in **FontWeight**.

Default value: **FontWeight.Normal**

 |
| fontFamily | string | [Resource](../../../arkts-components/common-definitions/basic-types/document.md#resource) | No | Yes | 

Font family of the measured text. Default value: **'HarmonyOS Sans'**

Only the default font is supported.

 |
| letterSpacing | number | string | No | Yes | 

Letter spacing of the measured text.

Default value: **0**

 |
| textAlign10+ | number | [TextAlign](../../../arkts-components/common-definitions/enums/document.md#textalign) | No | Yes | 

Horizontal alignment mode of the measured text.

Default value: **TextAlign.Start**

Value range for the number type: \[0, 3\], with intervals of 1, corresponding to the values in the **TextAlign** enum

 |
| overflow10+ | number | [TextOverflow](../../../arkts-components/common-definitions/enums/document.md#textoverflow) | No | Yes | 

Display mode when the measured text is too long.

Default value: **1**

Value range for the number type: \[0, 3\], with intervals of 1, corresponding to the values in the **TextOverflow** enum

 |
| maxLines10+ | number | No | Yes | 

Maximum number of lines in the measured text.

Value range: \[0, INT32\_MAX\]

 |
| lineHeight10+ | number | string | [Resource](../../../arkts-components/common-definitions/basic-types/document.md#resource) | No | Yes | Line height of the measured text. |
| baselineOffset10+ | number | string | No | Yes | 

Baseline offset of the measured text.

Default value: **0**

 |
| textCase10+ | number | [TextCase](../../../arkts-components/common-definitions/enums/document.md#textcase) | No | Yes | 

Case of the measured text.

Default value: **TextCase.Normal**

Value range for the number type: \[0, 2\], with intervals of 1, corresponding to the values in the **TextCase** enum

 |
| textIndent11+ | number | string | No | Yes | Indentation of the first line. Default value: **0**. |
| wordBreak11+ | [WordBreak](../../../arkts-components/common-definitions/enums/document.md#wordbreak11) | No | Yes | 

Line break rule.

Default value: **WordBreak.BREAK\_WORD**

**NOTE**

When used with **{overflow: TextOverflow.Ellipsis}** and **maxLines**, **WordBreak.BREAK\_ALL** can insert line breaks between letters when overflow occurs and display excess content with an ellipsis (...).

 |
