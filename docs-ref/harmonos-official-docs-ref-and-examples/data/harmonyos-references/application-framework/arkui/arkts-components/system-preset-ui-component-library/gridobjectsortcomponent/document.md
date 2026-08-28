# GridObjectSortComponent

**GridObjectSortComponent** is a grid object organizer that you can use to edit, drag to sort, add, and delete grid objects.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ea/v3/T7NciGt1SQu5zf5_QB3CUw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062250Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B2A30A85235C97C5A2223A3255DCBFC25A6E53F93F4D49D00A70A650A1F14C23)

This component is supported since API version 11. Updates will be marked with a superscript to indicate their earliest API version.

#### Modules to Import

import { GridObjectSortComponent, GridObjectSortComponentItem, GridObjectSortComponentOptions, GridObjectSortComponentType , SymbolGlyphModifier } from '@kit.ArkUI';

#### Child Components

Not supported

#### Attributes

The [universal attributes](../../universal-attributes/document.md) are not supported.

#### GridObjectSortComponent

GridObjectSortComponent({options: GridObjectSortComponentOptions, dataList: Array<GridObjectSortComponentItem>, onSave: (select: Array<GridObjectSortComponentItem>, unselect: Array<GridObjectSortComponentItem>) => void, onCancel: () => void })

Creates a **GridObjectSortComponent** component.

**Decorator**: @Component

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Device behavior differences**: On wearables, calling this API results in a runtime exception indicating that the API is undefined. On other devices, the API works correctly.

| Name | Type | Mandatory | Decorator | Description |
| :-- | :-- | :-- | :-- | :-- |
| options | [GridObjectSortComponentOptions](#gridobjectsortcomponentoptions) | Yes | @Prop | Component configuration. |
| dataList | Array<[GridObjectSortComponentItem](#gridobjectsortcomponentitem)\> | Yes | \- | Data to pass. The maximum data length is 50 characters. If it is exceeded, only the first 50 characters are used. |
| onSave | (select: Array<[GridObjectSortComponentItem](#gridobjectsortcomponentitem)\>, unselect: Array<[GridObjectSortComponentItem](#gridobjectsortcomponentitem)\>) => void | Yes | \- | Callback invoked when changes are saved. The data after the changes is returned. |
| onCancel | () => void | Yes | \- | Callback invoked when changes are canceled. |

#### GridObjectSortComponentOptions

Provides configuration options for the **GridObjectSortComponent** component.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Device behavior differences**: On wearables, calling this API results in a runtime exception indicating that the API is undefined. On other devices, the API works correctly.

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| type | [GridObjectSortComponentType](#gridobjectsortcomponenttype) | No | Yes | 
Component display type: text only or image with text.

Default value: **GridObjectSortComponentType.TEXT**

 |
| imageSize | number | [Resource](../../common-definitions/basic-types/document.md#resource) | No | Yes | 

Image size, in vp.

The value must be greater than or equal to 0.

Default value: **56vp**.

 |
| normalTitle | [ResourceStr](../../common-definitions/basic-types/document.md#resourcestr) | No | Yes | 

Title displayed in the non-editing state.

Default value: **Channel**

 |
| showAreaTitle | [ResourceStr](../../common-definitions/basic-types/document.md#resourcestr) | No | Yes | 

First subtitle of the display area.

Default value: **Drag to sort**

 |
| addAreaTitle | [ResourceStr](../../common-definitions/basic-types/document.md#resourcestr) | No | Yes | 

Second subtitle of the display area.

Default value: **Tap to add**

 |
| editTitle | [ResourceStr](../../common-definitions/basic-types/document.md#resourcestr) | No | Yes | 

Title displayed in the editing state.

Default value: **Edit**

 |

#### GridObjectSortComponentType

Enumerates display types for nodes in the **GridObjectSortComponent** component.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Device behavior differences**: On wearables, calling this API results in a runtime exception indicating that the API is undefined. On other devices, the API works correctly.

| Name | Value | Description |
| :-- | :-- | :-- |
| IMAGE\_TEXT | "image\_text" | Image with text. |
| TEXT | "text" | Text only. |

#### GridObjectSortComponentItem

Provides data item configuration for the **GridObjectSortComponent** component.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Device behavior differences**: On wearables, calling this API results in a runtime exception indicating that the API is undefined. On other devices, the API works correctly.

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| id | number | string | No | No | 
Data ID, which must be unique.

The default value is an empty string.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| text | [ResourceStr](../../common-definitions/basic-types/document.md#resourcestr) | No | No | 

Text information.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| selected | boolean | No | No | 

Whether the grid object has been added. The value **true** means that the grid object has been added, and **false** means the opposite.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| url | [ResourceStr](../../common-definitions/basic-types/document.md#resourcestr) | No | Yes | 

URL of the image. Required when **GridObjectSortComponentType** is set to **IMAGE\_TEXT**.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| symbolStyle18+ | [SymbolGlyphModifier](../../universal-attributes/modifiers-and-custom-property/symbol-glyph-modifier/document.md#symbolglyphmodifier) | No | Yes | 

Symbol resource of the image. Required when **GridObjectSortComponentType** is set to **IMAGE\_TEXT**. The priority of this property is higher than that of **url**.

**Atomic service API**: This API can be used in atomic services since API version 18.

 |
| order | number | No | No | 

Sequence number.

The value must be greater than or equal to 0.

Default value: **0**.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |

#### Events

The [universal events](../../universal-events/document.md) are not supported.

#### Example

This example illustrates the basic usage of the **GridObjectSortComponent** component, involving component configuration initialization, data initialization, and the use of the save and cancel APIs.

import { GridObjectSortComponent, GridObjectSortComponentItem, GridObjectSortComponentOptions, GridObjectSortComponentType, SymbolGlyphModifier } from '@kit.ArkUI';

@Entry
@Component
struct Index {
  // Initialize the component data.
  @State dataList: GridObjectSortComponentItem\[\] = \[
    {
      id: 0,
      url: $r('sys.media.ohos\_save\_button\_filled'),
      text: 'Download',
      selected: true,
      order: 3
    },
    {
      id: 1,
      url: $r('sys.media.ohos\_ic\_public\_web'),
      text: 'Network',
      selected: true,
      order: 9
    },
    {
      id: 2,
      url: $r('sys.media.ohos\_ic\_public\_video'),
      text: 'Video',
      selected: false,
      order: 1
    },
    {
      id: 3,
      symbolStyle: new SymbolGlyphModifier($r('sys.symbol.record\_circle')),
      text: 'Recording',
      selected: false,
      order: 4
    }
  \]

  // Initialize the component configuration information.
  @State option: GridObjectSortComponentOptions = {
    type: GridObjectSortComponentType.IMAGE\_TEXT,
    imageSize: 45,
    normalTitle: 'Menu',
    editTitle: 'Edit',
    showAreaTitle: 'Drag to sort',
    addAreaTitle: 'Touch to add'
  }

  build() {
    Column() {
      GridObjectSortComponent({
        options: this.option,
        dataList: this.dataList,
        // Callback invoked when changes are saved. The data after the changes is returned.
        onSave: (
          select: Array<GridObjectSortComponentItem>,
          unselect: Array<GridObjectSortComponentItem>
        ) => {
          // save ToDo
        },
        // Callback invoked when changes are canceled.
        onCancel: () =>{
          // cancel ToDo
        }
      })
    }
  }
}
