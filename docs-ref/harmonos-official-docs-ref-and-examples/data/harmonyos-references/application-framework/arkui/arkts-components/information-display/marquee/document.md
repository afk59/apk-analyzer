# Marquee

The **Marquee** component is used to display a scrolling piece of text. Text scrolling is activated only when the content width is greater than or equal to the component's width.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a8/v3/KYpCB8A5RJeJE5hJ0ggreQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062244Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A177AD994EE44CB3C658C37E6E86B5F94E4FD3AD2B7973CF9A112C27EDF511D3)

This component is supported since API version 8. Updates will be marked with a superscript to indicate their earliest API version.

To ensure that scrolling frame rates are not affected, it is recommended that the number of **Marquee** components in a scroll container does not exceed four, or alternatively, use the [Text](../../text-and-input/text/document.md) component's [TextOverflow.MARQUEE](../../common-definitions/enums/document.md#textoverflow) as a substitute.

For the scenario where the frame rate of the **Marquee** component is dynamic, you can use the [MarqueeDynamicSyncScene](../../../arkts-api/ui/ohos-arkui-uicontext-uicontext/class-marqueedynamicsyncscene/document.md) API.

If the text width is less than the **Marquee** component width, use the [property animation](../../animation/property-animation-animation/document.md) to implement scrolling.

#### Child Components

Not supported

#### APIs

Marquee(options: MarqueeOptions)

Creates a marquee.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| options | [MarqueeOptions](#marqueeoptions18)18+ | Yes | Parameters of the marquee. |

#### MarqueeOptions18+

Describes the initialization options of the **Marquee** component.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a2/v3/1EHzvNc6RCq4LbyLxKLImQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062244Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3E7A4785AC190257EC1659F8E3E741521E0FFB5589B2EBAA932D7B1F3105395E)

To standardize anonymous object definitions, the element definitions here have been revised in API version 18. While historical version information is preserved for anonymous objects, there may be cases where the outer element's @since version number is higher than inner elements'. This does not affect interface usability.

**Widget capability**: This API can be used in ArkTS widgets since API version 18.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| start8+ | boolean | No | No | 
Whether to start scrolling.

**true**: yes; **false**: no

**NOTE**

This parameter cannot be used to restart scrolling that has been completed.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| step8+ | number | No | Yes | 

Step length of the scrolling animation text. If the value is greater than the text width of the marquee, the default value is used.

Default value: **6**

Unit: [vp](../../common-definitions/pixel-units/document.md)

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| loop8+ | number | No | Yes | 

Number of times the marquee will scroll. If the value is less than or equal to **0**, the marquee will scroll continuously.

Default value: **\-1**

**NOTE**

Regardless of the value, the marquee scrolls only once on an ArkTS widget.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| fromStart8+ | boolean | No | Yes | 

Whether the text scrolls from the start.

**true**: Scroll from the start.

**false**: Scroll from the end.

Default value: **true**.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| src8+ | string | No | No | 

Text to scroll.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |

#### Attributes

In addition to the [universal attributes](../../universal-attributes/document.md), the following attributes are supported.

#### \[h2\]fontColor

fontColor(value: ResourceColor)

