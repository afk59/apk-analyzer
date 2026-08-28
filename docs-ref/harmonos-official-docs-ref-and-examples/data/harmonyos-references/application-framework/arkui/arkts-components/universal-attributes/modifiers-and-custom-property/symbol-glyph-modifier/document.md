# Symbol Glyph Modifier

**SymbolGlyphModifier** is used to dynamically set the attributes and styles of the **SymbolGlyph** component. The **if/else** statements can be used. [SymbolGlyph](../../../text-and-input/symbolglyph/document.md) is a component used to display symbol glyphs.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fd/v3/1Et5jYY-QC6Buw5u1eC_Bw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062236Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E17FE9C38C32901CEEE11222380BCB6335FB5B32B65B62B15576E4757F3ED52A)

The initial APIs of this module are supported since API version 12. Updates will be marked with a superscript to indicate their earliest API version.

#### SymbolGlyphModifier

Defines the **SymbolGlyphModifier**.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

#### \[h2\]constructor

constructor(src?: Resource)

A constructor used to create a **SymbolGlyphModifier** object.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| src | [Resource](../../../common-definitions/basic-types/document.md#resource) | No | Resource information. |

#### \[h2\]applyNormalAttribute

applyNormalAttribute?(instance: SymbolGlyphAttribute): void

Applies the style of a component in the normal state.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| instance | [SymbolGlyphAttribute](../../../text-and-input/symbolglyph/document.md) | Yes | Dynamic attribute setting for the SymbolGlyph component. |

#### Example

This example demonstrates how to use [SymbolGlyphModifier](#symbolglyphmodifier) and the [cancelButton](../../../text-and-input/textinput/document.md#cancelbutton18) attribute of the **TextInput** component to customize the style of the symbol-type cancel button on the right side of the text box.

import { SymbolGlyphModifier } from '@kit.ArkUI';

// xxx.ets
@Entry
@Component
struct Index {
  @State text: string = '';
  symbolModifier: SymbolGlyphModifier =
    new SymbolGlyphModifier($r('sys.symbol.trash')).fontColor(\[Color.Red\]).fontSize(16).fontWeight(FontWeight.Regular);

  build() {
    Column() {
      TextInput({ text: this.text, placeholder: 'input your word...' })
        .height(50)
        .cancelButton({
          style: CancelButtonStyle.CONSTANT,
          icon: this.symbolModifier // The symbol type is supported since API version 18.
        })
    }.margin(10)
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8f/v3/FH4fqDFgSMqp4a4gDXc2fQ/en-us_image_0000002568685203.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062236Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C0CF24CDAFAFE8C249D93029553F0D670C3F93B815F085596AB2A97CDBEECD0E)
