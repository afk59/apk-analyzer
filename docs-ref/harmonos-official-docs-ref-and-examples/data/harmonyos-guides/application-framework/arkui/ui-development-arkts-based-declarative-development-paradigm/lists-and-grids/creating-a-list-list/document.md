# Creating a List (List)

#### Overview

A list is a container that displays a collection of items. If the list items go beyond the screen, the list can scroll to reveal the content off the screen. The list is applicable for presenting similar data types or data type sets, such as images and text. Some common lists seen in applications are the contacts list, playlist, and shopping list.

You can use lists to easily and efficiently display structured, scrollable information. Specifically, you can provide a single view of rows or columns by arranging the [ListItemGroup](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-container-listitemgroup) or [ListItem](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-container-listitem) child components linearly in a vertical or horizontal direction in the [List](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-container-list) component, or use [ForEach](../../ui-paradigm-rendering-control/foreach-rendering-repeated-content/document.md) to iterate over a group of rows or columns, or mix any number of single views and **ForEach** structures to build a list. The **List** component supports the generation of child components in various [rendering](../../ui-paradigm-rendering-control/rendering-control-overview/document.md) modes, including [conditional rendering](../../ui-paradigm-rendering-control/if-else-conditional-rendering/document.md), rendering of repeated content, and [lazy data loading](../../ui-paradigm-rendering-control/lazyforeach-lazy-data-loading/document.md).

On devices with circular screens, the [ArcList](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-container-arclist) component is recommended. For details, see [Creating an Arc List (ArcList)](../creating-an-arc-list-arclist-recommended-for-circular-screens/document.md).

#### Layout and Constraints

A list automatically arranges child components in the direction it scrolls. Adding or removing child components from the list will trigger re-arrangement of the child components.

As shown in the following figure, in a vertical list, **ListItemGroup** or **ListItem** components are automatically arranged vertically.

**ListItemGroup** is used to display list data by group. Its child component is also **ListItem**. **ListItem** represents a list item, which can contain a single child component.

**Figure 1** Relationships between List, ListItemGroup, and ListItem

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/75/v3/jJztN6OZQ2eYKRcwOFkeZA/en-us_image_0000002537924536.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061933Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C6BDE387D06C625940D25EC9B6AE259D85B312021DC3BDCFF961C5D08A93994F)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b4/v3/K6E8OLshSSWhoyymkZ8eNg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061933Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3DF4EEE5DDDE88C9400A18FC714790B41295ED62D11FDBD23BC85482FD85A626)

A **List** component can contain only **ListItemGroup** or **ListItem** as its child components. **ListItemGroup** and **ListItem** must be used together with **List**.

## Layout

In addition to providing vertical and horizontal layout support with adaptive scrolling for off-screen content, the **List** component also offers the capability of adapting to the number of rows in the cross axis direction.

When used in vertical layout, the list can contain one or more scrollable columns, as shown below.

**Figure 2** Vertical scrolling list (left: one column; right: multiple columns)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b4/v3/IzHV2oqZTXifezB5Kdp-7g/en-us_image_0000002537924534.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061933Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=81F68FE96181008072B13157EEB7E340C9D7680CC2119C3D3EFA1AA9D56CBC66)

When used in horizontal layout, the list can contain one or more scrollable rows, as shown below.

**Figure 3** Horizontal scrolling list (left: one column; right: multiple columns)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e0/v3/Dz5VgywmQEe8uTfgg-LzAg/en-us_image_0000002568684313.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061933Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F7BF4FF7073208A3D6C7AB4E76A0A70B4C94E1C0E96473127A476679D1BE2991)

While **Grid** and **WaterFlow** can also create single-column and multi-column layouts, there are scenarios where the **List** is the more suitable choice. Specifically, if your layout design requires columns of equal width and items do not need to span rows or columns, opt for the **List**.

## Constraints

The main axis direction of a list refers to the direction in which the child component columns are laid out and in which the list scrolls. An axis perpendicular to the main axis is referred to as a cross axis, and the direction of the cross axis is perpendicular to a direction of the main axis.

As shown below, the main axis of a vertical list is in the vertical direction, and the cross axis is in the horizontal direction. The main axis of a horizontal list is in the horizontal direction, and the cross axis is in the vertical direction.

**Figure 4** Main axis and cross axis of the list

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/84/v3/Pr2HAqZgRaCvV5pInVn8nQ/en-us_image_0000002568764323.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061933Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5BCB8DFF42F80713BD555BE2BA41698CD444EFDCC005D89DD46A82A21CD988C6)

If a size is set for the main axis or cross axis of the **List** component, it is used as the size of the component in the corresponding direction.

If no size is set for the main axis of the **List** component, the size of the **List** component in the main axis direction automatically adapts to the total size of its child components, as long as the total size of the child components in the main axis direction does not exceed the size of the parent component of **List**.

In the example shown below, no height is set for vertical list B, and the height of its parent component A is 200 vp. If the total height of all child components C is 150 vp, the height of list B is 150 vp.

**Figure 5** Main axis height constraint example 1 (A: parent component of List; B: List component; C: all child components of List)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7f/v3/jPnWf9jrRC2iTC6jHJh4eA/en-us_image_0000002537764598.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061933Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0094772BFF3410D8817AAF60D19D7E5CA2A8F77075DF589EED82D6FE954F2CAC)

If the total size of the child components in the main axis direction is greater than the size of the parent component of **List**, the size of the **List** component in the main axis direction automatically adapts to the size of its parent component.

In the example shown below, still no height is set for vertical list B, and the height of its parent component A is 200 vp. If the total height of all child components C is 300 vp, the height of list B is 200 vp.

**Figure 6** Main axis height constraint example 2 (A: parent component of List; B: List component; C: all child components of List)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e1/v3/RCK8iYpKQAuBiifyD9Ubag/en-us_image_0000002537924538.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061933Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=BB9CB8B3BCBD4CFB0E8A508240A9C573ADA395A43EEA192FD7EFA9BC91A044BC)

If no size is set for the cross axis of the **List** component, the size of the **List** component in the cross axis direction automatically adapts to the size of its parent component.

#### Developing the Layout

## Setting the Main Axis Direction

By default, the main axis of the **List** component runs in the vertical direction. This means that you can create a vertical scrolling list without the need to manually set the list direction.