Sets the font color.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [ResourceColor](../../common-definitions/basic-types/document.md#resourcecolor) | Yes | 
Font color.

Default value: **'#c5ffffff'** (light blue) on wearables; **'e6182431'** (black) on other devices

 |

#### \[h2\]fontSize

fontSize(value: Length)

Sets the text size.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [Length](../../common-definitions/basic-types/document.md#length) | Yes | Font size. If **fontSize** is of the number type, the unit fp is used. The default font size is 16 fp. This parameter cannot be set in percentage. |

#### \[h2\]fontWeight

fontWeight(value: number | FontWeight | string)

Sets the font weight. If the value is too large, the text may be clipped depending on the font.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | number | [FontWeight](../../common-definitions/enums/document.md#fontweight) | string | Yes | 
Font weight. For the number type, the value range is \[100, 900\], at an interval of 100. The default value is **400**. A larger value indicates a heavier font weight. For the string type, only strings that represent a number, for example, **400**, and the following enumerated values of **FontWeight** are supported: **bold**, **bolder**, **lighter**, **regular**, and **medium**.

Default value: **FontWeight.Normal**

 |

#### \[h2\]fontFamily

fontFamily(value: string | Resource)

Sets the font family.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | string | [Resource](../../common-definitions/basic-types/document.md#resource) | Yes | 
Font family. Default font: **'HarmonyOS Sans'**

Supported fonts include **'HarmonyOS Sans'** and custom fonts registered using [loadFontSync](../../../../../graphics/arkgraphics-2d/arkts-apis/ohos-graphics-text-text/document.md#loadfontsync).

Only the 'HarmonyOS Sans' font is supported for widgets.

 |

#### \[h2\]allowScale

allowScale(value: boolean)

Sets whether to allow text to scale.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | boolean | Yes | 
Whether to allow text to scale.

**true**: yes; **false**: no

Default value: **false**

**NOTE**

This parameter is effective only when [fontSize](#fontsize) is in fp units.

 |

#### \[h2\]marqueeUpdateStrategy12+

marqueeUpdateStrategy(value: MarqueeUpdateStrategy)

Sets the scrolling strategy for the marquee after its attributes are updated. (This attribute takes effect when the marquee is in the playing state and the text content width exceeds the width of the marquee component.)

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [MarqueeUpdateStrategy](../../common-definitions/enums/document.md#marqueeupdatestrategy12) | Yes | 
Scrolling strategy for the marquee after its attributes are updated.

Default value: **MarqueeUpdateStrategy.DEFAULT**

 |

#### Events

#### \[h2\]onStart

onStart(event: () => void)

Triggered when the marquee text changes or starts scrolling.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| event | () => void | Yes | Callback invoked when the marquee text changes or starts scrolling. |

#### \[h2\]onBounce

onBounce(event: () => void)

Triggered when the marquee has reached the end. This event will be triggered for multiple times if the **loop** attribute is not set to **1**.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| event | () => void | Yes | Callback invoked when the marquee has finished scrolling once. |

#### \[h2\]onFinish

onFinish(event: () => void)

Triggered when the marquee has finished the number of scrolling times set by the **loop** attribute.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| event | () => void | Yes | Callback invoked when the marquee has finished the number of scrolling times set by the **loop** attribute. |

#### Example

This example shows the dynamic updating of a marquee's content by setting parameters such as **start**, **step**, **loop**, **fromStart**, **src**, **spacing**, and [marqueeUpdateStrategy](#marqueeupdatestrategy12) of [MarqueeOptions](#marqueeoptions18).

// xxx.ets
@Entry
@Component
struct MarqueeExample {
  @State start: boolean = false;
  @State src: string = '';
  @State marqueeText: string = 'Running Marquee';
  private fromStart: boolean = true;
  private step: number = 10;
  private loop: number = Number.POSITIVE\_INFINITY;
  controller: TextClockController = new TextClockController();

  convert2time(value: number): string {
    let date = new Date(Number(value + '000'));
    let hours = date.getHours().toString().padStart(2, '0');
    let minutes = date.getMinutes().toString().padStart(2, '0');
    let seconds = date.getSeconds().toString().padStart(2, '0');
    return hours + ":" + minutes + ":" + seconds;
  }

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Marquee({
        start: this.start,
        step: this.step,
        loop: this.loop,
        fromStart: this.fromStart,
        src: this.marqueeText + this.src
      })
        .marqueeUpdateStrategy(MarqueeUpdateStrategy.PRESERVE\_POSITION)
        .width('300vp')
        .height('80vp')
        .fontColor('#FFFFFF')
        .fontSize('48fp')
        .allowScale(true) // Set this to true if you want the marquee text to scale with the system font size when using the fp unit for fontSize.
        .fontWeight(700)
        .fontFamily('HarmonyOS Sans') // Use 'HarmonyOS Sans' to avoid following the theme font.
        .backgroundColor('#182431')
        .margin({ bottom: '40vp' })
        .onStart(() => {
          console.info('Succeeded in completing the onStart callback of marquee animation');
        })
        .onBounce(() => {
          console.info('Succeeded in completing the onBounce callback of marquee animation');
        })
        .onFinish(() => {
          console.info('Succeeded in completing the onFinish callback of marquee animation');
        })
      Button('Start')
        .onClick(() => {
          this.start = true
          // Start the text clock.
          this.controller.start();
        })
        .width('120vp')
        .height('40vp')
        .fontSize('16fp')
        .fontWeight(500)
        .backgroundColor('#007DFF')
      TextClock({ timeZoneOffset: -8, controller: this.controller })
        .format('hms')
        .onDateChange((value: number) => {
          this.src = this.convert2time(value);
        })
        .margin('20vp')
        .fontSize('30fp')
    }
    .width('100%')
    .height('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/62/v3/CogX3mRUSqOIvd2WEZuGKA/en-us_image_0000002537925726.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062244Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A502C550DA1F93605A40B6FACF32C25A3FD64620C852239BC9B4709F88A5BAE7)
