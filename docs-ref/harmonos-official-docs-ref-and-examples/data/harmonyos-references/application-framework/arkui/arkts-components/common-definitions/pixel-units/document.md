# Pixel Units

ArkUI provides four pixel units, with vp as the reference data unit.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/51/v3/IKFN5ST2SACIPbK2L94CUw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062252Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D5D36C19324E56CE66A95EC550EE8B4245AC1DA6549668EF358030F9B86BA888)

-   The initial APIs of this module are supported since API version 7. Newly added APIs will be marked with a superscript to indicate their earliest API version.
    
-   Directly using vp2px/px2vp/fp2px/px2fp/lpx2px/px2lpx may cause issues due to [ambiguous UI context](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-global-interface#ambiguous-ui-context). The following APIs are deprecated since API version 18. It is recommended to obtain a [UIContext](../../../arkts-api/ui/ohos-arkui-uicontext-uicontext/class-uicontext/document.md) instance via **getUIContext()** and then use the [vp2px](../../../arkts-api/ui/ohos-arkui-uicontext-uicontext/class-uicontext/document.md#vp2px12)/[px2vp](../../../arkts-api/ui/ohos-arkui-uicontext-uicontext/class-uicontext/document.md#px2vp12)/[fp2px](../../../arkts-api/ui/ohos-arkui-uicontext-uicontext/class-uicontext/document.md#fp2px12)/[px2fp](../../../arkts-api/ui/ohos-arkui-uicontext-uicontext/class-uicontext/document.md#px2fp12)/[lpx2px](../../../arkts-api/ui/ohos-arkui-uicontext-uicontext/class-uicontext/document.md#lpx2px12)/[px2lpx](../../../arkts-api/ui/ohos-arkui-uicontext-uicontext/class-uicontext/document.md#px2lpx12) under **UIContext** to call instance-bound APIs.
    
-   When no UI instance is created, vp2px/px2vp uses the default screen's virtual pixel ratio for conversion. In this scenario, if you need to replace this API with a UIContext-based one, refer to [Replacing Pixel Unit Conversion APIs with UIContext APIs](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-global-interface#replacing-pixel-unit-conversion-apis-with-uicontext-apis).
    

| Name | Description |
| :-- | :-- |
| px | Physical pixel unit of the screen. |
| vp | 
Pixel unit specific to the screen density. Pixels in this unit are converted into physical pixels of the screen based on the screen pixel density. This unit is used for values whose unit is not specified.

**NOTE**

The ratio of vp to px is subject to the screen pixel density.

 |
| fp | Font pixel, which is similar to vp and varies according to the system font size. |
| lpx | Logical pixel unit of the window. It is the ratio of the actual screen width to the logical width (configured by [designWidth](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/module-configuration-file#pages)). For example, if **designWidth** is set to **720** (default value), then 1 lpx is equal to 2 px for a screen with an actual width of 1440 physical pixels. |

#### vp2px(deprecated)

vp2px(value: number): number

Converts a value in units of vp to a value in units of px.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4b/v3/OZvWSGNIQjWuu9fSydFZxA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062252Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=571F2F08EB9C1AF5F31138DC145C15503634351310472B5B81CC56797028A412)

By default, the virtual pixel ratio of the screen hosting the current UI instance is used for unit conversion. If the UI instance cannot be identified, the virtual pixel ratio of the default screen is used instead, which may lead to unexpected conversion results.

This API is supported since API version 7 and deprecated since API version 18. You are advised to use [vp2px](../../../arkts-api/ui/ohos-arkui-uicontext-uicontext/class-uicontext/document.md#vp2px12) instead.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | number | Yes | 
Value to convert.

Value range: (-∞, +∞).

 |

**Return value**

| Type | Description |
| :-- | :-- |
| number | 
Value after conversion.

Value range: (-∞, +∞).

 |

#### px2vp(deprecated)

px2vp(value: number): number

Converts a value in units of px to a value in units of vp.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/97/v3/6QFEbSPESze-sh78NLWqgA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062252Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=BA45F552774F971B210D391E8790119292F9C4EC8484EF6F538F08282C18098C)

By default, the virtual pixel ratio of the screen hosting the current UI instance is used for unit conversion. If the UI instance cannot be identified, the virtual pixel ratio of the default screen is used instead, which may lead to unexpected conversion results.

This API is supported since API version 7 and deprecated since API version 18. You are advised to use [px2vp](../../../arkts-api/ui/ohos-arkui-uicontext-uicontext/class-uicontext/document.md#px2vp12) instead.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | number | Yes | 
Value to convert.

Value range: (-∞, +∞).

 |

**Return value**

| Type | Description |
| :-- | :-- |
| number | 
Value after conversion.

Value range: (-∞, +∞).

 |

#### fp2px(deprecated)

fp2px(value: number): number

Converts a value in units of fp to a value in units of px.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6f/v3/Dejs3EUnQO22yWlmHApilw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062252Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=785BCF28267B8739372C7A95ACB901E9B2EEFCBB028FC2E7F7578F23067B576E)

This API is supported since API version 7 and deprecated since API version 18. You are advised to use [fp2px](../../../arkts-api/ui/ohos-arkui-uicontext-uicontext/class-uicontext/document.md#fp2px12) instead.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | number | Yes | 
Value to convert.

Value range: (-∞, +∞).

 |

**Return value**

| Type | Description |
| :-- | :-- |
| number | 
Value after conversion.

Value range: (-∞, +∞).

 |

#### px2fp(deprecated)

px2fp(value: number): number

Converts a value in units of px to a value in units of fp.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/92/v3/FfmtSUuSQcWWlwYA2gI3JQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062252Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=35095BF658301A430B7E0E7F81402CCCAAAF5DE593D65C27F5A31565E8AFDF77)

This API is supported since API version 7 and deprecated since API version 18. You are advised to use [px2fp](../../../arkts-api/ui/ohos-arkui-uicontext-uicontext/class-uicontext/document.md#px2fp12) instead.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | number | Yes | 
Value to convert.

Value range: (-∞, +∞).

 |

**Return value**

| Type | Description |
| :-- | :-- |
| number | 
Value after conversion.

Value range: (-∞, +∞).

 |

#### lpx2px(deprecated)

lpx2px(value: number): number

Converts a value in units of lpx to a value in units of px.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/51/v3/CvAFpL8bR92vwnm_es1AFg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062252Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C2225E6B27002B7CF7C9BA5D45CCBFF1E1AC6B0E0D94D12E1844D52B2A61C35A)

This API is supported since API version 7 and deprecated since API version 18. You are advised to use [lpx2px](../../../arkts-api/ui/ohos-arkui-uicontext-uicontext/class-uicontext/document.md#lpx2px12) instead.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | number | Yes | 
Value to convert.

Value range: (-∞, +∞).

 |

**Return value**

| Type | Description |
| :-- | :-- |
| number | 
Value after conversion.

Value range: (-∞, +∞).

 |

#### px2lpx(deprecated)

px2lpx(value: number): number

Converts a value in units of px to a value in units of lpx.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/69/v3/TDZgB0t_QUaXUgD-_ZvUdg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062252Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0FB4E34061393CB936F5542E7BC5982CD109653912E99ED9F11DB7909EB20D76)

This API is supported since API version 7 and deprecated since API version 18. You are advised to use [px2lpx](../../../arkts-api/ui/ohos-arkui-uicontext-uicontext/class-uicontext/document.md#px2lpx12) instead.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | number | Yes | 
Value to convert.

Value range: (-∞, +∞).

 |

**Return value**

| Type | Description |
| :-- | :-- |
| number | 
Value after conversion.

Value range: (-∞, +∞).

 |

#### Example

// xxx.ets
@Entry
@Component
struct Example {
  build() {
    Column() {
      Flex({ wrap: FlexWrap.Wrap }) {
        Column() {
          Text("width(220)")
            .width(220)
            .height(40)
            .backgroundColor(0xF9CF93)
            .textAlign(TextAlign.Center)
            .fontColor(Color.White)
            .fontSize('12vp')
        }.margin(5)

        Column() {
          Text("width('220px')")
            .width('220px')
            .height(40)
            .backgroundColor(0xF9CF93)
            .textAlign(TextAlign.Center)
            .fontColor(Color.White)
        }.margin(5)

        Column() {
          Text("width('220vp')")
            .width('220vp')
            .height(40)
            .backgroundColor(0xF9CF93)
            .textAlign(TextAlign.Center)
            .fontColor(Color.White)
            .fontSize('12vp')
        }.margin(5)

        Column() {
          Text("width('220lpx') designWidth:720")
            .width('220lpx')
            .height(40)
            .backgroundColor(0xF9CF93)
            .textAlign(TextAlign.Center)
            .fontColor(Color.White)
            .fontSize('12vp')
        }.margin(5)

        Column() {
          Text("width(vp2px(220) + 'px')")
            .width(this.getUIContext().vp2px(220) + 'px')
            .height(40)
            .backgroundColor(0xF9CF93)
            .textAlign(TextAlign.Center)
            .fontColor(Color.White)
            .fontSize('12vp')
        }.margin(5)

        Column() {
          Text("fontSize('12fp')")
            .width(220)
            .height(40)
            .backgroundColor(0xF9CF93)
            .textAlign(TextAlign.Center)
            .fontColor(Color.White)
            .fontSize('12fp')
        }.margin(5)

        Column() {
          Text("width(px2vp(220))")
            .width(this.getUIContext().px2vp(220))
            .height(40)
            .backgroundColor(0xF9CF93)
            .textAlign(TextAlign.Center)
            .fontColor(Color.White)
            .fontSize('12fp')
        }.margin(5)
      }.width('100%')
    }
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7c/v3/CsfauwZ3SKOaSjAfhZk_-w/en-us_image_0000002537766006.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062252Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C11F56E6CABE9712B12E467B90677B134D2AAF5CD3737E3C47147E6728015397)
