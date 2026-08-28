# Checkbox

**Checkbox** is a component that is used to enable or disable an option.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c8/v3/53fMnwQFQAuRM6SojJsTew/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062240Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7A7E2F11AFE204D197B075225BD02C40241FDFF66282B658D901D87F809D9C14)

Since API version 11, the default style of the **Checkbox** component is changed from rounded square to circle.

This component is supported since API version 8. Updates will be marked with a superscript to indicate their earliest API version.

#### Child Components

Not supported

#### APIs

Checkbox(options?: CheckboxOptions)

Creates a check box.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| options | [CheckboxOptions](#checkboxoptions) | No | Check box parameters. |

#### CheckboxOptions

Provides information about the check box.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| name | string | No | Yes | 
Name of the check box.

Default value: **undefined**. If this parameter is set to **undefined**, it does not take effect.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| group | string | No | Yes | 

Group name of the check box (that is, the name of the check box group to which the check box belongs).

Default value: **undefined**. In the default state, this parameter is used together with the option whose **group** value is **undefined** in [CheckboxGroupOptions](../checkboxgroup/document.md#checkboxgroupoptions).

**NOTE**

For the settings to take effect, this parameter must be used with the [CheckboxGroup](../checkboxgroup/document.md) component.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| indicatorBuilder12+ | [CustomBuilder](../../common-definitions/basic-types/document.md#custombuilder8) | No | Yes | 

Custom component to indicate that the check box is selected. This custom component is center aligned with the check box. When **indicatorBuilder** is set to **undefined** or **null**, it defaults to the state where it is not set.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |

#### Attributes

In addition to the [universal attributes](../../universal-attributes/document.md), the following attributes are supported.

#### \[h2\]select

select(value: boolean)

Sets whether the check box is selected.

Since API version 10, this attribute supports two-way binding through [$$](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-two-way-sync).

Since API version 18, this attribute supports two-way binding through [!!](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-new-binding#two-way-binding-between-built-in-component-parameters).

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | boolean | Yes | 
Whether the check box is selected.

Default value: **false**

**true**: The check box is selected.

**false**: The check box is not selected.

 |

#### \[h2\]select18+

select(isSelected: Optional<boolean>)

Sets whether the check box is selected. Compared with [select](#select), this API supports the **undefined** type for the **isSelected** parameter.

This attribute supports two-way binding through [$$](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-two-way-sync) and [!!](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-new-binding#two-way-binding-between-built-in-component-parameters).

**Widget capability**: This API can be used in ArkTS widgets since API version 18.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| isSelected | [Optional](../../universal-attributes/modifiers-and-custom-property/custom-property/document.md#optionalt)<boolean> | Yes | 
Whether the check box is selected.

If **isSelected** is set to **undefined**, the default value **false** is used.

**true**: The check box is selected.

**false**: The check box is not selected.

 |

#### \[h2\]selectedColor

selectedColor(value: ResourceColor)

Sets the color of the check box when it is selected.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [ResourceColor](../../common-definitions/basic-types/document.md#resourcecolor) | Yes | 
Color of the check box when it is selected.

Default value: **$r('sys.color.ohos\_id\_color\_text\_primary\_activated')**

An invalid value is handled as the default value.

 |

#### \[h2\]selectedColor18+

selectedColor(resColor: Optional<ResourceColor>)

Sets the color of the check box when it is selected. Compared with [selectedColor](#selectedcolor), this API supports the **undefined** type for the **resColor** parameter.

**Widget capability**: This API can be used in ArkTS widgets since API version 18.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| resColor | [Optional](../../universal-attributes/modifiers-and-custom-property/custom-property/document.md#optionalt)<[ResourceColor](../../common-definitions/basic-types/document.md#resourcecolor)\> | Yes | 
Color of the check box when it is selected.

If **resColor** is set to **undefined**, the default value **$r('sys.color.ohos\_id\_color\_text\_primary\_activated')** is used.

An invalid value is handled as the default value.

 |

#### \[h2\]unselectedColor10+

unselectedColor(value: ResourceColor)

Sets the border color of the check box when it is not selected.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [ResourceColor](../../common-definitions/basic-types/document.md#resourcecolor) | Yes | 
Border color of the check box when it is not selected.

Default value: **$r('sys.color.ohos\_id\_color\_switch\_outline\_off')**

 |

#### \[h2\]unselectedColor18+

unselectedColor(resColor: Optional<ResourceColor>)

Sets the border color of the check box when it is not selected. Compared with [unselectedColor](#unselectedcolor10)10+, this API supports the **undefined** type for the **resColor** parameter.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| resColor | [Optional](../../universal-attributes/modifiers-and-custom-property/custom-property/document.md#optionalt)<[ResourceColor](../../common-definitions/basic-types/document.md#resourcecolor)\> | Yes | 
Border color of the check box when it is not selected.

If **resColor** is set to **undefined**, the default value **$r('sys.color.ohos\_id\_color\_switch\_outline\_off')** is used.

 |

#### \[h2\]mark10+

mark(value: MarkStyle)

Sets the check mark style of the check box.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [MarkStyle](../../common-definitions/basic-types/document.md#markstyle10) | Yes | 
Check mark style of the check box. Since API version 12, if **indicatorBuilder** is set, the style is determined by **indicatorBuilder**.

Default value: {

strokeColor : $r('sys.color.ohos\_id\_color\_foreground\_contrary'),

strokeWidth: $r('sys.float.ohos\_id\_checkbox\_stroke\_width'),

size: '20vp'

}

 |

#### \[h2\]mark18+

mark(style: Optional<MarkStyle>)

Sets the check mark style of the check box. Compared with [mark](#mark10)10+, this API supports the **undefined** type for the **style** parameter.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| style | [Optional](../../universal-attributes/modifiers-and-custom-property/custom-property/document.md#optionalt)<[MarkStyle](../../common-definitions/basic-types/document.md#markstyle10) > | Yes | 
Check mark style of the check box. If **indicatorBuilder** is set, the style is determined by **indicatorBuilder**.

If **style** is set to **undefined**, the default value is used: {

strokeColor : $r('sys.color.ohos\_id\_color\_foreground\_contrary'),

strokeWidth: $r('sys.float.ohos\_id\_checkbox\_stroke\_width'),

size: '20vp'

}

 |

#### \[h2\]shape11+

shape(value: CheckBoxShape)

Sets the check box shape. To adjust the style of the current check box, use [contentModifier](#contentmodifier12).

**Widget capability**: This API can be used in ArkTS widgets since API version 11.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [CheckBoxShape](../../common-definitions/enums/document.md#checkboxshape11) | Yes | 
Shape of the check box.

Default value: **CheckBoxShape.CIRCLE**

 |

#### \[h2\]shape18+

shape(shape: Optional<CheckBoxShape>)

Sets the check box shape. Compared with [shape](#shape11)11+, this API supports the **undefined** type for the **shape** parameter. To adjust the style of the current check box, use [contentModifier](#contentmodifier12).

**Widget capability**: This API can be used in ArkTS widgets since API version 18.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| shape | [Optional](../../universal-attributes/modifiers-and-custom-property/custom-property/document.md#optionalt)<[CheckBoxShape](../../common-definitions/enums/document.md#checkboxshape11)\> | Yes | 
Shape of the check box.

If **shape** is set to **undefined**, the default value **CheckBoxShape.CIRCLE** is used.

 |

#### \[h2\]contentModifier12+

contentModifier(modifier: ContentModifier<CheckBoxConfiguration>)

Creates a content modifier for the **Checkbox** component. Setting this attribute will invalidate other attribute settings.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| modifier | [ContentModifier](../../universal-attributes/modifiers-and-custom-property/content-modifier/document.md#contentmodifiert)[<CheckBoxConfiguration>](#checkboxconfiguration12) | Yes | 
Content modifier to apply to the **Checkbox** component.

**modifier**: content modifier. You need a custom class to implement the **ContentModifier** API.

 |

#### \[h2\]contentModifier18+

contentModifier(modifier: Optional<ContentModifier<CheckBoxConfiguration>>)

Creates a content modifier for the **Checkbox** component. Compared with [contentModifier](#contentmodifier12)12+, this API supports the **undefined** type for the **modifier** parameter. Setting this attribute will invalidate other attribute settings.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| modifier | [Optional](../../universal-attributes/modifiers-and-custom-property/custom-property/document.md#optionalt)<[ContentModifier](../../universal-attributes/modifiers-and-custom-property/content-modifier/document.md#contentmodifiert)[<CheckBoxConfiguration>](#checkboxconfiguration12)\> | Yes | 
Content modifier to apply to the **Checkbox** component.

**modifier**: content modifier. You need a custom class to implement the **ContentModifier** API.

If **modifier** is set to **undefined**, no content modifier is used.

 |

#### Events

In addition to the [universal events](../../universal-events/document.md), the following events are supported.

#### \[h2\]onChange

onChange(callback: OnCheckboxChangeCallback)

Invoked when the selected state of the check box changes.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | [OnCheckboxChangeCallback](#oncheckboxchangecallback18) | Yes | Callback used to return the selected state. |

#### \[h2\]onChange18+

onChange(callback: Optional<OnCheckboxChangeCallback>)

Invoked when the selected state of the check box changes. Compared with [onChange](#onchange), this API supports the **undefined** type for the **callback** parameter.

**Widget capability**: This API can be used in ArkTS widgets since API version 18.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | [Optional](../../universal-attributes/modifiers-and-custom-property/custom-property/document.md#optionalt)<[OnCheckboxChangeCallback](#oncheckboxchangecallback18)\> | Yes | 
Callback used to return the selected state.

If **callback** is set to **undefined**, the callback function is not used.

 |

#### OnCheckboxChangeCallback18+

type OnCheckboxChangeCallback = (value: boolean) => void

Represents the callback invoked when the selected state of the check box changes.

**Widget capability**: This API can be used in ArkTS widgets since API version 18.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | boolean | Yes | Whether the check box is selected. The value **true** means that the check box is selected, and **false** means the opposite. |

#### CheckBoxConfiguration12+

You need a custom class to implement the **ContentModifier** API. Inherits from [CommonConfiguration](../../universal-attributes/modifiers-and-custom-property/content-modifier/document.md#commonconfigurationt).

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| name | string | No | No | Name of the check box. |
| selected | boolean | No | No | 
Whether the check box is selected.

**true**: The check box is selected.

**false**: The check box is not selected.

If the **select** attribute is not set, the default value **false** is used.

If the **select** attribute is set, the attribute value is used here.

 |
| triggerChange | Callback<boolean> | No | No | 

Triggers a change in the check box selection state.

The value **true** indicates a change from unselected to selected, and **false** indicates a change from selected to unselected.

 |

#### Example

## Example 1: Setting the Check Box Shape

This example shows how to set **CheckBoxShape** to implement check boxes in circle and rounded square shapes.

// xxx.ets
@Entry
@Component
struct CheckboxExample {
  build() {
    Flex({ justifyContent: FlexAlign.SpaceEvenly }) {
      Checkbox({ name: 'checkbox1', group: 'checkboxGroup' })
        .select(true)
        .selectedColor(0xed6f21)
        .shape(CheckBoxShape.CIRCLE)
        .onChange((value: boolean) => {
          console.info('Checkbox1 change is' + value);
        })
      Checkbox({ name: 'checkbox2', group: 'checkboxGroup' })
        .select(false)
        .selectedColor(0x39a2db)
        .shape(CheckBoxShape.ROUNDED\_SQUARE)
        .onChange((value: boolean) => {
          console.info('Checkbox2 change is' + value);
        })
    }
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ac/v3/4xI4tQlXSIuDNG1My5e37g/en-us_image_0000002568685317.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062240Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D23CD8466292818A04995333904468038D8D9CC5F15EE884507FE2256964733C)

## Example 2: Setting the Check Box Color

This example demonstrates how to set **mark** to customize the color of a check box.

// xxx.ets
@Entry
@Component
struct Index {

  build() {
    Row() {
      Column() {
        Flex({ justifyContent: FlexAlign.Center, alignItems: ItemAlign.Center }) {
          Checkbox({ name: 'checkbox1', group: 'checkboxGroup' })
            .selectedColor(0x39a2db)
            .shape(CheckBoxShape.ROUNDED\_SQUARE)
            .onChange((value: boolean) => {
              console.info('Checkbox1 change is'+ value);
            })
            .mark({
              strokeColor:Color.Black,
              size: 50,
              strokeWidth: 5
            })
            .unselectedColor(Color.Red)
            .width(30)
            .height(30)
          Text('Checkbox1').fontSize(20)
        }
        Flex({ justifyContent: FlexAlign.Center, alignItems: ItemAlign.Center }) {
          Checkbox({ name: 'checkbox2', group: 'checkboxGroup' })
            .selectedColor(0x39a2db)
            .shape(CheckBoxShape.ROUNDED\_SQUARE)
            .onChange((value: boolean) => {
              console.info('Checkbox2 change is' + value);
            })
            .width(30)
            .height(30)
          Text('Checkbox2').fontSize(20)
        }
      }
      .width('100%')
    }
    .height('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/90/v3/NlB8aItgTtmuCjA9USSPbA/en-us_image_0000002568765327.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062240Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=966AB5499668444F6011B4CF0C5295169160EC4C907998D570877ED5C525A312)

## Example 3: Customizing the Check Box Style

This example demonstrates how to implement a custom check box using [contentModifier](#contentmodifier12). This check box comes in the custom pentagon style. When selected, the check box shows a red triangle pattern inside, and the title displays the word "Selected;" when deselected, the check box hides the red triangle pattern inside, and the title displays the word "Unselected."

// xxx.ets
class MyCheckboxStyle implements ContentModifier<CheckBoxConfiguration> {
  selectedColor: Color = Color.White;

  constructor(selectedColor: Color) {
    this.selectedColor = selectedColor;
  }

  applyContent(): WrappedBuilder<\[CheckBoxConfiguration\]> {
    return wrapBuilder(buildCheckbox);
  }
}

@Builder
function buildCheckbox(config: CheckBoxConfiguration) {
  Column({ space: 10 }) {
    Text(config.name + (config.selected ? "(Selected)" : "(Unselected)")).margin({ right: 70, top: 50 })
    Text(config.enabled ? "enabled true" : "enabled false").margin({ right: 110 })
    Shape() {
      Path()
        .width(100)
        .height(100)
        .commands('M100 0 L0 100 L50 200 L150 200 L200 100 Z')
        .fillOpacity(0)
        .strokeWidth(3)
        .onClick(() => {
          if (config.selected) {
            config.triggerChange(false);
          } else {
            config.triggerChange(true);
          }
        })
        .opacity(config.enabled ? 1 : 0.1)
      Path()
        .width(10)
        .height(10)
        .commands('M50 0 L100 100 L0 100 Z')
        .visibility(config.selected ? Visibility.Visible : Visibility.Hidden)
        .fill(config.selected ? (config.contentModifier as MyCheckboxStyle).selectedColor : Color.Black)
        .stroke((config.contentModifier as MyCheckboxStyle).selectedColor)
        .margin({ left: 10, top: 10 })
        .opacity(config.enabled ? 1 : 0.1)
    }
    .width(300)
    .height(200)
    .viewPort({
      x: 0,
      y: 0,
      width: 310,
      height: 310
    })
    .strokeLineJoin(LineJoinStyle.Miter)
    .strokeMiterLimit(5)
    .margin({ left: 50 })
  }
}

@Entry
@Component
struct Index {
  @State checkboxEnabled: boolean = true;

  build() {
    Column({ space: 100 }) {
      Checkbox({ name: 'Check box status', group: 'checkboxGroup' })
        .contentModifier(new MyCheckboxStyle(Color.Red))
        .onChange((value: boolean) => {
          console.info('Checkbox change is' + value);
        }).enabled(this.checkboxEnabled)

      Row() {
        Toggle({ type: ToggleType.Switch, isOn: true }).onChange((value: boolean) => {
          if (value) {
            this.checkboxEnabled = true;
          } else {
            this.checkboxEnabled = false;
          }
        })
      }.position({ x: 50, y: 130 })
    }.margin({ top: 30 })
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ae/v3/kqwuZK-xSUiqAB7txJRVgw/en-us_image_0000002537765602.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062240Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C50A436E75320959155517A3DE092C95E5EFDD5814645BADB3B9537699706B7F)

## Example 4: Setting the Text Check Box Style

This example configures the selected style of a check box to display as text using the **indicatorBuilder** property.

// xxx.ets
@Entry
@Component
struct CheckboxExample {
  @Builder
  indicatorBuilder(value: number) {
    Column(){
      Text(value > 99 ? '99+': value.toString())
        .textAlign(TextAlign.Center)
        .fontSize(value > 99 ?  '16vp': '20vp')
        .fontWeight(FontWeight.Medium)
        .fontColor('#ffffffff')
    }
  }
  build() {
    Row() {
      Column() {
        Flex({ justifyContent: FlexAlign.Center, alignItems: ItemAlign.Center}) {
          Checkbox({ name: 'checkbox1', group: 'checkboxGroup', indicatorBuilder:()=>{this.indicatorBuilder(9)}})
            .shape(CheckBoxShape.CIRCLE)
            .onChange((value: boolean) => {
              console.info('Checkbox1 change is'+ value);
            })
            .mark({
              strokeColor:Color.Black,
              size: 50,
              strokeWidth: 5
            })
            .width(30)
            .height(30)
          Text('Checkbox1').fontSize(20)
        }.padding(15)
        Flex({ justifyContent: FlexAlign.Center, alignItems: ItemAlign.Center }) {
          Checkbox({ name: 'checkbox2', group: 'checkboxGroup', indicatorBuilder:()=>{this.indicatorBuilder(100)}})
            .shape(CheckBoxShape.ROUNDED\_SQUARE)
            .onChange((value: boolean) => {
              console.info('Checkbox2 change is' + value);
            })
            .width(30)
            .height(30)
          Text('Checkbox2').fontSize(20)
        }
      }
      .width('100%')
    }
    .height('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cb/v3/T11e3TaZRHKx3cWmAuS2sw/en-us_image_0000002537925542.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062240Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A09836B606D476EAA93E62BD72D928C652F797ADE0542EA058076B8A6700984E)

## Example 5: Obtaining the Check Box Selection Information

This example demonstrates how to obtain selection information by selecting check boxes and check box groups.

// xxx.ets
@Entry
@Component
struct CheckboxExample {
  @State arrOne: Array<string> = \['1', '2', '3'\];
  @State arrTwo: Array<string> = \['1', '2', '3', '4'\];
  @State arrThree: Array<string> = \['1', '2', '3', '4', '5', '6'\];
  @State selected: boolean = false;
  @State infoOne: string = '';
  @State infoTwo: string = '';
  @State infoThree: string = '';

  build() {
    Column() {
      // Select All button for the first group
      Flex({ justifyContent: FlexAlign.Start, alignItems: ItemAlign.Center }) {
        CheckboxGroup({ group: 'checkboxGroupOne' })
          .selectAll(this.selected)
          .checkboxShape(CheckBoxShape.ROUNDED\_SQUARE)
          .selectedColor('#007DFF')
          .onChange((itemName: CheckboxGroupResult) => {
            this.infoOne = "checkboxGroupOne" + JSON.stringify(itemName);
            console.info("checkboxGroupOne" + JSON.stringify(itemName));
          })
        Text('checkboxGroupOne Select All').fontSize(14).lineHeight(20).fontColor('#182431').fontWeight(500)
      }

      // Options for the first group
      Flex({ justifyContent: FlexAlign.Start, alignItems: ItemAlign.Center }) {
        Column() {
          ForEach(this.arrOne, (item: string) => {
            Row() {
              Checkbox({ name: 'checkbox' + item, group: 'checkboxGroupOne' })
                .selectedColor('#007DFF')
                .shape(CheckBoxShape.ROUNDED\_SQUARE)
                .onChange((value: boolean) => {
                  console.info('Checkbox' + item + 'change is' + value);
                })
                .margin({ left: 20 })
              Text('Checkbox' + item)
                .fontSize(14)
                .lineHeight(20)
                .fontColor('#182431')
                .fontWeight(500)
                .margin({ left: 10 })
            }
          }, (item: string) => item)
        }
      }.margin({ bottom: 15 })

      Flex({ justifyContent: FlexAlign.Start, alignItems: ItemAlign.Center }) {
        CheckboxGroup({ group: 'checkboxGroupTwo' })
          .selectAll(this.selected)
          .checkboxShape(CheckBoxShape.ROUNDED\_SQUARE)
          .selectedColor('#007DFF')
          .onChange((itemName: CheckboxGroupResult) => {
            this.infoTwo = "checkboxGroupTwo" + JSON.stringify(itemName);
            console.info("checkboxGroupTwo" + JSON.stringify(itemName));
          })
        Text('checkboxGroupTwo Select All').fontSize(14).lineHeight(20).fontColor('#182431').fontWeight(500)
      }

      // Options for the second group
      Flex({ justifyContent: FlexAlign.Start, alignItems: ItemAlign.Center }) {
        Column() {
          ForEach(this.arrTwo, (item: string) => {
            Row() {
              Checkbox({ name: 'checkbox' + item, group: 'checkboxGroupTwo' })
                .selectedColor('#007DFF')
                .shape(CheckBoxShape.ROUNDED\_SQUARE)
                .onChange((value: boolean) => {
                  console.info('Checkbox' + item + 'change is' + value);
                })
                .margin({ left: 20 })
              Text('Checkbox' + item)
                .fontSize(14)
                .lineHeight(20)
                .fontColor('#182431')
                .fontWeight(500)
                .margin({ left: 10 })
            }
          }, (item: string) => item)
        }
      }.margin({ bottom: 15 })

      Flex({ justifyContent: FlexAlign.Start, alignItems: ItemAlign.Center }) {
        CheckboxGroup({ group: 'checkboxGroupThree' })
          .selectAll(this.selected)
          .checkboxShape(CheckBoxShape.ROUNDED\_SQUARE)
          .selectedColor('#007DFF')
          .onChange((itemName: CheckboxGroupResult) => {
            this.infoThree = "checkboxGroupThree" + JSON.stringify(itemName);
            console.info("checkboxGroupThree" + JSON.stringify(itemName));
          })
        Text('checkboxGroupThree Select All').fontSize(14).lineHeight(20).fontColor('#182431').fontWeight(500)
      }

      // Options for the third group
      Flex({ justifyContent: FlexAlign.Start, alignItems: ItemAlign.Center }) {
        Column() {
          ForEach(this.arrThree, (item: string) => {
            Row() {
              Checkbox({ name: 'checkbox' + item, group: 'checkboxGroupThree' })
                .selectedColor('#007DFF')
                .shape(CheckBoxShape.ROUNDED\_SQUARE)
                .onChange((value: boolean) => {
                  console.info('Checkbox' + item + 'change is' + value);
                })
                .margin({ left: 20 })
              Text('Checkbox' + item)
                .fontSize(14)
                .lineHeight(20)
                .fontColor('#182431')
                .fontWeight(500)
                .margin({ left: 10 })
            }
          }, (item: string) => item)
        }
      }.margin({ bottom: 15 })

      // Select all.
      Flex({ justifyContent: FlexAlign.Start, alignItems: ItemAlign.Center }) {
        Row() {
          CheckboxGroup({ group: 'checkboxGroup' })
            .checkboxShape(CheckBoxShape.CIRCLE)
            .selectedColor('#007DFF')
            .width(30)
            .margin({ left: 10 })
            .onChange(() => {
              this.selected = !this.selected
            })
          Text('Select All')
            .fontSize(14)
            .lineHeight(20)
            .fontColor('#182431')
            .fontWeight(500)
            .margin({ left: 10 })
        }
      }.margin({ bottom: 15 })

      // Obtain the selected information.
      Button('get selected info')
        .margin({ top: 10 })
        .onClick(() => {
          this.getUIContext().getPromptAction().showToast({
            message: 'selected info: ' + this.infoOne + '\\n' + this.infoTwo + '\\n' + this.infoThree
          })
        })
    }.padding(10)
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/40/v3/j7Rr3wujSqGVXs14Sg7NCg/en-us_image_0000002568685319.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062240Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=41D76509045B59A7C1783CEAC292D443C6B9EE89AA07A806941D24F522A0EA43)

## Example 6: Implementing Swipe-based Multi-Selection

This example implements swipe-based multi-selection for **Checkbox** components through gesture event configuration.

// xxx.ets
import { componentUtils, ComponentUtils, UIContext } from '@kit.ArkUI';
import { LinkedList } from '@kit.ArkTS';

@Entry
@Component
struct Index {
  @State isChoosing: boolean = false;
  @State selectedStart: number = -1;
  @State @Watch('onSelectedEndChange') selectedEnd: number = -1;
  selectedPhotos: LinkedList<number> = new LinkedList();
  @State selectedList: number\[\] = \[\];
  @State image: Resource\[\] =
    // Replace $r('app.media.xxx') with the image resource file you use.
    \[$r("app.media.imageOne"), $r('app.media.imageTwo'), $r('app.media.imageThree'), $r('app.media.imageFour')\];
  private selectedState: SelectedState = SelectedState.None;
  private componentUtils: ComponentUtils = this.getUIContext().getComponentUtils();
  private listScroller: ListScroller = new ListScroller();
  private currentOffsetY: number = 0;

  onChange() {
    console.info('change successful');
  }

  getSpeed(fingerY: number, edge: number) {
    return 150 \* 150 \* (fingerY - edge) / 2000 / Math.abs(fingerY - edge);
  }

  getIndex(fingerX: number, fingerY: number) {
    let rect: componentUtils.ComponentInfo | null = null;
    for (let i = 0; i < 100; i++) {
      let uiContext: UIContext = this.getUIContext();
      rect = this.componentUtils.getRectangleById(\`stack${i}\`);
      if (rect) {
        const x1 = uiContext.px2vp(rect.windowOffset.x);
        const x2 = uiContext.px2vp(rect.windowOffset.x + rect.size.width);
        const y1 = uiContext.px2vp(rect.windowOffset.y);
        const y2 = uiContext.px2vp(rect.windowOffset.y + rect.size.height);
        if (x1 <= fingerX && fingerX < x2 && y1 <= fingerY && fingerY < y2) {
          return i;
        }
      }
    }
    return this.selectedEnd;
  }
  
  onSelectedEndChange() {
    let start: number = -1;
    let end: number = -1;
    if (this.selectedEnd > this.selectedStart) {
      start = this.selectedStart;
      end = this.selectedEnd;
    } else {
      end = this.selectedStart;
      start = this.selectedEnd;
    }
    if (this.selectedState == SelectedState.Selected) {
      for (let i = start; i <= end; i++) {
        if (!this.selectedPhotos.has(i)) {
          this.selectedPhotos.add(i);
        }
      }
    } else if (this.selectedState == SelectedState.Remove) {
      for (let i = start; i <= end; i++) {
        if (this.selectedPhotos.has(i)) {
          this.selectedPhotos.remove(i);
        }
      }
    }
    this.selectedList = this.selectedPhotos.convertToArray();
  }

  scroll(fingerY: number) {
    if (fingerY > 700 && !this.listScroller.isAtEnd()) {
      this.listScroller.scrollBy(0, this.getSpeed(fingerY, 700));
      return;
    }
    if (fingerY < 200 && this.currentOffsetY > 0) {
      this.listScroller.scrollBy(0, this.getSpeed(fingerY, 200));
      return;
    }
  }

  onPanGestureUpdate(event: GestureEvent) {
    const fingerInfo = event.fingerList\[event.fingerList.length - 1\];
    const fingerX = fingerInfo.globalX;
    const fingerY = fingerInfo.globalY;
    this.selectedEnd = this.getIndex(fingerX, fingerY);
    this.scroll(fingerY);
  }

  build() {
    Column() {
      if (this.isChoosing) {
        Row() {
          Text ('Cancel')
            .onClick(() => {
              this.isChoosing = false;
              this.selectedStart = -1;
              this.selectedEnd = -1;
              this.selectedPhotos.clear();
              this.selectedList = \[\];
            })
        }
        .width('100%')
        .justifyContent(FlexAlign.SpaceEvenly)
      }
      List({ space: 10, scroller: this.listScroller }) {
        ForEach(Array.from({ length: 100 }), (item: string, index: number) => {
          ListItem() {
            Stack({ alignContent: Alignment.TopEnd }) {
              Image(this.image\[(index % 4)\])
                .width('100%')
                .draggable(false)
              Checkbox({ name: index.toString() })
                .shape(CheckBoxShape.CIRCLE)
                .visibility(this.isChoosing ? Visibility.Visible : Visibility.None)
                .select(this.selectedList.includes(index))
            }
            .id(\`stack${index}\`)
            .width('100%')
          }
          .draggable(false)
        }, (item: string, index: number) => 'listItem' + index)
      }
      .id('list')
      .height('100%')
      .width('100%')
      .lanes(4)
      .alignListItem(ListItemAlign.Center)
      .onDidScroll(() => {
        this.currentOffsetY = this.listScroller.currentOffset().yOffset;
      })
      .gesture(
        GestureGroup(GestureMode.Exclusive,
          GestureGroup(GestureMode.Sequence,
            LongPressGesture()
              .onAction(() => {
                this.isChoosing = true;
              }),
            PanGesture()
              .onActionStart(event => {
                if (!this.isChoosing) {
                  return;
                }
                const fingerInfo = event.fingerList\[event.fingerList.length - 1\];
                const fingerX = fingerInfo.globalX;
                const fingerY = fingerInfo.globalY;
                this.selectedStart = this.getIndex(fingerX, fingerY);
                if (this.selectedPhotos.has(this.selectedStart)) {
                  this.selectedState = SelectedState.Remove;
                } else {
                  this.selectedState = SelectedState.Selected;
                }
              })
              .onActionUpdate(event => {
                if (!this.isChoosing) {
                  return;
                }
                this.onPanGestureUpdate(event);
              })
              .onActionEnd(() => {
                if (!this.isChoosing) {
                  return;
                }
                this.selectedState = SelectedState.None;
              })
          ),
          PanGesture()
            .onActionStart(event => {
              if (!this.isChoosing) {
                return;
              }
              const fingerInfo = event.fingerList\[event.fingerList.length - 1\];
              const fingerX = fingerInfo.globalX;
              const fingerY = fingerInfo.globalY;
              this.selectedStart = this.getIndex(fingerX, fingerY);
              if (this.selectedPhotos.has(this.selectedStart)) {
                this.selectedState = SelectedState.Remove;
              } else {
                this.selectedState = SelectedState.Selected;
              }
            })
            .onActionUpdate(event => {
              if (!this.isChoosing) {
                return;
              }
              this.onPanGestureUpdate(event);
            })
            .onActionEnd(() => {
              if (!this.isChoosing) {
                return;
              }
              this.selectedState = SelectedState.None;
            })
        )
      )
    }
  }
}

enum SelectedState {
  None,
  Selected,
  Remove
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f6/v3/1PyOnW8OT0aoz8A0QpTowg/en-us_image_0000002568765329.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062240Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=102D2E86FE3E7BA689DC446BFF4561C2A8DD5C6F421C6EA6BB9BF1D1294D1F7B)
