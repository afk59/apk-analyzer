# Swiper

The **Swiper** component is able to display child components in a carousel-like manner.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9b/v3/72glngSxQ5S14jRKskDX1Q/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062239Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B4CC303FA1656A5FCF1C1D30E303E53599D9B570CFFE84D4DAAC1DB5CF929DF5)

-   This component is supported since API version 7. Updates will be marked with a superscript to indicate their earliest API version.
    
-   The **Swiper** component implements the scrolling carousel effect through the built-in [PanGesture](../../gesture-handling/basic-gestures/pangesture/document.md) gesture. When the [disableSwipe](#disableswipe8) attribute is set to **true**, the gesture listening is disabled, thereby preventing the scrolling operation.
    
-   When [NodeContainer](../../custom-placeholder-components/nodecontainer/document.md) is reused in the **Swiper** component, recursive updates of parent component state variables by child nodes are prohibited.
    

#### Child Components

Supported

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/aa/v3/EcWvos0RSt61RgvhlcDGGQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062239Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=14965F70AA01C05648763FF9BC5E6ECAEB35FD5ADD7F28B35B8FAA813D6D2559)

-   Allowed child component types: built-in and custom components, including rendering control types ([if/else](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-rendering-control-ifelse), [ForEach](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-rendering-control-foreach), [LazyForEach](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-rendering-control-lazyforeach), and [Repeat](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-new-rendering-control-repeat)). To maximize the benefits of lazy loading, avoid mixing lazy loading components (including **LazyForEach** and **Repeat**) and non-lazy loading components, and exercise caution when using multiple lazy loading components. Avoid modifying the data source while an animation is in progress, as doing so can lead to layout issues.
    
