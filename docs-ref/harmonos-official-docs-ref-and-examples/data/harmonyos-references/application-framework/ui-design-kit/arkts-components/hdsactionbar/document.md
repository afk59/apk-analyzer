# HdsActionBar

This module enables multi-button actions. If there is a primary button, other buttons can expand and collapse from the primary button. This module includes 0 or 1 primary button, 0 or multiple non-primary buttons, and a background. You can use **CustomBuilder** to customize the primary button.

**Start version**: 6.0.0(20)

#### Modules to Import

import { HdsActionBar } from '@kit.UIDesignKit';

#### API

HdsActionBar({ primaryButton?: ActionBarButton, primaryButtonBuilder?: CustomBuilder, primaryButtonBuilderWidth?: LengthMetrics, startButtons?: Array<ActionBarButton>, endButtons?: Array<ActionBarButton>, actionBarStyle?: ActionBarStyle, isExpand?: boolean, $isExpand?: Callback<boolean>, blurStrategy?: BlurStrategy})

Key operation component of **HdsActionBar**.

**Decorator type**: @ComponentV2

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.UIDesign.HDSPattern.Standard

**Start version**: 6.0.0(20)

**Parameters:**

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Decorator Type

 | 

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

primaryButton

 | 

[ActionBarButton](#section1092811431828)

 | 

No

 | 

@Param

 | 

Primary button.

 |
| 

primaryButtonBuilder

 | 

[CustomBuilder](../../../arkui/arkts-components/common-definitions/basic-types/document.md#custombuilder8)

 | 

No

 | 

@BuilderParam

 | 

Custom primary button.

NOTE:

The priority of **primaryButtonBuilder** is higher than that of **primaryButton**.

 |
| 

primaryButtonBuilderWidth

 | 

[LengthMetrics](../../../arkui/arkts-api/ui/arkui/graphics/document.md#lengthmetrics12)

 | 

No

 | 

@Param

 | 

Width of the primary button, which is set when the primary button is a custom one.

 |
| 

startButtons

 | 

Array<[ActionBarButton](#section1092811431828)\>

 | 

No

 | 

@Param

 | 

Button array preceding the primary button of the **HdsActionBar** component.

 |
| 

endButtons

 | 

Array<[ActionBarButton](#section1092811431828)\>

 | 

No

 | 

@Param

 | 

Button array following the primary button of the **HdsActionBar** component.

 |
| 

actionBarStyle

 | 

[ActionBarStyle](#section1511110111610)

 | 

No

 | 

@Param

 | 

Style of the **HdsActionBar** component.

 |
| 

isExpand

 | 

boolean

 | 

No

 | 

@Param

 | 

Indicates whether the buttons of the **HdsActionBar** component are expanded or collapsed. The value **true** indicates expanded and the value **false** indicates collapsed.

The default value is **false**.

 |
| 

$isExpand

 | 

[Callback](../../../arkui/arkts-components/common-definitions/basic-types/document.md#callback12)<boolean>

 | 

No

 | 

@Event

 | 

Callback that indicates whether the **HdsActionBar** component is expanded.

NOTE:

The value **true** indicates that the **HdsActionBar** component is expanded, and the value **false** indicates that the **HdsActionBar** component is collapsed.

 |
| 

blurStrategy

 | 

[BlurStrategy](../hdsnavigation/document.md#section1086755971212)

 | 

No

 | 

@Param

 | 

Effective strategy of the **HdsActionBar** component.

The default value is **BlurStrategy.ADAPTIVE**.

 |

#### ActionBarButton

Defines buttons for the **HdsActionBar** component.

**Decorator type**: @ObservedV2

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.UIDesign.HDSPattern.Standard

**Start version**: 6.0.0(20)

#### \[h2\]Attributes

Defines attributes for **ActionBarButton**.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.UIDesign.HDSPattern.Standard

**Start version**: 6.0.0(20)

**Parameters:**

| 
Name

 | 

Type

 | 

Read-Only

 | 

Optional

 | 

Decorator Type

 | 

Description

 |
| :-- | :-- | :-- | :-- | :-- | :-- |
| 

width

 | 

[LengthMetrics](../../../arkui/arkts-api/ui/arkui/graphics/document.md#lengthmetrics12)

 | 

No

 | 

Yes

 | 

@Trace

 | 

Width of the round button.

NOTE:

The unit can be px, vp, fp, or lpx. The unit percent is not supported.

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

@Trace

 | 

Background color of the round button.

 |
| 

shadowStyle

 | 

[ShadowOptions](../../../arkui/arkts-components/universal-attributes/visual-effects/image-effect/document.md#shadowoptions) | [ShadowStyle](../../../arkui/arkts-components/universal-attributes/visual-effects/image-effect/document.md#shadowstyle10)

 | 

No

 | 

Yes

 | 

@Trace

 | 

Shadow of the round button.

The default value is **ShadowStyle.OUTER\_DEFAULT\_LG**.

 |
| 

enabled

 | 

boolean

 | 

No

 | 

Yes

 | 

@Trace

 | 

Indicates whether the round button is enabled.

The default value is **true**.

NOTE:

The value **true** indicates that the round button is enabled, and the value **false** indicates that the round button is disabled.

 |
| 

baseIcon

 | 

[ResourceStr](../../../arkui/arkts-components/common-definitions/basic-types/document.md#resourcestr)

 | 

No

 | 

Yes

 | 

@Trace

 | 

Icon of the primary button in the initial state.

NOTE:

For a non-primary button, this parameter also takes effect, specifying the button icon.

 |
| 

altIcon

 | 

[ResourceStr](../../../arkui/arkts-components/common-definitions/basic-types/document.md#resourcestr)

 | 

No

 | 

Yes

 | 

@Trace

 | 

Icon of the primary button after the expansion animation.

NOTE:

For a non-primary button, this parameter does not take effect.

 |
| 

iconFillColor

 | 

[ColorMetrics](../../../arkui/arkts-api/ui/arkui/graphics/document.md#colormetrics12)

 | 

No

 | 

Yes

 | 

@Trace

 | 

Icon color of the round button.

 |
| 

iconSize

 | 

[LengthMetrics](../../../arkui/arkts-api/ui/arkui/graphics/document.md#lengthmetrics12)

 | 

No

 | 

Yes

 | 

@Trace

 | 

Icon size of the round button.

 |
| 

baseIconSymbolGlyphModifier

 | 

[SymbolGlyphModifier](../../../arkui/arkts-components/universal-attributes/modifiers-and-custom-property/attribute-modifier/document.md#custom-modifier)

 | 

No

 | 

Yes

 | 

@Trace

 | 

Modifier style of the round button icon before the expansion animation.

 |
| 

altIconSymbolGlyphModifier

 | 

[SymbolGlyphModifier](../../../arkui/arkts-components/universal-attributes/modifiers-and-custom-property/attribute-modifier/document.md#custom-modifier)

 | 

No

 | 

Yes

 | 

@Trace

 | 

Modifier style of the round button icon after the expansion animation.

 |
| 

accessibilityText

 | 

[ResourceStr](../../../arkui/arkts-components/common-definitions/basic-types/document.md#resourcestr)

 | 

No

 | 

Yes

 | 

@Trace

 | 

Accessibility text of the round button. If a component does not contain text information, it will not be announced by the screen reader when selected. In this case, the screen reader user cannot know which component is selected. To solve this problem, you can set accessibility text for components without text information. When such a component is selected, the screen reader announces the specified accessibility text, informing the user which component is selected.

Default value: **""**

 |
| 

accessibilityDescription

 | 

[ResourceStr](../../../arkui/arkts-components/common-definitions/basic-types/document.md#resourcestr)

 | 

No

 | 

Yes

 | 

@Trace

 | 

Accessibility description of the round button. You can provide comprehensive text explanations to help users understand the operation they are about to perform and its potential consequences, especially when these cannot be inferred from the component's attributes and accessibility text alone. If a component contains both text information and the accessible description, the text is announced first and then the accessible description, when the component is selected.

Default value: **"Double-tap to activate"**

 |
| 

accessibilityLevel

 | 

string

 | 

No

 | 

Yes

 | 

@Trace

 | 

Accessibility level of the round button, which is used to set whether this component can be recognized by accessibility services.

The options are as follows:

**"auto"**: This option is treated as "yes" by the system for this component.

**"yes"**: The component can be recognized by accessibility services.

**"no"**: The component cannot be recognized by accessibility services.

**"no-hide-descendants"**: Neither the component nor its child components can be recognized by accessibility services.

The default value is **"auto"**.

 |
| 

id

 | 

string

 | 

No

 | 

Yes

 | 

@Trace

 | 

ID of the round button, which is used for [openPopup](../../../arkui/arkts-api/ui/ohos-arkui-uicontext-uicontext/class-promptaction/document.md#openpopup18) binding.

 |
| 

hoverTips

 | 

[ResourceStr](../../../arkui/arkts-components/common-definitions/basic-types/document.md#resourcestr)

 | 

No

 | 

Yes

 | 

@Trace

 | 

Floating message of the round button.

 |
| 

buttonModifier

 | 

[ButtonModifier](../../../arkui/arkts-components/universal-attributes/modifiers-and-custom-property/attribute-modifier/document.md#custom-modifier)

 | 

No

 | 

Yes

 | 

@Trace

 | 

Modifier of the round button.

 |

#### \[h2\]constructor

constructor(options: ActionBarButtonOptions)

Constructor for **ActionBarButton**.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.UIDesign.HDSPattern.Standard

**Start version**: 6.0.0(20)

**Parameters:**

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

options

 | 

[ActionBarButtonOptions](#section82531145191119)

 | 

Yes

 | 

Button parameters of the **HdsActionBar** component.

 |

#### ActionBarButtonOptions

Defines the constructor parameters of the **ActionBarButton** component.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.UIDesign.HDSPattern.Standard

**Start version**: 6.0.0(20)

**Parameters:**

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

Width of the round button.

NOTE:

The unit can be px, vp, fp, or lpx. The unit percent is not supported.

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

Background color of the round button.

 |
| 

shadowStyle

 | 

[ShadowOptions](../../../arkui/arkts-components/universal-attributes/visual-effects/image-effect/document.md#shadowoptions) | [ShadowStyle](../../../arkui/arkts-components/universal-attributes/visual-effects/image-effect/document.md#shadowstyle10)

 | 

No

 | 

Yes

 | 

Shadow of the round button.

The default value is **ShadowStyle.OUTER\_DEFAULT\_LG**.

 |
| 

enabled

 | 

boolean

 | 

No

 | 

Yes

 | 

Indicates whether the round button is enabled.

The default value is **true**.

NOTE:

The value **true** indicates that the round button is enabled, and the value **false** indicates that the round button is disabled.

 |
| 

onClick

 | 

[Callback](../../../arkui/arkts-components/common-definitions/basic-types/document.md#callback12)<void>

 | 

No

 | 

Yes

 | 

Tap event of the round button.

 |
| 

baseIcon

 | 

[ResourceStr](../../../arkui/arkts-components/common-definitions/basic-types/document.md#resourcestr)

 | 

No

 | 

Yes

 | 

Icon of the primary button in the initial state.

NOTE:

For a non-primary button, this parameter also takes effect, specifying the button icon.

 |
| 

altIcon

 | 

[ResourceStr](../../../arkui/arkts-components/common-definitions/basic-types/document.md#resourcestr)

 | 

No

 | 

Yes

 | 

Icon of the primary button after the expansion animation.

NOTE:

For a non-primary button, this parameter does not take effect.

 |
| 

iconFillColor

 | 

[ColorMetrics](../../../arkui/arkts-api/ui/arkui/graphics/document.md#colormetrics12)

 | 

No

 | 

Yes

 | 

Icon color of the round button.

 |
| 

iconSize

 | 

[LengthMetrics](../../../arkui/arkts-api/ui/arkui/graphics/document.md#lengthmetrics12)

 | 

No

 | 

Yes

 | 

Icon size of the round button.

 |
| 

baseIconSymbolGlyphModifier

 | 

[SymbolGlyphModifier](../../../arkui/arkts-components/universal-attributes/modifiers-and-custom-property/attribute-modifier/document.md#custom-modifier)

 | 

No

 | 

Yes

 | 

Modifier style of the round button icon before the expansion animation.

 |
| 

altIconSymbolGlyphModifier

 | 

[SymbolGlyphModifier](../../../arkui/arkts-components/universal-attributes/modifiers-and-custom-property/attribute-modifier/document.md#custom-modifier)

 | 

No

 | 

Yes

 | 

Modifier style of the round button icon after the expansion animation.

 |
| 

accessibilityText

 | 

[ResourceStr](../../../arkui/arkts-components/common-definitions/basic-types/document.md#resourcestr)

 | 

No

 | 

Yes

 | 

Accessibility text of the round button. If a component does not contain text information, it will not be announced by the screen reader when selected. In this case, the screen reader user cannot know which component is selected. To solve this problem, you can set accessibility text for components without text information. When such a component is selected, the screen reader announces the specified accessibility text, informing the user which component is selected.

Default value: **""**

 |
| 

accessibilityDescription

 | 

[ResourceStr](../../../arkui/arkts-components/common-definitions/basic-types/document.md#resourcestr)

 | 

No

 | 

Yes

 | 

Accessibility description of the round button. You can provide comprehensive text explanations to help users understand the operation they are about to perform and its potential consequences, especially when these cannot be inferred from the component's attributes and accessibility text alone. If a component contains both text information and the accessible description, the text is announced first and then the accessible description, when the component is selected.

Default value: **"Double-tap to activate"**

 |
| 

accessibilityLevel

 | 

string

 | 

No

 | 

Yes

 | 

Accessibility level of the round button, which is used to set whether this component can be recognized by accessibility services.

The options are as follows:

**"auto"**: This option is treated as "yes" by the system for this component.

**"yes"**: The component can be recognized by accessibility services.

**"no"**: The component cannot be recognized by accessibility services.

**"no-hide-descendants"**: Neither the component nor its child components can be recognized by accessibility services.

The default value is **"auto"**.

 |
| 

id

 | 

string

 | 

No

 | 

Yes

 | 

ID of the round button, which is used for [openPopup](../../../arkui/arkts-api/ui/ohos-arkui-uicontext-uicontext/class-promptaction/document.md#openpopup18) binding.

 |
| 

hoverTips

 | 

[ResourceStr](../../../arkui/arkts-components/common-definitions/basic-types/document.md#resourcestr)

 | 

No

 | 

Yes

 | 

Floating message of the round button.

 |
| 

buttonModifier

 | 

[ButtonModifier](../../../arkui/arkts-components/universal-attributes/modifiers-and-custom-property/attribute-modifier/document.md#custom-modifier)

 | 

No

 | 

Yes

 | 

Modifier of the round button.

 |

#### ActionBarStyle

Defines the style of the **HdsActionBar** component.

**Decorator type**: @ObservedV2

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.UIDesign.HDSPattern.Standard

**Start version**: 6.0.0(20)

#### \[h2\]Attributes

Defines attributes for **ActionBarStyle**.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.UIDesign.HDSPattern.Standard

**Start version**: 6.0.0(20)

**Parameters:**

| 
Name

 | 

Type

 | 

Read-Only

 | 

Optional

 | 

Decorator Type

 | 

Description

 |
| :-- | :-- | :-- | :-- | :-- | :-- |
| 

height

 | 

[LengthMetrics](../../../arkui/arkts-api/ui/arkui/graphics/document.md#lengthmetrics12)

 | 

No

 | 

Yes

 | 

@Trace

 | 

Background height of the **HdsActionBar** component.

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

@Trace

 | 

Background blur effect of the **HdsActionBar** component.

The default value is **BlurStyle.COMPONENT\_REGULAR**.

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

@Trace

 | 

Background color of the **HdsActionBar** component.

 |
| 

innerSpace

 | 

[LengthMetrics](../../../arkui/arkts-api/ui/arkui/graphics/document.md#lengthmetrics12)

 | 

No

 | 

Yes

 | 

@Trace

 | 

Distance between the primary button and the start button of the **HdsActionBar** component in the main axis direction, or distance between the primary button and the end button of the **HdsActionBar** component in the main axis direction.

 |
| 

startSpace

 | 

[LengthMetrics](../../../arkui/arkts-api/ui/arkui/graphics/document.md#lengthmetrics12)

 | 

No

 | 

Yes

 | 

@Trace

 | 

Distance between the start button of the **HdsActionBar** component and the left border of the background in the main axis direction.

 |
| 

endSpace

 | 

[LengthMetrics](../../../arkui/arkts-api/ui/arkui/graphics/document.md#lengthmetrics12)

 | 

No

 | 

Yes

 | 

@Trace

 | 

Distance between the end button of the **HdsActionBar** component and the right border of the background in the main axis direction.

 |
| 

enabled

 | 

boolean

 | 

No

 | 

Yes

 | 

@Trace

 | 

Indicates whether to enable the **HdsActionBar** component.

The default value is **true**.

NOTE:

If **enabled** is set to **false**, the background and all buttons are disabled. If **enabled** is set to **true**, each button can be enabled or disabled individually.

 |
| 

isHorizontal

 | 

boolean

 | 

No

 | 

Yes

 | 

@Trace

 | 

Indicates whether the **HdsActionBar** component is horizontally or vertically arranged. The options are **true** (horizontal) and **false** (vertical).

The default value is **true**.

 |
| 

isPrimaryIconChanged

 | 

boolean

 | 

No

 | 

Yes

 | 

@Trace

 | 

Indicates whether to change the primary button after the animation. The options are **true** (change the icon to **altIcon**) and **false** (keep the **baseIcon**).

The default value is **false**.

 |

#### \[h2\]constructor

constructor(options: ActionBarStyleOptions)

Constructor for **ActionBarStyle**.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.UIDesign.HDSPattern.Standard

**Start version**: 6.0.0(20)

**Parameters:**

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

options

 | 

[ActionBarStyleOptions](#section13821143712333)

 | 

Yes

 | 

Style parameters of the **HdsActionBar** component.

 |

#### ActionBarStyleOptions

Defines the constructor parameters of the **ActionBarStyle** component.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.UIDesign.HDSPattern.Standard

**Start version**: 6.0.0(20)

**Parameters:**

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

height

 | 

[LengthMetrics](../../../arkui/arkts-api/ui/arkui/graphics/document.md#lengthmetrics12)

 | 

No

 | 

Yes

 | 

Background height of the **HdsActionBar** component.

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

Background blur effect of the **HdsActionBar** component.

The default value is **BlurStyle.COMPONENT\_REGULAR**.

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

Background color of the **HdsActionBar** component.

 |
| 

innerSpace

 | 

[LengthMetrics](../../../arkui/arkts-api/ui/arkui/graphics/document.md#lengthmetrics12)

 | 

No

 | 

Yes

 | 

Distance between the primary button and the start button of the **HdsActionBar** component in the main axis direction, or distance between the primary button and the end button of the **HdsActionBar** component in the main axis direction.

 |
| 

startSpace

 | 

[LengthMetrics](../../../arkui/arkts-api/ui/arkui/graphics/document.md#lengthmetrics12)

 | 

No

 | 

Yes

 | 

Distance between the start button of the **HdsActionBar** component and the left border of the background in the main axis direction.

 |
| 

endSpace

 | 

[LengthMetrics](../../../arkui/arkts-api/ui/arkui/graphics/document.md#lengthmetrics12)

 | 

No

 | 

Yes

 | 

Distance between the end button of the **HdsActionBar** component and the right border of the background in the main axis direction.

 |
| 

enabled

 | 

boolean

 | 

No

 | 

Yes

 | 

Indicates whether to enable the **HdsActionBar** component.

The default value is **true**.

NOTE:

If **enabled** is set to **false**, the background and all buttons are disabled. If **enabled** is set to **true**, each button can be enabled or disabled individually.

 |
| 

isHorizontal

 | 

boolean

 | 

No

 | 

Yes

 | 

Indicates whether the **HdsActionBar** component is horizontally or vertically arranged. The options are **true** (horizontal) and **false** (vertical).

The default value is **true**.

 |
| 

isPrimaryIconChanged

 | 

boolean

 | 

No

 | 

Yes

 | 

Indicates whether to change the primary button after the animation. The options are **true** (change the icon to **altIcon**) and **false** (keep the **baseIcon**).

The default value is **false**.

 |

#### Example

The following is a multi-button example of the **HdsActionBar** component:

import { HdsActionBar, ActionBarButton, ActionBarStyle } from '@kit.UIDesignKit'

@Entry
@ComponentV2
struct TestActionBar {
  @Local isExpand: boolean = true;

  @Local isPrimaryIconChanged: boolean = false;

  @Local primaryHoverTips: ResourceStr = 'Start';

  build() {
    Column() {
      HdsActionBar({
        startButtons: \[new ActionBarButton({
          baseIcon: $r('sys.symbol.stopwatch\_fill')
        })\],
        endButtons: \[new ActionBarButton({
          baseIcon: $r('sys.symbol.mic\_fill')
        })\],
        primaryButton: new ActionBarButton({
          baseIcon: $r('sys.symbol.plus'),
          altIcon: $r('sys.symbol.play\_fill'),
          onClick: () => {
            this.isExpand = !this.isExpand;
            this.isPrimaryIconChanged = !this.isPrimaryIconChanged;
            if (this.isPrimaryIconChanged) {
              this.primaryHoverTips = 'Pause';
            } else {
              this.primaryHoverTips = 'Start';
            }
          },
          hoverTips: this.primaryHoverTips
        }),
        actionBarStyle: new ActionBarStyle({
          isPrimaryIconChanged: this.isPrimaryIconChanged
        }),
        isExpand: this.isExpand!!
      })
    }
    .width('100%')
    .height('100%')
    .backgroundColor(0xF1F3F5)
    .justifyContent(FlexAlign.Center)
    .alignItems(HorizontalAlign.Center)
  }
}

Display effect:

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0e/v3/Cseun10tStm27hzoPdZScQ/en-us_image_0000002532144121.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062328Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4065ED693630AB169D0F4D49784970B0E190DF869FEB0803E7C8F9BB665DE027)