To create a horizontal scrolling list, set the [listDirection](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-container-list#listdirection) attribute to **Axis.Horizontal**. The default value of **listDirection** is **Axis.Vertical**.

List(
  // ···
) {
  // ···
}
.listDirection(Axis.Horizontal)

## Setting the Cross Axis Layout

The cross axis layout of the **List** component can be set using the [lanes](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-container-list#lanes9) and [alignListItem](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-container-list#alignlistitem9) attributes. The **lanes** attribute controls the number of list items along the cross axis, and the **alignListItem** attribute controls the alignment mode of child components along the cross axis.

The **lanes** attribute of the **List** component is usually used to adaptively construct lists with different numbers of rows or columns for devices of different sizes, enabling one-time development for multi-device deployment. Its value type is number or [LengthConstrain](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-types#lengthconstrain). If you are building a two-column vertical list shown on the right in Figure 2, set the **lanes** attribute to **2**. The default value of **lanes** is **1**.

List(
  // ···
) {
  // ···
}
.lanes(2)

If set to a value of the LengthConstrain type, the **lanes** attribute determines the number of rows or columns based on the LengthConstrain settings and the size of the **List** component.

@Entry
@Component
export struct ListLayout {
  @State egLanes: LengthConstrain = { minLength: 200, maxLength: 300 };
  build() {
    // ···
          List(
            // ···
          ) {
            // ···
          }
          .lanes(this.egLanes)
        // ···
  }
}

For example, if the **lanes** attribute is set to **{ minLength: 200, maxLength: 300 }** for a vertical list, then:

-   When the list width is 300 vp, the list contains one column because **minLength** is 200 vp.
    
-   When the list width changes to 400 vp, which is twice that of the **minLength** value, the list is automatically adapted to two-column.
    

With regard to a vertical list, when the **alignListItem** attribute is set to **ListItemAlign.Center**, list items are center-aligned horizontally; when the **alignListItem** attribute is at its default value **ListItemAlign.Start**, list items are aligned toward the start edge of the cross axis in the list.

List(
  // ···
) {
  // ···
}
// ···
.alignListItem(ListItemAlign.Center)

#### ListItem Lifecycle Management

## Creating ListItem Components with ForEach

When a **List** component is created, all **ListItem** components are created immediately, but their behavior varies by area:

Visible area: **ListItem** components are laid out during the first frame.

Preload area: **ListItem** components are laid out during idle time.

Outside the preload area: Only the **ListItem** containers are created; their child components are not created.

During scrolling, the **ListItem** components entering the preload and visible areas create their child components and complete layout, and the **ListItem** components leaving these areas are not destroyed.

**Figure 7** Lifecycle of ListItem components created using ForEach

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/63/v3/hyRAbXd_RkCeHR0EDXIMqQ/en-us_image_0000002568684315.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061933Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C6EB75BAFD627C245D4945F3943A35474BC2084C31618D6D463E24855A3E11D5)

## Creating ListItem Components with LazyForEach

When a **List** component is created:

Visible area: **ListItem** components are created and laid out immediately. Preload area: **ListItem** components are created and laid out during idle time but not mounted to the component tree. Outside the preload area: No **ListItem** components are created.

During scrolling, the **ListItem** components entering the preload and visible areas are created and laid out. If they contain @Reusable decorated custom components, these components are reused from the cache pool when possible. **ListItem** components leaving the preload and visible areas are destroyed. If they contain @Reusable decorated custom components, these components are recycled into the cache pool.

**Figure 8** Lifecycle of ListItem components created using LazyForEach

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e7/v3/P0WPmQMjRwmLq7nIV1f_cw/en-us_image_0000002568764325.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061933Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1B0A56C14F4A46ADEE54C7CA1024DD504F04EDDEE119FC41A7D7481E3112E762)

## Creating ListItem Components with Repeat

**With virtualScroll Enabled**

When a **List** component is created and **Repeat** is used with [virtualScroll](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-rendering-control-repeat#virtualscroll) enabled to generate **ListItem** components:

Visible area: **ListItem** components are created and laid out immediately. Preload area: **ListItem** components are created and laid out during idle time of the rendering thread, and then mounted to the component tree. Outside the preload area: No **ListItem** components are created.

During scrolling, for **ListItem** components entering the preload and visible areas, the system first attempts to reuse components from cache pool. If no components are unavailable in the cache pool, the system creates **ListItem** components and lays them out. **ListItem** components leaving the preload and visible areas are recycled into the cache pool.

**Figure 9** Lifecycle of ListItem components created using Repeat with virtualScroll enabled

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/66/v3/q_73sxQ4RcWQAp3cAIFjYw/en-us_image_0000002537764600.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061933Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=953AA236DA7E20F518318A5CB25364C85022DDE43FB9DC4076B8E8044477C60B)

**With virtualScroll Disabled**

When a **List** component is created, all **ListItem** components are created immediately, but their behavior varies by area:

Visible area: **ListItem** components are laid out during the first frame.

Preload area: **ListItem** components are laid out during idle time.

Outside the preload area: No layout is performed.

During scrolling, the **ListItem** components in the preload and visible areas are laid out; the **ListItem** components leaving these areas are not destroyed.

**Figure 10** Lifecycle of ListItem components created using Repeat with virtualScroll disabled

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/79/v3/pPCip0SVTkmbiRSgAnAI_Q/en-us_image_0000002537924540.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061933Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=04103CC35AAC5A89CF638C0D887A8E6615242FAF411CD39884B82BAB4A020149)

#### Displaying Data in the List

The list displays a collection of items horizontally or vertically and can scroll to reveal content off the screen. In the simplest case, a **List** component is statically made up of **ListItem** components.

**Figure 11** Example of a city list

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1b/v3/3pFS504fQpyDP--7EZ90Pw/en-us_image_0000002568684317.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061933Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A9381F7C9D956C617A6E60E44AC7EFCC20E5950B6EDF4E9C098F175FA9FEF3C7)

@Entry
@Component
export struct DataInList {
  build() {
    // ···
          List() {
            ListItem() {
              // The value in the app.string.city\_beijing resource file is 'Beijing.'
              Text($r('app.string.city\_beijing'))
                .fontSize(24)
            }

            ListItem() {
              // The value in the app.string.city\_hangzhou resource file is 'Hangzhou.'
              Text($r('app.string.city\_hangzhou'))
                .fontSize(24)
            }

            ListItem() {
              // The value in the app.string.city\_shanghai resource file is 'Shanghai.'
              Text($r('app.string.city\_shanghai'))
                .fontSize(24)
            }
          }
          .backgroundColor('#FFF1F3F5')
          .alignListItem(ListItemAlign.Center)
        // ···
  }
}

Each **ListItem** component can contain only one root child component. Therefore, it does not allow for child components in tile mode. If tile mode is required, encapsulate the child components into a container or create a custom component.

**Figure 12** Example of a contacts list

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/30/v3/JrY-ie-VTTeODpYzkxtTLw/en-us_image_0000002568764327.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061933Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5935B1E936F3A701C701DA9946CF44E34A91686D9F5EF99AF8CE1B1035F12759)

As shown above, as a list item, each contact has a profile picture and a name. To present it, you can encapsulate **Image** and **Text** components into a **Row** container.

List() {
  ListItem() {
    Row() {
      // app.media.iconE is a custom resource.
      Image($r('app.media.iconE'))
        .width(40)
        .height(40)
        .margin(10)

      // The value in the app.string.peopleOne resource file is 'Tom.'
      Text($r('app.string.peopleOne'))
        .fontSize(20)
    }
  }

  ListItem() {
    Row() {
      // app.media.iconF is a custom resource.
      Image($r('app.media.iconF'))
        .width(40)
        .height(40)
        .margin(10)

      // The value in the app.string.peopleTwo resource file is 'Tracy.'
      Text($r('app.string.peopleTwo'))
        .fontSize(20)
    }
  }
}

#### Iterating List Content

Compared with a static list, a dynamic list is more common in applications. For dynamic lists, you can use [ForEach](../../ui-paradigm-rendering-control/foreach-rendering-repeated-content/document.md) to obtain data from the data source and create components for each data item, thereby reducing code complexity.

ArkTS provides component loop rendering capabilities using [ForEach](../../ui-paradigm-rendering-control/foreach-rendering-repeated-content/document.md). For example, when creating a contacts list, you can store the contact name and profile picture data in a **Contact** class structure to the **contacts** array, and nest **ListItem** components in **ForEach**, thereby reducing repeated code needed for tiling similar **ListItem** components.

import { util } from '@kit.ArkTS';

class Contact {
  public key: string = util.generateRandomUUID(true);
  public name: ResourceStr;
  public icon: Resource;

  constructor(name: ResourceStr, icon: Resource) {
    this.name = name;
    this.icon = icon;
  }
}

@Entry
@Component
export struct ListIteration {
  private contacts: Array<Contact> = \[

    // The value in the app.string.peopleOne resource file is 'Tom', and app.media.iconA is a custom resource.
    new Contact($r('app.string.peopleOne'), $r('app.media.iconA')),
    // The value in the app.string.peopleTwo resource file is 'Tracy', and app.media.iconB is a custom resource.
    new Contact($r('app.string.peopleTwo'), $r('app.media.iconB'))
  \];

