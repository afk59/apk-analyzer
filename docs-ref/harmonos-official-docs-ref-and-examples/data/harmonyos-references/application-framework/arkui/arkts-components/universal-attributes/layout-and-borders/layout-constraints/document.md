# Layout Constraints

Layout constraints refer to constraints on the aspect ratio and display priority of components.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8/v3/3kS1rfGRTVGQpFGzyENyjQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062233Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4573C223AF2E5745056C11BDB5E36B3DE1C282D476510F13253EAB9D0E8BC839)

The initial APIs of this module are supported since API version 7. Updates will be marked with a superscript to indicate their earliest API version.

#### aspectRatio

aspectRatio(value: number): T

Sets the aspect ratio of the component, which can be obtained using the following formula: width/height.

-   If only **width** and **aspectRatio** are set, the height is calculated using the following formula: width/aspectRatio.
-   If only **height** and **aspectRatio** are set, the width is calculated using the following formula: height x aspectRatio.
-   If **width**, **height**, and **aspectRatio** are all set, the explicitly set height is ignored, and the effective height is calculated using the following formula: width/aspectRatio.

After the **aspectRatio** attribute is set, the component's width and height will be limited by the size of the parent component's content area. The priority of [constraintSize](../sizing/document.md#constraintsize) is higher than that of **aspectRatio**.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | number | Yes | 
Aspect ratio of the component.

The default value varies by API version.

API version 9 and earlier: **1.0**

API version 10: none

**NOTE**

This parameter takes effect only when a valid value greater than 0 is specified.

For example, if a **Row** component has only its width set and does not have any child component, then when **aspectRatio** is not set or is set to a negative value, the height of the **Row** component is 0.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| T | Current component. |

#### displayPriority

displayPriority(value: number): T

Sets the display priority for the component in the layout container.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | number | Yes | 
Display priority of the component in the layout container.

Default value: **1**

**NOTE**

This parameter is only effective in [Row](../../../rows-columns-and-stacking/row/document.md), [Column](../../../rows-columns-and-stacking/column/document.md), and [Flex (single-line)](../../../rows-columns-and-stacking/flex/document.md) container components.

The digits after the decimal point are not counted in determining the display priority. That is, numbers in the \[x, x + 1) range are considered to represent the same priority. For example, **1.0** and **1.9** represent the same priority.

If the **displayPriority** value of all child components is not greater than 1, there is no difference in priority.

When the **displayPriority** value of a child component is greater than 1, a larger value indicates higher priority. If the parent container does not have enough space, child components with lower priority are hidden. If child components of a certain priority are hidden, those with an even lower priority are also hidden.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| T | Current component. |

#### Example

## Example 1: Setting the Component Aspect Ratio

This example illustrates how to use the **aspectRatio** attribute to set different aspect ratios for a component.

// xxx.ets
@Entry
@Component
struct AspectRatioExample {
  private children: string\[\] = \['1', '2', '3', '4', '5', '6'\]

  build() {
    Column({ space: 20 }) {
      Text('using container: row').fontSize(14).fontColor(0xCCCCCC).width('100%')
      Row({ space: 10 }) {
        ForEach(this.children, (item:string) => {
          // Component width = Component height x 1.5 = 90
          Text(item)
            .backgroundColor(0xbbb2cb)
            .fontSize(20)
            .aspectRatio(1.5)
            .height(60)
          // Component height = Component width/1.5 = 60/1.5 = 40
          Text(item)
            .backgroundColor(0xbbb2cb)
            .fontSize(20)
            .aspectRatio(1.5)
            .width(60)
        }, (item:string) => item)
      }
      .size({ width: "100%", height: 100 })
      .backgroundColor(0xd2cab3)
      .clip(true)

      // Grid child component width/height = 3/2
      Text('using container: grid').fontSize(14).fontColor(0xCCCCCC).width('100%')
      Grid() {
        ForEach(this.children, (item:string) => {
          GridItem() {
            Text(item)
              .backgroundColor(0xbbb2cb)
              .fontSize(40)
              .width('100%')
              .aspectRatio(1.5)
          }
        }, (item:string) => item)
      }
      .columnsTemplate('1fr 1fr 1fr')
      .columnsGap(10)
      .rowsGap(10)
      .size({ width: "100%", height: 165 })
      .backgroundColor(0xd2cab3)
    }.padding(10)
  }
}

**Figure 1** Portrait display

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/70/v3/5f_2e1B0QLuCivds_3BI_Q/en-us_image_0000002537925346.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062233Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E2EFFD4E2A3ACCACB2B0F20A0F5AA688434C70FA23F87383F4500D2CD0F3512E)

**Figure 2** Landscape display

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cf/v3/arIcW-KZS7KiZdznnoSLlQ/en-us_image_0000002568685123.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062233Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7D498A2E5CF92393B8B59F8102552E8C137527E2E632C9910E053DEC8A027EFE)

## Example 2: Setting the Component Display Priority

This example shows how to use **displayPriority** to set the display priority for child components.

class ContainerInfo {
  label: string = '';
  size: string = '';
}

class ChildInfo {
  text: string = '';
  priority: number = 0;
}

@Entry
@Component
struct DisplayPriorityExample {
  // Display the container size.
  private container: ContainerInfo\[\] = \[
    { label: 'Big container', size: '90%' },
    { label: 'Middle container', size: '50%' },
    { label: 'Small container', size: '30%' }
  \]
  private children: ChildInfo\[\] = \[
    { text: '1\\n(priority:2)', priority: 2 },
    { text: '2\\n(priority:1)', priority: 1 },
    { text: '3\\n(priority:3)', priority: 3 },
    { text: '4\\n(priority:1)', priority: 1 },
    { text: '5\\n(priority:2)', priority: 2 }
  \]
  @State currentIndex: number = 0;

  build() {
    Column({ space: 10 }) {
      // Switch the size of the parent container.
      Button(this.container\[this.currentIndex\].label).backgroundColor(0x317aff)
        .onClick(() => {
          this.currentIndex = (this.currentIndex + 1) % this.container.length;
        })
      // Set the width for the parent flex container through variables.
      Flex({ justifyContent: FlexAlign.SpaceBetween }) {
        ForEach(this.children, (item:ChildInfo) => {
          // Bind the display priority to the child component through displayPriority.
          Text(item.text)
            .width(120)
            .height(60)
            .fontSize(24)
            .textAlign(TextAlign.Center)
            .backgroundColor(0xbbb2cb)
            .displayPriority(item.priority)
        }, (item:ChildInfo) => item.text)
      }
      .width(this.container\[this.currentIndex\].size)
      .backgroundColor(0xd2cab3)
    }.width("100%").margin({ top: 50 })
  }
}

Landscape display in containers of different sizes

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/20/v3/8TTQBg9CR7-nrIVdDJE_tA/en-us_image_0000002568765133.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062233Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D6080357110C2192B0127BB217376121FE57CEDB2A2C12DDAFB730E0304A514A)
