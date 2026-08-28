# StepperItem

The **StepperItem** component represents a page component used within a [Stepper](../stepper/document.md) container.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2b/v3/yXoj1mH8TEmvYwvX-gmT-w/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062253Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=EF3F7411E6028E11A7CB7FB4F94202CCD2E24627462AAA6F1CE7D620B626F40A)

This component is deprecated since API version 22. You are advised to use [Swiper](../../scroll-and-swipe/swiper/document.md) instead.

This component is supported since API version 8. Updates will be marked with a superscript to indicate their earliest API version.

#### Child Components

This component supports only one child component.

#### APIs

StepperItem()

Creates a page component for the [Stepper](../stepper/document.md) container.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b4/v3/2RGZk5mUQNidfbGQVGCnbw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062253Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=648A1D0BC53AD3E8315BED76599513F6D782952C102AF82863B84A7308CD0A56)

This API is supported since API version 8 and deprecated since API version 22. You are advised to use [Swiper](../../scroll-and-swipe/swiper/document.md#attributes) instead.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

#### Attributes

#### \[h2\]prevLabel(deprecated)

prevLabel(value: string)

Sets the text label of the button on the left, which is not displayed on the first page. When the **Stepper** contains more than one page, the default value for all pages except the first page is **Back**.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/80/v3/AY_mRRG2SQimVoFbLr2QnA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062253Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=67137B74CAE2416747F61997B6A84DB1E6D5649ED887ADF39C199EECED8C2FF6)

This API is supported since API version 8 and deprecated since API version 22. You are advised to use [showPrevious](../../scroll-and-swipe/swiper/document.md#showprevious) instead.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | string | Yes | Text label of the button on the left. When the string is too long, it is scaled down, wrapped in two lines, and then clipped. |

#### \[h2\]nextLabel(deprecated)

nextLabel(value: string)

Sets the text label of the button on the right. The default value is **Start** for the last page and **Next** for the other pages.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ea/v3/-P3T3YhORvirtBFtmnky0Q/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062253Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5595F716E5F01F3843D19CC0CF05D6D245FDBD72FBEE3EAE021798304716B2D4)

This API is supported since API version 8 and deprecated since API version 22. You are advised to use [showNext](../../scroll-and-swipe/swiper/document.md#shownext) instead.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | string | Yes | Text label of the button on the right. When the string is too long, it is scaled down, wrapped in two lines, and then clipped. |

#### \[h2\]status(deprecated)

status(value?: ItemState)

Sets the display status of **nextLabel** in the stepper.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0a/v3/X-uuJGoVQhS3gVpeKGmOOg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062253Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=51C3589740971E02AE449BEF3DD1ADA0088C911C66EA672C3C24E88B4F5CD36F)

This API is supported since API version 8 and deprecated since API version 22. You are advised to use [indicatorInteractive](../../scroll-and-swipe/swiper/document.md#indicatorinteractive12) instead.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [ItemState](#itemstate) | No | 
Display status of **nextLabel** in the stepper.

Default value: **ItemState.Normal**

 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/80/v3/eIUeuaKETQmMP-c_eeynFA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062253Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=804F484B824B1A7DEFE4D3250E5C9CD621B7C7499BA766485D2EF857B4F4E297)

-   The **StepperItem** component does not support setting of the universal width attribute. By default, its width is the same as that of the parent **Stepper** component.
-   The **StepperItem** component does not support setting of the universal height attribute. Its height is the height of the parent **Stepper** component minus the height of the label button.
-   The **StepperItem** component does not support setting dimension-affecting attributes such as [aspectRatio](../../universal-attributes/layout-and-borders/layout-constraints/document.md#aspectratio) or [constraintSize](../../universal-attributes/layout-and-borders/sizing/document.md#constraintsize).

#### ItemState

Display status of **nextLabel** in the stepper.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Value | Description |
| :-- | :-- | :-- |
| Normal | 0 | 
The button on the right is clickable and can navigate users to the next **StepperItem** when it is clicked.

**NOTE**

This API is supported since API version 8 and deprecated since API version 22. You are advised to use [index](../../scroll-and-swipe/swiper/document.md#index) instead.

 |
| Disabled | 1 | 

The button on the right is disabled.

**NOTE**

This API is supported since API version 8 and deprecated since API version 22. You are advised to use [indicatorInteractive](../../scroll-and-swipe/swiper/document.md#indicatorinteractive12) instead.

 |
| Waiting | 2 | 

The button on the right is not displayed, and a progress bar is displayed instead.

**NOTE**

This API is supported since API version 8 and deprecated since API version 22. You are advised to use [Swiper](../../scroll-and-swipe/swiper/document.md) instead.

 |
| Skip | 3 | 

The button on the right reads "Skip" by default. You can define the processing logic for this state in the **onSkip** callback of the stepper.

**NOTE**

This API is supported since API version 8 and deprecated since API version 22. You are advised to use [index](../../scroll-and-swipe/swiper/document.md#index) instead.

 |

#### Example

See [Stepper](../stepper/document.md).