  build() {
    // ...
          List() {
            ForEach(this.contacts, (item: Contact) => {
              ListItem() {
                Row() {
                  Image(item.icon)
                    .width(40)
                    .height(40)
                    .margin(10)
                  Text(item.name).fontSize(20)
                }
                .width('100%')
                .justifyContent(FlexAlign.Start)
              }
            }, (item: Contact) => JSON.stringify(item))
          }
          .width('100%')
          // ...
  }
}

In the **List** component, **ForEach** can be used to render **ListItemGroup** items as well as **ListItem** items. For details, see [Adding Grouping Support](#adding-grouping-support).

#### Customizing the List Style

## Setting the Spacing

When initializing the **List** component, use the **space** parameter of [ListOptions](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-container-list#listoptions18) to configure spacing between list items. In the following example, a 10 vp spacing is added between list items along the main axis:

List({ space: 10 }) {
  // ···
}

## Adding Dividers

A divider separates UI items to make them easier to identify. In the following figure that shows the settings screen, a divider is added between the setting items, appearing below the text.

**Figure 13** Using dividers between the setting items

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/56/v3/bkro-PSyTxOtDZdBgDA_xg/en-us_image_0000002537764602.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061933Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B94FE03CD97A0F7084FF3ADC6F5F9A0671E8FA6BC10A89AF6878D9A663538D15)

To add dividers between list items, use the [divider](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-container-list#divider) attribute together with the following style attributes:

**strokeWidth** and **color**: stroke width and color of the divider, respectively.

**startMargin** and **endMargin**: distance between the divider and the start edge and end edge of the list, respectively.

class DividerTmp {
  public strokeWidth: Length = 1;
  public startMargin: Length = 60;
  public endMargin: Length = 10;
  public color: ResourceColor = '#ffe9f0f0';

  constructor(strokeWidth: Length, startMargin: Length, endMargin: Length, color: ResourceColor) {
    this.strokeWidth = strokeWidth;
    this.startMargin = startMargin;
    this.endMargin = endMargin;
    this.color = color;
  }
}

@Entry
@Component
export struct CustomListStyle {
  @State egDivider: DividerTmp = new DividerTmp(1, 60, 10, '#ffe9f0f0');

// ···

  build() {
    // ···
          List(
            // ···
          ) {
            // ···
          }
          .divider(this.egDivider)
        // ···
  }
}

This example draws a divider with a stroke thickness of 1 vp from a position 60 vp away from the start edge of the list to a position 10 vp away from the end edge of the list. The effect is shown in Figure 9.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c3/v3/_jI95kHPQaOP9yr1Sh9kDw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061933Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D997EF9C729AA8AA9B5CB50BA5C41C71CF603B146F7BFDEEA42BECAA3A45FF5D)

1.  The stroke width of the divider causes some space between list items. If the content spacing set for the list is smaller than the stroke width of the divider, the latter is used instead.
    
2.  When a list contains multiple columns, the **startMargin** and **endMargin** attributes of the divider apply to each column.
    
3.  The divider is drawn between list items. No divider is drawn above the first list item and below the last list item.
    

## Adding a Scrollbar

When the total height (width) of list items exceeds the screen height (width), the list can scroll vertically (horizontally). The scrollbar of a list enables users to quickly navigate the list content, as shown below.

**Figure 14** Scrollbar of a list

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/59/v3/DiNgdTqSRPCMoFp398RWDg/en-us_image_0000002537924542.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061933Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5D656026F2BD8BFB30BFE8464E014563AEE6E8D3D801BD4B8BE33CF2EDE60603)

