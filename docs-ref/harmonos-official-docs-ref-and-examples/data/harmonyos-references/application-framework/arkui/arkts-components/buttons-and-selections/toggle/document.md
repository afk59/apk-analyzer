# Toggle

The **Toggle** component provides a clickable element in the check box, button, or switch type.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cd/v3/a47no5WOTzSv2rZ-RgL4Kw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062240Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9741D0CD8DB4AD1972FCEAF03EA94240ECDD9DEE98E320C6AED3BA157C84DCED)

This component is supported since API version 8. Updates will be marked with a superscript to indicate their earliest API version.

#### Child Components

This component can contain child components only when **ToggleType** is set to **Button**.

#### APIs

Toggle(options: ToggleOptions)

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| options | [ToggleOptions](#toggleoptions18) | Yes | Options of the toggle. |

#### ToggleOptions18+

Options of the toggle.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a6/v3/34cb7HNNQ_G2SG4Km9cyRA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062240Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C46A750CCB67A4BF9AACE5E97D5FD7B798F2F599C30470430EC3FEBD20956225)

To standardize anonymous object definitions, the element definitions here have been revised in API version 18. While historical version information is preserved for anonymous objects, there may be cases where the outer element's @since version number is higher than inner elements'. This does not affect interface usability.

**Widget capability**: This API can be used in ArkTS widgets since API version 18.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| type8+ | [ToggleType](#toggletype) | No | No | 
Type of the toggle.

Default value: **ToggleType.Switch**

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| isOn8+ | boolean | No | Yes | 

Whether the toggle is turned on.

**true**: on. **false**: off.

Default value: **false**

This parameter supports two-way binding through [$$](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-two-way-sync).

This parameter supports two-way binding through the [!! syntax](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-new-binding#two-way-binding-between-built-in-component-parameters).

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |

#### ToggleType

Enumerates toggle types.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Value | Description |
| :-- | :-- | :-- |
| Checkbox | 0 | 
Check box type.

**NOTE**

Since API version 11, the default style of the **Checkbox** component is changed from rounded square to circle.

The default value of the universal attribute [margin](../../universal-attributes/layout-and-borders/sizing/document.md#margin) is as follows:

{

top: '14px',

right: '14px',

bottom: '14px',

left: '14px'

}.

Default size:

{width:'20vp', height:'20vp'}

 |
| Switch | 1 | 

Switch type.

**NOTE**

The default value of the universal attribute [margin](../../universal-attributes/layout-and-borders/sizing/document.md#margin) is as follows:

{

top: '6px',

right: '14px',

bottom: '6px',

left: '14px'

}.

Default size:

{width:'36vp', height:'20vp'}

 |
| Button | 2 | Status button type. If child content contains text, the text is displayed on the button. The default height is 28 vp, and there is no default width. |

#### Attributes

In addition to the [universal attributes](../../universal-attributes/document.md), the following attributes are supported.

#### \[h2\]selectedColor

selectedColor(value: ResourceColor)

Background color of the component when it is turned on.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [ResourceColor](../../common-definitions/basic-types/document.md#resourcecolor) | Yes | 
Background color of the component when it is turned on.

Default value:

When **ToggleType** is set to **Switch**, the default value is **$r('sys.color.ohos\_id\_color\_emphasize')**.

When **ToggleType** is set to **Checkbox**, the default value is **$r('sys.color.ohos\_id\_color\_emphasize')**.

When **ToggleType** is set to **Button**, the default value is **$r('sys.color.ohos\_id\_color\_emphasize')** with the opacity of **$r('sys.float.ohos\_id\_alpha\_highlight\_bg')**.

 |

#### \[h2\]switchPointColor

switchPointColor(color: ResourceColor)

Sets the color of the circular slider when the component is of the **Switch** type. This attribute is valid only when **type** is set to **ToggleType.Switch**.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| color | [ResourceColor](../../common-definitions/basic-types/document.md#resourcecolor) | Yes | 
Color of the circular slider when the component is of the **Switch** type.

Default value: **$r('sys.color.ohos\_id\_color\_foreground\_contrary')**

 |

#### \[h2\]switchStyle12+

switchStyle(value: SwitchStyle)

Sets the style for the component of the **Switch** type. This attribute is valid only when **type** is set to **ToggleType.Switch**.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [SwitchStyle](#switchstyle12) | Yes | Style of the component of the **Switch** type. |

#### \[h2\]contentModifier12+

contentModifier(modifier: ContentModifier<ToggleConfiguration>)

Creates a content modifier.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| modifier | [ContentModifier](../../universal-attributes/modifiers-and-custom-property/content-modifier/document.md#contentmodifiert)[<ToggleConfiguration>](#toggleconfiguration12) | Yes | 
Content modifier to apply to the current component.

**modifier**: content modifier. You need a custom class to implement the **ContentModifier** API.

 |

#### SwitchStyle12+

Describes the switch type.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| pointRadius | number | [Resource](../../common-definitions/basic-types/document.md#resource) | No | Yes | 
Radius of the circular slider when the component is of the **Switch** type. The unit is vp.

**NOTE**

Percentage values are not supported. The value specified is used only when it is greater than or equal to 0.

If the value is not specified or the specified one is less than 0, the radius is set using the following formula:

(Component height (in vp)/2) - (2 vp x Component height (in vp)/20 vp)

 |
| unselectedColor | [ResourceColor](../../common-definitions/basic-types/document.md#resourcecolor) | No | Yes | 

Background color of the component when it is of the **Switch** type and is disabled.

Default value: **0x337F7F7F** (applies to both dark and light modes). Starting from API version 20, when [optimizing color mode switching overhead](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/ui-dark-light-color-adaptation#optimizing-color-mode-switching-overhead) is enabled, the default value is 0x19000000 (black with 10% transparency) in light mode and 0x19FFFFFF (white with 10% transparency) in dark mode.

 |
| pointColor | [ResourceColor](../../common-definitions/basic-types/document.md#resourcecolor) | No | Yes | 

Color of the circular slider when the component is of the **Switch** type.

Default value: **$r('sys.color.ohos\_id\_color\_foreground\_contrary')**

 |
| trackBorderRadius | number | [Resource](../../common-definitions/basic-types/document.md#resource) | No | Yes | 

Radius of the slider track border corners when the component is of the **Switch** type. The unit is vp.

**NOTE**

This parameter cannot be set in percentage. If the value specified is less than 0, the radius is set using the default value formula. If the value specified is greater than half of the component height, the latter is used. In other cases, the value specified is used.

If the value is not specified or the specified one is less than 0, the radius is set using the default value formula.

Default value formula: Component height (in vp)/2

 |

#### Events

In addition to the [universal events](../../universal-events/document.md), the following events are supported.

#### \[h2\]onChange

onChange(callback: (isOn: boolean) => void)

Triggered when the toggle status changes.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| isOn | boolean | Yes | 
Toggle status.

**true**: The toggle is turned on. **false**: The toggle is turned off.

 |

#### ToggleConfiguration12+

You need a custom class to implement the **ContentModifier** API. This API inherits from [CommonConfiguration](../../universal-attributes/modifiers-and-custom-property/content-modifier/document.md#commonconfigurationt).

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| isOn | boolean | No | No | 
Whether the toggle is turned on.

**true**: The toggle is turned on. **false**: The toggle is turned off.

Default value: **false**

 |
| enabled | boolean | No | No | 

Whether the toggle is enabled for state switching.

**true**: The state can be changed. **false**: The state cannot be changed.

Default value: **true**

 |
| triggerChange | Callback<boolean> | No | No | 

Callback invoked when the toggle's state changes.

**true**: The toggle is turned on. **false**: The toggle is turned off.

 |

#### Example

## Example 1: Setting the Toggle Style

This example demonstrates how to configure the style for different types of toggles (checkbox, switch, and button) using **ToggleType**.

// xxx.ets
@Entry
@Component
struct ToggleExample {
  build() {
    Column({ space: 10 }) {
      Text('type: Switch').fontSize(12).fontColor(0xcccccc).width('90%')
      Flex({ justifyContent: FlexAlign.SpaceEvenly, alignItems: ItemAlign.Center }) {
        Toggle({ type: ToggleType.Switch, isOn: false })
          .selectedColor('#007DFF')
          .switchPointColor('#FFFFFF')
          .onChange((isOn: boolean) => {
            console.info('Component status:' + isOn);
          })

        Toggle({ type: ToggleType.Switch, isOn: true })
          .selectedColor('#007DFF')
          .switchPointColor('#FFFFFF')
          .onChange((isOn: boolean) => {
            console.info('Component status:' + isOn);
          })
      }

      Text('type: Checkbox').fontSize(12).fontColor(0xcccccc).width('90%')
      Flex({ justifyContent: FlexAlign.SpaceEvenly, alignItems: ItemAlign.Center }) {
        Toggle({ type: ToggleType.Checkbox, isOn: false })
          .size({ width: 20, height: 20 })
          .selectedColor('#007DFF')
          .onChange((isOn: boolean) => {
            console.info('Component status:' + isOn);
          })

        Toggle({ type: ToggleType.Checkbox, isOn: true })
          .size({ width: 20, height: 20 })
          .selectedColor('#007DFF')
          .onChange((isOn: boolean) => {
            console.info('Component status:' + isOn);
          })
      }

      Text('type: Button').fontSize(12).fontColor(0xcccccc).width('90%')
      Flex({ justifyContent: FlexAlign.SpaceEvenly, alignItems: ItemAlign.Center }) {
        Toggle({ type: ToggleType.Button, isOn: false }) {
          Text('status button').fontColor('#182431').fontSize(12)
        }.width(106)
        .selectedColor('rgba(0,125,255,0.20)')
        .onChange((isOn: boolean) => {
          console.info('Component status:' + isOn);
        })

        Toggle({ type: ToggleType.Button, isOn: true }) {
          Text('status button').fontColor('#182431').fontSize(12)
        }.width(106)
        .selectedColor('rgba(0,125,255,0.20)')
        .onChange((isOn: boolean) => {
          console.info('Component status:' + isOn);
        })
      }
    }.width('100%').padding(24)
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c0/v3/iLpZxl2hSimmOri-Ro8jJg/en-us_image_0000002568765325.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062240Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B175FE4447B8675F917C5A5BB10997F2A3783CB320D65B69485AB22CE617E58B)

## Example 2: Customizing the Toggle Style

This example implements a toggle of the **Switch** type with custom settings, including the radius and color of the circular slider, background color in the off state, and radius of the slider track border corners.

// xxx.ets
@Entry
@Component
struct ToggleExample {
  build() {
    Column({ space: 10 }) {
      Text('type: Switch').fontSize(12).fontColor(0xcccccc).width('90%')
      Flex({ justifyContent: FlexAlign.SpaceEvenly, alignItems: ItemAlign.Center }) {
        Toggle({ type: ToggleType.Switch, isOn: false })
          .selectedColor('#007DFF')
          .switchStyle({
            pointRadius: 15,
            trackBorderRadius: 10,
            pointColor: '#D2B48C',
            unselectedColor: Color.Pink })
          .onChange((isOn: boolean) => {
            console.info('Component status:' + isOn);
          })

        Toggle({ type: ToggleType.Switch, isOn: true })
          .selectedColor('#007DFF')
          .switchStyle({
            pointRadius: 15,
            trackBorderRadius: 10,
            pointColor: '#D2B48C',
            unselectedColor: Color.Pink })
          .onChange((isOn: boolean) => {
            console.info('Component status:' + isOn);
          })
      }
    }.width('100%').padding(24)
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/04/v3/aSq4nXpATDOrVSWZTzVooQ/en-us_image_0000002537765600.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062240Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=75CF6EFA3A78E8E1721BE13F0DDAB3C65C375A5307BE12C4033CB592EACD6276)

## Example 3: Implementing a Custom Toggle Style

This example shows how to implement a custom toggle style. The toggle button switches the background color. Clicking the blue circle changes the background to blue. Clicking the yellow circle changes it to yellow.

// xxx.ets
class MySwitchStyle implements ContentModifier<ToggleConfiguration> {
  selectedColor: Color = Color.White;
  lamp: string = 'string';

  constructor(selectedColor: Color, lamp: string) {
    this.selectedColor = selectedColor;
    this.lamp = lamp;
  }

  applyContent(): WrappedBuilder<\[ToggleConfiguration\]> {
    return wrapBuilder(buildSwitch);
  }
}

@Builder
function buildSwitch(config: ToggleConfiguration) {
  Column({ space: 50 }) {
    Circle({ width: 150, height: 150 })
      .fill(config.isOn ? (config.contentModifier as MySwitchStyle).selectedColor : Color.Blue)
    Row() {
      Button('Blue ' + JSON.stringify((config.contentModifier as MySwitchStyle).lamp))
        .onClick(() => {
          config.triggerChange(false);
        })
      Button('Yellow ' + JSON.stringify((config.contentModifier as MySwitchStyle).lamp))
        .onClick(() => {
          config.triggerChange(true);
        })
    }
  }
}

@Entry
@Component
struct Index {
  build() {
    Column({ space: 50 }) {
      Toggle({ type: ToggleType.Switch })
        .enabled(true)
        .contentModifier(new MySwitchStyle(Color.Yellow, 'light'))
        .onChange((isOn: boolean) => {
          console.info('Switch Log:' + isOn);
        })
    }.height('100%').width('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7c/v3/Puo9R2UnQ5ydoDfi0-2sBQ/en-us_image_0000002537925540.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062240Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1FA63C83C80CCB73CF23F21C18604D50F58F70687A3EC2328A3FA1CD3E422F72)
