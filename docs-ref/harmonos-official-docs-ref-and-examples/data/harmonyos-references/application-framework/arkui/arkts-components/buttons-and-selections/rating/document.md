# Rating

The **Rating** component provides a rating bar.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/59/v3/QPrsacubTDO7H9vVcjwzpg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062241Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6DE0F1FE9B0EDDC1F52149F675924EFBA4CAE54477B499E7767F3931520D6991)

-   This component is supported since API version 7. Updates will be marked with a superscript to indicate their earliest API version.
    
-   If the parent node of the **Rating** component has fixed dimensions, you must also specify the width and height for the **Rating** component, or set its parent node's [clip](../../universal-attributes/visual-effects/shape-clipping/document.md#clip18) attribute to **true**.
    

#### Child Components

Not supported

#### APIs

Rating(options?: RatingOptions)

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| options | [RatingOptions](#ratingoptions18) | No | Rating bar options. |

#### Attributes

#### \[h2\]stars

stars(value: number)

Sets the total number of stars. Values less than 0 are treated as the default value.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | number | Yes | 
Total number of stars.

Default value: **5**

 |

#### \[h2\]stars18+

stars(starCount: Optional<number>)

Sets the total number of stars. Values less than 0 are treated as the default value. Compared with [stars](#stars), this API supports the **undefined** type for the **starCount** parameter.

**Widget capability**: This API can be used in ArkTS widgets since API version 18.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| starCount | [Optional](../../universal-attributes/modifiers-and-custom-property/custom-property/document.md#optionalt)<number> | Yes | 
Total number of stars.

If **starCount** is set to **undefined**, the default value **5** is used.

 |

#### \[h2\]stepSize

stepSize(value: number)

Sets the step for rating. Values less than 0.1 are treated as the default value.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | number | Yes | 
Step for rating.

Default value: **0.5**

Value range: \[0.1, stars\]

 |

#### \[h2\]stepSize18+

stepSize(size: Optional<number>)

Sets the step for rating. Values less than 0.1 are treated as the default value. Compared with [stepSize](#stepsize), this API supports the **undefined** type for the **size** parameter.

**Widget capability**: This API can be used in ArkTS widgets since API version 18.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| size | [Optional](../../universal-attributes/modifiers-and-custom-property/custom-property/document.md#optionalt)<number> | Yes | 
Step for rating.

If **size** is set to **undefined**, the default value **0.5** is used.

Value range: \[0.1, stars\]

 |

#### \[h2\]starStyle

starStyle(options: StarStyleOptions)

Sets the star style. For details about the supported image types, see [Image](../../images-and-videos/image/document.md).

Local and network images are supported. The PixelMap type is not supported.

By default, the image is loaded in asynchronous mode. Synchronous loading is not supported.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| options | [StarStyleOptions](#starstyleoptions18) | Yes | 
Star style.

**NOTE**

If an incorrect image path is provided for **backgroundUri**, **foregroundUri**, or **secondaryUri**, the previously displayed image will be retained. If the first provided path is incorrect, no image will be displayed.

When **backgroundUri** or **foregroundUri** is set to **undefined** or an empty string, the **Rating** component falls back to the default star image.

If **secondaryUri** is not set, or is set to **undefined** or an empty string, **backgroundUri** will be used as a fallback. The behavior in this case is the same as when only **foregroundUri** and **backgroundUri** are configured.

 |

#### \[h2\]starStyle18+

starStyle(options: Optional<StarStyleOptions>)

Sets the star style. For details about the supported image types, see [Image](../../images-and-videos/image/document.md).

Local and network images are supported. The PixelMap type is not supported.

By default, the image is loaded in asynchronous mode. Synchronous loading is not supported.

Compared with [starStyle](#starstyle), this API supports the **undefined** type for the **options** parameter.

**Widget capability**: This API can be used in ArkTS widgets since API version 18.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| options | [Optional](../../universal-attributes/modifiers-and-custom-property/custom-property/document.md#optionalt)<[StarStyleOptions](#starstyleoptions18)\> | Yes | 
Star style.

**NOTE**

If an incorrect image path is provided for **backgroundUri**, **foregroundUri**, or **secondaryUri**, the previously displayed image will be retained. If the first provided path is incorrect, no image will be displayed.

When **backgroundUri** or **foregroundUri** is set to **undefined** or an empty string, the **Rating** component falls back to the default star image.

If **secondaryUri** is not set, or is set to **undefined** or an empty string, **backgroundUri** will be used as a fallback. The behavior in this case is the same as when only **foregroundUri** and **backgroundUri** are configured.

 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/92/v3/830jzR4xTvOV18V_G3pfAg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062241Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A291EFE5C5B38A314DD9BD2E7985AA8CE5F9149A68535AFCBE4CEA21D3F192CF)

When the **Rating** component's size is \[width, height\], the drawing area for each star is \[width / stars, height\].

To ensure a square drawing area for each star, it is recommended that you set the width and height in the format \[height × stars, height\]; that is, width = height × stars.

#### \[h2\]contentModifier12+

contentModifier(modifier: ContentModifier<RatingConfiguration>)

Creates a content modifier.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| modifier | [ContentModifier<RatingConfiguration>](#ratingconfiguration12) | Yes | 
Content modifier to apply to the current component.

**modifier**: content modifier. You need a custom class to implement the **ContentModifier** API.

 |

#### \[h2\]contentModifier18+

contentModifier(modifier: Optional<ContentModifier<RatingConfiguration>>)

Creates a content modifier. Compared with [contentModifier](#contentmodifier12), this API supports the **undefined** type for the **modifier** parameter.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| modifier | [Optional](../../universal-attributes/modifiers-and-custom-property/custom-property/document.md#optionalt)<[ContentModifier<RatingConfiguration>](#ratingconfiguration12)\> | Yes | 
Content modifier to apply to the current component.

**modifier**: content modifier. You need a custom class to implement the **ContentModifier** API.

If **modifier** is set to **undefined**, no content modifier is used.

 |

#### Events

#### \[h2\]onChange

onChange(callback:(value: number) => void)

Triggered when the rating value changes.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | number | Yes | Rating value. |

#### \[h2\]onChange18+

onChange(callback:Optional<OnRatingChangeCallback>)

Triggered when the rating value changes. Compared with [onChange](#onchange), this API supports the **undefined** type for the **callback** parameter.

**Widget capability**: This API can be used in ArkTS widgets since API version 18.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | [Optional](../../universal-attributes/modifiers-and-custom-property/custom-property/document.md#optionalt)<[OnRatingChangeCallback](#onratingchangecallback18)\> | Yes | 
Defines the callback triggered when the rating value changes.

If **callback** is set to **undefined**, the callback function is not used.

 |

#### OnRatingChangeCallback18+

type OnRatingChangeCallback = (rating: number) => void

Defines the callback triggered when the rating value changes.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| rating | number | Yes | Rating value. |

#### Sequential Keyboard Navigation Specifications

| Key | Description |
| :-- | :-- |
| Tab | Switch the focus between components. |
| Left and right arrow keys | Increase or decrease the rating on preview at the specified step, without changing the actual rating. |
| Home | Move the focus to the first star, without changing the actual rating. |
| End | Move the focus to the last star, without changing the actual rating. |
| Space/Enter | Submit the rating result based on the current rating. |

#### RatingConfiguration12+

You need a custom class to implement the **ContentModifier** API. Inherits from [CommonConfiguration](../../universal-attributes/modifiers-and-custom-property/content-modifier/document.md#commonconfigurationt).

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| rating | number | No | No | 
Value to rate.

Default value: **0**

Value range: \[0, stars\]

Values less than 0 are treated as **0**, and values greater than the value of [stars](#stars) are treated as the value of **stars**.

This parameter supports two-way binding through [$$](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-two-way-sync).

This parameter supports two-way binding through [!!](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-new-binding#two-way-binding-between-built-in-component-parameters).

 |
| indicator | boolean | No | No | 

Whether the rating bar is used as an indicator. **true**: used as an indicator. **false**: not used as an indicator.

Default value: **false**

 |
| stars | number | No | No | 

Total number of ratings.

Default value: **5**

 |
| stepSize | number | No | No | 

Step of an operation.

Default value: **0.5**

 |
| triggerChange | Callback<number> | No | No | Callback triggered when the rating value changes. |

#### RatingOptions18+

Provides configuration options for the **Rating** component.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f1/v3/87_ebryCS6KZfElovyXpTw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062241Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7D10C098174564A5B4A0D80917F81C508982D4C3816483352D60E4BFE902995B)

To standardize anonymous object definitions, the element definitions here have been revised in API version 18. While historical version information is preserved for anonymous objects, there may be cases where the outer element's @since version number is higher than inner elements'. This does not affect interface usability.

**Widget capability**: This API can be used in ArkTS widgets since API version 18.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| rating7+ | number | No | No | 
Value to rate.

Default value: **0**

Value range: \[0, stars\]

Values less than 0 are treated as **0**, and values greater than the value of [stars](#stars) are treated as the value of **stars**.

This parameter supports two-way binding through [$$](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-two-way-sync).

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| indicator7+ | boolean | No | Yes | 

Whether the component is used as an indicator. If this parameter is set to **true**, the rating value cannot be changed.

Default value: **false**

**NOTE**

When **indicator** is set to **true**, the default component height is 12.0 vp, and the component width is calculated as follows: Height x Value of **stars**.

When **indicator** is set to **false**, the default component height is 28.0 vp, and the component width is calculated as follows: Height x Value of **stars**.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |

#### StarStyleOptions18+

Provides style settings for the selected, unselected, and partially selected stars in the **Rating** component.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/66/v3/bVevNnkUQIKU5NRuwX0apw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062241Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9B9AB618B13C87A52A4617993E777C87D562DE6A32241307C5BC0334C13890D1)

To standardize anonymous object definitions, the element definitions here have been revised in API version 18. While historical version information is preserved for anonymous objects, there may be cases where the outer element's @since version number is higher than inner elements'. This does not affect interface usability.

**Widget capability**: This API can be used in ArkTS widgets since API version 18.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| backgroundUri7+ | [ResourceStr](../../common-definitions/basic-types/document.md#resourcestr) | No | No | 
Image path for the unselected star. You can use the default system image or a custom image.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

Resource configuration is supported since API version 20. For details, see [Example 3: Setting the Rating Style Through Resource Configuration](#example-3-setting-the-rating-style-through-resource-configuration).

 |
| foregroundUri7+ | [ResourceStr](../../common-definitions/basic-types/document.md#resourcestr) | No | No | 

Image path for the selected star. You can use the default system image or a custom image.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

Resource configuration is supported since API version 20. For details, see [Example 3: Setting the Rating Style Through Resource Configuration](#example-3-setting-the-rating-style-through-resource-configuration).

 |
| secondaryUri7+ | [ResourceStr](../../common-definitions/basic-types/document.md#resourcestr) | No | Yes | 

Image path for the partially selected star. You can use the default system image or a custom image.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

Resource configuration is supported since API version 20. For details, see [Example 3: Setting the Rating Style Through Resource Configuration](#example-3-setting-the-rating-style-through-resource-configuration).

 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7a/v3/gq6wdUhmRZmvpO0MXcOHYA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062241Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E886DB4092672A2082F4B252F96D69A941AB518C18743D5F0948BCDD41613B5E)

The string type can be used to load network images and local images. When a relative path is used to reference a local image, for example, **Image("common/test.jpg")**, the **common** directory must be placed at the same level as the **pages** directory. Base64-encoded strings are also supported.

#### Example

## Example 1: Setting the Default Rating Style

This example shows how to create a **Rating** component with the default star style.

// xxx.ets
@Entry
@Component
struct RatingExample {
  @State rating: number = 3.5;

  build() {
    Column() {
      Column() {
        Rating({ rating: this.rating, indicator: false })
          .stars(5)
          .stepSize(0.5)
          .margin({ top: 24 })
          .onChange((value: number) => {
            this.rating = value;
          })
        Text('current score is ' + this.rating)
          .fontSize(16)
          .fontColor('rgba(24,36,49,0.60)')
          .margin({ top: 16 })
      }.width(360).height(113).backgroundColor('#FFFFFF').margin({ top: 68 })

      Row() {
        Image('common/testImage.jpg')
          .width(40)
          .height(40)
          .borderRadius(20)
          .margin({ left: 24 })
        Column() {
          Text('Yue')
            .fontSize(16)
            .fontColor('#182431')
            .fontWeight(500)
          Row() {
            Rating({ rating: 3.5, indicator: false }).margin({ top: 1, right: 8 })
            Text('2021/06/02')
              .fontSize(10)
              .fontColor('#182431')
          }
        }.margin({ left: 12 }).alignItems(HorizontalAlign.Start)

        Text('1st Floor')
          .fontSize(10)
          .fontColor('#182431')
          .position({ x: 295, y: 8 })
      }.width(360).height(56).backgroundColor('#FFFFFF').margin({ top: 64 })
    }.width('100%').height('100%').backgroundColor('#F1F3F5')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ac/v3/oR3WTlNnT4yfcrJb9MpHTA/en-us_image_0000002537765620.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062241Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4B8E245365D69533FAB34AF339833F4C67C89A7F7E58A1D7E3DBF9A20DA435DF)

## Example 2: Implementing a Custom Rating Bar

This example implements a custom rating bar, with each circle representing 0.5 point. When **ratingIndicator** is set to **true**, the rating bar acts as an indicator and the value cannot be changed. When **ratingIndicator** is set to **false**, the rating is interactive. **ratingStars** sets the total number of stars, and **ratingStepSize** sets the increment step.

// xxx.ets
class MyRatingStyle implements ContentModifier<RatingConfiguration> {
  name: string = "";
  style: number = 0;

  constructor(value1: string, value2: number) {
    this.name = value1;
    this.style = value2;
  }

  applyContent(): WrappedBuilder<\[RatingConfiguration\]> {
    return wrapBuilder(buildRating);
  }
}

@Builder
function buildRating(config: RatingConfiguration) {
  Column() {
    Row() {
      Circle({ width: 25, height: 25 })
        .fill(config.rating >= 0.4 ? Color.Black : Color.Red)
        .onClick((event: ClickEvent) => {
          if (!config.indicator) {
            if (config.stepSize === 0.5) {
              config.triggerChange(0.5);
              return
            }
            if (config.stepSize === 1.0) {
              config.triggerChange(1);
              return
            }
          }
        }).visibility(config.stars >= 1 ? Visibility.Visible : Visibility.Hidden)
      Circle({ width: 25, height: 25 })
        .fill(config.rating >= 0.9 ? Color.Black : Color.Red)
        .onClick((event: ClickEvent) => {
          if (!config.indicator) {
            config.triggerChange(1);
          }
        }).visibility(config.stars >= 1 ? Visibility.Visible : Visibility.Hidden)
      Circle({ width: 25, height: 25 })
        .fill(config.rating >= 1.4 ? Color.Black : Color.Red)
        .onClick((event: ClickEvent) => {
          if (!config.indicator) {
            if (config.stepSize === 0.5) {
              config.triggerChange(1.5);
              return
            }
            if (config.stepSize === 1.0) {
              config.triggerChange(2);
              return
            }
          }
        }).visibility(config.stars >= 2 ? Visibility.Visible : Visibility.Hidden).margin({ left: 10 })
      Circle({ width: 25, height: 25 })
        .fill(config.rating >= 1.9 ? Color.Black : Color.Red)
        .onClick((event: ClickEvent) => {
          if (!config.indicator) {
            config.triggerChange(2);
          }
        }).visibility(config.stars >= 2 ? Visibility.Visible : Visibility.Hidden)
      Circle({ width: 25, height: 25 })
        .fill(config.rating >= 2.4 ? Color.Black : Color.Red)
        .onClick((event: ClickEvent) => {
          if (!config.indicator) {
            if (config.stepSize === 0.5) {
              config.triggerChange(2.5);
              return
            }
            if (config.stepSize === 1.0) {
              config.triggerChange(3);
              return
            }
          }
        }).visibility(config.stars >= 3 ? Visibility.Visible : Visibility.Hidden).margin({ left: 10 })
      Circle({ width: 25, height: 25 })
        .fill(config.rating >= 2.9 ? Color.Black : Color.Red)
        .onClick((event: ClickEvent) => {
          if (!config.indicator) {
            config.triggerChange(3);
          }
        }).visibility(config.stars >= 3 ? Visibility.Visible : Visibility.Hidden)
      Circle({ width: 25, height: 25 })
        .fill(config.rating >= 3.4 ? Color.Black : Color.Red)
        .onClick((event: ClickEvent) => {
          if (!config.indicator) {
            if (config.stepSize === 0.5) {
              config.triggerChange(3.5);
              return
            }
            if (config.stepSize === 1.0) {
              config.triggerChange(4);
              return
            }
          }
        }).visibility(config.stars >= 4 ? Visibility.Visible : Visibility.Hidden).margin({ left: 10 })
      Circle({ width: 25, height: 25 })
        .fill(config.rating >= 3.9 ? Color.Black : Color.Red)
        .onClick((event: ClickEvent) => {
          if (!config.indicator) {
            config.triggerChange(4);
          }
        }).visibility(config.stars >= 4 ? Visibility.Visible : Visibility.Hidden)
      Circle({ width: 25, height: 25 })
        .fill(config.rating >= 4.4 ? Color.Black : Color.Red)
        .onClick((event: ClickEvent) => {
          if (!config.indicator) {
            if (config.stepSize === 0.5) {
              config.triggerChange(4.5);
              return
            }
            if (config.stepSize === 1.0) {
              config.triggerChange(5);
              return
            }
          }
        }).visibility(config.stars >= 5 ? Visibility.Visible : Visibility.Hidden).margin({ left: 10 })
      Circle({ width: 25, height: 25 })
        .fill(config.rating >= 4.9 ? Color.Black : Color.Red)
        .onClick((event: ClickEvent) => {
          if (!config.indicator) {
            config.triggerChange(5);
          }
        }).visibility(config.stars >= 5 ? Visibility.Visible : Visibility.Hidden)
    }

    Text("Rating: "+ config.rating)
  }
}

@Entry
@Component
struct ratingExample {
  @State rating: number = 0;
  @State ratingIndicator: boolean = true;
  @State ratingStars: number = 0;
  @State ratingStepSize: number = 0.5;
  @State ratingEnabled: boolean = true;

  build() {
    Row() {
      Column() {
        Rating({
          rating: 0,
          indicator: this.ratingIndicator
        })
          .stepSize(this.ratingStepSize)
          .stars(this.ratingStars)
          .backgroundColor(Color.Transparent)
          .width('100%')
          .height(50)
          .onChange((value: number) => {
            console.info('Rating change is' + value);
            this.rating = value;
          })
          .contentModifier(new MyRatingStyle("hello", 3))
        Button(this.ratingIndicator ? "ratingIndicator : true" : "ratingIndicator : false")
          .onClick((event) => {
            if (this.ratingIndicator) {
              this.ratingIndicator = false;
            } else {
              this.ratingIndicator = true;
            }
          }).margin({ top: 5 })

        Button(this.ratingStars < 5 ? "ratingStars + 1, ratingStars =" + this.ratingStars : "Maximum value of ratingStars: 5")
          .onClick((event) => {
            if (this.ratingStars < 5) {
              this.ratingStars += 1;
            }
          }).margin({ top: 5 })

        Button(this.ratingStars > 0 ? "ratingStars - 1, ratingStars =" + this.ratingStars :
          "ratingStars: Values less than or equal to 0 are treated as 5")
          .onClick((event) => {
            if (this.ratingStars > 0) {
              this.ratingStars -= 1;
            }
          }).margin({ top: 5 })

        Button(this.ratingStepSize == 0.5 ? "ratingStepSize : 0.5" : "ratingStepSize : 1")
          .onClick((event) => {
            if (this.ratingStepSize == 0.5) {
              this.ratingStepSize = 1;
            } else {
              this.ratingStepSize = 0.5;
            }
          }).margin({ top: 5 })
      }
      .width('100%')
      .height('100%')
      .justifyContent(FlexAlign.Center)
    }
    .height('100%')
  }
}

## Example 3: Setting the Rating Style Through Resource Configuration

This example demonstrates how to set **starStyle** through resource configuration to customize the star image link. This method is recommended for setting the style since API version 20.

// xxx.ets
@Entry
@Component
struct RatingExample {
  @State rating: number = 3.5;

  build() {
    Column() {
      Rating({ rating: this.rating, indicator: false })
        .stars(5)
        .stepSize(0.5)
        .starStyle({
          // Replace $r('app.media.xxx') with the image resource file you use.
          backgroundUri: $r('app.media.imag1'),
          foregroundUri: $r('app.media.imag2'),
          secondaryUri: $r('app.media.imag3')
        })
        .margin({ top: 24 })
        .onChange((value: number) => {
          this.rating = value;
        })
      Text('current score is ' + this.rating)
        .fontSize(16)
        .fontColor('rgba(24,36,49,0.60)')
        .margin({ top: 16 })
    }.width('100%').height('100%').backgroundColor('#F1F3F5')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e4/v3/dsxRiuf8RdeatJvMpnI0tQ/en-us_image_0000002537925560.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062241Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=65678804DBB2D98FD5056B10DC7C4619F3696BB92260B2EE363A257A4B7F831E)

## Example 4: Customizing the Rating Style

This example shows how to customize the star images by configuring **starStyle**.

**Note**

The resources used in this example are not located in the **src** > **main** > **resource** directory. Starting from DevEco Studio 6.0.0 Beta2, the resources that are located outside the **resources** directory are not packaged by default when a project or module is created. To package these resources, go to **buildOptions** in the module's **build-profile.json5** file > **resOptions** > **copyCodeResource**, and set **enable** to **true**. For details, see the description of [resOptions](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/ide-hvigor-build-profile#table1476161719356).

// xxx.ets
@Entry
@Component
struct RatingExample {
  @State rating: number = 3.5;

  build() {
    Column() {
      Rating({ rating: this.rating, indicator: false })
        .stars(5)
        .stepSize(0.5)
        .starStyle({
          backgroundUri: '/common/image1.png', // The common directory is at the same level as the pages directory.
          foregroundUri: '/common/image2.png',
          secondaryUri: '/common/image3.png'
        })
        .margin({ top: 24 })
        .onChange((value: number) => {
          this.rating = value;
        })
      Text('current score is ' + this.rating)
        .fontSize(16)
        .fontColor('rgba(24,36,49,0.60)')
        .margin({ top: 16 })
    }.width('100%').height('100%').backgroundColor('#F1F3F5')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f9/v3/P-dpqa_9Q8qviKp9nOlb9Q/en-us_image_0000002537925560.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062241Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=10F8DFB365F44B9745C3F0BEC027800A6127291DDF67214B5959E011D32C4491)
