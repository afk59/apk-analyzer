# Stack

The **Stack** component provides a stack container where child components are successively stacked and the latter one overwrites the previous one.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6b/v3/DIRHkvvHTdyxSABdOTNQEQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062237Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=58CA4E3F2631B96C39BD7E150C5BB2164486FBA6CA969A42F9ABEDB3EA61B453)

-   This component is supported since API version 7. Updates will be marked with a superscript to indicate their earliest API version.
    
-   The general attribute [align](../../universal-attributes/layout-and-borders/location/document.md#align) supports the mirroring capability on this component.
    

#### Child Components

Supported.

#### APIs

Stack(options?: StackOptions)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/28/v3/m55LC8IWT8u4aDgRFAZspQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062237Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E1D7E01FD5E845E3E4B734B9A48EA9CC945DC6B715F3AF7AC0DC444C8CCCDD9A)

Excessive component nesting can lead to performance degradation. In some scenarios, using component attributes directly or leveraging system APIs can achieve the same effect as the stack container, reducing the number of nested components and optimizing performance. For best practices, see [Preferentially Using Component Properties Instead of Nested Components](https://developer.huawei.com/consumer/en/doc/best-practices/bpta-component-nesting-optimization#section78181114123811).

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| options | [StackOptions](#stackoptions18) | No | Alignment of child components in the container. |

#### StackOptions18+

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/38/v3/7pxed-ofTmiIO3-1kECDaw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062237Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=282704DEB07B9D40D9130E19C23C03D0AE94658A95D47F0DE85C7AB33E1BA01E)

To standardize anonymous object definitions, the element definitions here have been revised in API version 18. The initial version information of the historical anonymous objects has been retained, which may result in the outer element's @since version number being later than the inner element's version number. However, this does not affect the use of the API.

**Widget capability**: This API can be used in ArkTS widgets since API version 18.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| alignContent7+ | [Alignment](../../common-definitions/enums/document.md#alignment) | No | Yes | 
Alignment of child components in the container.

Default value: **Alignment.Center**

Invalid values are treated as the default value.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |

#### Attributes

In addition to the [universal attributes](../../universal-attributes/document.md), the following attributes are supported.

#### \[h2\]alignContent

alignContent(value: Alignment)

Sets the alignment of child components in the container. When both this attribute and the [align](../../universal-attributes/layout-and-borders/location/document.md#align) attribute are set, whichever is set last takes effect. When this attribute and the constructor input parameters are set simultaneously, the attribute setting prevails.

**Atomic service API**: This API can be used in atomic services since API version 11.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [Alignment](../../common-definitions/enums/document.md#alignment) | Yes | 
Alignment of child components in the container.

Default value: **Alignment.Center**

Invalid values are treated as the default value.

 |

#### Events

The [universal events](../../universal-events/document.md) are supported.

#### Example

This example demonstrates the display effect of child components when the **alignContent** attribute of the **Stack** component is set to **Alignment.Bottom**.

// xxx.ets
@Entry
@Component
struct StackExample {
  build() {
    Stack({ alignContent: Alignment.Bottom }) {
      Text('First child, show in bottom').width('90%').height('100%').backgroundColor(0xd2cab3).align(Alignment.Top)
      Text('Second child, show in top').width('70%').height('60%').backgroundColor(0xc1cbac).align(Alignment.Top)
    }.width('100%').height(150).margin({ top: 5 })
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/02/v3/lyJUyoShSnuwoeud7kFBDQ/en-us_image_0000002537925442.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062237Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=70E07F4DB80992BE900243A7A2EA04B8CD962E8DC8FD16660386BF58DDC00B1F)