-   If a child component has its [visibility](../../universal-attributes/basic-attributes/visibility-control/document.md#visibility) attribute set to **Visibility.None** and the **Swiper** component has its **displayCount** attribute set to **'auto'**, the child component does not take up space in the viewport, but does not affect the number of navigation points. If a child component has its **visibility** attribute set to **Visibility.None** or **Visibility.Hidden**, it takes up space in the viewport, but is not displayed.
    
-   Child components of the **Swiper** component are drawn based on their level if they have the [offset](../../universal-attributes/layout-and-borders/location/document.md#offset) attribute set. A child component with a higher level overwrites one with a lower level. For example, if the **Swiper** contains three child components and **offset({ x: 100 })** is set for the third child component, the third child component overwrites the first child component during horizontal loop playback. To prevent the first child component from being overwritten, set its [zIndex](../../universal-attributes/basic-attributes/z-order-control/document.md#zindex) attribute to a value greater than that of the third child component.
    
-   When focus is moved to a custom child node, navigation indicators and arrows may be obscured by [focus styles](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-common-events-focus-event#focus-style) modifications that change **zIndex**.
    
-   For a **Swiper** component with many child components, you can optimize the performance and reduce memory consumption by using lazy loading, data caching, preloading, and component reuse techniques. For best practices, see [Optimizing Frame Loss During Swiper Component Loading](https://developer.huawei.com/consumer/en/doc/best-practices/bpta-swiper_high_performance_development_guide).
    

#### APIs

Swiper(controller?: SwiperController)

Creates a **Swiper** component.

**Widget capability**: This API can be used in ArkTS widgets since API version 10.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| controller | [SwiperController](#swipercontroller) | No | Controller to bind to the component to manage page switching and preload specific child components. |

#### Attributes

In addition to the [universal attributes](../../universal-attributes/document.md), the following attributes are supported.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fd/v3/0UyRYoEuStWrO-CbMDFsEA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062239Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=75EEAE46452AE6ABB3361A8F21F6ADDF250902A914312F1593823AA304300695)

The default value of the universal attribute [clip](../../universal-attributes/visual-effects/shape-clipping/document.md#clip12) is **true** for the **Swiper** component.

#### \[h2\]index

index(value: number)

Sets the index of the child component currently displayed in the container.

Since API version 10, this attribute supports two-way binding through [$$](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-two-way-sync).

**Widget capability**: This API can be used in ArkTS widgets since API version 10.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | number | Yes | 
Index of the child component currently displayed in the container.

Default value: **0**

**NOTE**

If the value specified is less than 0 or greater than the maximum page index, the value **0** is used.

 |

#### \[h2\]autoPlay

autoPlay(value: boolean)

Sets whether to enable automatic playback for child components, with the direction from the smallest to largest index.

If [loop](#loop) is set to **false**, the automatic playback stops at the last page and resumes after navigated away from the last page using gestures. If the **Swiper** component becomes invisible, the playback stops.

**Widget capability**: This API can be used in ArkTS widgets since API version 10.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | boolean | Yes | 
Whether to enable automatic playback for child components.

**true**: yes; **false**: no

If an invalid value is passed, the value **false** is used.

 |

#### \[h2\]autoPlay18+

autoPlay(autoPlay: boolean, options: AutoPlayOptions)

Sets whether to enable automatic playback for child components, with **options** controlling whether child components stop automatic playback when the screen is pressed by fingers, a mouse device, or other input devices.

If [loop](#loop) is set to **false**, automatic playback stops at the last page and resumes after navigated away from the last page using gestures. Automatic playback also stops when the **Swiper** component is not visible.

**Widget capability**: This API can be used in ArkTS widgets since API version 18.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| autoPlay | boolean | Yes | 
Whether to enable automatic playback for child components.

**true**: yes; **false**: no

If an invalid value is passed, the value **false** is used.

 |
| options | [AutoPlayOptions](#autoplayoptions18) | Yes | 

Whether child components stop automatic playback when the screen is pressed by fingers, a mouse device, or other input devices. If **stopWhenTouched** is set to **true**, automatic playback resumes after any finger lifts in multi-touch scenarios.

Default value: **{ stopWhenTouched: true }**.

 |

#### \[h2\]indicator

indicator(value: DotIndicator | DigitIndicator | boolean)

Sets the style of the navigation indicator.

**Widget capability**: This API can be used in ArkTS widgets since API version 10.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [DotIndicator](#dotindicator10)10+ | [DigitIndicator](#digitindicator10)10+ | boolean | Yes | 
Style of the navigation indicator.

\- **DotIndicator**: dot-style indicator.

\- **DigitIndicator**: digit-style indicator.

\- **boolean**: whether to enable the navigation indicator. **true** to enable, **false** otherwise.

Default value: **true**

Default style: **DotIndicator**

 |

#### \[h2\]indicator15+

indicator(indicator: IndicatorComponentController | DotIndicator | DigitIndicator | boolean)

Sets the navigation indicator for the component.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/39/v3/QrLDS3EaRseTz2T_CeRXxA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062239Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E0574FA6B218A3659EDA86A85450FA41B4F7BB7281D180FA8BD32DD332FB028F)

An externally bound navigation indicator component can be used together if it is set. The display position and size can be customized for the external navigation indicator. For details, see [Indicator](../../navigation-and-switching/indicator/document.md).

**Widget capability**: This API can be used in ArkTS widgets since API version 15.

**Atomic service API**: This API can be used in atomic services since API version 15.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| indicator | [IndicatorComponentController](../../navigation-and-switching/indicator/document.md#indicatorcomponentcontroller)15+ | [DotIndicator](#dotindicator10) | [DigitIndicator](#digitindicator10) | boolean | Yes | 
Style of the navigation indicator.

\- **IndicatorComponentController**: separate navigation indicator controller. This controller can be bound to an external navigation indicator, but the external and internal indicators cannot coexist.

\- **DotIndicator**: dot-style indicator.

\- **DigitIndicator**: digit-style indicator.

\- **boolean**: whether to enable the navigation indicator. **true** to enable, **false** otherwise.

Default value: **true**

Default style: **DotIndicator**

 |

#### \[h2\]nestedScroll11+

nestedScroll(value: SwiperNestedScrollMode)

Sets the nested scrolling mode of the **Swiper** component and its parent container. When [loop](#loop) is set to **true**, the **Swiper** component has no edge effect and does not trigger nested scrolling of its parent container.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/69/v3/KjFer802QVKG_tceWEa2kw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062239Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=21EE9E46473412FCEE02B2B496A5EFFA15A47E233B93360AA3C5621A97F77AD0)

The **Swiper** component's flick animation logic differs from other scrollable components, as **Swiper** can only slide one page at a time and performs a page-flip animation during a flick. When a **Swiper** component is nested with other scrollable components, it will not accept the scroll offset values transmitted by its child nodes after its page-turning animation has already started. At this point, the page-turning animation of the **Swiper** and the edge effect animation of the child node will be executed simultaneously.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [SwiperNestedScrollMode](#swipernestedscrollmode11) | Yes | 
Nested scrolling mode of the **Swiper** component and its parent container.

If an invalid value is passed, the value **SwiperNestedScrollMode.SELF\_ONLY** is used.

 |

#### \[h2\]loop

loop(value: boolean)

Sets whether to enable loop playback. In **LazyForEach** mode, it is recommended that the number of loaded components be greater than 5.

**Widget capability**: This API can be used in ArkTS widgets since API version 10.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | boolean | Yes | 
Whether to enable loop playback.

**true**: yes; **false**: no

If the input parameter is invalid, the value **true** is used.

 |

#### \[h2\]effectMode8+

effectMode(value: EdgeEffect)

Edge sliding effect. This parameter takes effect only when [loop](#loop) is set to **false** or all child nodes are displayed on one screen in the **Swiper** viewport. When the [SwiperController.changeIndex()](#changeindex12), [SwiperController.showNext()](#shownext), or [SwiperController.showPrevious()](#showprevious) API is called to go to the first or last page, the rebound effect does not take effect.

**Widget capability**: This API can be used in ArkTS widgets since API version 10.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [EdgeEffect](../../common-definitions/enums/document.md#edgeeffect) | Yes | 
Effect used when the component is at one of the edges.

Default value: **EdgeEffect.Spring**

 |

#### \[h2\]interval

interval(value: number)

Sets the interval for automatic playback.

**Widget capability**: This API can be used in ArkTS widgets since API version 10.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | number | Yes | 
Interval for automatic playback. If the value is smaller than the value of [duration](#duration), the next carousel starts immediately after page switching completes.

Default value: **3000**.

Unit: ms

Value range: \[0, +∞). If a value less than 0 is set, the default value is used.

 |

#### \[h2\]duration

duration(value: number)

Sets the duration of the animation for child component switching.

**duration** must be used in conjunction with [curve](#curve8).

The default curve for the animation is [interpolatingSpring](../../../arkts-api/ui/ohos-curves-interpolation-calculation/document.md#curvesinterpolatingspring10). When this curve is applied, the duration of the animation is determined solely by the parameters of the curve itself and is no longer governed by the **duration** setting. For curves that are not governed by the **duration** setting, see [Interpolation Calculation](../../../arkts-api/ui/ohos-curves-interpolation-calculation/document.md). Among others, [springMotion](../../../arkts-api/ui/ohos-curves-interpolation-calculation/document.md#curvesspringmotion9), [responsiveSpringMotion](../../../arkts-api/ui/ohos-curves-interpolation-calculation/document.md#curvesresponsivespringmotion9), and interpolatingSpring do not respect the **duration** setting. To have the animation duration managed by **duration**, you should select a different curve for the **curve** attribute.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | number | Yes | 
Duration of the autoplay for child component switching.

Default value: **400**

Unit: ms

Value range: \[0, +∞). If a value less than 0 is set, the default value is used.

 |

#### \[h2\]curve8+

curve(value: Curve | string | ICurve)

Sets the animation curve. The interpolating spring curve is used by default. For details about common curves, see [Curve](../../common-definitions/enums/document.md#curve). You can also create custom curves (interpolation curve objects) by using the API provided by the [interpolation calculation](../../../arkts-api/ui/ohos-curves-interpolation-calculation/document.md) module.

**Widget capability**: This API can be used in ArkTS widgets since API version 10.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [Curve](../../common-definitions/enums/document.md#curve) | string | [ICurve](../../../arkts-api/ui/ohos-curves-interpolation-calculation/document.md#icurve9) | Yes | 
Animation curve.

The **string** type is deprecated since API version 9 (see [curves.init](../../../arkts-api/ui/ohos-curves-interpolation-calculation/document.md#curvesinitdeprecated), [curves.steps](../../../arkts-api/ui/ohos-curves-interpolation-calculation/document.md#curvesstepsdeprecated), [curves.cubicBezier](../../../arkts-api/ui/ohos-curves-interpolation-calculation/document.md#curvescubicbezierdeprecated), and [curves.spring](../../../arkts-api/ui/ohos-curves-interpolation-calculation/document.md#curvesspringdeprecated)). Use **Curve** or **ICurve** instead.

Default value: **[interpolatingSpring](../../../arkts-api/ui/ohos-curves-interpolation-calculation/document.md#curvesinterpolatingspring10)(-1, 1, 328, 34)**.

 |

#### \[h2\]vertical

vertical(value: boolean)

Sets whether vertical swiping is used.

**Widget capability**: This API can be used in ArkTS widgets since API version 10.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | boolean | Yes | 
Whether vertical swiping is used. The value **true** means vertical swiping, and **false** means horizontal swiping.

Default value: **false**.

 |

#### \[h2\]itemSpace

itemSpace(value: number | string)

Sets the space between child components. Percentage values are not supported.

If the type is number, the default unit is vp. If the type is string, the pixel unit must be explicitly specified, for example, **'10px'**; if the unit is not specified, for example, **'10'**, the default unit vp is used.

**Widget capability**: This API can be used in ArkTS widgets since API version 10.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | number | string | Yes | 
Space between child components.

Default value: **0**

Value range: \[0, +∞). Values less than 0 or exceeding the **Swiper** component width are treated as the default value.

 |

#### \[h2\]cachedCount8+

cachedCount(value: number)

Sets the number of child components to be preloaded (cached), which are needed for the specific number of pages immediately before and after the current page. If a preceding item is deleted, the succeeding items will shift forward. For example, if **cachedCount** is set to **1**, the child components on the previous page and the next page are cached. If **swipeByGroup** in **displayCount** is set to **true**, child components are cached by group. For example, if **cachedCount** is set to **1** and **swipeByGroup** is set to **true**, the child components in the previous and next groups are cached.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/84/v3/fB5b_6HYTQeyrby7BJEaQA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062239Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=66FF23B110558A473C43200F08B3BE3EE80CF747052C3C7AEC86697B1DDBFFF9)

-   In continuous scrolling scenarios where one **Swiper** child component is displayed per screen, setting **cachedCount** to **1** or **2** is typically sufficient. For best practices, see [Optimizing Frame Loss During Swiper Component Loading – Caching Data Items](https://developer.huawei.com/consumer/en/doc/best-practices/bpta-swiper_high_performance_development_guide#section143504547145).
    
-   This parameter takes effect only when used with [LazyForEach](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-rendering-control-lazyforeach) or the [Repeat](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-new-rendering-control-repeat) component that has virtualScroll enabled. Child components outside the visible area and cache range will be released after this parameter takes effect.
    

**Widget capability**: This API can be used in ArkTS widgets since API version 10.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | number | Yes | 
Number of child components to be preloaded (cached).

Default value: **1**

Value range: \[0, +∞). If a value less than 0 is set, the default value is used.

 |

#### \[h2\]cachedCount15+

cachedCount(count: number, isShown: boolean)

Sets the number of child components to be cached.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/93/v3/haXHe3g2TZq0Nnc52LHAzA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062239Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=DF58C7B54525A0DB7DAC9445DD2BB9E8648C9FE0B4425E6DCC70BE64DF01B0B3)

-   When the value of **isShown** is **true** and the value of **count** is too large, if there are insufficient loadable nodes within the preload range, the same loadable node will only be laid out on one side in loop scenarios.

**Widget capability**: This API can be used in ArkTS widgets since API version 15.

**Atomic service API**: This API can be used in atomic services since API version 15.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| count | number | Yes | 
Number of child components to be preloaded (cached).

Default value: **1**

Value range: \[0, +∞). If a value less than 0 is set, the default value is used.

 |
| isShown | boolean | Yes | 

Whether the cached nodes within the range rendered without being added to the render tree.

**true**: yes; **false**: no

If an invalid value is passed, the value **false** is used.

 |

#### \[h2\]disableSwipe8+

disableSwipe(value: boolean)

Sets whether to disable the swipe feature.

**Widget capability**: This API can be used in ArkTS widgets since API version 10.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | boolean | Yes | 
Whether to disable the swipe feature. The value **true** means to disable the feature, and **false** means the opposite.

Default value: **false**.

 |

#### \[h2\]displayCount8+

displayCount(value: number | string | SwiperAutoFill, swipeByGroup?: boolean)

Sets the number of elements to display per page.

**number** type: Child elements' main-axis width adapts to the **Swiper** component's main-axis width. The child elements are stretched or shrunk to equally divide the **Swiper** component's width (minus **displayCount-1** times **itemSpace**). Values less than or equal to 0 are treated as the default value **1**.

**string** type: Only **'auto'** is supported. Child elements are laid out linearly based on their main-axis width without adapting to the **Swiper** component's width. [customContentTransition](#customcontenttransition12) and [onContentDidScroll](#oncontentdidscroll12) events are disabled.

**SwiperAutoFill** type: Child elements' main-axis width adapts to the **Swiper** component's main-axis width. The system automatically works out the number of elements per page based on the width and **minSize** settings of the **Swiper** component. If **minSize** is left empty or set to a value less than or equal to 0, the **Swiper** component displays one column.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c1/v3/xUdcv3E-Q5m6Q4S0hH-iZQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062239Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6D000E768029627CEBBB82D6D0CB21688B40552FC117FC6C6698471FB23F63BC)

-   When turning pages by group is used, the drag distance threshold for turning pages is half of the width of the **Swiper** component (50% of the child elements width if turning pages by child element is used). If the number of child elements in the last group is less than the value of **displayCount**, placeholders are used, but they show the **Swiper** background style directly and do not display any content.
    
-   When **displayCount** is set to **'auto'** and **loop** is set to **false**, the position of the selected navigation indicator aligns with the first page in the viewport. If the first page is only partially displayed in the viewport after switching, the selected navigation indicator remains aligned with the page's position, between two unselected indicators. In this case, you are advised to hide the navigation indicators.
    
-   If the navigation indicator is in dot style, the number of displayed navigation dots equals the number of child elements when the number of child elements displayed in the viewport is 1 (single-page scenario) or **displayCount** is set to **'auto'**.
    
-   If **displayCount** is set to **'auto'** and **swipeByGroup** is set to **true**, each child element will be treated as a group for page switching, allowing only one page to be switched at a time. In this case, you are advised not to set **swipeByGroup** or set **swipeByGroup** to **false**.
    
-   This API can be called within [attributeModifier](../../universal-attributes/modifiers-and-custom-property/attribute-modifier/document.md#attributemodifier) since API version 18.
    

When the navigation indicator is set to dot style and the number of child elements displayed in the viewport is greater than 1 (multi-page scenario), the number of displayed navigation dots follows the rules below.

| Total Children Count > Visible Children Count | Swiping by Group Enabled | Loop Status | Number of Navigation Dots Displayed | Description |
| :-- | :-- | :-- | :-- | :-- |
| Yes | Yes | **loop** set to **true** | Equals the number of groups (calculated by dividing the total number of child elements by the number of visible child elements, with rounding up if there is a remainder). | Not effective when **displayCount** is set to **'auto'**. |
| Yes | Yes | **loop** set to **false** | Equals the number of groups (calculated by dividing the total number of child elements by the number of visible child elements, with rounding up if there is a remainder). | Not effective when **displayCount** is set to **'auto'**. |
| Yes | No | **loop** set to **true** | Equals the actual number of page turns available (that is, the total number of child elements). | —— |
| Yes | No | **loop** set to **false** | Equals the actual number of page turns available (calculated as total number of child elements minus the number of visible child elements, plus 1). | Not effective when **displayCount** is set to **'auto'**. |
| No (while the total number of child elements is greater than 0) | —— | —— | 1 | Not effective when **displayCount** is set to **'auto'**. |
| No (while the total number of child elements is 0) | —— | —— | 0 | —— |

**Widget capability**: This API can be used in ArkTS widgets since API version 10.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | number | string | [SwiperAutoFill](#swiperautofill10)10+ | Yes | 
Number of elements to display per page.

Default value: **1**

Value range: (0, +∞). If this parameter is set to a value less than or equal to 0, the default value is used.

 |
| swipeByGroup11+ | boolean | No | 

Whether to turn pages by group. The value **true** means to turn pages by group, and **false** means to turn pages by child element. When turning pages by group is used, the number of child elements per group is the value of **displayCount**.

Default value: **false**.

 |

#### \[h2\]displayCount22+

displayCount(value: number | string | SwiperAutoFill | ItemFillPolicy, swipeByGroup?: boolean)

Sets the number of elements to display per page.

**number** type: Child elements' main-axis width adapts to the **Swiper** component's main-axis width. The child elements are stretched or shrunk to equally divide the **Swiper** component's width (minus **displayCount-1** times **itemSpace**). Values less than or equal to 0 are treated as the default value **1**.

**string** type: Only **'auto'** is supported. Child elements are laid out linearly based on their main-axis width without adapting to the **Swiper** component's width. [customContentTransition](#customcontenttransition12) and [onContentDidScroll](#oncontentdidscroll12) events are disabled.

**SwiperAutoFill** type: Child elements' main-axis width adapts to the **Swiper** component's main-axis width. The system automatically works out the number of elements per page based on the width and **minSize** settings of the **Swiper** component. If **minSize** is left empty or set to a value less than or equal to 0, the **Swiper** component displays one column.

**ItemFillPolicy** type: Child elements' main-axis width adapts to the **Swiper** component's main-axis width. The number of displayed elements is determined based on the breakpoint type corresponding to the **Swiper** component's width. For example, if the breakpoint type is set to **ItemFillPolicy.BREAKPOINT\_DEFAULT**, one column is displayed when the component width falls within the sm or smaller breakpoint range, two columns are displayed for the md breakpoint range, and three columns are displayed for the lg or a larger breakpoint range.

For details about the parameter, see [displayCount](#displaycount8).

**Widget capability**: This API can be used in ArkTS widgets since API version 22.

**Atomic service API**: This API can be used in atomic services since API version 22.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | number | string | [SwiperAutoFill](#swiperautofill10) | [ItemFillPolicy](../../common-definitions/basic-types/document.md#itemfillpolicy22) | Yes | 
Number of elements to display per page.

The value range is (0, +∞). If the value is less than or equal to 0, the value **1** is used.

 |
| swipeByGroup | boolean | No | 

Whether to turn pages by group. The value **true** means to turn pages by group, and **false** means to turn pages by child element. When turning pages by group is used, the number of child elements per group is the value of **displayCount**.

Default value: **false**.

 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4f/v3/mrMGLyvnS6Gv78UctypwsQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062239Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=16E92C1C6D1C64EE154888E27D5EDEEF0060686AF387310252B12F63B1D622B1)

When the number of **Swiper**'s child components is less than or equal to the total number of nodes displayed in the content area of the **Swiper** component (totalDisplayCount = DisplayCount + prevMargin?(1 : 0) + nextMargin? (1 : 0)), the **Swiper** component generally uses the non-looping mode for layout. In this case, the child components specified by **nextMargin** and **prevMargin** take up space in the viewport, but are not displayed. The specifications of the **Swiper** component are calculated based on the value of **totalDisplayCount**. The exceptions are as follows:

-   When the number of child components is equal to the total number of allowed nodes in the content area and both **prevMargin** and **nextMargin** take effect, set **loop** to **true** to enable loop playback.
    
-   When the number of child components is equal to the value of **displayCount** plus 1 and at least one of **prevMargin** and **nextMargin** takes effect, set **loop** to **true** to enable loop playback in non-group paging mode. When loop playback is enabled, a snapshot is generated as the placeholder image. (The snapshot may not be correctly generated for those components that take a long time to display, such as those that use asynchronous image loading. Avoid enabling loop playback under this scenario.)
    

#### \[h2\]displayArrow10+

displayArrow(value: ArrowStyle | boolean, isHoverShow?: boolean)

Sets the arrow style of the navigation indicator.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6d/v3/E7GDBvr7Re2x01ZhyJnnEQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062239Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E02632AC44C5B98869F3C821562D0024ACF5DA34E0AD2652FD2F9FD0F3296909)

When all child nodes fit within the viewport, resulting in only one screen's worth of content being visible, the **Swiper** component displays only that screen without any left or right page-turning arrows.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [ArrowStyle](#arrowstyle10) | boolean | Yes | 
Arrow and background to set. In cases of exceptions, the default values in the **ArrowStyle** object are used. The value **true** means to show the arrow and background in the default styles, and **false** means to hide the arrow and background.

Default value: **false**.

 |
| isHoverShow | boolean | No | 

Whether to show the arrow on mouse hover.

Default value: **false**.

**NOTE**

1\. **false**: The arrow is always displayed.

2\. **true**: The arrow is displayed.

With navigation indicators, the arrow is displayed when the mouse pointer hovers over the indicators or arrow areas.

Without navigation indicators, the arrow is displayed when the mouse pointer hovers over the **Swiper** display area.

3\. When the arrow is displayed, clicking the arrow turns pages.

 |

#### \[h2\]displayMode

displayMode(value: SwiperDisplayMode)

Sets the mode in which elements are displayed along the main axis. This API takes effect only when [displayCount](#displaycount8) is not set.

**Widget capability**: This API can be used in ArkTS widgets since API version 10.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [SwiperDisplayMode](#swiperdisplaymode) | Yes | 
Mode in which elements are displayed along the main axis.

Default value: **SwiperDisplayMode.STRETCH**

 |

#### \[h2\]nextMargin10+

nextMargin(value: Length, ignoreBlank?:boolean)

Sets the trailing margin to reveal a portion of the next item. For the implementation example, see [Example 1: Setting the Navigation Indicator Interaction and Page Turning Effect](#example-1-setting-the-navigation-indicator-interaction-and-page-turning-effect). This attribute is effective only when the layout mode of the child components in **Swiper** is set to stretch, which mainly includes two scenarios: 1. **displayMode** is set to **SwiperDisplayMode.STRETCH**; 2. **displayCount** is assigned a numeric value.

When the main axis runs horizontally and either **nextMargin** or **prevMargin** is greater than the measured width of the child component, both margins are hidden.

When the main axis runs vertically and either **nextMargin** or **prevMargin** is greater than the measured height of the child component, both margins are hidden.

When using the **nextMargin** or **prevMargin** API, avoid applying [size constraints](../../universal-attributes/layout-and-borders/sizing/document.md#constraintsize) to child components. Otherwise, the main axis of the child nodes will not be stretched to the expected length, causing the margins to lose their effect.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d1/v3/j9h2Qo5RTF6XS45kVAqaPg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062239Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2D677D898A379BD1B8CF764A4D45555F5D667C70CBEF0CDAC73989A29A75FEF7)

This API cannot be called within [attributeModifier](../../universal-attributes/modifiers-and-custom-property/attribute-modifier/document.md#attributemodifier).

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [Length](../../common-definitions/basic-types/document.md#length) | Yes | 
Trailing margin. Percentage values are not supported.

Default value: **0**

 |
| ignoreBlank12+ | boolean | No | 

Whether to hide the trailing margin for the last page in non-loop scenarios.

**true**: Hide the trailing margin, in which case, the right edge of the last page is aligned with that of the **Swiper** component's viewable area.

**false**: Show the trailing margin, in which case, the last page has a **nextMargin**\-specified gap from the **Swiper** component's right edge.

Default value: **false**.

**NOTE**

On the last page, the values of **prevMargin** and **nextMargin** are added to create a left margin that allows the previous page to be displayed partially.

 |

#### \[h2\]prevMargin10+

prevMargin(value: Length, ignoreBlank?:boolean)

Sets the leading margin to reveal a portion of the previous item. For the implementation example, see [Example 1: Setting the Navigation Indicator Interaction and Page Turning Effect](#example-1-setting-the-navigation-indicator-interaction-and-page-turning-effect). This attribute is effective only when the layout mode of the child components in **Swiper** is set to stretch, which mainly includes two scenarios: 1. **displayMode** is set to **SwiperDisplayMode.STRETCH**; 2. **displayCount** is assigned a numeric value.

When the main axis runs horizontally and either **nextMargin** or **prevMargin** is greater than the measured width of the child component, both margins are hidden.

When the main axis runs vertically and either **nextMargin** or **prevMargin** is greater than the measured height of the child component, both margins are hidden.

When using the **nextMargin** or **prevMargin** API, avoid applying [size constraints](../../universal-attributes/layout-and-borders/sizing/document.md#constraintsize) to child components. Otherwise, the main axis of the child nodes will not be stretched to the expected length, causing the margins to lose their effect.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3b/v3/uBB-lHnZSNS6QeToxV2LkA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062239Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F2DDC16CE9A7CF8C7B0F365EE7568C9BDED6A2A95E62BAC7B83A02B96659AD31)

This API cannot be called within [attributeModifier](../../universal-attributes/modifiers-and-custom-property/attribute-modifier/document.md#attributemodifier).

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [Length](../../common-definitions/basic-types/document.md#length) | Yes | 
Leading margin. Percentage values are not supported.

Default value: **0**

 |
| ignoreBlank12+ | boolean | No | 

Whether to hide the leading margin for the first page in non-loop scenarios.

**true**: Hide the leading margin, in which case, the left edge of the first page is aligned with that of the **Swiper** component's viewable area.

**false**: Show the leading margin, in which case, the first page has a **prevMargin**\-specified gap from the **Swiper** component's left edge.

Default value: **false**.

**NOTE**

On the first page, the values of **prevMargin** and **nextMargin** are added to create a right margin that allows the next page to be displayed partially.

 |

#### \[h2\]indicatorInteractive12+

indicatorInteractive(value: boolean)

Sets whether the navigation indicator is interactive.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | boolean | Yes | 
Whether the navigation indicator is interactive.

The value **true** means that the navigation indicator is interactive, and **false** means the opposite.

If the input parameter is invalid, the value **true** is used.

 |

#### \[h2\]pageFlipMode15+

pageFlipMode(mode: Optional<PageFlipMode>)

Sets the mode for flipping pages using the mouse wheel. If this API is not used, the continuous page flipping mode (specified by value **PageFlipMode.CONTINUOUS**) is used by default.

**Widget capability**: This API can be used in ArkTS widgets since API version 15.

**Atomic service API**: This API can be used in atomic services since API version 15.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| mode | [Optional](../../universal-attributes/modifiers-and-custom-property/custom-property/document.md#optionalt)<[PageFlipMode](../../common-definitions/enums/document.md#pageflipmode15)\> | Yes | 
Mode for flipping pages using the mouse wheel.

If the value is **undefined**, the value **PageFlipMode.CONTINUOUS** is used.

 |

#### \[h2\]maintainVisibleContentPosition20+

maintainVisibleContentPosition(enabled: boolean)

Sets whether to maintain the visible content position when data is inserted or deleted above or ahead of the viewport. This applies to **Swiper** components using a single [LazyForEach](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-rendering-control-lazyforeach) as the child node, where the data source is modified using **LazyForEach** API such as [onDataAdd](../../state-management-and-rendering-control/lazyforeach/document.md#ondataadd8) or [onDataDelete](../../state-management-and-rendering-control/lazyforeach/document.md#ondatadelete8). In other scenarios, the position of the visible content changes when data is inserted or deleted above or before the display area.

When **swipeByGroup** in [displayCount](#displaycount8) is set to **true**, the visible content position remains unchanged only if the amount of data inserted or deleted above or before the display area is a multiple of the group size. Otherwise, the visible content position may change during group recalculation.

**Widget capability**: This API can be used in ArkTS widgets since API version 20.

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| enabled | boolean | Yes | 
Whether to maintain the visible content position when data is inserted or deleted above or ahead of the viewport.

Default value: **false**.

**false**: The visible content position will change when data is inserted or deleted. **true**: The visible content position remains unchanged when data is inserted or deleted. Animations stop if the data source is modified during an animation due to target index changes.

 |

#### \[h2\]indicatorStyle(deprecated)

indicatorStyle(value?: IndicatorStyle)

Sets the style of the navigation indicator.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c4/v3/X3j2Ty6DTlO3qx1xhn8vqQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062239Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D32FE7B1F9D6ABFA817D50B3DCA2EC89CDEEBABCCEB43D4B304EF82DDA22C377)

This API is supported since API version 8 and deprecated since API version 10. You are advised to use [indicator](#indicator) instead.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [IndicatorStyle](#indicatorstyledeprecated) | No | Style of the navigation indicator. |

#### SwiperDisplayMode

Enumerates the modes in which elements are displayed along the main axis.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Value | Description |
| :-- | :-- | :-- |
| Stretch(deprecated) | 0 | 
The width of each page in the **Swiper** component equals the component's own width.

Note: This API is supported since API version 7 and deprecated since API version 10. You are advised to use **STRETCH** instead.

**Widget capability**: This API can be used in ArkTS widgets since API version 7.

 |
| AutoLinear(deprecated) | 1 | 

The width of each page in the **Swiper** component equals the maximum width of child components. This enumerated value behaves the same as setting [displayCount](#displaycount8) to **'auto'** (string type). For details, see [displayCount](#displaycount8).

Note: This API is supported since API version 7 and deprecated since API version 10. You are advised to use **AUTO\_LINEAR** instead.

**Widget capability**: This API can be used in ArkTS widgets since API version 7.

 |
| STRETCH10+ | 0 | 

The width of each page in the **Swiper** component equals the component's own width.

**Widget capability**: This API can be used in ArkTS widgets since API version 10.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| AUTO\_LINEAR(deprecated) | 1 | 

The width of each page in the **Swiper** component equals the width of the leftmost child component in the viewport. This enumerated value behaves the same as setting [displayCount](#displaycount8) to **'auto'** (string type). For details, see [displayCount](#displaycount8).

Note: This API is supported since API version 10 and deprecated since API version 12. You are advised to use [Scroller.scrollTo](../scroll/document.md#scrollto) instead.

**Widget capability**: This API can be used in ArkTS widgets since API version 10.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |

#### SwiperNestedScrollMode11+

Enumerates the nested scrolling modes of the **Swiper** component and its parent container.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Value | Description |
| :-- | :-- | :-- |
| SELF\_ONLY | 0 | The scrolling is contained within the **Swiper** component, and no scroll chaining occurs, that is, the parent container does not scroll when the component scrolling reaches the boundary. |
| SELF\_FIRST | 1 | The **Swiper** component scrolls first, and when it hits the boundary, the parent container scrolls. When the parent container hits the boundary, its edge effect is displayed. If no edge effect is specified for the parent container, the edge effect of the **Swiper** component is displayed instead. |

#### SwiperController

Implements the controller for the **Swiper** component. Bind this object to a **Swiper** component to control page turning and other functionalities.

**Widget capability**: This API can be used in ArkTS widgets since API version 10.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

#### \[h2\]constructor

constructor()

A constructor used to create a **SwiperController** object.

**Widget capability**: This API can be used in ArkTS widgets since API version 10.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

#### \[h2\]showNext

showNext()

Turns to the next page. The page turning includes a transition animation, with the duration set by the [duration](#duration) attribute of the **Swiper** component.

**Widget capability**: This API can be used in ArkTS widgets since API version 10.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

#### \[h2\]showPrevious

showPrevious()

Turns to the previous page. The page turning includes a transition animation, with the duration set by the [duration](#duration) attribute of the **Swiper** component.

**Widget capability**: This API can be used in ArkTS widgets since API version 10.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

#### \[h2\]changeIndex12+

changeIndex(index: number, useAnimation?: boolean)

Goes to a specified page.

**Widget capability**: This API can be used in ArkTS widgets since API version 12.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| index | number | Yes | 
Index of the target page in the **Swiper** component.

**NOTE**

If the value specified is less than 0 or greater than the maximum page index, the value **0** is used.

 |
| useAnimation | boolean | No | 

Whether to use an animation for when the target page is reached. The value **true** means to use an animation, and **false** means the opposite.

Default value: **false**

 |

#### \[h2\]changeIndex15+

changeIndex(index: number, animationMode?: SwiperAnimationMode | boolean)

Moves to a specific page.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5/v3/InE4Pm3YRDqR1zrY53daAQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062239Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A119AC4B1BE3E702CE5AD817740D7B6F0B8119CF3249466A1DC26226D8DBE94D)

This API itself supports jumping without animation (set **animationMode** to **false** or **SwiperAnimationMode.NO\_ANIMATION**). Avoid starting an animation with **changeIndex** and then interrupt it with **finishAnimation** to achieve animation-free jumping.

**Widget capability**: This API can be used in ArkTS widgets since API version 15.

**Atomic service API**: This API can be used in atomic services since API version 15.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| index | number | Yes | 
Index of the target page in the **Swiper** component.

**NOTE**

If the value specified is less than 0 or greater than the maximum page index, the value **0** is used.

 |
| animationMode | [SwiperAnimationMode](#swiperanimationmode15) | boolean | No | 

Animation mode for moving to the specified page.

Default value: **SwiperAnimationMode.NO\_ANIMATION**

**NOTE**

The value **true** is equivalent to **SwiperAnimationMode.DEFAULT\_ANIMATION**, which means to use the default animation. The value **false** is equivalent to **SwiperAnimationMode.NO\_ANIMATION**, which means to use no animation.

 |

#### \[h2\]finishAnimation

finishAnimation(callback?: VoidCallback)

Stops an animation.

**Widget capability**: This API can be used in ArkTS widgets since API version 10.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | [VoidCallback](../../common-definitions/basic-types/document.md#voidcallback12) | No | Callback invoked when the animation stops. |

#### \[h2\]preloadItems18+

preloadItems(indices: Optional<Array<number>>): Promise<void>

Preloads child nodes for **Swiper**. After this API is called, all specified child nodes will be loaded at once. Therefore, for performance considerations, it is recommended that you load child nodes in batches. This API uses a promise to return the result.

If the **SwiperController** object is not bound to any **Swiper** component, any attempt to call APIs on it will result in a JavaScript exception, together with the error code 100004. Therefore, you are advised to use **try-catch** to handle potential exceptions when calling APIs on **SwiperController**.

When combining with [LazyForEach](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-rendering-control-lazyforeach) and custom components, be aware that [LazyForEach](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-rendering-control-lazyforeach) only retains custom components within the cache range. Components outside this range are removed. Therefore, make sure the indexes of nodes to be preloaded via this API are within the cache range to avoid issues.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b7/v3/zu-RhAKyQ2ejysOxzR134A/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062239Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=09C183466D0EC18A4A7028D6ECAFA014D0A5C04619A08D6ED5F8ADE04868C306)

**preloadItems** of **Swiper** needs to be called after **Swiper** is created. You are advised to control the first preloading in the [onAppear](../../universal-events/component-change-events/show-hide-event/document.md#onappear) lifecycle of **Swiper**.

**Widget capability**: This API can be used in ArkTS widgets since API version 18.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| indices | [Optional](../../universal-attributes/modifiers-and-custom-property/custom-property/document.md#optionalt)<Array<number>> | Yes | Array of indexes of the child nodes to preload. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [Scrollable Component Error Codes](../../../error-codes/ui/scrollable-component-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter invalid. Possible causes: 1. The parameter type is not Array<number>; 2. The parameter is an empty array; 3. The parameter contains an invalid index. |
| 100004 | Controller not bound to component. |

#### SwiperAnimationMode15+

Enumerates the animation mode for moving to a specific page in the **Swiper** component.

**Widget capability**: This API can be used in ArkTS widgets since API version 15.

**Atomic service API**: This API can be used in atomic services since API version 15.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Value | Description |
| :-- | :-- | :-- |
| NO\_ANIMATION | 0 | Move to the specified page without any animation. |
| DEFAULT\_ANIMATION | 1 | Move to the specified page with the default animation. |
| FAST\_ANIMATION | 2 | Move to a page near the specified page without animation, and then navigate to the specified page with the default animation. |

#### Indicator10+

Sets the distance between the navigation indicator and the **Swiper** component. Note that due to its default interaction area height of 32 vp, the navigation indicator cannot be placed flush against the bottom edge. To implement the function of completely attaching to the bottom, you can use the [IndicatorComponent](../../navigation-and-switching/indicator/document.md#indicatorcomponent) component to adjust the position more flexibly.

**Widget capability**: This API can be used in ArkTS widgets since API version 10.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

#### \[h2\]left

left(value: Length): T

Sets the position of the navigation indicator relative to the left edge of the **Swiper** component.

**Widget capability**: This API can be used in ArkTS widgets since API version 10.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [Length](../../common-definitions/basic-types/document.md#length) | Yes | 
Position of the navigation indicator relative to the left edge of the **Swiper** component.

If neither **left** nor **right** is set, the navigation indicator is centered along the main axis based on its own size and the size of the **Swiper** component.

If the value specified is **0**, the navigation indicator is placed at the position 0.

Priority: higher than the **right** property

Value range: \[0, Swiper width - Navigation indicator area width\]. Values outside this range are adjusted to the nearest boundary.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| T | Current navigation indicator. |

#### \[h2\]top

top(value: Length): T

Sets the position of the navigation indicator relative to the top edge of the **Swiper** component.

**Widget capability**: This API can be used in ArkTS widgets since API version 10.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [Length](../../common-definitions/basic-types/document.md#length) | Yes | 
Position of the navigation indicator relative to the top edge of the **Swiper** component.

If neither **top** nor **bottom** is set, the navigation indicator is aligned at the bottom along the cross axis based on its own size and the size of the **Swiper** component, which is the same effect as setting **bottom=0**.

If the value specified is **0**, the navigation indicator is placed at the position 0.

Priority: higher than the **bottom** property

Value range: \[0, Swiper height - Navigation indicator area height\]. Values outside this range are adjusted to the nearest boundary.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| T | Current navigation indicator. |

#### \[h2\]right

right(value: Length): T

Sets the position of the navigation indicator relative to the right edge of the **Swiper** component.

**Widget capability**: This API can be used in ArkTS widgets since API version 10.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [Length](../../common-definitions/basic-types/document.md#length) | Yes | 
Position of the navigation indicator relative to the right edge of the **Swiper** component.

If neither **left** nor **right** is set, the navigation indicator is centered along the main axis based on its own size and the size of the **Swiper** component.

If the value specified is **0**, the navigation indicator is placed at the position 0.

Priority: lower than the **left** property.

Value range: \[0, Swiper width - Navigation indicator area width\]. Values outside this range are adjusted to the nearest boundary.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| T | Current navigation indicator. |

#### \[h2\]bottom

bottom(value: Length): T

Sets the position of the navigation indicator relative to the bottom edge of the **Swiper** component.

**Widget capability**: This API can be used in ArkTS widgets since API version 10.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [Length](../../common-definitions/basic-types/document.md#length) | Yes | 
Position of the navigation indicator relative to the bottom edge of the **Swiper** component.

If neither **top** nor **bottom** is set, the navigation indicator is aligned at the bottom along the cross axis based on its own size and the size of the **Swiper** component, which is the same effect as setting **bottom=0**.

If the value specified is **0**, the navigation indicator is placed at the position 0.

Priority: lower than the **top** property

Value range: \[0, Swiper height - Navigation indicator area height\]. Values outside this range are adjusted to the nearest boundary.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| T | Current navigation indicator. |

#### \[h2\]bottom19+

bottom(bottom: LengthMetrics | Length, ignoreSize: boolean): T

Sets the position of the navigation indicator relative to the bottom edge of the **Swiper** component. You can also choose to ignore the size of the navigation indicator using the **ignoreSize** property.

**Widget capability**: This API can be used in ArkTS widgets since API version 19.

**Atomic service API**: This API can be used in atomic services since API version 19.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| bottom | [LengthMetrics](../../../arkts-api/ui/arkui/graphics/document.md#lengthmetrics12) | [Length](../../common-definitions/basic-types/document.md#length) | Yes | 
Position of the navigation indicator relative to the bottom edge of the **Swiper** component.

If neither **top** nor **bottom** is set, the navigation indicator is aligned at the bottom along the cross axis based on its own size and the size of the **Swiper** component, which is the same effect as setting **bottom=0**.

If the value specified is **0**, the navigation indicator is placed at the position 0.

Priority: lower than the **top** property

Value range: \[0, Swiper height - Navigation indicator area height\]. Values outside this range are adjusted to the nearest boundary.

 |
| ignoreSize | boolean | Yes | 

Whether to ignore the size of the navigation indicator.

Default value: **false**.

Setting **true** positions the indicator closer to the **Swiper** component's bottom. For the usage, see [Example 9: Using the space and bottom APIs on the Navigation Indicator](#example-9-using-the-space-and-bottom-apis-on-the-navigation-indicator).

**NOTE**

The **ignoreSize** property does not apply to the digit-style navigation indicator in the following scenarios:

• [vertical](#vertical) is set to **false** and the value of **bottom** is greater than 0.

• When [vertical](#vertical) is set to **true**:

1\. The value of **bottom** is greater than 0.

2\. The value of **bottom** is **undefined**.

3\. **isSidebarMiddle** is set to **false**.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| T | Current navigation indicator. |

#### \[h2\]start12+

start(value: LengthMetrics): T

Sets the distance between the navigation indicator and the right edge (in [RTL](../../state-management-and-rendering-control/built-in-environment-variables/document.md#layoutdirection) scripts) or the left edge (in [LTR](../../state-management-and-rendering-control/built-in-environment-variables/document.md#layoutdirection) scripts) of the **Swiper** component.

**Widget capability**: This API can be used in ArkTS widgets since API version 12.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [LengthMetrics](../../../arkts-api/ui/arkui/graphics/document.md#lengthmetrics12) | Yes | 
Right-to-left scripts: Distance between the navigation indicator and the right edge of the **Swiper** component.

Left-to-right scripts: Distance between the navigation indicator and the left edge of the **Swiper** component.

Default value: **0**

Unit: vp

Value range: \[0, Swiper width - Navigation indicator area width\]. Values outside this range are adjusted to the nearest boundary.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| T | Current navigation indicator. |

#### \[h2\]end12+

end(value: LengthMetrics): T

Sets the distance between the navigation point indicator and the left edge (in right-to-left scripts) or the right edge (in left-to-right scripts) of the **Swiper** component.

**Widget capability**: This API can be used in ArkTS widgets since API version 12.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [LengthMetrics](../../../arkts-api/ui/arkui/graphics/document.md#lengthmetrics12) | Yes | 
Right-to-left scripts: Distance between the navigation indicator and the left edge of the **Swiper** component.

Left-to-right scripts: Distance between the navigation indicator and the right edge of the **Swiper** component.

Default value: **0**

Unit: vp

Value range: \[0, Swiper width - Navigation indicator area width\]. Values outside this range are adjusted to the nearest boundary.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| T | Current navigation indicator. |

#### \[h2\]dot

static dot(): DotIndicator

Returns a **DotIndicator** object.

**Widget capability**: This API can be used in ArkTS widgets since API version 10.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Return value**

| Type | Description |
| :-- | :-- |
| [DotIndicator](#dotindicator10) | Dot-style indicator. |

#### \[h2\]digit

static digit(): DigitIndicator

Returns a **DigitIndicator** object.

**Widget capability**: This API can be used in ArkTS widgets since API version 10.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Return value**

| Type | Description |
| :-- | :-- |
| [DigitIndicator](#digitindicator10) | Digit-style indicator. |

#### DotIndicator10+

A constructor used to create a **DotIndicator** object. It inherits from [Indicator](#indicator10).

**Widget capability**: This API can be used in ArkTS widgets since API version 10.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

#### \[h2\]constructor

constructor()

A constructor used to create a **DotIndicator** object.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/33/v3/-z6rNi9aR8SEBvBWuGfxOQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062239Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3806202473B22AFFE556CA5DDF0D9A44FA7FF000728D621FDACDF9AB41243A17)

-   When pressed, the navigation indicator is zoomed in to 1.33 times. To account for this, there is a certain distance between the navigation indicator's visible boundary and its actual boundary in the non-pressed state. The distance increases with the value of **itemWidth**, **itemHeight**, **selectedItemWidth**, and **selectedItemHeight**.
    
-   If there are too many pages and dot-style indicators exceed the page, you are advised to use the **maxDisplayCount** parameter to set the number of dots to be displayed.
    

**Widget capability**: This API can be used in ArkTS widgets since API version 10.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

#### \[h2\]itemWidth

itemWidth(value: Length): DotIndicator

Sets the width of a dot-style navigation indicator of the **Swiper** component.

**Widget capability**: This API can be used in ArkTS widgets since API version 10.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [Length](../../common-definitions/basic-types/document.md#length) | Yes | 
Width of the dot-style indicator. This parameter cannot be set in percentage.

Default value: **6**

Unit: vp

Value range: (0, +∞)

 |

**Return value**

| Type | Description |
| :-- | :-- |
| [DotIndicator](#dotindicator10) | Current dot-style navigation indicator. |

#### \[h2\]itemHeight

itemHeight(value: Length): DotIndicator

Sets the height of a dot-style navigation indicator of the **Swiper** component.

**Widget capability**: This API can be used in ArkTS widgets since API version 10.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [Length](../../common-definitions/basic-types/document.md#length) | Yes | 
Height of the dot-style indicator. This parameter cannot be set in percentage.

Default value: **6**

Unit: vp

Value range: (0, +∞)

 |

**Return value**

| Type | Description |
| :-- | :-- |
| [DotIndicator](#dotindicator10) | Current dot-style navigation indicator. |

#### \[h2\]selectedItemWidth

selectedItemWidth(value: Length): DotIndicator

Sets the width of the selected dot-style navigation indicator.

**Widget capability**: This API can be used in ArkTS widgets since API version 10.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [Length](../../common-definitions/basic-types/document.md#length) | Yes | 
Width of the selected dot-style navigation indicator. This parameter cannot be set in percentage.

Default value: **6**

Unit: vp

Value range: (0, +∞)

 |

**Return value**

| Type | Description |
| :-- | :-- |
| [DotIndicator](#dotindicator10) | Current dot-style navigation indicator. |

#### \[h2\]selectedItemHeight

selectedItemHeight(value: Length): DotIndicator

Sets the height of the selected dot-style navigation indicator.

**Widget capability**: This API can be used in ArkTS widgets since API version 10.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [Length](../../common-definitions/basic-types/document.md#length) | Yes | 
Height of the selected dot-style indicator. This parameter cannot be set in percentage.

Default value: **6**

Unit: vp

Value range: (0, +∞)

 |

**Return value**

| Type | Description |
| :-- | :-- |
| [DotIndicator](#dotindicator10) | Current dot-style navigation indicator. |

#### \[h2\]mask

mask(value: boolean): DotIndicator

Sets whether to enable the mask for the dot-style navigation indicator.

**Widget capability**: This API can be used in ArkTS widgets since API version 10.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | boolean | Yes | 
Whether to enable the mask for the dot-style navigation indicator. The value **true** means to enable the mask for the dot-style navigation indicator, and **false** means the opposite.

Default value: **false**.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| [DotIndicator](#dotindicator10) | Current dot-style navigation indicator. |

#### \[h2\]color

color(value: ResourceColor): DotIndicator

Sets the color of the dot-style navigation indicator.

**Widget capability**: This API can be used in ArkTS widgets since API version 10.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [ResourceColor](../../common-definitions/basic-types/document.md#resourcecolor) | Yes | 
Color of the dot-style navigation indicator.

Default value: **'#1A182431'** (light gray)

 |

**Return value**

| Type | Description |
| :-- | :-- |
| [DotIndicator](#dotindicator10) | Current dot-style navigation indicator. |

#### \[h2\]selectedColor

selectedColor(value: ResourceColor): DotIndicator

Sets the color of the selected dot-style navigation indicator.

**Widget capability**: This API can be used in ArkTS widgets since API version 10.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [ResourceColor](../../common-definitions/basic-types/document.md#resourcecolor) | Yes | 
Color of the selected dot-style navigation indicator.

Default value: **'#007DFF'** (blue)

 |

**Return value**

| Type | Description |
| :-- | :-- |
| [DotIndicator](#dotindicator10) | Current dot-style navigation indicator. |

#### \[h2\]maxDisplayCount12+

maxDisplayCount(maxDisplayCount: number): DotIndicator

Sets the maximum number of navigation dots in the dot-style navigation indicator.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| maxDisplayCount | number | Yes | 
Maximum number of navigation dots in the dot-style navigation point indicator. If the actual number of navigation dots exceeds this limit, the overflow effect is activated, as shown in [Example 5](#example-5-configuring-overflow-for-the-dot-style-indicator).

This parameter has no default value. If an invalid value is set, no overflow effect is applied.

Value range: \[6, 9\].

**NOTE**

In scenarios involving overflow display:

1\. Interactive features, such as gestures and mouse operations, are not supported.

2\. The position of the selected navigation dot corresponding to the middle page is not strictly fixed; it depends on the sequence of previous page-turning operations.

3\. Currently, only scenarios with **displayCount** set to **1** are supported.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| [DotIndicator](#dotindicator10) | Current dot-style navigation indicator. |

#### \[h2\]space19+

space(space: LengthMetrics): DotIndicator

Sets the spacing between dot-style navigation indicators of the **Swiper** component.

**Widget capability**: This API can be used in ArkTS widgets since API version 19.

**Atomic service API**: This API can be used in atomic services since API version 19.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| space | [LengthMetrics](../../../arkts-api/ui/arkui/graphics/document.md#lengthmetrics12) | Yes | 
Spacing between the dots in the dot-style navigation indicator. Percentage values are not supported.

Default value: **10** for PCs and 2-in-1 devices and **8** for other devices

Unit: vp

Value range: \[0, +∞)

 |

**Return value**

| Type | Description |
| :-- | :-- |
| [DotIndicator](#dotindicator10) | Current dot-style navigation indicator. |

#### DigitIndicator10+

A constructor used to create a **DigitIndicator** object. It inherits from [Indicator](#indicator10).

**Widget capability**: This API can be used in ArkTS widgets since API version 10.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cc/v3/aWbLsYPgT8i-IlDicJGjLA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062239Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8D2934B5F221B8BE89BBDAA0AE2314C941396CCA9401F5030746D9093E8F623C)

When pages are turned by group, the child nodes displayed in the digit-style navigation indicator do not count placeholder nodes.

The maximum value of [maxFontScale](../../text-and-input/text/document.md#maxfontscale12) for the digit-style navigation indicator is **2**.

The mirror display of the page number depends on the RTL status of the system.

#### \[h2\]fontColor

fontColor(value: ResourceColor): DigitIndicator

Sets the font color of the digit-style navigation indicator.

**Widget capability**: This API can be used in ArkTS widgets since API version 10.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [ResourceColor](../../common-definitions/basic-types/document.md#resourcecolor) | Yes | 
Font color of the digit-style navigation indicator.

Default value: **'#ff182431'**

 |

**Return value**

| Type | Description |
| :-- | :-- |
| [DigitIndicator](#digitindicator10) | Current digit-style navigation indicator. |

#### \[h2\]selectedFontColor

selectedFontColor(value: ResourceColor): DigitIndicator

Sets the font color of the selected digit-style navigation indicator.

**Widget capability**: This API can be used in ArkTS widgets since API version 10.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [ResourceColor](../../common-definitions/basic-types/document.md#resourcecolor) | Yes | 
Font color of the selected digit-style navigation indicator.

Default value: **'#ff182431'**

 |

**Return value**

| Type | Description |
| :-- | :-- |
| [DigitIndicator](#digitindicator10) | Current digit-style navigation indicator. |

#### \[h2\]digitFont

digitFont(value: Font): DigitIndicator

Sets the font style of the digit-style navigation indicator.

**Widget capability**: This API can be used in ArkTS widgets since API version 10.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [Font](../../common-definitions/basic-types/document.md#font) | Yes | 
Font style of the digit-style navigation indicator.

Only the **size** and **weight** parameters in **Font** are adjustable. Setting **family** and **style** has no effect.

Default value:

{ size: 14, weight: FontWeight.Normal }

 |

**Return value**

| Type | Description |
| :-- | :-- |
| [DigitIndicator](#digitindicator10) | Current digit-style navigation indicator. |

#### \[h2\]selectedDigitFont

selectedDigitFont(value: Font): DigitIndicator

Sets the font style of the selected digit-style navigation indicator.

**Widget capability**: This API can be used in ArkTS widgets since API version 10.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [Font](../../common-definitions/basic-types/document.md#font) | Yes | 
Font style of the selected digit-style navigation indicator.

Default value:

{ size: 14, weight: FontWeight.Normal }

 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/55/v3/bGh1VBCiT-KKqy7oW1N7hA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062239Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=644A628C68852C036AEB8726D3554BE2FDD0BEF2A3E455EAB8784FB1CFA7B4C7)

When pages are turned by group, the child nodes displayed in the digit-style navigation indicator do not count placeholder nodes.

**Return value**

| Type | Description |
| :-- | :-- |
| [DigitIndicator](#digitindicator10) | Current digit-style navigation indicator. |

#### \[h2\]constructor

constructor()

A constructor used to create a **DigitIndicator** object.

**Widget capability**: This API can be used in ArkTS widgets since API version 10.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

#### ArrowStyle10+

Describes the left and right arrow attributes.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| showBackground | boolean | No | Yes | 
Whether to show the background for the arrow. The value **true** means to show the background for the arrow, and **false** means the opposite.

Default value: **false**.

 |
| isSidebarMiddle | boolean | No | Yes | 

Whether the arrow is centered on both sides of the **Swiper** component. The value **true** means that the arrow is centered on both sides of the **Swiper** component, and **false** means that the arrow is show on either side of the navigation indicator.

Default value: **false**.

 |
| backgroundSize | [Length](../../common-definitions/basic-types/document.md#length) | No | Yes | 

Size of the background.

On both sides of the navigation indicator:

Default value: **24vp**.

On both sides of the component:

Default value: **32vp**.

Percentage values are not supported.

 |
| backgroundColor | [ResourceColor](../../common-definitions/basic-types/document.md#resourcecolor) | No | Yes | 

Color of the background.

On both sides of the navigation indicator:

Default value: **'#00000000'**.

On both sides of the component:

Default value: **'#19182431'**.

 |
| arrowSize | [Length](../../common-definitions/basic-types/document.md#length) | No | Yes | 

Size of the arrow.

On both sides of the navigation indicator:

Default value: **18vp**.

On both sides of the component:

Default value: **24vp**.

**NOTE**

If **showBackground** is set to **true**, the value of **arrowSize** is 3/4 of the value of **backgroundSize**.

Percentage values are not supported.

 |
| arrowColor | [ResourceColor](../../common-definitions/basic-types/document.md#resourcecolor) | No | Yes | 

Color of the arrow.

Default value: **'#182431'**

 |

#### SwiperAutoFill10+

Describes the auto-fill attribute.

**Widget capability**: This API can be used in ArkTS widgets since API version 10.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| minSize | [VP](../../common-definitions/basic-types/document.md#vp10) | No | No | 
Minimum width of the element.

Default value: **0**

 |

#### AutoPlayOptions18+

Defines the properties for controlling the automatic playback behavior.

**Widget capability**: This API can be used in ArkTS widgets since API version 18.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| stopWhenTouched | boolean | No | No | 
Whether the automatic playback stops immediately when the component is touched.

The value **true** means that the automatic playback stops immediately when the component is touched, and **false** means the opposite.

Default value: **true**.

 |

#### Events

In addition to the [universal events](../../universal-events/document.md), the following events are supported.

#### \[h2\]onChange

onChange(event: Callback<number>)

Triggered when the index of the currently displayed element changes. The return value is the index of the currently displayed element.

When the **Swiper** component is used together with **LazyForEach**, the subpage UI update cannot be triggered in the **onChange** event.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/43/v3/PUhVRVfNTQalWeCXyOkGPw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062239Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=081BAC1D36AE38097C6E208B60A551E3B508AB65BEEDBB2AAB09BD1E05857B41)

If the index change is caused by an animation, this callback is triggered when the animation ends.

**Widget capability**: This API can be used in ArkTS widgets since API version 10.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| event | [Callback](../../common-definitions/basic-types/document.md#callback12)<number> | Yes | Index of the currently displayed element. |

#### \[h2\]onAnimationStart9+

onAnimationStart(event: OnSwiperAnimationStartCallback)

Triggered when the page transition animation starts.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/90/v3/af_G0U78T9GjBpua1VPC4w/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062239Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D83C281B6577F2A360FA4C351C0EC7F6C5B6C1380E6288802360C1D5B2D53E46)

-   When this callback is invoked, the page transition animation logic is executed in the rendering thread, allowing the idle main thread to load resources required by child components. This reduces preloading time for nodes within the **cachedCount** range. For best practices, see [Optimizing Frame Loss During Swiper Component Loading – Preloading Data](https://developer.huawei.com/consumer/en/doc/best-practices/bpta-swiper_high_performance_development_guide#section8783121513246).
    
-   When the duration of the page transition animation is set to **0**, this callback is triggered only in the following scenarios: swiping to turn pages, automatic playback, calling **SwiperController.showNext()** or **SwiperController.showPrevious()**, and touching navigation indicators to navigate.
    

**Widget capability**: This API can be used in ArkTS widgets since API version 10.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| event | [OnSwiperAnimationStartCallback](#onswiperanimationstartcallback18) | Yes | Callback triggered when the page transition animation starts. |

#### \[h2\]onAnimationEnd9+

onAnimationEnd(event: OnSwiperAnimationEndCallback)

Triggered when the page transition animation ends.

This event is triggered when the switching animation of the **Swiper** component ends, whether it is caused by gesture interruption or by calling **finishAnimation** through **SwiperController**.

**Widget capability**: This API can be used in ArkTS widgets since API version 10.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| event | [OnSwiperAnimationEndCallback](#onswiperanimationendcallback18) | Yes | Callback triggered when the page transition animation ends. |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/51/v3/1xGpqjsSRaS2BiMLUAI4Jg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062239Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4B44A98C1CB09180049FDCE2A199293FAF73BD8124816B3E5F4FDB1705A1BE33)

-   When the duration of the page transition animation is set to **0**, this callback is triggered only in the following scenarios: swiping to turn pages, automatic playback, calling **SwiperController.showNext()** or **SwiperController.showPrevious()**, and touching navigation indicators to navigate.

#### \[h2\]onGestureSwipe10+

onGestureSwipe(event: OnSwiperGestureSwipeCallback)

Triggered on a frame-by-frame basis when the page is turned by a swipe.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| event | [OnSwiperGestureSwipeCallback](#onswipergestureswipecallback18) | Yes | Callback triggered on a frame-by-frame basis when the page is turned by a swipe. **onGestureSwipe** is called after **onTouch**. For post-release operations, consider using [onAnimationStart](#onanimationstart9). |

#### \[h2\]customContentTransition12+

customContentTransition(transition: SwiperContentAnimatedTransition)

Defines a custom page transition animation. During finger-following swipes and post-release transition animations, this triggers a frame-by-frame callback for all pages in the viewport, allowing you to customize animations by modifying properties like opacity, scale, and translation.

Instructions:

1.  This API does not work when **prevMargin** and **nextMargin** are set in such a way that the **Swiper** frontend and backend display the same page during loop playback.
    
    2\. During finger-following swipes and post-release transition animations, the [SwiperContentTransitionProxy](#swipercontenttransitionproxy12) callback is invoked for all pages in the viewport on a frame-by-frame basis. For example, when there are two pages whose subscripts are 0 and 1 in the viewport, two callbacks whose indexes are 0 and 1 are invoked in each frame.
    
    3\. When the **swipeByGroup** parameter of the **displayCount** attribute is set to **true**, the callback is invoked for all pages in a group if any page in the group is within the viewport; and all pages in a group are removed from the render tree if none of them are within the viewport.
    
    4\. During finger-following swipes and post-release transition animations, the default animation (page scrolling) is still effective. If you do not want the page to scroll, you can set the **translate** property on the main axis to offset the page scrolling. For example, if the value of **displayCount** is **2** and there are two pages whose subscripts are 0 and 1 within the viewport, you can set the **translate** property on the main axis to the following on a frame-by-frame basis: **translate** for page 0 = **\-position** x **mainAxisLength**; **translate** for page 1 = **\-(position - 1)** x **mainAxisLength**
    

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| transition | [SwiperContentAnimatedTransition](#swipercontentanimatedtransition12) | Yes | Information about the custom page transition animation. |

#### \[h2\]onContentDidScroll12+

onContentDidScroll(handler: ContentDidScrollCallback)

Triggered when content in the **Swiper** component scrolls.

Instructions:

1.  This API does not work when **prevMargin** and **nextMargin** are set in such a way that the **Swiper** frontend and backend display the same page during loop playback.
    
    2\. During page scrolling, the [ContentDidScrollCallback](#contentdidscrollcallback12) callback is invoked for all pages in the viewport on a frame-by-frame basis. For example, when there are two pages whose subscripts are 0 and 1 in the viewport, two callbacks whose indexes are 0 and 1 are invoked in each frame.
    
    3\. When the **swipeByGroup** parameter of the **displayCount** attribute is set to **true**, the callback is invoked for all pages in a group if any page in the group is within the viewport.
    

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| handler | [ContentDidScrollCallback](#contentdidscrollcallback12) | Yes | Callback triggered when content in the **Swiper** component scrolls. |

#### \[h2\]onSelected18+

onSelected(event: Callback<number>)

Triggered when the selected element changes. The index of the currently selected element is returned.

**Widget capability**: This API can be used in ArkTS widgets since API version 18.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| event | [Callback](../../common-definitions/basic-types/document.md#callback12)<number> | Yes | Index of the currently selected element. |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8/v3/kp4IVwGlSNWo9nmWJDTSTQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062239Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=ACC30B2AA08621A403755E2A6507CACFFF1F398DD3A2FA30AEEB590D18A34B6E)

In the **onSelected** callback, do not modify the **index** attribute of the **Swiper** component, or call the **SwiperController.changeIndex()**, **SwiperController.showNext()**, or **SwiperController.showPrevious()** APIs.

#### \[h2\]onUnselected18+

onUnselected(event: Callback<number>)

Triggered when the selected element changes. The index of the element that is about to be hidden is returned.

**Widget capability**: This API can be used in ArkTS widgets since API version 18.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| event | [Callback](../../common-definitions/basic-types/document.md#callback12)<number> | Yes | Index of the element that is about to be hidden. |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/77/v3/i-oS56zGRhu9tkZqHaJmtQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062239Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F4D2D855EFE79E11D4F5074EB98824BCB86005DB423A99B8AE7775CF4D762656)

In the **onUnselected** callback, do not modify the **index** attribute of the **Swiper** component, nor call the **SwiperController.changeIndex()**, **SwiperController.showNext()**, or **SwiperController.showPrevious()** APIs.

#### \[h2\]onContentWillScroll15+

onContentWillScroll(handler: ContentWillScrollCallback)

Triggered when the **Swiper** component is about to scroll. This event allows you to intercept and control the scrolling behavior of the component. The component determines whether to allow the scroll action based on the return value. If **true** is returned, the scroll action is allowed, and the pages in the **Swiper** component will follow the scrolling. If **false** is returned, the scroll action is disallowed, and the pages will remain stationary.

1.  This event is only triggered by gesture operations, including finger swipes, scrolling the mouse wheel, and moving focus using keyboard arrow keys.
    
2.  During finger swipes, the event is triggered for each frame. The system uses the return value of the event to determine whether to respond to the swipe for each frame.
    
3.  For scrolling the mouse wheel and moving focus using keyboard arrow keys, the event is triggered once per page turning. The system uses the return value to decide whether to allow the page turning.
    

**Widget capability**: This API can be used in ArkTS widgets since API version 15.

**Atomic service API**: This API can be used in atomic services since API version 15.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| handler | [ContentWillScrollCallback](#contentwillscrollcallback15) | Yes | Callback triggered when content in the **Swiper** component scrolls. |

#### \[h2\]onScrollStateChanged20+

onScrollStateChanged(event: Callback<ScrollState>)

Defines the callback of the swipe state change event for the **Swiper** component. This callback is triggered when the swipe state changes across the followings: scrolling with the touch, animating after release, and stopped.

**Widget capability**: This API can be used in ArkTS widgets since API version 20.

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| event | [Callback](../../common-definitions/basic-types/document.md#callback12)<[ScrollState](../list/document.md#scrollstate)\> | Yes | Callback triggered when the sliding status changes. |

#### OnSwiperAnimationStartCallback18+

type OnSwiperAnimationStartCallback = (index: number, targetIndex: number, extraInfo: SwiperAnimationEvent) => void

Defines the callback triggered when the page transition animation starts.

**Widget capability**: This API can be used in ArkTS widgets since API version 18.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| index | number | Yes | Index of the currently displayed element. If there are multiple columns, **index** indicates the index of the leftmost component. |
| targetIndex10+ | number | Yes | Index of the target element to switch to. |
| extraInfo10+ | [SwiperAnimationEvent](#swiperanimationevent10) | Yes | Extra information of the animation, including the offset of the currently displayed element and target element relative to the start position of the **Swiper** along the main axis, and the hands-off velocity. |

#### OnSwiperAnimationEndCallback18+

type OnSwiperAnimationEndCallback = (index: number, extraInfo: SwiperAnimationEvent) => void

Defines the callback triggered when the page transition animation ends.

**Widget capability**: This API can be used in ArkTS widgets since API version 18.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| index | number | Yes | Index of the currently displayed element. If there are multiple columns, **index** indicates the index of the leftmost component. |
| extraInfo10+ | [SwiperAnimationEvent](#swiperanimationevent10) | Yes | Extra information of the animation, which is the offset of the currently displayed element relative to the start position of the **Swiper** along the main axis. |

#### OnSwiperGestureSwipeCallback18+

type OnSwiperGestureSwipeCallback = (index: number, extraInfo: SwiperAnimationEvent) => void

Defines the callback triggered on a frame-by-frame basis when the page is turned by a swipe.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| index | number | Yes | Index of the currently displayed element. If there are multiple columns, **index** indicates the index of the leftmost component. |
| extraInfo | [SwiperAnimationEvent](#swiperanimationevent10) | Yes | Extra information of the animation, which is the offset of the currently displayed element relative to the start position of the **Swiper** along the main axis. |

#### ContentDidScrollCallback12+

type ContentDidScrollCallback = (selectedIndex: number, index: number, position: number, mainAxisLength: number) => void

Triggered during the swipe action of the **Swiper** component. For details about the parameters, see [SwiperContentTransitionProxy](#swipercontenttransitionproxy12).

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| selectedIndex | number | Yes | Index of the currently selected page. |
| index | number | Yes | Index of a page in the viewport. |
| position | number | Yes | Position of the page specified by **index** relative to the start position of the **Swiper** main axis (start position of the page corresponding to **selectedIndex**). |
| mainAxisLength | number | Yes | Length of the page specified by **index** along the main axis, in vp. |

#### ContentWillScrollCallback15+

type ContentWillScrollCallback = (result: SwiperContentWillScrollResult) => boolean

Defines the callback triggered when the **Swiper** component is about to scroll. The return value indicates whether the scroll action is allowed.

**Widget capability**: This API can be used in ArkTS widgets since API version 15.

**Atomic service API**: This API can be used in atomic services since API version 15.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| result | [SwiperContentWillScrollResult](#swipercontentwillscrollresult15) | Yes | Information related to the upcoming scroll action, including the index of the current page, the index of the page that will be displayed in the scroll direction, and the displacement of the scroll action. |

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Whether the scroll action is allowed. The value **true** means the scroll action is allowed, and **false** means the opposite. |

#### SwiperContentWillScrollResult15+

Provides information related to the upcoming scroll action, including the index of the current page, the index of the page that will be displayed in the scroll direction, and the displacement of the scroll action.

**Widget capability**: This API can be used in ArkTS widgets since API version 15.

**Atomic service API**: This API can be used in atomic services since API version 15.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| currentIndex | number | No | No | Index of the current page. During a finger swipe, this value remains constant as long as the finger is on the screen, even if the page has completely moved out of view. |
| comingIndex | number | No | No | Index of the page that will be displayed in the scroll direction. |
| offset | number | No | No | 
Displacement of the scroll action, which is signed to indicate different swipe directions. A positive value indicates a swipe from index=1 to index=0, while a negative value indicates a swipe from index=0 to index=1.

This value represents the offset for each frame during a finger swipe and the distance for page turning when the mouse wheel or keyboard navigation is used.

 |

#### SwiperAnimationEvent10+

Describes the animation information of the **Swiper** component.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| currentOffset | number | No | No | 
Offset of the currently displayed element relative to the start position of the **Swiper** along the main axis. Unit: vp

Default value: **0**

 |
| targetOffset | number | No | No | 

Offset of the target element relative to the start position of the **Swiper** along the main axis. Unit: vp

Default value: **0**

 |
| velocity | number | No | No | 

Hands-off velocity at the beginning of the animation. Unit: VP/S

Default value: **0**

 |

#### SwiperContentAnimatedTransition12+

Provides the information about the custom page transition animation.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| timeout | number | No | Yes | Timeout for the page transition animation. The timeout timer starts when the default animation (page scrolling) reaches the point where the first frame is moved out of the viewport. If you do not call the **finishTransition** API of [SwiperContentTransitionProxy](#swipercontenttransitionproxy12) before the timer expires, the component considers that the custom animation of the page ends and immediately removes the page node from the render tree. The unit is ms. The default value is **0**. |
| transition | Callback<[SwiperContentTransitionProxy](#swipercontenttransitionproxy12)\> | No | No | Content of the custom page transition animation. |

#### SwiperContentTransitionProxy12+

Implements the proxy object returned during the execution of the custom page transition animation of the **Swiper** component. You can use this object to obtain the page information in the custom animation viewport. You can also call the **finishTransition** API of this object to notify the **Swiper** component that the custom animation has finished playing.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

## Attributes

| Name | Type | Read Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| selectedIndex | number | No | No | Index of the currently selected page. |
| index | number | No | No | Index of a page in the viewport. |
| position | number | No | No | Position of the page specified by **index** relative to the start position of the **Swiper** main axis (start position of the page corresponding to **selectedIndex**). |
| mainAxisLength | number | No | No | Length of the page specified by **index** along the main axis, in vp. |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f5/v3/4IZnm8J3T6-B7Tsg1_dtUg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062239Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9C7FBB908F5E196AEACCE4D045FC277DB4435A5507B138B79284B8DB3C98A6AE)

-   For example, when the index of the currently selected child component is 0, during a transition animation from page 0 to page 1, the callback is triggered for all pages within the viewport on every frame. When pages 0 and 1 are both in the viewport, the callback is triggered twice per frame. The first callback has **selectedIndex** as **0**, **index** as **0**, **position** as the ratio of how much page 0 has moved relative to its position before the animation started on the current frame, and **mainAxisLength** as the length of page 0 on the main axis. The second callback has **selectedIndex** as **0**, **index** as **1**, **position** as the ratio of how much page 1 has moved relative to page 0 before the animation started on the current frame, and **mainAxisLength** as the length of page 1 on the main axis.
    
-   If the animation curve is a spring interpolation curve, during the transition animation from page 0 to page 1, due to the position and velocity when the user lifts their finger off the screen, animation may overshoot and slide past to page 2, then bounce back to page 1. Throughout this process, a callback is triggered for pages 1 and 2 within the viewport on every frame.
    

#### \[h2\]finishTransition12+

finishTransition(): void

Notifies the **Swiper** component that the custom animation has finished playing.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

#### IndicatorStyle(deprecated)

Defines the style of the navigation indicator.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c7/v3/l15TNWSNS--o9xLBd_XlbA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062239Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=35CB9D7D8869D62D91992283B9C7324E803EF0533021B13E3625000ABC1210F3)

This API is supported since API version 8 and deprecated since API version 10. You are advised to use [indicator](#indicator10) instead.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| left | [Length](../../common-definitions/basic-types/document.md#length) | No | Yes | 
Position of the navigation indicator relative to the left edge of the **Swiper** component.

If neither **left** nor **right** is set, the navigation indicator is centered along the main axis based on its own size and the size of the **Swiper** component.

If the value specified is **0**, the navigation indicator is placed at the position 0.

Priority: higher than the **right** property

Value range: \[0, Swiper width - Navigation indicator area width\]. Values outside this range are adjusted to the nearest boundary.

 |
| top | [Length](../../common-definitions/basic-types/document.md#length) | No | Yes | 

Position of the navigation indicator relative to the top edge of the **Swiper** component.

If neither **top** nor **bottom** is set, the navigation indicator is aligned at the bottom along the cross axis based on its own size and the size of the **Swiper** component, which is the same effect as setting **bottom=0**.

If the value specified is **0**, the navigation indicator is placed at the position 0.

Priority: higher than the **bottom** property

Value range: \[0, Swiper height - Navigation indicator area height\]. Values outside this range are adjusted to the nearest boundary.

 |
| right | [Length](../../common-definitions/basic-types/document.md#length) | No | Yes | 

Position of the navigation indicator relative to the right edge of the **Swiper** component.

If neither **left** nor **right** is set, the navigation indicator is centered along the main axis based on its own size and the size of the **Swiper** component.

If the value specified is **0**, the navigation indicator is placed at the position 0.

Priority: lower than the **left** property.

Value range: \[0, Swiper width - Navigation indicator area width\]. Values outside this range are adjusted to the nearest boundary.

 |
| bottom | [Length](../../common-definitions/basic-types/document.md#length) | No | Yes | 

Position of the navigation indicator relative to the bottom edge of the **Swiper** component.

If neither **top** nor **bottom** is set, the navigation indicator is aligned at the bottom along the cross axis based on its own size and the size of the **Swiper** component, which is the same effect as setting **bottom=0**.

If the value specified is **0**, the navigation indicator is placed at the position 0.

Priority: lower than the **top** property

Value range: \[0, Swiper height - Navigation indicator area height\]. Values outside this range are adjusted to the nearest boundary.

 |
| size | [Length](../../common-definitions/basic-types/document.md#length) | No | Yes | 

Diameter of the navigation indicator. Percentage values are not supported.

Default value: **6vp**

 |
| mask | boolean | No | Yes | 

Whether to enable the mask for the navigation indicator.

**true**: yes; **false**: no

Default value: **false**.

 |
| color | [ResourceColor](../../common-definitions/basic-types/document.md#resourcecolor) | No | Yes | 

Color of the navigation indicator.

Default value: **'#1A182431'** (light gray)

 |
| selectedColor | [ResourceColor](../../common-definitions/basic-types/document.md#resourcecolor) | No | Yes | 

Color of the selected navigation indicator.

Default value: **'#007DFF'** (blue)

 |

#### Example

## Example 1: Setting the Navigation Indicator Interaction and Page Turning Effect

In this example, the [changeIndex](#changeindex15) API is used to set the [SwiperAnimationMode](#swiperanimationmode15) animation mode to implement the page turning of the **Swiper** component to a specified page.

// xxx.ets
class MyDataSource implements IDataSource {
  private list: number\[\] = \[\];

  constructor(list: number\[\]) {
    this.list = list;
  }

  totalCount(): number {
    return this.list.length;
  }

  getData(index: number): number {
    return this.list\[index\];
  }

  registerDataChangeListener(listener: DataChangeListener): void {
  }

  unregisterDataChangeListener() {
  }
}

@Entry
@Component
struct SwiperExample {
  private swiperController: SwiperController = new SwiperController();
  private data: MyDataSource = new MyDataSource(\[\]);

  aboutToAppear(): void {
    let list: number\[\] = \[\];
    for (let i = 1; i <= 10; i++) {
      list.push(i);
    }
    this.data = new MyDataSource(list);
  }

  build() {
    Column({ space: 5 }) {
      Swiper(this.swiperController) {
        LazyForEach(this.data, (item: string) => {
          Text(item.toString())
            .width('90%')
            .height(160)
            .backgroundColor(0xAFEEEE)
            .textAlign(TextAlign.Center)
            .fontSize(30)
        }, (item: string) => item)
      }
      .cachedCount(2)
      .index(1)
      .autoPlay(true)
      .interval(4000)
      .loop(true)
      .indicatorInteractive(true)
      .duration(1000)
      .itemSpace(5)
      .prevMargin(35)
      .nextMargin(35)
      .indicator ( // Set the dot-style navigation indicator.
        new DotIndicator()
          .itemWidth(15)
          .itemHeight(15)
          .selectedItemWidth(15)
          .selectedItemHeight(15)
          .color(Color.Gray)
          .selectedColor(Color.Blue))
      .displayArrow({ // Set the arrow-style navigation indicator.
        showBackground: true,
        isSidebarMiddle: true,
        backgroundSize: 24,
        backgroundColor: Color.White,
        arrowSize: 18,
        arrowColor: Color.Blue
      }, false)
      .curve(Curve.Linear)
      .onChange((index: number) => {
        console.info(index.toString());
      })
      .onScrollStateChanged((event: ScrollState) => {
        console.info("event: " + event);
      })
      .onGestureSwipe((index: number, extraInfo: SwiperAnimationEvent) => {
        console.info("index: " + index);
        console.info("current offset: " + extraInfo.currentOffset);
      })
      .onAnimationStart((index: number, targetIndex: number, extraInfo: SwiperAnimationEvent) => {
        console.info("index: " + index);
        console.info("targetIndex: " + targetIndex);
        console.info("current offset: " + extraInfo.currentOffset);
        console.info("target offset: " + extraInfo.targetOffset);
        console.info("velocity: " + extraInfo.velocity);
      })
      .onAnimationEnd((index: number, extraInfo: SwiperAnimationEvent) => {
        console.info("index: " + index);
        console.info("current offset: " + extraInfo.currentOffset);
      })

      Row({ space: 12 }) {
        Button('showPrevious')
          .onClick(() => {
            this.swiperController.showPrevious();
          })
        Button('showNext')
          .onClick(() => {
            this.swiperController.showNext();
          })
      }.margin(5)
      Row({ space: 5 }) {
        Button('FAST 0')
          .onClick(() => {
            // Controller: Jump to index 0 and use the fast animation mode.
            this.swiperController.changeIndex(0, SwiperAnimationMode.FAST\_ANIMATION);
          })
        Button('FAST 3')
          .onClick(() => {
            // Controller: Jump to index 3 and use the fast animation mode.
            this.swiperController.changeIndex(3, SwiperAnimationMode.FAST\_ANIMATION);
          })
        Button('FAST ' + 9)
          .onClick(() => {
            // Controller: Jump to index 9 and use the fast animation mode.
            this.swiperController.changeIndex(9, SwiperAnimationMode.FAST\_ANIMATION);
          })
      }.margin(5)
    }.width('100%')
    .margin({ top: 5 })
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/57/v3/ziTwAIFkRCymM69Ggy5o1A/en-us_image_0000002537765544.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062239Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9F8ED938778DDE04874EA33A955C6175D34499F6C6D69FA66D320A1ADE401A38)

## Example 2: Implementing a Digit Indicator

This example uses the [DigitIndicator](#digitindicator10) API to implement a digit-style indicator.

// xxx.ets
class MyDataSource implements IDataSource {
  private list: number\[\] = \[\];

  constructor(list: number\[\]) {
    this.list = list;
  }

  totalCount(): number {
    return this.list.length;
  }

  getData(index: number): number {
    return this.list\[index\];
  }

  registerDataChangeListener(listener: DataChangeListener): void {
  }

  unregisterDataChangeListener() {
  }
}

@Entry
@Component
struct SwiperExample {
  private swiperController: SwiperController = new SwiperController();
  private data: MyDataSource = new MyDataSource(\[\]);

  aboutToAppear(): void {
    let list: number\[\] = \[\];
    for (let i = 1; i <= 10; i++) {
      list.push(i);
    }
    this.data = new MyDataSource(list);
  }

  build() {
    Column({ space: 5 }) {
      Swiper(this.swiperController) {
        LazyForEach(this.data, (item: string) => {
          Text(item.toString())
            .width('90%')
            .height(160)
            .backgroundColor(0xAFEEEE)
            .textAlign(TextAlign.Center)
            .fontSize(30)
        }, (item: string) => item)
      }
      .cachedCount(2)
      .index(1)
      .autoPlay(true)
      .interval(4000)
      .indicator(Indicator.digit() // Set the digit-style navigation indicator.
        .top(200)
        .fontColor(Color.Gray)
        .selectedFontColor(Color.Gray)
        .digitFont({ size: 20, weight: FontWeight.Bold })
        .selectedDigitFont({ size: 20, weight: FontWeight.Normal }))
      .loop(true)
      .duration(1000)
      .itemSpace(0)
      .displayArrow(true, false)

      Row({ space: 12 }) {
        Button('showNext')
          .onClick(() => {
            this.swiperController.showNext();
          })
        Button('showPrevious')
          .onClick(() => {
            this.swiperController.showPrevious();
          })
      }.margin(5)
    }.width('100%')
    .margin({ top: 5 })
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2f/v3/iRw6MuE8RK6zLSoUHE6s_g/en-us_image_0000002537925484.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062239Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4E183233889E39E48A2FA90BE65D3BB49B453E39DE602622BF99B8CB76275A1F)

## Example 3: Setting the Page Turning by Group

This example demonstrates how to implement the group-based page turning effect using the [displayCount](#displaycount8) attribute.

// xxx.ets
class MyDataSource implements IDataSource {
  private list: number\[\] = \[\];

  constructor(list: number\[\]) {
    this.list = list;
  }

  totalCount(): number {
    return this.list.length;
  }

  getData(index: number): number {
    return this.list\[index\];
  }

  registerDataChangeListener(listener: DataChangeListener): void {
  }

  unregisterDataChangeListener() {
  }
}

@Entry
@Component
struct SwiperExample {
  private swiperController: SwiperController = new SwiperController();
  private data: MyDataSource = new MyDataSource(\[\]);

  aboutToAppear(): void {
    let list: number\[\] = \[\];
    for (let i = 1; i <= 10; i++) {
      list.push(i);
    }
    this.data = new MyDataSource(list);
  }

  build() {
    Column({ space: 5 }) {
      Swiper(this.swiperController) {
        LazyForEach(this.data, (item: string) => {
          Text(item.toString())
            .width('90%')
            .height(160)
            .backgroundColor(0xAFEEEE)
            .textAlign(TextAlign.Center)
            .fontSize(30)
        }, (item: string) => item)
      }
      .displayCount (3, true) // Enable the function of turning pages by group. Three carousel items are displayed on each page, and the entire group is switched during page turning.
      .autoPlay(true)
      .interval(4000)
      .loop(true)
      .duration(1000)
      .itemSpace(10)
      .indicator ( // Set the dot-style navigation indicator.
        new DotIndicator()
          .itemWidth(15)
          .itemHeight(15)
          .selectedItemWidth(15)
          .selectedItemHeight(15)
          .color(Color.Gray)
          .selectedColor(Color.Blue))

      Row({ space: 12 }) {
        Button('showNext')
          .onClick(() => {
            this.swiperController.showNext();
          })
        Button('showPrevious')
          .onClick(() => {
            this.swiperController.showPrevious();
          })
      }.margin(5)
    }.width('100%')
    .margin({ top: 5 })
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7e/v3/kfsQW-vXR8qmVdVymtJOsA/en-us_image_0000002568685261.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062239Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=28DF634CE363028AB159ADE60E1377E7F627B601EA02F521FF44C626E375B8DD)

## Example 4: Customizing the Page Transition Animation

This example presents how to implement a custom page transition animation for the **Swiper** component through the [customContentTransition](#customcontenttransition12) API.

// EntryAbility.ets
import { Configuration, UIAbility } from '@kit.AbilityKit';
import { i18n } from '@kit.LocalizationKit';
import { CommonUtil } from '../common/CommonUtil';

export default class EntryAbility extends UIAbility {
  onConfigurationUpdate(newConfig: Configuration): void {
    // Listen for system configuration changes.
    if (newConfig.language) {
      CommonUtil.setIsRTL(i18n.isRTL(newConfig.language));
    }
  }
}

// CommonUtil.ets
export class CommonUtil {
  private static isRTL: boolean = false;

  public static setIsRTL(isRTL: boolean): void {
    CommonUtil.isRTL = isRTL;
  }

  public static getIsRTL(): boolean {
    return CommonUtil.isRTL;
  }
}

// xxx.ets
import { CommonUtil } from '../common/CommonUtil';

@Entry
@Component
struct SwiperCustomAnimationExample {
  private DISPLAY\_COUNT: number = 2;
  private MIN\_SCALE: number = 0.75;

  @State backgroundColors: Color\[\] = \[Color.Green, Color.Blue, Color.Yellow, Color.Pink, Color.Gray, Color.Orange\];
  @State opacityList: number\[\] = \[\];
  @State scaleList: number\[\] = \[\];
  @State translateList: number\[\] = \[\];
  @State zIndexList: number\[\] = \[\];

  aboutToAppear(): void {
    for (let i = 0; i < this.backgroundColors.length; i++) {
      this.opacityList.push(1.0);
      this.scaleList.push(1.0);
      this.translateList.push(0.0);
      this.zIndexList.push(0);
    }
  }

  build() {
    Column() {
      Swiper() {
        ForEach(this.backgroundColors, (backgroundColor: Color, index: number) => {
          Text(index.toString()).width('100%').height('100%').fontSize(50).textAlign(TextAlign.Center)
            .backgroundColor(backgroundColor)
            // Customize how the opacity, scale, translate, and other properties change during the custom page transition animation.
            .opacity(this.opacityList\[index\])
            .scale({ x: this.scaleList\[index\], y: this.scaleList\[index\] })
            .translate({ x: this.translateList\[index\] })
            .zIndex(this.zIndexList\[index\])
        })
      }
      .height(300)
      .indicator(false)
      .displayCount(this.DISPLAY\_COUNT, true)
      .customContentTransition({
        // The page is removed from the render tree when 1000 ms (timeout time) has elapsed.
        timeout: 1000,
        // Called on a frame-by-frame basis for all pages in the viewport. You can change the values of attributes such as opacity, scale, translate, and zIndex in the callback to implement a custom animation.
        transition: (proxy: SwiperContentTransitionProxy) => {
          if (!CommonUtil.getIsRTL()) {
            if (proxy.position <= proxy.index % this.DISPLAY\_COUNT || proxy.position >= this.DISPLAY\_COUNT + proxy.index % this.DISPLAY\_COUNT) {
              // Reset the attribute values when a page in the same group is swiped left or is swiped right to be completely out of the viewport.
              this.opacityList\[proxy.index\] = 1.0;
              this.scaleList\[proxy.index\] = 1.0;
              this.translateList\[proxy.index\] = 0.0;
              this.zIndexList\[proxy.index\] = 0;
            } else {
              // When a page in the same group is swiped right but is still within the viewport, the attribute values of the left and right pages in the same group are changed frame by frame based on the position. The changes implement the custom page transition animation in which the two pages move close to the middle of the <Swiper> and are transparently scaled in or out.
              if (proxy.index % this.DISPLAY\_COUNT === 0) {
                this.opacityList\[proxy.index\] = 1 - proxy.position / this.DISPLAY\_COUNT;
                this.scaleList\[proxy.index\] = this.MIN\_SCALE + (1 - this.MIN\_SCALE) \* (1 - proxy.position / this.DISPLAY\_COUNT);
                this.translateList\[proxy.index\] = -proxy.position \* proxy.mainAxisLength + (1 - this.scaleList\[proxy.index\]) \* proxy.mainAxisLength / 2.0;
              } else {
                this.opacityList\[proxy.index\] = 1 - (proxy.position - 1) / this.DISPLAY\_COUNT;
                this.scaleList\[proxy.index\] = this.MIN\_SCALE + (1 - this.MIN\_SCALE) \* (1 - (proxy.position - 1) / this.DISPLAY\_COUNT);
                this.translateList\[proxy.index\] = -(proxy.position - 1) \* proxy.mainAxisLength - (1 - this.scaleList\[proxy.index\]) \* proxy.mainAxisLength / 2.0;
              }
              this.zIndexList\[proxy.index\] = -1;
            }
          } else {
            // Layout adaptation for right-to-left scripts
            if (proxy.position >= -proxy.index % this.DISPLAY\_COUNT || proxy.position <= -this.DISPLAY\_COUNT - proxy.index % this.DISPLAY\_COUNT) {
              // Reset the properties when a page in the same group is swiped out of the viewport.
              this.opacityList\[proxy.index\] = 1.0;
              this.scaleList\[proxy.index\] = 1.0;
              this.translateList\[proxy.index\] = 0.0;
              this.zIndexList\[proxy.index\] = 0;
            } else {
              // When a page in the same group is swiped left but is still within the viewport, modify property values frame by frame based on the position for the left and right pages in the group to achieve a custom transition animation where the two pages move toward the center of the Swiper with opacity and scaling effects.
              if (proxy.index % this.DISPLAY\_COUNT === 0) {
                this.opacityList\[proxy.index\] = 1 + proxy.position / this.DISPLAY\_COUNT;
                this.scaleList\[proxy.index\] = this.MIN\_SCALE + (1 - this.MIN\_SCALE) \* (1 + proxy.position / this.DISPLAY\_COUNT);
                this.translateList\[proxy.index\] = -proxy.position \* proxy.mainAxisLength - (1 - this.scaleList\[proxy.index\]) \* proxy.mainAxisLength / 2.0;
              } else {
                this.opacityList\[proxy.index\] = 1 + (proxy.position + 1) / this.DISPLAY\_COUNT;
                this.scaleList\[proxy.index\] = this.MIN\_SCALE + (1 - this.MIN\_SCALE) \* (1 + (proxy.position + 1) / this.DISPLAY\_COUNT);
                this.translateList\[proxy.index\] = -(proxy.position + 1) \* proxy.mainAxisLength + (1 - this.scaleList\[proxy.index\]) \* proxy.mainAxisLength / 2.0;
              }
              this.zIndexList\[proxy.index\] = -1;
            }
          }
        }
      })
      .onContentDidScroll((selectedIndex: number, index: number, position: number, mainAxisLength: number) => {
        // Listen for Swiper page scroll events. In this callback, you can customize the navigation indicator animation.
        console.info("onContentDidScroll selectedIndex: " + selectedIndex + ", index: " + index + ", position: " + position + ", mainAxisLength: " + mainAxisLength);
      })
    }.width('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5a/v3/GnSahovuQY2Dwmrkgo4QpA/en-us_image_0000002568765271.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062239Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=BC0CEA482606E79B044B29C031A98EFAD832D6CF30B5F2FFD85AE743C4597662)

## Example 5: Configuring Overflow for the Dot-Style Indicator

This example demonstrates how to implement an animation for the overflow effect when the number of navigation dots exceeds the limit set through the [maxDisplayCount](#maxdisplaycount12) property of the **DotIndicator** API.

class MyDataSource implements IDataSource {
  private list: number\[\] = \[\];

  constructor(list: number\[\]) {
    this.list = list;
  }

  totalCount(): number {
    return this.list.length;
  }

  getData(index: number): number {
    return this.list\[index\];
  }

  registerDataChangeListener(listener: DataChangeListener): void {
  }

  unregisterDataChangeListener() {
  }
}

@Entry
@Component
struct Index {
  private swiperController: SwiperController = new SwiperController();
  private data: MyDataSource = new MyDataSource(\[\]);

  aboutToAppear(): void {
    let list: number\[\] = \[\];
    for (let i = 1; i <= 15; i++) {
      list.push(i);
    }
    this.data = new MyDataSource(list);
  }

  build() {
    Column({ space: 5 }) {
      Swiper(this.swiperController) {
        LazyForEach(this.data, (item: string) => {
          Text(item.toString())
            .width('90%')
            .height(160)
            .backgroundColor(0xAFEEEE)
            .textAlign(TextAlign.Center)
            .fontSize(30)
        }, (item: string) => item)
      }
      .cachedCount(2)
      .index(5)
      .autoPlay(true)
      .interval(4000)
      .loop(true)
      .duration(1000)
      .itemSpace(0)
      .indicator ( // Set the dot-style navigation indicator.
        new DotIndicator()
          .itemWidth(8)
          .itemHeight(8)
          .selectedItemWidth(16)
          .selectedItemHeight(8)
          .color(Color.Gray)
          .selectedColor(Color.Blue)
          .maxDisplayCount(9)) // Set the maximum number of navigation indicators to 9.
      .displayArrow({ // Set the arrow-style navigation indicator.
        showBackground: true,
        isSidebarMiddle: true,
        backgroundSize: 24,
        backgroundColor: Color.White,
        arrowSize: 18,
        arrowColor: Color.Blue
      }, false)
      .curve(Curve.Linear)
      Row({ space: 12 }) {
        Button('showNext')
          .onClick(() => {
            this.swiperController.showNext();
          })
        Button('showPrevious')
          .onClick(() => {
            this.swiperController.showPrevious();
          })
      }.margin(5)
    }.width('100%')
    .margin({ top: 5 })
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/43/v3/hkaZpQPhRcmqhKBcIM4jfA/en-us_image_0000002537765546.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062239Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F85359C3691EB10D3B9C7300AB1B81D55EA715883202A4BBB67F2853A5BDDC67)

## Example 6: Preloading Child Nodes

This example demonstrates how to use the [preloadItems](#preloaditems18) API to preload specified child nodes.

// xxx.ets
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct SwiperPreloadItems {
  @State currentIndex: number = 1;
  private swiperController: SwiperController = new SwiperController();
  @State arr: string\[\] = \["0", "1", "2", "3", "4", "5"\];

  build() {
    Column() {
      Swiper(this.swiperController) {
        ForEach(this.arr, (item: string) => {
          MyComponent({ txt: item })
        })
      }
      .cachedCount(1, true)
      .width("70%")
      .height("50%")

      Button('preload items: \[2, 3\]')
        .margin(5)
        .onClick(() => {
          // Preload child nodes with index=2 and index=3.
          try {
            this.swiperController.preloadItems(\[2, 3\])
              .then(() => {
                console.info('preloadItems \[2, 3\] success.');
              })
              .catch((error: BusinessError) => {
                console.error('preloadItems \[2, 3\] failed, error code: ' + error.code + ', error message: ' + error.message);
              })
          } catch (error) {
            console.error('preloadItems \[2, 3\] failed, error code: ' + error.code + ', error message: ' + error.message);
          }

        })
    }
    .width("100%")
    .margin(5)
  }
}

@Component
struct MyComponent {
  private txt: string = "";

  aboutToAppear(): void {
    console.info('aboutToAppear txt:' + this.txt);
  }

  aboutToDisappear(): void {
    console.info('aboutToDisappear txt:' + this.txt);
  }

  build() {
    Text(this.txt)
      .textAlign(TextAlign.Center)
      .width('100%')
      .height('100%')
      .backgroundColor(0xAFEEEE)
  }
}

## Example 7: Implementing Synchronized Switching Between the Tabs and Swiper Components

This example associates [Tabs](../../navigation-and-switching/tabs/document.md) with the **Swiper** component through the [onSelected](#onselected18) API.

// xxx.ets
class MyDataSource implements IDataSource {
  private list: number\[\] = \[\];

  constructor(list: number\[\]) {
    this.list = list;
  }

  totalCount(): number {
    return this.list.length;
  }

  getData(index: number): number {
    return this.list\[index\];
  }

  registerDataChangeListener(listener: DataChangeListener): void {
  }

  unregisterDataChangeListener() {
  }
}

@Entry
@Component
struct TabsSwiperExample {
  @State fontColor: string = '#182431';
  @State selectedFontColor: string = '#007DFF';
  @State currentIndex: number = 0;
  private list: number\[\] = \[\];
  private tabsController: TabsController = new TabsController();
  private swiperController: SwiperController = new SwiperController();
  private swiperData: MyDataSource = new MyDataSource(\[\]);

  aboutToAppear(): void {
    for (let i = 0; i <= 9; i++) {
      this.list.push(i);
    }
    this.swiperData = new MyDataSource(this.list);
  }

  @Builder tabBuilder(index: number, name: string) {
    Column() {
      Text(name)
        .fontColor(this.currentIndex === index ? this.selectedFontColor : this.fontColor)
        .fontSize(16)
        .fontWeight(this.currentIndex === index ? 500 : 400)
        .lineHeight(22)
        .margin({ top: 17, bottom: 7 })
      Divider()
        .strokeWidth(2)
        .color('#007DFF')
        .opacity(this.currentIndex === index ? 1 : 0)
    }.width('20%')
  }

  build() {
    Column() {
      Tabs({ barPosition: BarPosition.Start, controller: this.tabsController }) {
        ForEach(this.list, (index: number) =>{
          TabContent().tabBar(this.tabBuilder(index, 'Tab ' + this.list\[index\]))
        })
      }
      .onTabBarClick((index: number) => {
        this.currentIndex = index;
        this.swiperController.changeIndex(index, true);
      })
      .barMode(BarMode.Scrollable)
      .backgroundColor('#F1F3F5')
      .height(56)
      .width('100%')

      Swiper(this.swiperController) {
        LazyForEach(this.swiperData, (item: string) => {
          Text(item.toString())
            .onAppear(()=>{
              console.info('onAppear ' + item.toString());
            })
            .onDisAppear(()=>{
              console.info('onDisAppear ' + item.toString());
            })
            .width('100%')
            .height('40%')
            .backgroundColor(0xAFEEEE)
            .textAlign(TextAlign.Center)
            .fontSize(30)
        }, (item: string) => item)
      }
      .loop(false)
      // Triggered when a tab is selected or switched.
      .onSelected((index: number) => {
        console.info("onSelected:" + index);
        // Synchronize the selected index to currentIndex (update the selected tab).
        this.currentIndex = index;
        // Control the Tabs component to switch to the tab with the specified index.
        this.tabsController.changeIndex(index);
      })
    }
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/30/v3/DVnjvf6MSCq8WtxOIH5JKg/en-us_image_0000002537925486.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062239Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=ABA9C9F612901E1690C07BE0C1BE231428EA6D79A8DCE32B56F7AF557519CEA0)

## Example 8: Intercepting the Scrolling Behavior

This example demonstrates how to use the [onContentWillScroll](#oncontentwillscroll15) event to allow only forward scrolling and intercept backward scrolling.

// xxx.ets
class MyDataSource implements IDataSource {
  private list: number\[\] = \[\];

  constructor(list: number\[\]) {
    this.list = list;
  }

  totalCount(): number {
    return this.list.length;
  }

  getData(index: number): number {
    return this.list\[index\];
  }

  registerDataChangeListener(listener: DataChangeListener): void {
  }

  unregisterDataChangeListener() {
  }
}

@Entry
@Component
struct SwiperExample {
  private swiperController: SwiperController = new SwiperController();
  private data: MyDataSource = new MyDataSource(\[\]);
  private currentIndex: number = 4;

  aboutToAppear(): void {
    let list: number\[\] = \[\];
    for (let i = 1; i <= 10; i++) {
      list.push(i);
    }
    this.data = new MyDataSource(list);
  }

  build() {
    Column({ space: 5 }) {
      Swiper(this.swiperController) {
        LazyForEach(this.data, (item: string) => {
          Text(item.toString())
            .width('90%')
            .height(160)
            .backgroundColor(0xAFEEEE)
            .textAlign(TextAlign.Center)
            .fontSize(30)
        }, (item: string) => item)
      }
      .index(this.currentIndex)
      .loop(false)
      .onChange((index: number) => {
        this.currentIndex = index;
      })
      .onContentWillScroll((result: SwiperContentWillScrollResult) => {
        // result.comingIndex: target index that is about to be swiped to.
        // Interception logic:
        // 1. If the target index is greater than the current index, return false to intercept the scrolling behavior.
        // 2. If the target index is less than the current index, return true to allow the scrolling behavior.
        if (result.comingIndex > this.currentIndex) {
          return false;
        }
        return true;
      })

      Row({ space: 12 }) {
        Button('showNext')
          .onClick(() => {
            this.swiperController.showNext();
          })
        Button('showPrevious')
          .onClick(() => {
            this.swiperController.showPrevious();
          })
      }.margin(5)
    }.width('100%')
    .margin({ top: 5 })
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/42/v3/45ylqrr7S6qvuWHRnOdgWg/en-us_image_0000002568685263.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062239Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0C3B3B1750F1C2B3E6A2BA1A185DC3955146C5D06DF0F338A9111D1309819CCD)

## Example 9: Using the space and bottom APIs on the Navigation Indicator

This example uses the [bottom](#bottom19) and [space](#space19) APIs to achieve zero spacing control between the dot-style navigation indicators and the bottom, as well as spacing control between navigation indicators.

import { LengthMetrics } from '@kit.ArkUI';

// MyDataSource.ets
class MyDataSource implements IDataSource {
  private list: number\[\] = \[\];

  constructor(list: number\[\]) {
    this.list = list;
  }

  totalCount(): number {
    return this.list.length;
  }

  getData(index: number): number {
    return this.list\[index\];
  }

  registerDataChangeListener(listener: DataChangeListener): void {
  }

  unregisterDataChangeListener() {
  }
}

// SwiperExample.ets
@Entry
@Component
struct SwiperExample {

  @State space: LengthMetrics = LengthMetrics.vp(0);
  @State spacePool: LengthMetrics\[\] = \[LengthMetrics.vp(0), LengthMetrics.px(3), LengthMetrics.vp(10)\];
  @State spaceIndex: number = 0;

  @State ignoreSize: boolean = false;
  @State ignoreSizePool: boolean\[\] = \[false, true\];
  @State ignoreSizeIndex: number = 0;

  private swiperController1: SwiperController = new SwiperController();
  private data1: MyDataSource = new MyDataSource(\[\]);

  aboutToAppear(): void {
    let list1: number\[\] = \[\];
    for (let i = 1; i <= 10; i++) {
      list1.push(i);
    }
    this.data1 = new MyDataSource(list1);
  }

  build() {
    Scroll() {
      Column({ space: 20 }) {
        Swiper(this.swiperController1) {
          LazyForEach(this.data1, (item: string) => {
            Text(item.toString())
              .width('90%')
              .height(120)
              .backgroundColor(0xAFEEEE)
              .textAlign(TextAlign.Center)
              .fontSize(30)
          }, (item: string) => item)
        }
        .indicator(new DotIndicator()
          .space (this.space) // Control the spacing between navigation indicators.
          .bottom(LengthMetrics.vp(0), this.ignoreSize) // Control the spacing between the navigation indicators and the bottom of the Swiper component.
          .itemWidth(15)
          .itemHeight(15)
          .selectedItemWidth(15)
          .selectedItemHeight(15)
          .color(Color.Gray)
          .selectedColor(Color.Blue))
        .displayArrow({
          showBackground: true,
          isSidebarMiddle: true,
          backgroundSize: 24,
          backgroundColor: Color.White,
          arrowSize: 18,
          arrowColor: Color.Blue
        }, false)
        
        Column({ space: 4 }) {
          Button('spaceIndex:' + this.spaceIndex).onClick(() => {
            this.spaceIndex = (this.spaceIndex + 1) % this.spacePool.length;
            this.space = this.spacePool\[this.spaceIndex\];
          }).margin(10)

          Button('ignoreSizeIndex:' + this.ignoreSizeIndex).onClick(() => {
            this.ignoreSizeIndex = (this.ignoreSizeIndex + 1) % this.ignoreSizePool.length;
            this.ignoreSize = this.ignoreSizePool\[this.ignoreSizeIndex\];
          }).margin(10)
        }.margin(2)
      }.width('100%')
    }
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/39/v3/7nqRqwsFRJ-0F6A5Feg_ew/en-us_image_0000002568765273.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062239Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=227923064BABF8302068784E075C1F7AED5018ED223D8FC41AD1711AE59B6D28)

## Example 10: Displaying the Number of Elements Displayed in the Swiper Component Based on Breakpoints

This example demonstrates how to set the number of elements displayed in the **Swiper** viewport based on breakpoints.

From API version 22 onwards, the [displaycount](#displaycount22) API is added to set the number of elements displayed in the **Swiper** viewport.

class MyDataSource implements IDataSource {
  private list: number\[\] = \[\];

  constructor(list: number\[\]) {
    this.list = list;
  }

  totalCount(): number {
    return this.list.length;
  }

  getData(index: number): number {
    return this.list\[index\];
  }

  registerDataChangeListener(listener: DataChangeListener): void {
  }

  unregisterDataChangeListener() {
  }
}

@Entry
@Component
struct SwiperExample {
  private data: MyDataSource = new MyDataSource(\[\]);

  aboutToAppear(): void {
    let list: number\[\] = \[\];
    for (let i = 1; i <= 10; i++) {
      list.push(i);
    }
    this.data = new MyDataSource(list);
  }

  build() {
    Column() {
      Swiper() {
        LazyForEach(this.data, (item: string) => {
          Text(item.toString())
            .height(160)
            .backgroundColor(0xAFEEEE)
            .textAlign(TextAlign.Center)
            .fontSize(30)
        }, (item: string) => item)
      }
      .width('100%')
      .displayCount({fillType:PresetFillType.BREAKPOINT\_SM1MD2LG3}) // Set the number of elements to be displayed in a viewport based on breakpoints.
    }
  }
}

When the **Swiper** width falls within the [sm](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-layout-development-grid-layout#breakpoints) and smaller breakpoint range, one column is displayed.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a8/v3/xGhOyeA7SSWnadmO5uz_rA/en-us_image_0000002537765548.jpg?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062239Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0024E74D870EC358D3ED08EEF05D8E4D80FF94D796A86737AE0A1F0C31A7F1E3)

When the **Swiper** width falls within the \[md\](../../../ui/arkts-layout-development-grid-layout.md#breakpoints\], two columns are displayed.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cf/v3/zptqE7EySkmDe9pBfagRVQ/en-us_image_0000002537925488.jpg?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062239Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=25D7752961A2E200BBD0589F73C5E30D2F202DA0FB65296D2727E6BC6A6B84C9)
