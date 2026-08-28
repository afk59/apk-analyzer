# List and Grid Overview

Many applications require scrollable views to display collections of similar items, such as images, videos, music, news, or products. Depending on the layout requirements, these scenarios can be implemented using [List](../creating-a-list-list/document.md), [Grid](../creating-a-grid-grid-griditem/document.md), or [WaterFlow](../creating-a-waterfall-flow-waterflow/document.md). For circular screens, [ArcList](../creating-an-arc-list-arclist-recommended-for-circular-screens/document.md) is recommended.

#### List

The **List** component is ideal for single-column or multi-column layouts where columns have uniform widths. Common use cases include contact lists, music playlists, and shopping lists.

In scenarios like live comment feeds or instant messaging, where new data is appended to the bottom, the list should automatically scroll upward to reveal newly added items. This behavior can be enabled by [configuring the **List** component to stack from the end](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-container-list#stackfromend19).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/70/v3/BVfZ3RD1RTmrXJ6MscrZCw/en-us_image_0000002537924534.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061933Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=99352EE2880C89302BA1DA8957FB9D72BBF804843152141B9A6C623A8BEA4629)

#### Grid

A grid layout organizes items into rows and columns, allowing flexible positioning by specifying the target cell for each item. Typical use cases include image galleries, calendars, and calculators.

To support items that span multiple rows or columns, configure the grid using [GridLayoutOptions](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-container-grid#gridlayoutoptions10).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2f/v3/-xIoFEWvSZ6ypxxeOI8xzA/en-us_image_0000002568684311.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061933Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9C7E193FCF96E476C889102DA2F2F9177A3846D711787F1CCF662CF151292779)

#### Waterfall Flow

Waterfall flow is a multi-column layout where columns have equal width but items can vary in height. It is well-suited for staggered layouts such as image feeds, video previews, and product recommendations.

To support mixed layouts with varying column counts on the same page, use [WaterFlowSections](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-container-waterflow#waterflowoptions).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/98/v3/C40tfce9Sei-jLz9GMWH3w/en-us_image_0000002568764321.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061933Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=58667A5C4103562DE3F5EE5DA0AAD787811AA75854C966F4B20C71511CF6F151)

#### Arc List

An arc list is a specialized list designed for circular screens. It supports automatic scaling of items as they approach the top or bottom edges of the display.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/aa/v3/QkkVCCDBS9KccHjhF1mYrA/en-us_image_0000002537764596.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061933Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3AA189D24F5FF95EDD589B94A04D2BF40499154F50454348BFF233F4C5A80307)

#### Feature Comparison

| Feature | List | Grid | WaterFlow | ArcList |
| :-- | :-- | :-- | :-- | :-- |
| General scrolling capability | Supported | Supported | Supported | Supported |
| Item grouping | [ListItemGroup](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-container-listitemgroup) | [GridLayoutOptions](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-container-grid#gridlayoutoptions10) | [WaterFlowSections](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-container-waterflow#waterflowoptions) | Not supported |
| Sticky headers | Supported via the [sticky](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-container-list#sticky9) attribute | Not supported | Not supported | Not supported |
| Drag-and-drop sorting | Supported with [drag-and-drop sorting](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-universal-attributes-drag-sorting), including animations and automatic scrolling when dragged to the edge | Supported with [built-in animations](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-container-grid#supportanimation8) (only when all items occupy 1 row and 1 column), and no automatic scrolling when dragged to the edge | Not supported | Not supported |
| Swipe actions | Supported via the [swipeAction](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-container-listitem#swipeaction9) attribute | Not supported | Not supported | Not supported |
| Item spacing | Supported | Supported | Supported | Supported |
| Item dividers | Supported | Not supported | Not supported | Not supported |
