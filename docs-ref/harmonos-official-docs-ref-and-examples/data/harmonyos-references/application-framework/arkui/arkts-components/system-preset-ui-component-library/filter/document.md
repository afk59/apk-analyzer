# Filter

The advanced filter component allows users to filter data with multiple criteria combined. It consists of a floating bar and filters therein. The floating bar can be expanded to reveal the filters, which come in a multi-line collapsible or multi-line list style. For added convenience, you can append an additional quick filter.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ab/v3/H4-AHqSFQma3td-XUmrriw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062250Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A402875B1278E5A38B931FBC2421DEAFE199E9EFC7870498A82FDD02BD74E1EA)

This component is supported since API version 10. Updates will be marked with a superscript to indicate their earliest API version.

#### Modules to Import

import { Filter } from '@kit.ArkUI';

#### Child Components

Not supported

#### Attributes

The [universal attributes](../../universal-attributes/document.md) are not supported.

#### Filter

Filter({ multiFilters: Array<FilterParams>, additionFilters?: FilterParams, filterType?: FilterType, onFilterChanged: (filterResults: Array<FilterResult>) => void, container: ()=> void })

**Decorator**: @Component

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Device behavior differences**: On wearables, calling this API results in a runtime exception indicating that the API is undefined. On other devices, the API works correctly.

**Parameters**

| Name | Type | Mandatory | Decorator | Description |
| :-- | :-- | :-- | :-- | :-- |
| multiFilters | Array<[FilterParams](#filterparams)\> | Yes | @Prop | List of filter criteria. |
| additionFilters | [FilterParams](#filterparams) | No | @Prop | Additional quick filter. |
| filterType | [FilterType](#filtertype) | No | @Prop | 
Filter type.

Default value: **FilterType.LIST\_FILTER**.

 |
| onFilterChanged | (filterResults: Array<[FilterResult](#filterresult)\>) => void | Yes | \- | Callback invoked when the filter criteria is changed. The input parameter is the list of selected filter criteria. |
| container | ()=>void | Yes | @BuilderParam | Custom content of the filtering result display area, which is passed in a trailing closure. |

#### FilterParams

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Device behavior differences**: On wearables, calling this API results in a runtime exception indicating that the API is undefined. On other devices, the API works correctly.

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| name | [ResourceStr](../../common-definitions/basic-types/document.md#resourcestr) | No | No | 
Name of the filter criterion.

The default value is an empty string.

**NOTE**

If the text length exceeds the column width, it will be truncated.

 |
| options | Array<[ResourceStr](../../common-definitions/basic-types/document.md#resourcestr)\> | No | No | 

Options of the filter criterion.

The default value is an empty string.

**NOTE**

The text is truncated with an ellipsis (...) if it is too long.

 |

#### FilterType

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Device behavior differences**: On wearables, calling this API results in a runtime exception indicating that the API is undefined. On other devices, the API works correctly.

| Name | Value | Description |
| :-- | :-- | :-- |
| MULTI\_LINE\_FILTER | 0 | Multi-line collapsible. |
| LIST\_FILTER | 1 | Multi-line list. |

#### FilterResult

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Device behavior differences**: On wearables, calling this API results in a runtime exception indicating that the API is undefined. On other devices, the API works correctly.

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| name | [ResourceStr](../../common-definitions/basic-types/document.md#resourcestr) | No | No | 
Name of the filter criterion.

The default value is an empty string.

**NOTE**

If the text length exceeds the column width, it will be truncated.

 |
| index | number | No | No | 

Index of the selected option of the filter criterion.

Value range: an integer no less than -1

The default value is **\-1**, indicating that there is no selected option. Values less than -1 are treated as no selected option.

 |
| value | [ResourceStr](../../common-definitions/basic-types/document.md#resourcestr) | No | No | 

Value of the selected option of the filter criterion.

The default value is an empty string.

**NOTE**

If the text length exceeds the column width, it will be truncated.

 |

#### Events

The [universal events](../../universal-events/document.md) are not supported.

#### Example

This example shows how to implement a multi-line collapsible filter by setting **FilterType** to **MULTI\_LINE\_FILTER**.

import { Filter, FilterParams, FilterResult, FilterType } from '@kit.ArkUI';

@Entry
@Component
struct Index {
  private filterParam: Array<FilterParams> = \[{
    name: 'Month',
    options: \['All', 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'\],
  },
    {
      name: 'Year',
      options: \['All', '2023', '2022', '2021', '2020', '2019', '2018', '2017', '2016', '2015', '2014', '2013', '2012',
        '2011', '2010', '2009', '2008'\],
    },
    {
      name: 'Day',
      options: \['All', '1', '2', '3', '4', '5',' 6', '7','8', '9','10', '11', '12',
        '13','14', '15', '16', '17', '18','19','20','21','22', '23'\],
    }\];
  // Addition filter parameter. The name of the filter dimension must be specified. Otherwise, the entire filter dimension is not displayed.
  private additionParam: FilterParams =
    { name: 'Suggestions', options: \['Category 1', 'Category 2', 'Category 3', 'Category 4', 'Category 5', 'Category 6'\] };
  private arr: number\[\] = \[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10\];

  build() {
    Column() {
      Filter({
        multiFilters: this.filterParam,
        additionFilters: this.additionParam,
        filterType: FilterType.MULTI\_LINE\_FILTER,
        onFilterChanged: (select: Array<FilterResult>) => {
          console.info('rec filter change');
          for (let filter of select) {
            console.info('name:' + filter.name + ',index:' + filter.index + ',value:' + filter.value);
          }
        }
      }) {
        List({ initialIndex: 0 }) {
          ForEach(this.arr, (item: string, index: number) => {
            ListItem() {
              Text(item.toString())
                .width('100%')
                .height(100)
                .fontSize(16)
                .textAlign(TextAlign.Center)
                .borderRadius(10)
                .backgroundColor(Color.White)
                .margin({ top: 10, bottom: 10 })
            }
          })
        }.backgroundColor(Color.Gray)
        .padding({ left: 20, right: 20 })
      }
    }
    .height('100%')
    .width('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b0/v3/7NkTPoz4SJS-EnxF_rDZ1w/en-us_image_0000002537925912.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062250Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A9B68D5DABDFCDD10407A43D0CC00BC9966C660BE1FE920B123A164B0E67882B)
