# HdsSnackBar

This module provides non-modal pop-ups that can be used for displaying short notifications. A pop-up contains the icon, content, and operation areas.

**Start version**: 6.0.0(20)

#### Modules to Import

import { HdsSnackBar } from '@kit.UIDesignKit';

#### HdsSnackBar

Defines the **HdsSnackBar** class.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.UIDesign.HDSPattern.Standard

**Start version**: 6.0.0(20)

#### \[h2\]constructor

constructor(uiContext: UIContext)

Obtains an **HdsSnackBar** object.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.UIDesign.HDSPattern.Standard

**Start version**: 6.0.0(20)

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

uiContext

 | 

[UIContext](../../../arkui/arkts-api/ui/ohos-arkui-uicontext-uicontext/class-uicontext/document.md)

 | 

Yes

 | 

UI context of the app.

 |

#### \[h2\]show

show(icon: SnackBarIconOptions, message: SnackBarMessageOptions, operation: SnackBarOperationOptions, style?: SnackBarStyleOptions): void

Displays a pop-up of the **HdsSnackBar** component.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.UIDesign.HDSPattern.Standard

**Start version**: 6.0.0(20)

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

icon

 | 

[SnackBarIconOptions](#section1980950306)

 | 

Yes

 | 

Settings of the icon area of the **HdsSnackBar** component.

 |
| 

message

 | 

[SnackBarMessageOptions](#section193581154513)

 | 

Yes

 | 

Settings of the message in the content area of the **HdsSnackBar** component.

 |
| 

operation

 | 

[SnackBarOperationOptions](#section20215133710214)

 | 

Yes

 | 

Settings of the operation area of the **HdsSnackBar** component.

 |
| 

style

 | 

[SnackBarStyleOptions](#section460519981419)

 | 

No

 | 

Style settings of the **HdsSnackBar** component.

 |

#### \[h2\]dismiss

dismiss(): void

Closes the popup of the **HdsSnackBar** component.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.UIDesign.HDSPattern.Standard

**Start version**: 6.0.0(20)

#### SnackBarIconOptions

Defines icons on the left side of the **HdsSnackBar** component.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.UIDesign.HDSPattern.Standard

**Start version**: 6.0.0(20)

| 
Name

 | 

Type

 | 

Read-Only

 | 

Optional

 | 

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

icon

 | 

[ResourceStr](../../../arkui/arkts-components/common-definitions/basic-types/document.md#resourcestr)

 | 

No

 | 

Yes

 | 

Icon resource of the **HdsSnackBar** component. Both the **SymbolGlyph** and **Image** types are supported.

 |
| 

iconType

 | 

[SnackBarIconType](#section997613107164)

 | 

No

 | 

Yes

 | 

Icon type of the **HdsSnackBar** component.

The default value is **SnackBarIconType.SMALL**.

 |
| 

iconModifier

 | 

[ImageModifier](../../../arkui/arkts-components/universal-attributes/modifiers-and-custom-property/attribute-modifier/document.md#custom-modifier)

 | 

No

 | 

Yes

 | 

Modifier of an icon of the **Image** type.

 |
| 

iconSymbolModifier

 | 

[SymbolGlyphModifier](../../../arkui/arkts-components/universal-attributes/modifiers-and-custom-property/attribute-modifier/document.md#custom-modifier)

 | 

No

 | 

Yes

 | 

Modifier of an icon of the **SymbolGlyph** type.

 |

#### SnackBarMessageOptions

Defines the message displayed in the content area in the middle of the **HdsSnackBar** component.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.UIDesign.HDSPattern.Standard

**Start version**: 6.0.0(20)

| 
Name

 | 

Type

 | 

Read-Only

 | 

Optional

 | 

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

title

 | 

[ResourceStr](../../../arkui/arkts-components/common-definitions/basic-types/document.md#resourcestr)

 | 

No

 | 

Yes

 | 

Title of the message displayed in the middle of the **HdsSnackBar** component.

 |
| 

titleColor

 | 

[ColorMetrics](../../../arkui/arkts-api/ui/arkui/graphics/document.md#colormetrics12)

 | 

No

 | 

Yes

 | 

Color of the message title displayed in the middle of the **HdsSnackBar** component.

 |
| 

content

 | 

[ResourceStr](../../../arkui/arkts-components/common-definitions/basic-types/document.md#resourcestr)

 | 

No

 | 

Yes

 | 

Body of the message displayed in the middle of the **HdsSnackBar** component.

 |
| 

contentColor

 | 

[ColorMetrics](../../../arkui/arkts-api/ui/arkui/graphics/document.md#colormetrics12)

 | 

No

 | 

Yes

 | 

Color of the message body displayed in the middle of the **HdsSnackBar** component.

 |

#### SnackBarOperationOptions

Defines the operation area on the right of the **HdsSnackBar** component.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.UIDesign.HDSPattern.Standard

**Start version**: 6.0.0(20)

| 
Name

 | 

Type

 | 

Read-Only

 | 

Optional

 | 

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

operationType

 | 

[SnackBarOperationType](#section1436118313346)

 | 

No

 | 

Yes

 | 

Element style of the operation area on the right of the **HdsSnackBar** component.

 |
| 

content

 | 

[ResourceStr](../../../arkui/arkts-components/common-definitions/basic-types/document.md#resourcestr)

 | 

No

 | 

Yes

 | 

Text on the text button on the right side of the **HdsSnackBar** component.

NOTE:

This parameter does not take effect when the operation area on the right has a close icon (that is, **operationType** is set to **CLOSE\_BUTTON\_ONLY**).

 |
| 

contentColor

 | 

[ColorMetrics](../../../arkui/arkts-api/ui/arkui/graphics/document.md#colormetrics12)

 | 

No

 | 

Yes

 | 

Color of the text on the text button on the right side of the **HdsSnackBar** component.

NOTE:

This parameter does not take effect when the operation area on the right has a close icon (that is, **operationType** is set to **CLOSE\_BUTTON\_ONLY**).

 |
| 

onContentClick

 | 

[Callback](../../../arkui/arkts-components/common-definitions/basic-types/document.md#callback12)<void>

 | 

No

 | 

Yes

 | 

Tap event of the text button on the right side of the **HdsSnackBar** component.

NOTE:

This parameter does not take effect when the operation area on the right has only the close icon or text button with a right arrow (that is, **operationType** is set to **CLOSE\_BUTTON\_ONLY** or **TEXT\_WITH\_ARROW**).

 |
| 

contentAccessibilityText

 | 

[ResourceStr](../../../arkui/arkts-components/common-definitions/basic-types/document.md#resourcestr)

 | 

No

 | 

Yes

 | 

Accessibility text on the text button on the right side of the **HdsSnackBar** component. If a component does not contain text information, it will not be announced by the screen reader when selected. In this case, the screen reader user cannot know which component is selected. To solve this problem, you can set accessibility text for components without text information. When such a component is selected, the screen reader announces the specified accessibility text, informing the user which component is selected.

Default value: **""**

NOTE:

This parameter does not take effect when the operation area on the right has a close icon (that is, **operationType** is set to **CLOSE\_BUTTON\_ONLY**).

 |
| 

contentAccessibilityDescription

 | 

[ResourceStr](../../../arkui/arkts-components/common-definitions/basic-types/document.md#resourcestr)

 | 

No

 | 

Yes

 | 

Accessibility description of the text button on the right side of the **HdsSnackBar** component. You can provide comprehensive text explanations to help users understand the operation they are about to perform and its potential consequences, especially when these cannot be inferred from the component's attributes and accessibility text alone. If a component contains both text information and the accessible description, the text is announced first and then the accessible description, when the component is selected.

Default value: **"Double-tap to activate"**

NOTE:

This parameter does not take effect when the operation area on the right has a close icon (that is, **operationType** is set to **CLOSE\_BUTTON\_ONLY**).

 |
| 

onCloseButtonClick

 | 

[Callback](../../../arkui/arkts-components/common-definitions/basic-types/document.md#callback12)<void>

 | 

No

 | 

Yes

 | 

Tap event of the close icon on the right side of the **HdsSnackBar** component.

NOTE:

This parameter does not take effect when the operation area on the right has only the text button or text button with a right arrow (that is, **operationType** is set to **TEXT\_ONLY** or **TEXT\_WITH\_ARROW**).

 |
| 

closeButtonAccessibilityText

 | 

[ResourceStr](../../../arkui/arkts-components/common-definitions/basic-types/document.md#resourcestr)

 | 

No

 | 

Yes

 | 

Accessibility text on the close icon on the right side of the **HdsSnackBar** component. If a component does not contain text information, it will not be announced by the screen reader when selected. In this case, the screen reader user cannot know which component is selected. To solve this problem, you can set accessibility text for components without text information. When such a component is selected, the screen reader announces the specified accessibility text, informing the user which component is selected.

Default value: **""**

NOTE:

This parameter does not take effect when the operation area on the right has only the text button or text button with a right arrow (that is, **operationType** is set to **TEXT\_ONLY** or **TEXT\_WITH\_ARROW**).

 |
| 

closeButtonAccessibilityDescription

 | 

[ResourceStr](../../../arkui/arkts-components/common-definitions/basic-types/document.md#resourcestr)

 | 

No

 | 

Yes

 | 

Accessibility description of the close icon on the right side of the **HdsSnackBar** component. You can provide comprehensive text explanations to help users understand the operation they are about to perform and its potential consequences, especially when these cannot be inferred from the component's attributes and accessibility text alone. If a component contains both text information and the accessible description, the text is announced first and then the accessible description, when the component is selected.

Default value: **"Double-tap to activate"**

NOTE:

This parameter does not take effect when the operation area on the right has only the text button or text button with a right arrow (that is, **operationType** is set to **TEXT\_ONLY** or **TEXT\_WITH\_ARROW**).

 |
| 

arrowColor

 | 

[ColorMetrics](../../../arkui/arkts-api/ui/arkui/graphics/document.md#colormetrics12)\[\]

 | 

No

 | 

Yes

 | 

Color of the right arrow on the right side of the **HdsSnackBar** component.

NOTE:

This parameter takes effect only when the operation area on the right has only the text button with a right arrow (that is, **operationType** is set to **TEXT\_WITH\_ARROW**).

 |
| 

onArrowClick

 | 

[Callback](../../../arkui/arkts-components/common-definitions/basic-types/document.md#callback12)<void>

 | 

No

 | 

Yes

 | 

Tap event of the text button with a right arrow on the right side of the **HdsSnackBar** component.

NOTE:

This parameter takes effect only when the operation area on the right has only the text button with a right arrow (that is, **operationType** is set to **TEXT\_WITH\_ARROW**).

 |
| 

highlightBackBoardColor

 | 

[ColorMetrics](../../../arkui/arkts-api/ui/arkui/graphics/document.md#colormetrics12)

 | 

No

 | 

Yes

 | 

Background color of the highlighted text button on the right side of the **HdsSnackBar** component.

NOTE:

This parameter takes effect only when the operation area on the right has s highlighted text button with a close icon (that is, **operationType** is set to **HIGHLIGHT\_TEXT\_WITH\_CLOSE**).

 |
| 

textButtonId

 | 

string

 | 

No

 | 

Yes

 | 

ID of the text or highlighted text button of the **HdsSnackBar** component.

NOTE:

This parameter does not take effect when the operation area on the right has only the close icon or text button with a right arrow (that is, **operationType** is set to **CLOSE\_BUTTON\_ONLY** or **TEXT\_WITH\_ARROW**).

 |
| 

cancelButtonId

 | 

string

 | 

No

 | 

Yes

 | 

ID of the close icon of the **HdsSnackBar** component.

NOTE:

This parameter does not take effect when the operation area on the right has only the text button or text button with a right arrow (that is, **operationType** is set to **TEXT\_ONLY** or **TEXT\_WITH\_ARROW**).

 |
| 

arrowButtonId

 | 

string

 | 

No

 | 

Yes

 | 

ID of the text button with a right arrow in the **HdsSnackBar** component.

NOTE:

This parameter takes effect only when the operation area on the right has only the text button with a right arrow (that is, **operationType** is set to **TEXT\_WITH\_ARROW**).

 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4a/v3/28VAp2k1TFiNfsYyIts4vw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062328Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=385430578EB979375CD14742B2996C6049E34F2E48EF450E3C0B721DFB7C1657)

1\. When **operationType** is set to **TEXT\_WITH\_ARROW**, the interactive target area of **onArrowClick** is the entire **SnackBar** container. Therefore, you do not need to set **onContentClick**.

2\. The **textButtonId**, **cancelButtonId**, and **arrowButtonId** attributes can be used as focus shift target IDs.

#### SnackBarStyleOptions

Defines the style of the **HdsSnackBar** component.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.UIDesign.HDSPattern.Standard

**Start version**: 6.0.0(20)

| 
Name

 | 

Type

 | 

Read-Only

 | 

Optional

 | 

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

width

 | 

[LengthMetrics](../../../arkui/arkts-api/ui/arkui/graphics/document.md#lengthmetrics12)

 | 

No

 | 

Yes

 | 

Width of the **HdsSnackBar** component.

 |
| 

backgroundColor

 | 

[ColorMetrics](../../../arkui/arkts-api/ui/arkui/graphics/document.md#colormetrics12)

 | 

No

 | 

Yes

 | 

Background color of the **HdsSnackBar** component.

 |
| 

backgroundBlurStyle

 | 

[BlurStyle](../../../arkui/arkts-components/universal-attributes/basic-attributes/background/document.md#blurstyle9)

 | 

No

 | 

Yes

 | 

Background blur effect of the **HdsSnackBar** component.

 |
| 

duration

 | 

number

 | 

No

 | 

Yes

 | 

Duration until the **HdsSnackBar** component automatically disappears when it is configured for scheduled notification display.

The default value is **5000**.

Unit: millisecond

Value range: (-∞, +∞)

If this parameter is set to a value less than or equal to 0, the pop-up will be displayed in permanent mode.

 |
| 

keyboardDownAvoidHeight

 | 

[LengthMetrics](../../../arkui/arkts-api/ui/arkui/graphics/document.md#lengthmetrics12)

 | 

No

 | 

Yes

 | 

Avoidance height for the **HdsSnackBar** component when the on-screen keyboard is collapsed.

 |
| 

keyboardUpAvoidHeight

 | 

[LengthMetrics](../../../arkui/arkts-api/ui/arkui/graphics/document.md#lengthmetrics12)

 | 

No

 | 

Yes

 | 

Avoidance height for the **HdsSnackBar** component when the on-screen keyboard is expanded.

 |
| 

nextFocusId

 | 

string

 | 

No

 | 

Yes

 | 

ID of the next component to which the focus will shift from the **HdsSnackBar** component.

 |
| 

theme

 | 

[Theme](../../../arkui/arkts-api/ui/ohos-arkui-theme-theme/document.md#theme) | [CustomTheme](../../../arkui/arkts-api/ui/ohos-arkui-theme-theme/document.md#customtheme)

 | 

No

 | 

Yes

 | 

Theme of the **HdsSnackBar** component.

 |
| 

themeColorMode

 | 

[ThemeColorMode](../../../arkui/arkts-components/universal-attributes/visual-effects/foreground-blur/document.md#themecolormode)

 | 

No

 | 

Yes

 | 

Theme color of the **HdsSnackBar** component.

 |
| 

pressBackCallback

 | 

[Callback](../../../arkui/arkts-components/common-definitions/basic-types/document.md#callback12)<void>

 | 

No

 | 

Yes

 | 

Callback function customized for an app, to return to the previous page when an **HdsSnackBar** pop-up is displayed and a user swipes left.

 |
| 

blurStrategy

 | 

[BlurStrategy](../hdsnavigation/document.md#section1086755971212)

 | 

No

 | 

Yes

 | 

Effective strategy of the **HdsSnackBar** component.

The default value is **BlurStrategy.ADAPTIVE**.

 |

#### SnackBarOperationType

Defines the enumeration of **SnackBarOperationType**.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.UIDesign.HDSPattern.Standard

**Start version**: 6.0.0(20)

| 
Name

 | 

Value

 | 

Description

 |
| :-- | :-- | :-- |
| 

TEXT\_ONLY

 | 

0

 | 

Text button.

 |
| 

CLOSE\_BUTTON\_ONLY

 | 

1

 | 

Close icon.

 |
| 

TEXT\_WITH\_ARROW

 | 

2

 | 

Text button with a right arrow.

 |
| 

TEXT\_WITH\_CLOSE

 | 

3

 | 

Text button with a close icon.

 |
| 

HIGHLIGHT\_TEXT\_WITH\_CLOSE

 | 

4

 | 

Highlighted text button with a close icon.

 |

#### SnackBarIconType

Defines the enumeration of **SnackBarIconType**.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.UIDesign.HDSPattern.Standard

**Start version**: 6.0.0(20)

| 
Name

 | 

Value

 | 

Description

 |
| :-- | :-- | :-- |
| 

SMALL

 | 

0

 | 

Small icon.

 |
| 

NORMAL

 | 

1

 | 

Common-size icon.

 |

#### Example

The **HdsSnackBar** component provides pop-ups that support operation buttons.

import {
  HdsSnackBar,
  SnackBarIconOptions,
  SnackBarMessageOptions,
  SnackBarOperationOptions,
  SnackBarStyleOptions,
  SnackBarOperationType
} from '@kit.UIDesignKit'

@Entry
@ComponentV2
struct TestSnackBar {
  uiContext: UIContext = this.getUIContext();
  hdsSnackBar: HdsSnackBar = new HdsSnackBar(this.uiContext);
  icon: SnackBarIconOptions = {
    icon: $r('sys.symbol.checkmark\_circle')
  }
  message: SnackBarMessageOptions = {
    title: $r('sys.string.ohos\_id\_text\_location\_button\_description\_current\_position'),
    content: $r('sys.string.ohos\_id\_text\_save\_button\_description\_save')
  }
  operation: SnackBarOperationOptions = {
    operationType: SnackBarOperationType.TEXT\_WITH\_CLOSE,
    content: $r('sys.string.ohos\_id\_text\_save\_button\_description\_save\_image'),
    textButtonId: 'snackBarTextButton'
  }
  style: SnackBarStyleOptions = {
    nextFocusId: 'button',
    duration: -1
  }

  build() {
    Column() {
      Blank()
        .height(400)
      Button('SnackBar pop-up with a text button and a close icon in the right operation area, persistent')
        .onClick(() => {
          this.hdsSnackBar.show(this.icon, this.message, this.operation, this.style);
        })
        .id("button")

      Button('Follow')
        .nextFocus({
          // The forward ID must be the same as the **textButtonId** passed in **SnackBarOperationOptions**.
          forward: 'snackBarTextButton'
        })
    }
    .width('100%')
    .height('100%')
    .backgroundColor(0xF1F3F5)
  }
}

Display effect:

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a9/v3/XuNjo0MKRoe77kVpdCSXAQ/en-us_image_0000002532304107.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062328Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=600C516A097CD6933901EEB193C7356B95BC053ADF68766A3409B182864761D1)