When using the **List** component, you can use the **scrollBar** attribute to control the display of the list scrollbar. The value type of **scrollBar** is [BarState](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-appendix-enums#barstate). When the value is **BarState.Auto**, the scrollbar is displayed as required: It is displayed when the scrollbar area is touched and becomes thicker when being dragged; it automatically disappears after 2 seconds of inactivity.

The default value of the **scrollBar attribute** is **BarState.Off** in API version 9 and earlier versions and **BarState.Auto** since API version 10.

List(
  // ···
) {
  // ···
}
// ···
.scrollBar(BarState.Auto)

#### Adding an External Scrollbar

To add an external scrollbar to a [List](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-container-list) component, you can use the [ScrollBar](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-basic-components-scrollbar) component. By binding both the **List** and **ScrollBar** components to the same [Scroller](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-container-scroll#scroller) object, you can ensure they stay synchronized.

1.  Create a [Scroller](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-container-scroll#scroller) object named **listScroller**.
    
    private listScroller: Scroller = new Scroller();
    
2.  Bind the **listScroller** object to the **List** component using the [scroller](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-container-list#listoptions18) parameter.
    
    // Use listScroller to initialize the scroller parameter to bind it with the List component.
    List({ scroller: this.listScroller }) {
    // ···
    }
    
3.  Bind the **listScroller** object to the **ScrollBar** component using the [scroller](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-basic-components-scrollbar#scrollbaroptions) parameter.
    
    // Use listScroller to initialize the scroller parameter to bind it with the ScrollBar component.
    ScrollBar({ scroller: this.listScroller})
    

**Figure 15** External scrollbar of the List component

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ec/v3/0wcLNG-_SzKFa7r57cFDkw/en-us_image_0000002568684319.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061933Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=22E556E1989B3F401E7FD7267446D95859376CC14356743A6A7B12895E885B7C)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f1/v3/x5x_p2tfT_ex6rxDdWOMoQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061933Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=81B608336578BCF3ED5C1AAA59BBC8F1B7543862546D8DCE172BB2B31C5C1DC8)

-   The [ScrollBar](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-basic-components-scrollbar) component can also be used with other scrollable components such as [ArcList](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-container-arclist), [Grid](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-container-grid), [Scroll](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-container-scroll), and [WaterFlow](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-container-waterflow).
-   On devices with circular screens, you can use the [List](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-container-list) component with the [ArcScrollBar](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-basic-components-arcscrollbar) component to add an arc scrollbar to your list layout. For details, see [Adding an External Scrollbar: ArcScrollBar](../creating-an-arc-list-arclist-recommended-for-circular-screens/document.md#adding-an-external-scrollbar-arcscrollbar).

#### Adding Grouping Support

By allowing data to be displayed in groups in the list, you make the list easier to scan and navigate. Grouping is common in real-world applications. For example, the contacts list below use grouping.

**Figure 16** Contacts list with grouping

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/50/v3/OhA2y0hnQ8aFvET6X_ZSkw/en-us_image_0000002568764329.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061933Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D882059E255425C81CF9FD73C90F11B9878BA386A09EEB672F56C7726591E326)

You can use **ListItemGroup** to group items in the **List** component to build a two-dimensional list.

A **List** component allows one or more **ListItemGroup** child components. By default, the width of **ListItemGroup** is equal to that of **List**. When initializing **ListItemGroup**, you can use the **header** parameter to set its header.

@Entry
@Component
export struct GroupedList {
  @Builder
  itemHead(text: string) {
    // Header of the list group, corresponding to the group A and B locations.
    Text(text)
      .fontSize(20)
      .backgroundColor('#fff1f3f5')
      .width('100%')
      .padding(5)
  }

  build() {
    // ···
          List(
            // ···
          ) {
            ListItemGroup({ header: this.itemHead('A') }) {
              // Render the repeated list items of group A.
            // ···
            }

            ListItemGroup({ header: this.itemHead('B') }) {
              // Render the repeated list items of group B.
            // ···
            }
          }
        // ···
  }
}

If the structures of multiple **ListItemGroup** components are similar, you can combine the data of these components into an array and use **ForEach** to render them cyclically. For example, in the contacts list, the **contacts** data of each group (for details, see [Iterating List Content](#iterating-list-content)) and the **title** data of the corresponding group are combined and defined as the **contactsGroups** array. Then, with rendering of **contactsGroups** in **ForEach**, a contact list with multiple groups is implemented. For details, see the example in [Adding a Sticky Header](#adding-a-sticky-header).

#### Adding a Sticky Header

The sticky header is a common pattern for keeping the header in the same place on the screen while the user scrolls down the list. As shown in the following figure, when you scroll through group A in the contacts list, the header of group B is always below group A. When you start scrolling through group B, the header of group B is fixed at the top of the screen. After group B has been scrolled to the bottom, the header of group B is replaced by the header of next group.

Sticky headers not only signify the representation and usage of data in the respective groups, but also help users navigate through a large amount of information, thereby avoiding unnecessary scrolling between the top of the area where the header is located and the area of interest.

**Figure 17** Sticky header

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4d/v3/CXJJSbvfSXuFI1gmoJ7LLQ/en-us_image_0000002537764604.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061933Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4D4795ACE97D18343016E4631B32C2A22EF9AADF1D6213B6895EE8897F859AD6)

You can set a sticky header or footer for a **ListItemGroup** component by setting the [sticky](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-container-list#sticky9) attribute of its parent **List** component.

Setting the **sticky** attribute to **StickyStyle.Header** implements a sticky header. To implement a sticky footer, use the **footer** parameter to initialize the footer of **ListItemGroup** and set the **sticky** attribute to **StickyStyle.Footer**.

import { util } from '@kit.ArkTS';

class Contact {
  public key: string = util.generateRandomUUID(true);
  public name: string | Resource;
  public icon: Resource;

  constructor(name: string | Resource, icon: Resource) {
    this.name = name;
    this.icon = icon;
  }
}

class ContactsGroup {
  public title: string = '';
  public contacts: Array<object> | null = null;
  public key: string = '';
}

export class ContactsGroupDataSource implements IDataSource {
  private list: object\[\] = \[\];

  constructor(list: object\[\]) {
    this.list = list;
  }

  totalCount(): number {
    return this.list.length;
  }

  getData(index: number): object {
    return this.list\[index\];
  }

  registerDataChangeListener(listener: DataChangeListener): void {
  }

  unregisterDataChangeListener(listener: DataChangeListener): void {
  }
}

export let contactsGroups: object\[\] = \[
  {
    title: 'A',
    contacts: \[
      // The value in the app.string.contacts\_A\_one resource file is 'Alice', and app.media.iconA is a custom resource.
      new Contact($r('app.string.contacts\_A\_one'), $r('app.media.iconA')),
      // The value in the app.string.contacts\_A\_two resource file is 'Ann', and app.media.iconB is a custom resource.
      new Contact($r('app.string.contacts\_A\_two'), $r('app.media.iconB')),
      // app.media.iconC is a custom resource.
      new Contact('Angela', $r('app.media.iconC')),
    \],
    key: util.generateRandomUUID(true)
  } as ContactsGroup,
  {
    title: 'B',
    contacts: \[
      // The value in the app.string.contacts\_B\_one resource file is 'Ben', and app.media.iconD is a custom resource.
      new Contact($r('app.string.contacts\_B\_one'), $r('app.media.iconD')),
      // The value in the app.string.contacts\_B\_three resource file is 'Bryan', and app.media.iconE is a custom resource.
      new Contact($r('app.string.contacts\_B\_three'), $r('app.media.iconE'))
    \],
    key: util.generateRandomUUID(true)
  } as ContactsGroup
\];
export let contactsGroupsDataSource: ContactsGroupDataSource = new ContactsGroupDataSource(contactsGroups);

@Entry
@Component
export struct StickyHeaderList {
  // Define the contactsGroups array.
  @Builder
  itemHead(text: string) {
    // Header of the list group, corresponding to the group A and B locations.
    Text(text)
      .fontSize(20)
      .backgroundColor('#fff1f3f5')
      .width('100%')
      .padding(5)
  }

  build() {
    // ...
          List() {
            // Lazy-load the ListItemGroup components. contactsGroups is the data set of contacts and titles of multiple groups.
            LazyForEach(contactsGroupsDataSource, (itemGroup: ContactsGroup) => {
              ListItemGroup({ header: this.itemHead(itemGroup.title) }) {
                // Render ListItem components cyclically.
                if (itemGroup.contacts) {
                  LazyForEach(new ContactsGroupDataSource(itemGroup.contacts), (item: Contact) => {
                    ListItem() {
                      Row() {
                        Image(item.icon).width(40).height(40).margin(10)
                        Text(item.name).fontSize(20)
                      }.width('100%').justifyContent(FlexAlign.Start)
                    }
                  }, (item: Contact) => JSON.stringify(item))
                }
              }
            }, (itemGroup: ContactsGroup) => JSON.stringify(itemGroup))
          }
          .sticky(StickyStyle.Header) // Set a sticky title.
          // ...
  }
}

#### Controlling the Scroll Position

In some cases you may want to control the scroll position of a list. For example, when there are a huge number of items in the news page list, you may want to allow users to quickly jump to the top or bottom of the list after they have scrolled to a certain point. Below is an example.

**Figure 18** Returning to the top of the list

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4b/v3/u6-v_-DJSg-cv30ML19JTg/en-us_image_0000002537924544.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061933Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=13B48ECAEE89C82DFBDF672D901A06FD7C5CC8A5FE674571BA3DE3F5BBCFFA00)

When the **List** component is initialized, you can use the **scroller** parameter to bind a [Scroller](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-container-scroll#scroller) object to control the scrolling of the list. In this example of a news page list, the **scrollToIndex** API of the **Scroller** object is used to scroll the list to the list item with the specified index. This allows the user to return to the top of the list by clicking a specific button.

To start with, create a **Scroller** object **listScroller**.

private listScroller: Scroller = new Scroller();

Then, use **listScroller** to initialize the **scroller** parameter to bind it with the **List** component. Set **scrollToIndex** to **0**, meaning to return to the top of the list.

Stack({ alignContent: Alignment.Bottom }) {
  // Use listScroller to initialize the scroller parameter to bind it with the List component.
  List({ space: 20, scroller: this.listScroller }) {
    // ...
  }

  Button() {
    // ...
  }
  // ...
  .onClick(() => {
    // Specify where e to jump when the specific button is clicked, which is the top of the list in this example.
    this.listScroller.scrollToIndex(0);
  })
}

#### Handling Scroll Position Changes

Many applications need to listen for and respond to changes in list scroll positions. For example, with regard to a contacts list, if scrolling spans more than one group, the alphabetical index bar at one side of the list also needs to be updated to highlight the letter corresponding to the current group.

Another common example is a scrolling list working with a multi-level index bar, as in the case of a product category page in a shopping application.

**Figure 19** Alphabetical index bar's response to contacts list scrolling

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2/v3/IO9dXVy6QhegySYYaTiDBw/en-us_image_0000002568684321.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061933Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=65809B6065B492130B3AFD054FFAE0BDC7537FE09A5038569F4FE01E27281334)

As shown above, when the contacts list scrolls from group A to B, the alphabetical index bar on the right also changes from A to B. This behavior can be implemented by listening for the [onScrollIndex](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-container-list#onscrollindex) event of the **List** component. The alphabetical index bar is implemented using the [AlphabetIndexer](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-container-alphabet-indexer) component.

When the list scrolls, the **selectedIndex** value of the letter to highlight in the alphabet index bar is recalculated based on the **firstIndex** value of the item to which the list has scrolled. In the **AlphabetIndexer** component, the index of the highlighted item is set through the **selected** attribute. When the value of **selectedIndex** changes, the **AlphabetIndexer** component is re-rendered to highlight the corresponding letter.

const alphabets = \['#', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K',
  'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'\];

// ...

@Entry
@Component
export struct ResponsiveScrollPositionList {
  @State selectedIndex: number = 0;
  private listScroller: Scroller = new Scroller();
  // ...

  build() {
    // ...
          Stack({ alignContent: Alignment.End }) {
            // Use the List component to handle scroll position changes.
            // Use listScroller to initialize the scroller parameter to bind it with the List component.
            List({ scroller: this.listScroller }) {
              // ...
            }
            .onScrollIndex((firstIndex: number) => {
              // Recalculate the value of this.selectedIndex in the alphabetical index bar based on the index of the item to which the list has scrolled.
              // ...
            })

            // AlphabetIndexer component
            AlphabetIndexer({ arrayValue: alphabets, selected: 0 })
              .selected(this.selectedIndex)
              .onSelect((index: number) => {
                this.listScroller.scrollToIndex(index);
              })
          }
          // ...
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/99/v3/Uj7JyAcgSom-mMfHrMYFhg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061933Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7CAF66A8FB8AD761045C209852397FD0F4126B45BD16899D77CA294627BC74EE)

During index calculation, each **ListItemGroup** component is taken as a whole and assigned an index, and the indexes of the list items within are not included in the calculation.

#### Responding to Swipe on List Items

Swipe menus are common in many applications. For example, a messaging application generally provides a swipe-to-delete feature for its message list. This feature allows users to delete a message by swiping left on it and touching the delete button, as shown in the following figure. For details about how to add a badge to the profile picture of a list item, see [Adding a Badge to a List Item](#adding-a-badge-to-a-list-item).

**Figure 20** Swipe-to-delete feature

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a4/v3/jPZdILwYTD-vwl-jC5uhHg/en-us_image_0000002568764331.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061933Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C37DA278E9EEDC80443527544A6107307D53607A133E110A9691725240C94B2A)

Swiping left or right on a list item can be implemented through the [swipeAction](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-container-listitem#swipeaction9) attribute. In initialization of the **swipeAction** attribute, the **SwipeActionOptions** parameter is mandatory, wherein the **start** parameter indicates the component that appears from the start edge when the list item is swiped right, and the **end** parameter indicates the component that appears from the end edge when the list item is swiped left.

In the example of the message list, the **end** parameter is set to a custom delete button. In initialization of the **end** attribute, the index of the sliding list item is passed to the delete button. When the user touches the delete button, the data corresponding to the list item is deleted based on the index.

1.  Build the component that appears from the end edge when the list item is swiped left.
    
    @Builder
    itemEnd(index: number) {
      // Build the component that appears from the end edge when the list item is swiped left.
      Button({ type: ButtonType.Circle }) {
        Image($r('sys.media.ohos\_ic\_bottomsheet\_close'))
          .width(40)
          .height(40)
      }
      // ···
      .onClick(() => {
        // this.messages is the list data source, which can be constructed as required. A specified data item can be deleted from the data source upon click.
        this.arr.splice(index, 1);
      })
    }
    
2.  Binds the **swipeAction** attribute to a list item that can be swiped left.
    
    // When constructing a list, use ForEach to render list items based on the data source this.messages.
    ListItem() {
      // ···
    }.swipeAction({
      end: {
        // index is the index of the list item.
        builder: () => {
          // ···
          this.itemEnd(this.index);
        },
      }
    }) // Set the swipe action.
    

#### Adding a Badge to a List Item

A badge is an intuitive, unobtrusive visual indicator to draw attention and convey a specific message. For example, a badge can be displayed in the upper right corner of the message list to indicate that there are new messages, as shown in the following figure.

**Figure 21** Adding a badge to a list item

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7b/v3/BRimpH5sQ-yWS6ctH-NpUQ/en-us_image_0000002537764606.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061933Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E2BBE31431DFE4B19C489237290AD72CC58C0A061C5FDD54FF12075A737ACBCF)

To add a badge, use the [Badge](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-container-badge) component in **ListItem**. The **Badge** component is a container that can be attached to another component for tagging.

In a message list, if you want to display a badge in the upper right corner of a message, wrap the corresponding component inside the **Badge** component within the list item.

In the **Badge** component, the **count** and **position** parameters are used to set the number of notifications and the position to display the badge, respectively. You can also use the **style** parameter to spruce up the badge.

ListItem() {
  // Add a badge to the upper right corner of the message item.
  Badge({
    count: 1,
    position: BadgePosition.RightTop,
    style: { badgeSize: 16, badgeColor: '#FA2A2D' }
  }) {
    // ...
  }
}

#### Implementing Pull-Down-to-Refresh and Pull-Up-to-Load

The pull-down-to-refresh and pull-up-to-load features are widely used in mobile applications, such as news applications. In effect, the implementation of these two features follows the same process: (1) As response to a [touch event](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-universal-events-touch), a refresh or load view is displayed at the top or bottom of the page; (2) when the refresh or load is complete, the refresh or load view is hidden.

The following describes the implementation of the pull-and-refresh feature:

1.  Listen for the finger press event and record the value of the initial position.
    
2.  Listen for the finger movement event, and record and calculate the difference between the value of the current position and the initial value. If the difference is greater than 0, the finger moves downward. Set the maximum value for the movement.
    
3.  Listen for the finger lift event. If the movement reaches the maximum value, trigger data loading and display the refresh view. After the loading is complete, hide the view.
    

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fe/v3/bftx4ltJRXKsHc-Dy277Xg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061933Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=142C8931795E0923E3521C4B9710A02A0778FF30609D76B5BE0F0AE626D24D7B)

To implement the pull-down-to-refresh feature, you are advised to use the [Refresh](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-container-refresh) component.

For details about the implementation of pull-down refresh and pull-up loading, see "News Data Loading."

#### Editing a List

The list editing mode is frequently used in various scenarios, such as to-do list management, file management, and note management. In editing mode, adding and deleting list items are the most basic functions. The core is to add and delete data in the data set corresponding to the list items.

The following uses to-do list management as an example to describe how to quickly add and delete list items.

## Adding a List Item

As shown below, when a user touches **Add**, a page is displayed for the user to set options for the new list item. After the user touches **OK**, the corresponding item is added to the list.

**Figure 22** Adding a to-do task

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f5/v3/yaMOFCvrTymGQX47rnXO1g/en-us_image_0000002537924546.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061933Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=56430DD9CCBCA3C6DE66B804E4510D4FD1ED92DDC6D2017A0FDEA481482D4514)

The process of implementing the addition feature is as follows:

1.  Define the list item data structure. In this example, a to-do data structure is defined.
    
    //ToDo.ets
    import { util } from '@kit.ArkTS';
    
    export class ToDo {
      public key: string = util.generateRandomUUID(true);
      public name: string;
    
      constructor(name: string) {
        this.name = name;
      }
    }
    
2.  Build the overall list layout and list items.
    
    import { ToDo } from './ToDo';
    
    @Component
    export struct ToDoListItem {
      @Link isEditMode: boolean;
      @Link selectedItems: ToDo\[\];
      private toDoItem: ToDo = new ToDo('');
    
      build() {
        Flex({ justifyContent: FlexAlign.SpaceBetween, alignItems: ItemAlign.Center }) {
        // ···
        }
        // ···
        .width('100%')
        .height(80)
        // .padding(): Set this parameter based on the use case.
        .borderRadius(24)
        // .linearGradient(): Set this parameter based on the use case.
        .gesture(
          GestureGroup(GestureMode.Exclusive,
            LongPressGesture()
              .onAction(() => {
              })
          )
        )
      }
    }
    
3.  Initialize the to-do list data and available items, and build the list layout and list items.
    
    import { ToDo } from './ToDo';
    import { ToDoListItem } from './ToDoListItem';
    
    @Entry
    @Component
    export struct AddListItem {
      @State toDoData: ToDo\[\] = \[\];
      @Watch('onEditModeChange') @State isEditMode: boolean = false;
      @State selectedItems: ToDo\[\] = \[\];
      private availableThings: string \[\] = \[\];
    
      aboutToAppear(): void {
        const context = this.getUIContext().getHostContext() as common.UIAbilityContext;
        const reading = context.resourceManager.getStringByNameSync('Reading')
        this.availableThings.push(reading)
        const exercise = context.resourceManager.getStringByNameSync('Exercise')
        this.availableThings.push(exercise)
        const travel = context.resourceManager.getStringByNameSync('Travel')
        this.availableThings.push(travel)
        const listening = context.resourceManager.getStringByNameSync('Listening\_Music')
        this.availableThings.push(listening)
        const watching = context.resourceManager.getStringByNameSync('Watching\_Films')
        this.availableThings.push(watching)
        const singing = context.resourceManager.getStringByNameSync('Singing')
        this.availableThings.push(singing)
      }
    
      onEditModeChange() {
        if (!this.isEditMode) {
          this.selectedItems = \[\];
        }
      }
    
      build() {
        // ...
          Column(
            // ...
          ) {
            // ...
                Row() {
                  if (this.isEditMode) {
                    Text('X')
                      .fontSize(20)
                      .onClick(() => {
                        this.isEditMode = false;
                      })
                      .margin({ left: 20, right: 20 })
                  } else {
                    // The value in the app.string.TodoItem resource file is 'To-Do.'
                    Text($r('app.string.TodoItem'))
                      .fontSize(36)
                      .margin({ left: 40 })
                    Blank()
                    Text('+')// Provide an entry for adding a list item, that is, add a click event for the add button.
                    // ...
                      .onClick(() => {
                        this.getUIContext().showTextPickerDialog({
                          range: this.availableThings,
                          onAccept: (value: TextPickerResult) => {
                            let arr = Array.isArray(value.index) ? value.index : \[value.index\];
                            for (let i = 0; i < arr.length; i++) {
                              this.toDoData.push(new ToDo(this.availableThings\[arr\[i\]\])); // Add to-do list items (available items).
                            }
                          },
                        })
                      })
                  }
                  // ...
    
                List({ space: 10 }) {
                  ForEach(this.toDoData, (toDoItem: ToDo) => {
                    ListItem() {
                      // Place each item of toDoData into the list item in the form of model.
                      ToDoListItem({
                        isEditMode: this.isEditMode,
                        toDoItem: toDoItem,
                        selectedItems: this.selectedItems
                      })
                    }
                  }, (toDoItem: ToDo) => toDoItem.name.toString())
                }
              }
            }
            // ...
      }
    }
    

## Deleting a List Item

As shown below, when the user long presses a list item to enter the deletion mode, a page is displayed for the user to delete the list item. After the user selects the list item and touches the delete button, the list item is deleted.

**Figure 23** Deleting a to-do task

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bf/v3/bZZyIKGlS_Sn77zKJvnrHA/en-us_image_0000002568684323.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061933Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=AC7B8B077C6C2BC27AA4D0FFFE5601A639186565158D661B014F4FC657CB856C)

The process of implementing the deletion feature is as follows:

1.  Generally, the deletion feature is available only after the list enters the editing mode. Therefore, the entry to the editing mode needs to be provided.
    
    In this example, by listening for the long press event of a list item, the list enters the editing mode when the user long presses a list item.
    
    import { util } from '@kit.ArkTS';
    
    // Structure reference
    export class ToDo {
      public key: string = util.generateRandomUUID(true);
      public name: string;
      public toDoData: ToDo\[\] = \[\];
    
      constructor(name: string) {
        this.name = name;
      }
    }
    
    Refer to the code snippet below:
    
    Flex({ justifyContent: FlexAlign.SpaceBetween, alignItems: ItemAlign.Center }) {
    // ···
    }
    // ···
    .gesture(
      GestureGroup(GestureMode.Exclusive,
        LongPressGesture()
          .onAction(() => {
            if (!this.isEditMode) {
              this.isEditMode = true; // Enter the editing mode.
            }
          })
      )
    )
    
2.  Respond to the user's selection and record the list items to be deleted.
    
    In this to-do list example, the list items are selected or unselected according to the user's selection.
    
    import { util } from '@kit.ArkTS';
    
    // Structure reference
    export class ToDo {
      public key: string = util.generateRandomUUID(true);
      public name: string;
      public toDoData: ToDo\[\] = \[\];
    
      constructor(name: string) {
        this.name = name;
      }
    }
    
    Refer to the code snippet below:
    
    if (this.isEditMode) {
      Checkbox()
        .onChange((isSelected) => {
          if (isSelected) {
            this.selectedItems.push(new ToDo(this.toDoItem.name)); // When an item is selected, it is added to the selectedItems array. Make adjustment based on actual scenarios.
          } else {
            let index = this.selectedItems.indexOf(new ToDo(this.toDoItem.name));
            if (index !== -1) {
              this.selectedItems.splice(index, 1); // When an item is deselected, it is deleted from the selectedItems array.
            }
          }
        })
    }
    
3.  Respond to the user's clicking the delete button and delete the corresponding items from the list.
    
    import { util } from '@kit.ArkTS';
    
    // Structure reference
    export class ToDo {
      public key: string = util.generateRandomUUID(true);
      public name: string;
      public toDoData: ToDo\[\] = \[\];
    
      constructor(name: string) {
        this.name = name;
      }
    }
    
    Refer to the code snippet below:
    
    // The value in the app.string.delete resource file is 'Delete.'
    Button($r('app.string.delete'))
    // ···
      .onClick(() => {
        // this.toDoData is the to-do list item, which can be constructed based on service requirements. After an item is clicked, the corresponding data is removed.
        this.toDoData = this.toDoData.filter(toDoItem =>
        !this.selectedItems.some(selectedItem => selectedItem.name === toDoItem.name));
        this.isEditMode = false;
      })
    

#### Handling a Long List

While [ForEach](../../ui-paradigm-rendering-control/foreach-rendering-repeated-content/document.md) is suitable for short lists, using it for long lists with a large number of items can significantly slow down page loading, as it loads all items at once. Therefore, for better list performance, use [LazyForEach](../../ui-paradigm-rendering-control/lazyforeach-lazy-data-loading/document.md) instead to implement on-demand iterative data loading.

For details about the implementation, see the example in [LazyForEach: Lazy Data Loading](../../ui-paradigm-rendering-control/lazyforeach-lazy-data-loading/document.md).

When the list is rendered in lazy loading mode, to improve the list scrolling experience and minimize white blocks during list scrolling, you can use the **cachedCount** parameter of the **List** component to set the number of cached list items. With lazy loading, only content outside the visible area up to the [cachedCount](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-container-list#cachedcount) limit will be preloaded, whereas non-lazy loading will load all content. For both lazy and non-lazy loading, only the items within the visible area plus the **cachedCount**\-specified number of items outside the visible area are laid out.

List(
// ···
) {
// ···
}.cachedCount(3)

The following uses a vertical list as an example:

-   When **cachedCount** is set for the list, the system preloads and lays out the **cachedCount**\-specified number of rows of list items both above and below the currently visible area of the list. When calculating the number of rows for list items, the system takes into account the number of rows from the list items within a list item group. If a list item group does not contain any list items, then the entire list item group is counted as one row.
    
-   When a list is nested with **LazyForEach**, and within **LazyForEach** there is a list item group, **LazyForEach** will create **cachedCount**\-specified number of list item groups both above and below the currently visible area of the list.
    

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1e/v3/-_k1NN5mQqGZCO8aWSdFiQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061933Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=44B7D3CC4A19C3F552BB4B66D892AE54799163D7198C32854A2AAB69E7CA2622)

1.  A greater **cachedCount** value may result in higher CPU and memory overhead of the UI. Adjust the value by taking into account both the comprehensive performance and user experience.
    
2.  When a list uses data lazy loading, all list items except the list items in the display area and the cached list items are destroyed.
    

#### Collapsing and Expanding

The collapsing and expanding of list items are widely used, often applied in scenarios such as displaying information lists and filling out forms.

**Figure 24** Collapsing and expanding of list items

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c1/v3/uMGNwTEuQB2CBYs9DvBVgw/en-us_image_0000002568764333.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061933Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0612794FF64256C87F31A8C420AD993CBE1DAB916B4E8B4333410294B1BD2A8C)

The process of implementing the collapsing and expanding effect of list items is as follows:

1.  Define the list item data structure.
    
    import { curves } from '@kit.ArkUI';
    
    interface ItemInfo {
      index: number,
      name: ResourceStr,
      label: ResourceStr,
      type?: string,
    }
    
    interface ItemGroupInfo extends ItemInfo {
      children: ItemInfo\[\]
    }
    
2.  Construct a list structure.
    
      @State routes: ItemGroupInfo\[\] = \[
        {
          index: 0,
          name: 'basicInfo',
          // The value in the app.string.Personal\_Basic\_Information resource file is 'Basic personal information.'
          label: $r('app.string.Personal\_Basic\_Information'),
          children: \[
            {
              index: 0,
              // The value in the app.string.nick\_name resource file is 'Nickname.'
              name: $r('app.string.nick\_name'),
              label: 'xxxx',
              type: 'Text'
            },
            {
              index: 1,
              // The value in the app.string.avatar resource file is 'Profile picture.'
              name: $r('app.string.avatar'),
              label: $r('sys.media.ohos\_user\_auth\_icon\_face'),
              type: 'Image'
            },
            {
              index: 2,
              // The value in the app.string.age resource file is 'Age.'
              name: $r('app.string.age'),
              label: 'xxxx',
              type: 'Text'
            },
            {
              index: 3,
              // The value in the app.string.birthday resource file is 'Gender.'
              name: $r('app.string.birthday'),
              label: 'xxxxxxxxx',
              type: 'Text'
            },
            {
              index: 4,
              // The value in the app.string.gender resource file is ''.
              name: $r('app.string.gender'),
              label: 'xxxxxxxx',
              type: 'Text'
            },
          \]
        },
        {
          index: 1,
          name: 'equipInfo',
          // The value in the app.string.Device\_Information resource file is "Device information."
          label: $r('app.string.Device\_Information'),
          children: \[\]
        },
        {
          index: 2,
          name: 'appInfo',
          // The value in the app.string.Application\_usage\_information resource file is 'App usage.'
          label: $r('app.string.Application\_usage\_information'),
          children: \[\]
        },
        {
          index: 3,
          name: 'uploadInfo',
          // The value in the app.string.data\_you\_voluntarily\_uploaded resource file is 'Data you actively upload.'
          label: $r('app.string.data\_you\_voluntarily\_uploaded'),
          children: \[\]
        },
        {
          index: 4,
          name: 'tradeInfo',
          // The value in the app.string.Trading\_and\_asset\_information resource file is 'Transactions & assets.'
          label: $r('app.string.Trading\_and\_asset\_information'),
          children: \[\]
        },
        {
          index: 5,
          name: 'otherInfo',
          // The value in the app.string.Other\_materials resource file is 'Other materials.'
          label: $r('app.string.Other\_materials'),
          children: \[\]
        },
      \];
      @State expandedItems: boolean\[\] = Array(this.routes.length).fill(false);
      @State selection: string | null = null;
    
    // ...
    
      build() {
        // ...
              Column() {
                List({ space: 10 }) {
                  ForEach(this.routes, (itemGroup: ItemGroupInfo) => {
                    ListItemGroup({
                      header: this.ListItemGroupHeader(itemGroup),
                      style: ListItemGroupStyle.CARD,
                    }) {
                      if (this.expandedItems\[itemGroup.index\] && itemGroup.children) {
                        ForEach(itemGroup.children, (item: ItemInfo) => {
                          ListItem({ style: ListItemStyle.CARD }) {
                            Row() {
                              Text(item.name)
                              Blank()
                              if (item.type === 'Image') {
                                Image(item.label)
                                  .height(20)
                                  .width(20)
                              } else {
                                Text(item.label)
                              }
                              Image($r('sys.media.ohos\_ic\_public\_arrow\_right'))
                                .fillColor($r('sys.color.ohos\_id\_color\_fourth'))
                                .height(30)
                                .width(30)
                            }
                            .width("100%")
                          }
                          .width("100%")
                          .animation({ curve: curves.interpolatingSpring(0, 1, 528, 39) })
                        })
                      }
                    }.clip(true)
                  })
                }
                .width("100%")
              }
              .width('100%')
              .height('100%')
              .justifyContent(FlexAlign.Start)
              .backgroundColor($r('sys.color.ohos\_id\_color\_sub\_background'))
            // ...
      }
    }
    
3.  Control list item expansion by changing the state of **ListItem** components, and implement expand/collapse animations through [animation](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-animatorproperty#animation) and [animateTo](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-uicontext-uicontext#animateto).
    
    @Builder
    ListItemGroupHeader(itemGroup: ItemGroupInfo) {
      Row() {
        Text(itemGroup.label)
        Blank()
        Image($r('sys.media.ohos\_ic\_public\_arrow\_down'))
          .fillColor($r('sys.color.ohos\_id\_color\_fourth'))
          .height(30)
          .width(30)
          .rotate({ angle: !!itemGroup.children.length ? (this.expandedItems\[itemGroup.index\] ? 180 : 0) : 180 })
          .animation({ curve: curves.interpolatingSpring(0, 1, 228, 22) })
      }
      .width("100%")
      .padding(10)
      .animation({ curve: curves.interpolatingSpring(0, 1, 528, 39) })
      .onClick(() => {
        if (itemGroup.children.length) {
          this.getUIContext()?.animateTo({ curve: curves.interpolatingSpring(0, 1, 528, 39) }, () => {
            this.expandedItems\[itemGroup.index\] = !this.expandedItems\[itemGroup.index\];
          })
        }
      })
    }
    

#### Switching the Layout Direction

In certain scenarios, you may want a list to automatically scroll upward when new data is inserted at the bottom of the list to reveal the newly added items. Typical use cases include live-stream comments and instant messaging applications. By default, when the **List** component is using its normal layout, appending items to the bottom maintains the current content position without automatic scrolling. This behavior can be modified by switching the layout direction to achieve the desired effect.

**Figure 25** Real-time message scrolling

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/80/v3/ATswowMXSkyh2_l5TQEBhg/en-us_image_0000002537764608.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061933Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A9C4432C9AA0966EE95570D011E4697C5381C9364AAE07BC61D1931580CE313E)

1.  Define the list item data structure.
    
    interface Message {
      id: number
      content: ResourceStr
      sender: ResourceStr
    }
    
2.  Construct a list structure and set [stackFromEnd](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-container-list#stackfromend19) to **true**. This configuration causes the list to automatically scroll upward when new items are inserted at the bottom.
    
    @Builder
    MessageItem(message: Message) {
      Column() {
        Text(\`${message.sender}: ${message.content}\`)
          .fontSize(16)
          .textAlign(TextAlign.Start)
          .padding(10)
          .backgroundColor(message.sender === 'system' ? '#F0F0F0' : '#E6F3FF')
          .borderRadius(8)
      }
      .width('100%')
      .alignItems(HorizontalAlign.Start)
      .margin({ bottom: 8 })
    }
    
    @State messages: Message\[\] = \[\];
    
    aboutToAppear(): void {
      const context = this.getUIContext().getHostContext() as common.UIAbilityContext;
      // The value in the app.string.welcome\_live\_room resource file is 'Welcome to the live stream.'
      const welcomeLiveRoom = context.resourceManager.getStringByNameSync('welcome\_live\_room');
      // The value in the app.string.system resource file is 'System.'
      const system = context.resourceManager.getStringByNameSync('system');
      // The value in the app.string.hello\_everyone resource file is 'Hello everyone!'
      const helloEveryone = context.resourceManager.getStringByNameSync('hello\_everyone');
      // The value in the app.string.anchors resource file is 'Host.'
      const anchors = context.resourceManager.getStringByNameSync('anchors');
      this.messages = \[
        { id: 1, content: welcomeLiveRoom, sender: system },
        { id: 2, content: helloEveryone, sender: anchors }
      \];
    }
    
    build() {
      // ...
            Column() {
              // Chat message area.
              List({ space: 10 }) {
                ForEach(this.messages, (item: Message) => {
                  ListItem() {
                    this.MessageItem(item)
                  }
                }, (item: Message) => item.id.toString())
              }
              .stackFromEnd(true)
              .layoutWeight(1) // Occupy the remaining space.
              .alignListItem(ListItemAlign.Center)
    
              // ...
            }
            .width('100%')
            .height('100%')
            // ...
    }
    

#### Handling Swipe Release Events

Since API version 20, scrollable components ([Grid](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-container-grid), [List](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-container-list), [Scroll](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-container-scroll), and [WaterFlow](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-container-waterflow)) support swipe release event callbacks. These callbacks are triggered when the user lifts their finger from the screen, reporting the instantaneous swipe velocity. You can use the callbacks to implement custom scroll positioning effects, such as snap scrolling for short news items and free scrolling for long articles.

**Figure 26** Custom scroll positioning effects

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ff/v3/8maxKXwhRzOFkceOX0oo5Q/en-us_image_0000002537924548.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061933Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=CF573B1C57FE6DBE44BBC998A614A7E72036B729575895DE9E4E644BE68DEEB0)

1.  Define the news item data structure.
    
    class News {
      public id: string;
      public title: ResourceStr;
      public content: ResourceStr;
      public type: string;
    
      constructor(id: string, title: ResourceStr, content: ResourceStr, type: string) {
        this.id = id;
        this.title = title;
        this.content = content;
        this.type = type;
      }
    }
    
2.  Construct news data, using **type** to distinguish between news item types.
    
    @State newsData: Array<News> = \[
      // The value in the app.string.new\_title resource file is 'Headline.'
      // The value in the app.string.new\_short resource file is 'Short news content for quick browsing.'
      new News('1', $r('app.string.new\_title'), $r('app.string.new\_short'), 'short'),
      new News('2', $r('app.string.new\_title'), $r('app.string.new\_short'), 'short'),
      // The value in the app.string.new\_long resource file is 'Long news content for full browsing.'
      new News('3', $r('app.string.new\_title'), $r('app.string.new\_long'), 'long'),
      new News('4', $r('app.string.new\_title'), $r('app.string.new\_short'), 'short'),
      new News('5', $r('app.string.new\_title'), $r('app.string.new\_long'), 'long'),
    \];
    
3.  Implement the swipe release event handling (**onWillStopDragging**) and news processing logic:
    
    -   The **onWillStopDragging** callback reports the instantaneous swipe velocity when the user lifts their finger, with direction detection (positive value for upward swipes, negative for downward swipes).
        
        .onWillStopDragging((velocity: number) => {
          if (velocity < 0) {
            // Handle downward swipes.
          } else {
            // Handle upward swipes.
          }
        // ···
        })
        
    -   The current item's position information is obtained through the [getItemRect](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-container-scroll#getitemrect11) API.
        
        let rect = this.scrollerForList.getItemRect(this.currentIndex);
        
    -   For short news items, the list directly snaps to adjacent items.
        
        if (velocity > 10) {
          this.scrollerForList.scrollToIndex(this.currentIndex, true, ScrollAlign.START)
        } else if (velocity < -10) {
          this.scrollerForList.scrollToIndex(this.currentIndex + 1, true, ScrollAlign.START)
        }
        
    -   For long news articles, the system calculates the remaining visible area to determine the optimal scroll end point.
        
        let rect = this.scrollerForList.getItemRect(this.currentIndex);
        if (velocity < -30) {
          if (rect) {
            // Calculate the remaining visible portion of the current item.
            let leftRect = rect.y + rect.height;
            // Determine the scroll end point.
            let mainPosition = -velocity \* DEFAULT\_FRICTION / FRICTION\_SCALE;
            if (leftRect + mainPosition > 0.75 \* this.listHeight) {
              this.scrollerForList.scrollToIndex(this.currentIndex + 1, true, ScrollAlign.START);
              return;
            } else if (leftRect + mainPosition < 0.25 \* this.listHeight) {
              this.scrollerForList.scrollToIndex(this.currentIndex, true, ScrollAlign.END,
                { extraOffset: LengthMetrics.vp(this.listHeight \* 0.3) })
              return;
            }
          }
        } else if (velocity > 30) {
          let leftRect = rect?.y + rect?.height;
          let mainPosition = velocity \* DEFAULT\_FRICTION / FRICTION\_SCALE;
          if (leftRect + mainPosition > 0.75 \* this.listHeight) {
            this.scrollerForList.scrollToIndex(this.currentIndex, true, ScrollAlign.START);
            return;
          }
        }
        

#### Configuring the Edge Effect

The edge effect refers to the visual and interactive feedback when users scroll beyond the boundaries of a scrollable component. The **List** component supports three edge effect types via the [edgeEffect](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-container-list#edgeeffect) attribute: spring (bounce effect), shadow, and none. For details, see [EdgeEffect](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-appendix-enums#edgeeffect).

When the **List** content area occupies at least one full screen, the default edge effect is spring, as shown below.

**Figure 27** Spring edge effect

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/01/v3/K7RkwwuKQGKA3ar5WIg7zA/en-us_image_0000002568684325.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061933Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=312615596C55967C4EBD52842BA12282F5C8DFF1ACDD4003EB7A6F7AC58312C2)

If **.edgeEffect(EdgeEffect.None)** is used, the List component displays no edge effect, as shown below.

**Figure 28** No edge effect

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d8/v3/ePff8cLqQbmxNp04bwHoBA/en-us_image_0000002568764335.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061933Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=716AB2A21364B2DE07424C2ED538DE15547B37AA4A2DB76FC2518B834FFC2F46)

Since API version 18, **List** supports configuring edge effects for individual sides. For example, **.edgeEffect(EdgeEffect.Spring, { alwaysEnabled: true, effectEdge: EffectEdge.START })** applies the spring effect only to the start edge.

**Figure 29** Single-side edge effect

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/20/v3/gksrdC7RTCuvzb1wJNQsbA/en-us_image_0000002537764610.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061933Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=BC54A54B6C6421FD2D2BE1201AE7C4ED01DD0E7AEA0BA382FE7F9F7F078E276A)

Note: By default, the **List** component can produce a bounce effect only when there is more than one screen of content. To produce a bounce effect when there is less than one screen of content, configure **.edgeEffect(EdgeEffect.Spring, { alwaysEnabled: true })**.
