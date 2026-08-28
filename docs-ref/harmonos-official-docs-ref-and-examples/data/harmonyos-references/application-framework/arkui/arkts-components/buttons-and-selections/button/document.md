# Button

The **Button** component can be used to create different types of buttons.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f7/v3/aHVXN3pvSwO3cLHHoHAb9Q/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062240Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B4DE6F4BBE8F1184AAE3F12B8CFCEE7A30B89DE98E1FC4DEA1325F3773AC85C8)

This component is supported since API version 7. Updates will be marked with a superscript to indicate their earliest API version.

#### Child Components

This component can contain only one child component.

#### APIs

#### \[h2\]Button

Button(options: ButtonOptions)

Creates a button that can contain a single child component.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| options | [ButtonOptions](#buttonoptions) | Yes | Button settings. |

#### \[h2\]Button

Button(label: ResourceStr, options?: ButtonOptions)

Creates a button based on text content. In this case, the component cannot contain child components.

By default, the text content is displayed in a one line.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| label | [ResourceStr](../../common-definitions/basic-types/document.md#resourcestr) | Yes | 
Button text.

Note: If the text is longer than the width of the button, it is truncated.

 |
| options | [ButtonOptions](#buttonoptions) | No | Button settings. |

#### \[h2\]Button

Button()

Creates an empty button.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

#### ButtonOptions

Describes the button style.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| type | [ButtonType](#buttontype) | No | Yes | 
Button display style.

Default value: **ButtonType.ROUNDED\_RECTANGLE**.

API version 18 and later: The default value is **ButtonType.ROUNDED\_RECTANGLE**. Versions earlier than API version 18: The default value is **ButtonType.Capsule**.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| stateEffect | boolean | No | Yes | 

Whether to enable the pressed state effect when the button is clicked.

**true**: Enable the pressed state effect. **false**: Disable the pressed state effect.

Default value: **true**.

**NOTE**

When the pressed state effect is enabled and a custom pressed state style is configured, the resulting color displayed after pressing is a composite blend of the original background color and the newly defined pressed state color.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| buttonStyle11+ | [ButtonStyleMode](#buttonstylemode11) | No | Yes | 

Style and importance of the button. The system automatically adjusts the button background color and text color based on the enumerated value. You can also use the [backgroundColor](../../universal-attributes/basic-attributes/background/document.md#backgroundcolor), [fontColor](#fontcolor), and [role](#role12) APIs to set the background color and text color. The actual displayed effect will be determined by the last setting.

Default value: **ButtonStyleMode.EMPHASIZED**

**NOTE**

The button primacy is as follows, from high to low: emphasized button, normal button, text button.

**Widget capability**: This API can be used in ArkTS widgets since API version 11.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| controlSize11+ | [ControlSize](#controlsize11) | No | Yes | 

Button size.

Default value: **ControlSize.NORMAL**

**Widget capability**: This API can be used in ArkTS widgets since API version 11.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| role12+ | [ButtonRole](#buttonrole12) | No | Yes | 

Role of the button. The system automatically adjusts the button background color and text color based on the enumerated value. You can also use the [backgroundColor](../../universal-attributes/basic-attributes/background/document.md#backgroundcolor), [fontColor](#fontcolor), and [buttonStyle](#buttonstyle11) APIs to set the background color and text color. The actual displayed effect will be determined by the last setting.

Default value: **ButtonRole.NORMAL**

**Widget capability**: This API can be used in ArkTS widgets since API version 12.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |

#### Attributes

In addition to the [universal attributes](../../universal-attributes/document.md), the following attributes are supported.

#### \[h2\]type

type(value: ButtonType)

Sets the button type.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [ButtonType](#buttontype) | Yes | 
Button type.

API version 18 and later: The default value is **ButtonType.ROUNDED\_RECTANGLE**.

 |

#### \[h2\]fontSize

fontSize(value: Length)

Sets the font size for the button.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [Length](../../common-definitions/basic-types/document.md#length) | Yes | 
Font size of the button.

Default value:

**$r('sys.float.Body\_L')** when **controlSize** is set to **ControlSize.NORMAL**

**$r('sys.float.Body\_S')** when **controlSize** is set to **ControlSize.SMALL**

Note: For the string type, percentage values are not supported.

 |

#### \[h2\]fontColor

fontColor(value: ResourceColor)

Sets the font color for the button.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [ResourceColor](../../common-definitions/basic-types/document.md#resourcecolor) | Yes | 
Font color of the button.

Default value: **$r('sys.color.font\_on\_primary')**, which means white

 |

#### \[h2\]fontWeight

fontWeight(value: number | FontWeight | string)

Sets the font weight for the button.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | number | [FontWeight](../../common-definitions/enums/document.md#fontweight) | string | Yes | 
Font weight of the button. For the number type, the value ranges from 100 to 900, at an interval of 100. A larger value indicates a thicker font.

Default value: **500**

For the string type, only strings that represent a number, for example, **'400'**, and the following enumerated values of **FontWeight** are supported: **'bold'**, **'bolder'**, **'lighter'**, **'regular'**, and **'medium'**.

If the value is abnormal or invalid, the font weight defaults to 400.

 |

#### \[h2\]fontStyle8+

fontStyle(value: FontStyle)

Sets the font style for the button.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [FontStyle](../../common-definitions/enums/document.md#fontstyle) | Yes | 
Font style of the button.

Default value: **FontStyle.Normal**.

 |

#### \[h2\]stateEffect

stateEffect(value: boolean)

Specifies whether to enable the pressed state effect when the button is clicked.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | boolean | Yes | 
Whether to enable the pressed state effect when the button is clicked.

**true**: Enable the pressed state effect. **false**: Disable the pressed state effect.

Default value: **true**.

 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/01/v3/Q5p3XOQjSoyxMjXDqDxq-g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062240Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=EB07137EC8CF2D831B98EAB44BB9964B5CC3A0A2100723CC15E844A0221D13FB)

When the polymorphic style is used to set the pressed state, set **stateEffect** to **false** to avoid conflicts between the built-in and custom pressed state effects.

#### \[h2\]fontFamily8+

fontFamily(value: string | Resource)

Sets the font family.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | string | [Resource](../../common-definitions/basic-types/document.md#resource) | Yes | Font family. The 'HarmonyOS Sans' font and [registered custom fonts](../../../arkts-api/ui/ohos-font-custom-font-registration/document.md) are supported. |

#### \[h2\]labelStyle10+

labelStyle(value: LabelStyle)

Sets the label style for the button.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [LabelStyle](#labelstyle10) | Yes | Label style of the button. |

#### \[h2\]buttonStyle11+

buttonStyle(value: ButtonStyleMode)

Sets the style and primacy for the button. The system automatically adjusts the button background color and text color based on the enumerated value. You can also use the [backgroundColor](../../universal-attributes/basic-attributes/background/document.md#backgroundcolor), [fontColor](#fontcolor), and [role](#role12) APIs to set the background color and text color. The actual displayed effect will be determined by the last setting.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8f/v3/VAtTjcrPSn2c6-2PAvH57A/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062240Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=34400099C6AFB04EBFF4CA836F60BCA5CB10D6FB3659450FB0EF3C69842E5425)

This API can be called within [attributeModifier](../../universal-attributes/modifiers-and-custom-property/attribute-modifier/document.md#attributemodifier) since API version 12.

**Widget capability**: This API can be used in ArkTS widgets since API version 11.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [ButtonStyleMode](#buttonstylemode11) | Yes | 
Style and primacy of the button

Default value: **ButtonStyleMode.EMPHASIZED**

 |

#### \[h2\]controlSize11+

controlSize(value: ControlSize)

Sets the size for the button.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e/v3/U5EZbHbRQdq_YQ_I-Lt_aw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062240Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=095355846178EF0BAF6BEE7CFDB6751252BA5DCD5BAE80CA25FFFDC6BE845BDA)

This API can be called within [attributeModifier](../../universal-attributes/modifiers-and-custom-property/attribute-modifier/document.md#attributemodifier) since API version 12.

**Widget capability**: This API can be used in ArkTS widgets since API version 11.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [ControlSize](#controlsize11) | Yes | 
Size of the button.

Default value: **ControlSize.NORMAL**

 |

#### \[h2\]role12+

role(value: ButtonRole)

Sets the role of the button. The system automatically adjusts the button background color and text color based on the enumerated value. You can also use the [backgroundColor](../../universal-attributes/basic-attributes/background/document.md#backgroundcolor), [fontColor](#fontcolor), and [buttonStyle](#buttonstyle11) APIs to set the background color and text color. The actual displayed effect will be determined by the last setting.

**Widget capability**: This API can be used in ArkTS widgets since API version 12.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [ButtonRole](#buttonrole12) | Yes | 
Role of the button.

Default value: **ButtonRole.NORMAL**

 |

#### \[h2\]contentModifier12+

contentModifier(modifier: ContentModifier<ButtonConfiguration>)

Creates a content modifier.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| modifier | [ContentModifier](../../universal-attributes/modifiers-and-custom-property/content-modifier/document.md#contentmodifiert)[<ButtonConfiguration>](#buttonconfiguration12) | Yes | 
Content modifier to apply to the button.

**modifier**: content modifier. You need a custom class to implement the **ContentModifier** API.

 |

#### \[h2\]minFontScale18+

minFontScale(scale: number | Resource)

Sets the minimum font scale factor for text.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| scale | number | [Resource](../../common-definitions/basic-types/document.md#resource) | Yes | 
Minimum font scale factor for text.

Value range: \[0, 1\]

**NOTE**

A value less than 0 is handled as **0**. A value greater than 1 is handled as **1**. Abnormal values are ineffective by default.

 |

#### \[h2\]maxFontScale18+

maxFontScale(scale: number | Resource)

Sets the maximum font scale factor for text.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| scale | number | [Resource](../../common-definitions/basic-types/document.md#resource) | Yes | 
Maximum font scale factor for text.

Value range: \[1, +∞)

**NOTE**

A value less than 1 is handled as **1**. Abnormal values are ineffective by default.

If this parameter is not configured, the maximum scale for a circular button is 1x, while the maximum scale for capsule-type buttons, standard buttons, and rounded rectangle buttons defaults to the system-defined value.

 |

#### ButtonType

Enumerates the button types.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Value | Description |
| :-- | :-- | :-- |
| Normal | 0 | 
Normal button, with no rounded corners by default.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| Capsule | 1 | 

Capsule-type button (the round corner is half of the height by default).

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| Circle | 2 | 

Circular button.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| ROUNDED\_RECTANGLE15+ | 8 | 

Rounded rectangle button (default value: when **controlSize** is **NORMAL**, the corner radius is 20 vp; when controlSize is **SMALL**, the corner radius is 14 vp).

**Widget capability**: This API can be used in ArkTS widgets since API version 15.

**Atomic service API**: This API can be used in atomic services since API version 15.

 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e4/v3/NC5Qt25zSw6NktsxyKqcuw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062240Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=EA1A9EC7EC0FD9F564A6D7A3AC72EE2EBF86B29452D7B43D38D7B72CDAB551A0)

-   The corner radius of the rounded rectangle button is set using the universal attribute [borderRadius](../../universal-attributes/layout-and-borders/border-styling/document.md#borderradius).
-   For a button of the **Capsule** type, the **borderRadius** settings do not take effect, and the radius of its rounded corner is always half of the button height or width, whichever is smaller.
-   For a button of the **Circle** type: (1) If both its width and height are set, **borderRadius** does not take effect, and the button radius is half of the width or height (whichever is smaller). (2) If either its width or height is set, **borderRadius** does not take effect, and the button radius is half of the set width or height. (3) If neither its width nor height is set, the button radius is as specified by **borderRadius**; if **borderRadius** is set to a negative value, the value **0** will be used.
-   The button text is set using [fontSize](#fontsize), [fontColor](#fontcolor), [fontStyle](#fontstyle8), [fontFamily](#fontfamily8), and [fontWeight](#fontweight).
-   Before setting the [gradient color](../../universal-attributes/visual-effects/color-gradient/document.md), you need to set [backgroundColor](../../universal-attributes/basic-attributes/background/document.md#backgroundcolor) to transparent.
-   When **borderRadius** is not set, the corner radius of the rounded rectangle button remains at the default value. In this case, the corner radius does not change with the button height and is subject to the **controlSize** property. When **controlSize** is **NORMAL**, the corner radius is 20 vp; when **controlSize** is **SMALL**, the corner radius is 14 vp.
-   When [border](../../universal-attributes/layout-and-borders/border-styling/document.md#border) is set for the button, a default [borderRadius](../../universal-attributes/layout-and-borders/border-styling/document.md#borderradius) value is automatically applied. When both **border** and **borderRadius** attributes are used, **borderRadius** must be specified after **border** to prevent the border radius from being overridden by the default radius value in the border style.

#### LabelStyle10+

Label text and font style of the button.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| overflow | [TextOverflow](../../common-definitions/enums/document.md#textoverflow) | No | Yes | 
Display mode when the label text is too long. Text is clipped at the transition between words. To clip text in the middle of a word, add zero-width spaces between characters.

Default value: \*\*TextOverflow.Ellipsis

 |
| maxLines | number | No | Yes | 

Maximum number of lines in the label text. If this attribute is specified, the text will not exceed the specified number of lines. If there is extra text, you can use **overflow** to specify how it is displayed.

Default value: **1**

**NOTE**

If this parameter is set to a value less than or equal to 0, the default value is used.

 |
| minFontSize | number | [ResourceStr](../../common-definitions/basic-types/document.md#resourcestr) | No | Yes | 

Minimum font size of the label text. For the setting to take effect, this attribute must be used together with **maxFontSize**, **maxLines**, or layout constraint settings.

**NOTE**

If the value of **minFontSize** is less than or equal to 0, the adaptive font size does not take effect.

 |
| maxFontSize | number | [ResourceStr](../../common-definitions/basic-types/document.md#resourcestr) | No | Yes | Maximum font size of the label text. For the setting to take effect, this attribute must be used together with **minFontSize**, **maxLines**, or layout constraint settings. |
| heightAdaptivePolicy | [TextHeightAdaptivePolicy](../../common-definitions/enums/document.md#textheightadaptivepolicy10) | No | Yes | 

How the adaptive height is determined for the label text.

Default value: **TextHeightAdaptivePolicy.MAX\_LINES\_FIRST**.

 |
| font | [Font](../../common-definitions/basic-types/document.md#font) | No | Yes | 

Font of the label text.

Default value:

{

size:'16.0fp',

weight:FontWeight.Medium,

style:FontStyle.Normal,

family:'HarmonyOS Sans'

}

 |

#### ButtonStyleMode11+

Enumerates the button importance levels.

**Widget capability**: This API can be used in ArkTS widgets since API version 11.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Value | Description |
| :-- | :-- | :-- |
| NORMAL | 0 | Normal button (used to direct the user to a common task). |
| EMPHASIZED | 1 | Emphasized button (used to direct the user to the most important task). |
| TEXTUAL | 2 | Text button (displayed as simple text without any background color). |

#### ControlSize11+

Button size.

**Widget capability**: This API can be used in ArkTS widgets since API version 11.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Value | Description |
| :-- | :-- | :-- |
| SMALL | "small" | Small button. |
| NORMAL | "normal" | Normal button. |

#### ButtonRole12+

Role of the button.

**Widget capability**: This API can be used in ArkTS widgets since API version 12.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Value | Description |
| :-- | :-- | :-- |
| NORMAL | 0 | Normal button. |
| ERROR | 1 | Warning button. |

#### ButtonConfiguration12+

You need a custom class to implement the **ContentModifier** API. Inherits from [CommonConfiguration](../../universal-attributes/modifiers-and-custom-property/content-modifier/document.md#commonconfigurationt).

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| label | string | No | No | 
Text label of the button.

Note: If the text is longer than the width of the button, it is truncated.

 |
| pressed | boolean | No | No | 

Whether the button is pressed.

**true**: pressed; **false**: not pressed.

Default value: **false**.

**NOTE**

This setting applies to the original button size, not to any new component constructed using the builder.

 |
| triggerClick | [ButtonTriggerClickCallback](#buttontriggerclickcallback12) | No | No | Click event of the new component constructed using the builder. |

#### ButtonTriggerClickCallback12+

type ButtonTriggerClickCallback = (xPos: number, yPos: number) => void

Defines the callback type used in **ButtonConfiguration**.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| xPos | number | Yes | 
X-coordinate of the click point.

Unit: vp

 |
| yPos | number | Yes | 

Y-coordinate of the click point.

Unit: vp

 |

#### Events

The [universal events](../../universal-events/document.md) are supported.

#### Example

## Example 1: Setting the Button Display Style

This example demonstrates two methods to create buttons, either with child components or using text content.

// xxx.ets
@Entry
@Component
struct ButtonExample {
  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Start, justifyContent: FlexAlign.SpaceBetween }) {
      Text('Normal button').fontSize(9).fontColor(0xCCCCCC)
      Flex({ alignItems: ItemAlign.Center, justifyContent: FlexAlign.SpaceBetween }) {
        Button('OK', { type: ButtonType.Normal, stateEffect: true })
          .borderRadius(8)
          .backgroundColor(0x317aff)
          .width(90)
          .onClick(() => {
            console.info('ButtonType.Normal');
          })
        Button({ type: ButtonType.Normal, stateEffect: true }) {
          Row() {
            LoadingProgress().width(20).height(20).margin({ left: 12 }).color(0xFFFFFF)
            Text('loading').fontSize(12).fontColor(0xffffff).margin({ left: 5, right: 12 })
          }.alignItems(VerticalAlign.Center)
        }.borderRadius(8).backgroundColor(0x317aff).width(90).height(40)

        Button('Disable', { type: ButtonType.Normal, stateEffect: false }).opacity(0.4)
          .borderRadius(8).backgroundColor(0x317aff).width(90)
      }

      Text('Capsule button').fontSize(9).fontColor(0xCCCCCC)
      Flex({ alignItems: ItemAlign.Center, justifyContent: FlexAlign.SpaceBetween }) {
        Button('OK', { type: ButtonType.Capsule, stateEffect: true }).backgroundColor(0x317aff).width(90)
        Button({ type: ButtonType.Capsule, stateEffect: true }) {
          Row() {
            LoadingProgress().width(20).height(20).margin({ left: 12 }).color(0xFFFFFF)
            Text('loading').fontSize(12).fontColor(0xffffff).margin({ left: 5, right: 12 })
          }.alignItems(VerticalAlign.Center).width(90).height(40)
        }.backgroundColor(0x317aff)

        Button('Disable', { type: ButtonType.Capsule, stateEffect: false }).opacity(0.4)
          .backgroundColor(0x317aff).width(90)
      }

      Text('Circle button').fontSize(9).fontColor(0xCCCCCC)
      Flex({ alignItems: ItemAlign.Center, wrap: FlexWrap.Wrap }) {
        Button({ type: ButtonType.Circle, stateEffect: true }) {
          LoadingProgress().width(20).height(20).color(0xFFFFFF)
        }.width(55).height(55).backgroundColor(0x317aff)

        Button({ type: ButtonType.Circle, stateEffect: true }) {
          LoadingProgress().width(20).height(20).color(0xFFFFFF)
        }.width(55).height(55).margin({ left: 20 }).backgroundColor(0xF55A42)
      }
    }.height(400).padding({ left: 35, right: 35, top: 35 })
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/da/v3/xXbK9PRzRxakW1F_of8hiQ/en-us_image_0000002568765321.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062240Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1A3605CCC16FC5DE26F2C7EE6D63147F5738FFD422FE0BE345E79F1087259F71)

## Example 2: Adding Render Control to a Button

This example uses if/else statements to control the display text of the button.

// xxx.ets
@Entry
@Component
struct SwipeGestureExample {
  @State count: number = 0;

  build() {
    Column() {
      Text(\`${this.count}\`)
        .fontSize(30)
        .onClick(() => {
          this.count++;
        })
      if (this.count <= 0) {
        Button('count is negative').fontSize(30).height(50)
      } else if (this.count % 2 === 0) {
        Button('count is even').fontSize(30).height(50)
      } else {
        Button('count is odd').fontSize(30).height(50)
      }
    }.height('100%').width('100%').justifyContent(FlexAlign.Center)
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/82/v3/yxh83NtgTgCUrON_JZru2Q/en-us_image_0000002537765596.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062240Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=57698B74B1C1E3291EC8713AEACAD69E706284B9691B78140C15238D064A9A3F)

## Example 3: Setting the Button Text Style

This example customizes the display style of button text by configuring **labelStyle**.

// xxx.ets
@Entry
@Component
struct ButtonTestDemo {
  @State txt: string = 'overflowTextOverLengthTextOverflow.Clip';
  @State widthShortSize: number = 205;

  build() {
    Row() {
      Column() {
        Button(this.txt)
          .type(ButtonType.Capsule)
          .width(this.widthShortSize)
          .height(100)
          .backgroundColor(0x317aff)
          .labelStyle({ overflow: TextOverflow.Clip,
            maxLines: 1,
            minFontSize: 20,
            maxFontSize: 20,
            font: {
              size: 20,
              weight: FontWeight.Bolder,
              family: 'cursive',
              style: FontStyle.Italic
            }
          })
          .fontSize(40)
      }
      .width('100%')
    }
    .height('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/59/v3/Q0rE5H8URS2gKUO86w59Nw/en-us_image_0000002537925536.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062240Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B4330FF170B2974897B7A4353EEC31E8B88A4B52A59450E1FB3D1868A6F37AE6)

## Example 4: Setting Importance of Different Sized Buttons

This example demonstrates how to set the importance of buttons of different sizes by configuring **controlSize** and **buttonStyle**.

// xxx.ets
@Entry
@Component
struct ButtonExample {
  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Start, justifyContent: FlexAlign.SpaceBetween }) {
      Text('Normal size button').fontSize(9).fontColor(0xCCCCCC)
      Flex({ alignItems: ItemAlign.Center, justifyContent: FlexAlign.SpaceBetween }) {
        Button('Emphasized', { buttonStyle: ButtonStyleMode.EMPHASIZED });
        Button('Normal', { buttonStyle: ButtonStyleMode.NORMAL });
        Button('Textual', { buttonStyle: ButtonStyleMode.TEXTUAL });
      }

      Text('Small size button').fontSize(9).fontColor(0xCCCCCC)
      Flex({ alignItems: ItemAlign.Center, justifyContent: FlexAlign.SpaceBetween }) {
        Button('Emphasized', { controlSize: ControlSize.SMALL, buttonStyle: ButtonStyleMode.EMPHASIZED });
        Button('Normal', { controlSize: ControlSize.SMALL, buttonStyle: ButtonStyleMode.NORMAL });
        Button('Textual', { controlSize: ControlSize.SMALL, buttonStyle: ButtonStyleMode.TEXTUAL });
      }

      Text('Small size button').fontSize(9).fontColor(0xCCCCCC)
      Flex({ alignItems: ItemAlign.Center, justifyContent: FlexAlign.SpaceBetween }) {
        Button('Emphasized').controlSize(ControlSize.SMALL).buttonStyle(ButtonStyleMode.EMPHASIZED);
        Button('Normal').controlSize(ControlSize.SMALL).buttonStyle(ButtonStyleMode.NORMAL);
        Button('Textual').controlSize(ControlSize.SMALL).buttonStyle(ButtonStyleMode.TEXTUAL);
      }

    }.height(400).padding({ left: 35, right: 35, top: 35 })
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/60/v3/3Pb9LEtXSyCyW3_Ou_PGkQ/en-us_image_0000002568685313.jpeg?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062240Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=93B0D8D3CFE60DF500D64DAE05844942D160CBAED5E58A9FDC8B3D1E1462A9AC)

## Example 5: Setting the Button Role

This example demonstrates how to set the role of the button by configuring **role**.

// xxx.ets
@Entry
@Component
struct ButtonExample {
  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Start, justifyContent: FlexAlign.SpaceBetween }) {
      Text('Role is Normal button').fontSize(9).fontColor(0xCCCCCC)
      Flex({ alignItems: ItemAlign.Center, justifyContent: FlexAlign.SpaceBetween }) {
        Button('Emphasized', { buttonStyle: ButtonStyleMode.EMPHASIZED, role: ButtonRole.NORMAL });
        Button('Normal', { buttonStyle: ButtonStyleMode.NORMAL, role: ButtonRole.NORMAL });
        Button('Textual', { buttonStyle: ButtonStyleMode.TEXTUAL, role: ButtonRole.NORMAL });
      }
      Text('Role is Error button').fontSize(9).fontColor(0xCCCCCC)
      Flex({ alignItems: ItemAlign.Center, justifyContent: FlexAlign.SpaceBetween }) {
        Button('Emphasized', { buttonStyle: ButtonStyleMode.EMPHASIZED, role: ButtonRole.ERROR});
        Button('Normal', { buttonStyle: ButtonStyleMode.NORMAL, role: ButtonRole.ERROR });
        Button('Textual', { buttonStyle: ButtonStyleMode.TEXTUAL, role: ButtonRole.ERROR });
      }
    }.height(200).padding({ left: 15, right: 15, top: 35 })
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f4/v3/VPPgfLHsRfqp1jRDjmS7DQ/en-us_image_0000002568765323.jpeg?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062240Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C28E782A97917D263282AB6D8231F5B12258C65B1A320ECC0068AA12101AD7F3)

## Example 6: Implementing a Custom Button

This example implements a custom button in the shape of a circle. The circle is red when pressed, accompanied by the text "Pressed" in the title. It is black when not pressed, accompanied by the text "Not pressed" in the title.

class MyButtonStyle implements ContentModifier<ButtonConfiguration> {
  x: number = 0;
  y: number = 0;
  selectedColor: Color = Color.Black;

  constructor(x: number, y: number, colorType: Color) {
    this.x = x;
    this.y = y;
    this.selectedColor = colorType;
  }

  applyContent(): WrappedBuilder<\[ButtonConfiguration\]> {
    return wrapBuilder(buildButton1);
  }
}

@Builder
function buildButton1(config: ButtonConfiguration) {
  Column({ space: 30 }) {
    Text(config.enabled ? "enabled true" : "enabled false")
    Text('Circle state' + (config.pressed? "(Pressed)" : "(Not pressed)"))
    Text('X-coordinate of the click point:' + (config.enabled ? (config.contentModifier as MyButtonStyle).x : "0"))
    Text('Y-coordinate of the click point:' + (config.enabled ? (config.contentModifier as MyButtonStyle).y : "0"))
    Circle({ width: 50, height: 50 })
      .fill(config.pressed ? (config.contentModifier as MyButtonStyle).selectedColor : Color.Black)
      .gesture(
        TapGesture({ count: 1 }).onAction((event: GestureEvent) => {
          config.triggerClick(event.fingerList\[0\].localX, event.fingerList\[0\].localY)
        })).opacity(config.enabled ? 1 : 0.1)
  }
}

@Entry
@Component
struct ButtonExample {
  @State buttonEnabled: boolean = true;
  @State positionX: number = 0;
  @State positionY: number = 0;
  @State state: boolean\[\] = \[true, false\];
  @State index: number = 0;

  build() {
    Column() {
      Button('OK')
        .contentModifier(new MyButtonStyle(this.positionX, this.positionY, Color.Red))
        .onClick((event) => {
          console.info('change' + JSON.stringify(event));
          this.positionX = event.displayX;
          this.positionY = event.displayY;
        }).enabled(this.buttonEnabled)
      Row() {
        Toggle({ type: ToggleType.Switch, isOn: true }).onChange((value: boolean) => {
          if (value) {
            this.buttonEnabled = true;
          } else {
            this.buttonEnabled = false;
          }
        }).margin({ left: -80 })
      }
    }.height('100%').width('100%').justifyContent(FlexAlign.Center)
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/65/v3/ED0jM8gvTn--cEb8rOVJxg/en-us_image_0000002537765598.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062240Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=94A0B3917724AF926C0F99D2CA691DD3F17187E0CAAB21120CAFBE1289D7F153)

## Example 7: Setting Rounded Rectangle Buttons

This example creates rounded rectangle buttons by configuring **ButtonType.ROUNDED\_RECTANGLE**.

@Entry
@Component
struct ButtonExample {
  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Start, justifyContent: FlexAlign.SpaceBetween }) {
      Text('Rounded rectangle button with rounded corners by default.').fontSize(9).fontColor(0xCCCCCC)
      Flex({ alignItems: ItemAlign.Center, justifyContent: FlexAlign.SpaceBetween }) {
        Button('Rounded rectangle')
          .type(ButtonType.ROUNDED\_RECTANGLE)
          .backgroundColor(0x317aff)
          .controlSize(ControlSize.NORMAL)
          .width(180)
      }
      Text('Rounded rectangle button configured with a borderRadius of 5.').fontSize(9).fontColor(0xCCCCCC)
      Flex({ alignItems: ItemAlign.Center, justifyContent: FlexAlign.SpaceBetween }) {
        Button('Rounded rectangle')
          .type(ButtonType.ROUNDED\_RECTANGLE)
          .backgroundColor(0x317aff)
          .controlSize(ControlSize.NORMAL)
          .width(180)
          .borderRadius(5)
      }
      Text('Rounded rectangle button configured extra long text.').fontSize(9).fontColor(0xCCCCCC)
      Flex({ alignItems: ItemAlign.Center, justifyContent: FlexAlign.SpaceBetween }) {
        Button('Rounded rectangle Rounded rectangle Rounded rectangle Rounded rectangle')
          .type(ButtonType.ROUNDED\_RECTANGLE)
          .backgroundColor(0x317aff)
          .width(180)
          .labelStyle({overflow:TextOverflow.Ellipsis, maxLines:3, minFontSize: 0})
      }
    }.height(400).padding({ left: 35, right: 35, top: 35 })
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4e/v3/TyuG7DoMS2We8HreLmKEFg/en-us_image_0000002537925538.jpeg?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062240Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=EFFD091686E74576957656506A74822939D35C4688F6631EFEDF8AF47114241C)

## Example 8 (Setting the Horizontal Alignment Mode of the Label Text)

This example shows how to set the text alignment mode by configuring **textAlign** of [LabelStyle](#labelstyle10).

The **textAlign** API is supported since API version 23.

@Entry
@Component
struct Index {
  build() {
    Column(){
      Button('helloWorld helloWorld helloWorld helloWorld helloWorld helloWorld')
        .width(200)
        .labelStyle({
          textAlign: TextAlign.Center
        })
    }
    .width('100%')
    .alignItems(HorizontalAlign.Center)
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4b/v3/INeh19GwQcC29KbjDArnPg/en-us_image_0000002568685315.jpeg?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062240Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=39D62CDA62ABB7C33DFD62EFCEB5EBB94AEBB0C56D82FF031DBCB5B6983FA3B3)
