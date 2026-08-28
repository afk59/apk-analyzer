# Grid

The responsive grid configuration provides rules for layout design and resolves issues of dynamic layout across devices with different sizes, thereby ensuring layout consistency across layouts on different devices.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7b/v3/l4zctZAASB626AcZGebHDw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062253Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=31B9B7EFCE456609C4DE313E44DAF37C9D9EF29AB57B6C044E5C20FB341C052F)

-   The initial APIs of this module are supported since API version 7. Updates will be marked with a superscript to indicate their earliest API version.
    
-   This module is deprecated since API version 9. You are advised to use [GridCol](../../grid-and-column-layout/gridcol/document.md) and [GridRow](../../grid-and-column-layout/gridrow/document.md) instead.
    
-   The column width and column gap in the grid layout are determined by the nearest parent component **GridContainer**. The component tree that uses grid attributes must contain one **GridContainer** component or more.
    
-   To call the **gridSpan** or **gridOffset** attribute, its parent or ancestor component must be **GridContainer**.
    

#### Attributes

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Description |
| :-- | :-- | :-- |
| useSizeType(deprecated) | 
{

xs?: number | { span: number, offset: number },

sm?: number | { span: number, offset: number },

md?: number | { span: number, offset: number },

lg?: number | { span: number, offset: number }

}

 | 

Number of occupied columns and offset columns for a specific device width type. **span** indicates the number of occupied columns, and **offset** indicates the number of offset columns.

If the value is of the number type, only the number of columns can be set. If the value is in the format of {"span": 1, "offset": 0}, both the number of occupied columns and the number of offset columns need to be set.

\- **xs** indicates that the device width type is **SizeType.XS**.

\- **sm** indicates that the device width type is **SizeType.SM**.

\- **md** indicates that the device width type is **SizeType.MD**.

\- **lg** indicates that the device width type is **SizeType.LG**.

This attribute is deprecated since API version 9. You are advised to use [GridCol](../../grid-and-column-layout/gridcol/document.md) and [GridRow](../../grid-and-column-layout/gridrow/document.md) instead.

 |
| gridSpan(deprecated) | number | 

Default number of occupied columns, that is, the number of occupied columns when **span** in **useSizeType** is not set.

**NOTE**

If the **span** attribute is set, the component width is determined by the grid layout.

Default value: **1**

**Atomic service API**: This API can be used in atomic services since API version 11.

This attribute is deprecated since API version 14. You are advised to use [GridCol](../../grid-and-column-layout/gridcol/document.md) and [GridRow](../../grid-and-column-layout/gridrow/document.md) instead.

 |
| gridOffset(deprecated) | number | 

Default number of offset columns, that is, the number of offset columns in the start direction of the parent component (which is also the nth column where the component is located) when **offset** in **useSizeType** is not set.

**NOTE**

\- After this attribute is set, the horizontal layout of the current component does not follow the original layout of the parent component. Instead, it offsets along the start direction of the parent component.

\- Offset = (Column width + Gap) \* Number of columns.

\- After this attribute is set, sibling components will be arranged relatively to this component, as in the relative layout.

Default value: **0**

**Atomic service API**: This API can be used in atomic services since API version 11.

This attribute is deprecated since API version 14. You are advised to use [GridCol](../../grid-and-column-layout/gridcol/document.md) and [GridRow](../../grid-and-column-layout/gridrow/document.md) instead.

 |

#### Example

This example demonstrates how to set different widths for various device types and individually configure the **span** and **offset** attributes for components. It also shows how to implement the same effect using **useSizeType** for sm-sized devices.

// xxx.ets
@Entry
@Component
struct GridContainerExample1 {
  build() {
    Column() {
      Text('useSizeType').fontSize(15).fontColor(0xCCCCCC).width('90%')
      GridContainer() {
        Row() {
          Row() {
            Text('Left').fontSize(25)
          }
          .useSizeType({
            xs: { span: 1, offset: 0 }, sm: { span: 1, offset: 0 },
            md: { span: 1, offset: 0 }, lg: { span: 2, offset: 0 }
          })
          .height("100%")
          .backgroundColor(0x66bbb2cb)

          Row() {
            Text('Center').fontSize(25)
          }
          .useSizeType({
            xs: { span: 1, offset: 0 }, sm: { span: 2, offset: 1 },
            md: { span: 5, offset: 1 }, lg: { span: 7, offset: 2 }
          })
          .height("100%")
          .backgroundColor(0x66b6c5d1)

          Row() {
            Text('Right').fontSize(25)
          }
          .useSizeType({
            xs: { span: 1, offset: 0 }, sm: { span: 1, offset: 3 },
            md: { span: 2, offset: 6 }, lg: { span: 3, offset: 9 }
          })
          .height("100%")
          .backgroundColor(0x66bbb2cb)
        }
        .height(200)

      }
      .backgroundColor(0xf1f3f5)
      .margin({ top: 10 })

      // Set the span and offset of the component separately. The resultant effect is equivalent to that achieved by using sm in useSizeType on the device of the sm type.
      Text('gridSpan,gridOffset').fontSize(15).fontColor(0xCCCCCC).width('90%')
      GridContainer() {
        Row() {
          Row() {
            Text('Left').fontSize(25)
          }
          .gridSpan(1)
          .height("100%")
          .backgroundColor(0x66bbb2cb)

          Row() {
            Text('Center').fontSize(25)
          }
          .gridSpan(2)
          .gridOffset(1)
          .height("100%")
          .backgroundColor(0x66b6c5d1)

          Row() {
            Text('Right').fontSize(25)
          }
          .gridSpan(1)
          .gridOffset(3)
          .height("100%")
          .backgroundColor(0x66bbb2cb)
        }.height(200)
      }
    }
  }
}

**Figure 1** Device width type SM

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9f/v3/9kMDggtJTnSg-xAFtpukwg/en-us_image_0000002568765755.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062253Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=72BBBDC2555727F2B02189F062BB97F9E8E8DF2F1F9B069F361D0FD08718ED09)

**Figure 2** Device width type MD

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/13/v3/N8wPCtseQeWxOSSvzaLyJg/en-us_image_0000002537766030.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062253Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=68E53ED15C68A1F45F895DD220381DCB8EBFB2A7DA79E76B26E1ECE797EB5727)

**Figure 3** Device width type LG

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/87/v3/vh9kjAT5QHa9r4NAc3xwog/en-us_image_0000002537925970.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062253Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=73F54EE737AC4700B4A526387EA8556CF82569949F4686572F4068D152F5A4AA)

**Figure 4** Setting gridSpan and gridOffset separately has the same effect as useSizeType for a specific device width type

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a1/v3/62YyvssTTmuLTp8MaB161Q/en-us_image_0000002568685747.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062253Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C22896D5A1B2AAFCE090FA3189F3A6048D4F2FB64595CA2110F780A1C58945F8)
