# List

The **List** component provides a list container that presents a series of list items arranged in a column with the same width. It supports presentations of the same type of data in a multiple and coherent row style, for example, images or text.

Lazy loading of **List** loads the child components in the visible area as required. Compared with full loading, lazy loading can improve the app startup speed and reduce the memory usage. The lazy loading capabilities vary when the **List** component is used together with [ForEach](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-rendering-control-foreach), [LazyForEach](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-rendering-control-lazyforeach), or [Repeat](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-new-rendering-control-repeat).

-   When **List** is used together with **ForEach**, all child nodes are created at a time. The nodes within the screen range are laid out and rendered when needed. When a user swipes, the nodes that are out of the screen range are not removed from the tree, and the nodes that are within the screen range are laid out and rendered.
    
-   When **List** is used together with **LazyForEach**, all nodes within the screen range are created, laid out, and rendered at a time. When a user swipes, the nodes that are out of the screen range are removed from the tree, and the nodes that are within the screen range are created, laid out, and rendered.
    
-   When the **List** component is used together with **Repeat** with [virtualScroll](../../state-management-and-rendering-control/repeat/document.md#virtualscroll), the lazy loading behavior is the same as that of **LazyForEach**. When the **List** component is used together with **Repeat** without **virtualScroll**, the lazy loading behavior is the same as that of **ForEach**.
    

If a scrollable component is nested in a **List** component, their scrolling directions are the same, and the main axis size is not set for the **List** component, the **List** component loads all child components. As a result, lazy loading does not take effect. In this scenario, you are advised to use the [ListItemGroup](../listitemgroup/document.md) component to optimize the performance.

Preloading in **List** refers to loading not only the child components within the visible area but also some invisible child components outside the visible area during idle time. Preloading can reduce frame loss during scrolling and improve smoothness. Preloading takes effect only when lazy loading is used. You can set the number of components to be preloaded for the **List** component using [cachedCount](#cachedcount). By default, child components equivalent to one screen above and below the visible area are preloaded (up to a maximum of 16 rows). The preloading capabilities vary when the **List** component is used together with [ForEach](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-rendering-control-foreach), [LazyForEach](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-rendering-control-lazyforeach), or [Repeat](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-new-rendering-control-repeat).

-   When the **List** component is used together with **ForEach** and **cachedCount** is set, in addition to laying out child components within the visible area, child components within the range of **cachedCount** outside the visible area are pre-laid out during idle time.
    
-   When the **List** component is used together with **LazyForEach** and **cachedCount** is set, in addition to creating and laying out child components within the display area, child components within the range of **cachedCount** outside the display area are pre-created and pre-laid out during idle time.
    
-   When the **List** component is used together with **Repeat** with [virtualScroll](../../state-management-and-rendering-control/repeat/document.md#virtualscroll), the preloading behavior is the same as that of **LazyForEach**. When the **List** component is used together with **Repeat** without **virtualScroll**, the preloading behavior is the same as that of **ForEach**.
    

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/87/v3/yLcQf5abQACxLAxwBXJ28w/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062238Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5291B94982070C0ED257D5C29C01A8EA640DED5B0CC54BB98D26996A44DA006A)

This component is supported since API version 7. Updates will be marked with a superscript to indicate their earliest API version.

The component has been bound with gestures to implement functions such as follow-up scrolling. If you need to add custom gestures, refer to [Gesture Blocking Enhancement](../../gesture-handling/gesture-control/gesture-blocking-enhancement/document.md).

#### Child Components

Only the [ListItem](../listitem/document.md) and [ListItemGroup](../listitemgroup/document.md) child components and custom components are supported. When using custom components inside **List**, you are advised to wrap the custom component with a **ListItem** or **ListItemGroup** as the top-level container. Setting attributes or event methods directly on custom components is not recommended.

Child components can be dynamically generated using rendering control types [if/else](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-rendering-control-ifelse), [ForEach](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-rendering-control-foreach), [LazyForEach](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-rendering-control-lazyforeach), and [Repeat](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-new-rendering-control-repeat). **LazyForEach** or **Repeat** is recommended to optimize performance.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0c/v3/RY5o4fiQSXqwh2xQlWgFNg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062238Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=33CE03FCC79A00061CE9080AAD130CF3EE582584D219A9DB113CA6E391877710)

If performance lag occurs when you process a large number of child components, consider using lazy loading, list item caching, dynamic preloading, component reuse, and layout optimization. For best practices, see [Optimizing Frame Loss for Long List Loading](https://developer.huawei.com/consumer/en/doc/best-practices/bpta-best-practices-long-list).

Starting from API version 21, the maximum width or height for a single child component inside a **List** container is 16,777,216 px. In API version 20 and earlier versions, the limit was 1,000,000 px. If a child component exceeds the applicable size limit, scrolling or display behavior may become abnormal.

Below are the rules for calculating the indexes of the child components of **List**:

-   The index increases in ascending order of child components.
    
-   In the **if/else** statement, only the child components for which the condition evaluates to true participate in the index calculation.
    
-   In the **ForEach**, **LazyForEach**, or **Repeat** statement, the indexes of all expanded subnodes are calculated.
    
-   After changes occur in [if/else](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-rendering-control-ifelse), [ForEach](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-rendering-control-foreach), [LazyForEach](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-rendering-control-lazyforeach), and [Repeat](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-new-rendering-control-repeat), index values are updated accordingly for child components.
    
-   Each **ListItemGroup** component is taken as a whole and assigned an index, and the indexes of the list items within are not included in the index calculation.
    
-   Child components of **List** whose **visibility** attribute is set to **Hidden** or **None** are included in the index calculation.
    

#### APIs

List(options?: [ListOptions](#listoptions18))

Creates a list container.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| options | [ListOptions](#listoptions18) | No | Options of the **List** component. |

#### ListOptions18+

Defines the options of the **List** component.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/69/v3/8W6EAB9kQMSJAgPYqjrnvg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062238Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E004653840DF424AF2F57C921A0895BAF31136C524FE80ED185491069628DD52)

To standardize anonymous object definitions, the element definitions here have been revised in API version 18. While historical version information is preserved for anonymous objects, there may be cases where the outer element's @since version number is higher than inner elements'. This does not affect interface usability.

**Widget capability**: This API can be used in ArkTS widgets since API version 18.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| initialIndex7+ | number | No | Yes | 
Index of the item to be displayed at the start when the list is initially loaded.

Default value: **0**

**NOTE**

If the set value is a negative number or is greater than the index of the last item in the list, the value is invalid. In this case, the default value will be used.

Since API version 14, if the **scrollToIndex** or **scrollEdge** API without animation in **Scroller** is called after the **List** component is created but before its first layout (for example, in the [onAttach](../../universal-events/component-change-events/show-hide-event/document.md#onattach12) event of the **List** component), the value will override the value of **initialIndex**.

After **initialIndex** is set, the list starts layout from the child component corresponding to **initialIndex**. The child components before **initialIndex** are not involved in layout and the exact size cannot be calculated. Therefore, the total scroll offset of the list obtained through the [currentOffset](../scroll/document.md#currentoffset) API is estimated and may have errors. You can set [childrenMainSize](#childrenmainsize12) to ensure the accuracy of the total scrolling offset of a list.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| space7+ | number | string | No | Yes | 

Spacing between list items along the main axis.

Default value: **0**

If the parameter type is number, the unit is vp.

**NOTE**

If this parameter is set to a negative number or a value greater than or equal to the length of the list content area, the default value is used.

If this parameter is set to a value less than the width of the list divider, the width of the list divider is used as the spacing.

Child components of **List** whose **visibility** attribute is set to **None** are not displayed, but the spacing above and below them still takes effect.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| scroller7+ | [Scroller](../scroll/document.md#scroller) | No | Yes | 

Scroller, After being bound to **List**, it can be used to control its scrolling.

**NOTE**

It cannot be bound to the same scrolling control object as other scrollable components, such as [ArcList](../arclist/document.md), [List](#), [Grid](../grid/document.md), [Scroll](../scroll/document.md), and [WaterFlow](../waterflow/document.md).

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |

#### Attributes

In addition to [universal attributes](../../universal-attributes/document.md) and [scrollable component common attributes](../scrollable-component-common-apis/document.md#attributes), the following attributes are also supported.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/67/v3/kEyzas5_RRyVNcTvp3dSGQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062238Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=61BB0F1C2F2F0EABD44822231080D3B61BF3DE1584A83D14E3E1D92BBE1C91EE)

The default value of the universal attribute [clip](../../universal-attributes/visual-effects/shape-clipping/document.md#clip12) is **true** for the **List** component.

#### \[h2\]listDirection

listDirection(value: Axis)

Sets the direction in which the list items are arranged.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [Axis](../../common-definitions/enums/document.md#axis) | Yes | 
Direction in which the list items are arranged.

Default value: **Axis.Vertical**

 |

#### \[h2\]divider

divider(value: [ListDividerOptions](#listdivideroptions18) | null)

Sets the style of the divider for the list items. By default, there is no divider.

The divider is drawn between list items along the main axis, and not above the first list item and below the last list item.

In multi-column mode, the value of **startMargin** is calculated from the start edge of the cross axis of each column. In single-column mode, it is calculated from the start edge of the cross axis of the list.

When a list item has [polymorphic styles](../../universal-attributes/polymorphic-style/document.md) applied, the dividers above and below the pressed child component are not rendered.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [ListDividerOptions](#listdivideroptions18) | null | Yes | 
Style of the divider for the list items.

Default value: **null**

 |

#### \[h2\]scrollBar

scrollBar(value: BarState)

Sets the scrollbar state.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [BarState](../../common-definitions/enums/document.md#barstate) | Yes | 
Scrollbar state.

In API version 9 and earlier versions, the default value is **BarState.Off**. Since API version 10, the default value is **BarState.Auto**.

 |

#### \[h2\]cachedCount

cachedCount(value: number)

Sets the number of **ListItem** or **ListItemGroup** components to be preloaded (cached). In a lazy loading scenario, only the **cachedCount** rows of **ListItem** components above and below the visible area of the **List** component is preloaded. In a non-lazy loading scenario, all items are loaded at once. For both lazy and non-lazy loading, only the content within the list display area plus the content equivalent to **cachedCount** outside the display area is laid out.

When **cachedCount** is set for the list, the system preloads and lays out the **cachedCount**\-specified number of rows of list items both above and below the currently visible area of the list. When calculating the number of rows for list items, the system takes into account the number of rows from the list items within a list item group. If a list item group does not contain any list items, then the entire list item group is counted as one row.

When a list is nested with **LazyForEach**, and within **LazyForEach** there is a list item group, **LazyForEach** will create **cachedCount**\-specified number of list item groups both above and below the currently visible area of the list.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | number | Yes | 
Number of list items or list item groups to be preloaded (cached).

Default value: number of nodes visible on the screen, with the maximum value of 16

Value range: \[0, +∞).

Values less than 0 are treated as **1**.

 |

#### \[h2\]cachedCount14+

cachedCount(count: number, show: boolean)

Sets the number of list items or list item groups to be cached (preloaded) and specifies whether to display the preloaded nodes.

When **cachedCount** is set for the list, the system preloads and lays out the **cachedCount**\-specified number of rows of list items both above and below the currently visible area of the list. When calculating the number of rows for list items, the system takes into account the number of rows from the list items within a list item group. If a list item group does not contain any list items, then the entire list item group is counted as one row. This attribute can be combined with the [clip](../../universal-attributes/visual-effects/shape-clipping/document.md#clip12) or [content clipping](../scrollable-component-common-apis/document.md#clipcontent14) attributes to display the preloaded nodes.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dd/v3/ViaJbby8QEebtiWbDEKUKQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062238Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=FD938B2A8ECF085FD1F0CDB6DCFB8075E25B64AC8E842359BD9EC8B4455E127D)

You are advised to set cachedCount to n/2 (n indicates the number of list items displayed on one screen). You also need to consider other factors to balance the experience and memory usage. For best practices, see [Cache List Items](https://developer.huawei.com/consumer/en/doc/best-practices/bpta-best-practices-long-list#section11667144010222).

**Widget capability**: This API can be used in ArkTS widgets since API version 14.

**Atomic service API**: This API can be used in atomic services since API version 14.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| count | number | Yes | 
Number of list items to be preloaded.

Default value: number of nodes visible on the screen, with the maximum value of 16

Value range: \[0, +∞).

Values less than 0 are treated as **1**.

 |
| show | boolean | Yes | 

Whether to display the preloaded list items. If this parameter is set to **true**, the preloaded list items are displayed. If this parameter is set to **false**, the preloaded list items are not displayed.

Default value: **false**

 |

#### \[h2\]cachedCount22+

cachedCount(count: number | CacheCountInfo, show: boolean)

Sets the number of list items or list item groups to be cached (preloaded) and specifies whether to display the preloaded nodes.

If the first parameter of the **cachedCount** attribute is of the **number** type, a specified number (specified by **count**) of rows of list items will be preloaded and laid out above and below the visible area during idle frames.

If the first parameter of the **cachedCount** attribute is of the **CacheCountInfo** type, preloading and layout will occur during idle frames when the number of cached rows is less than **CacheCountInfo.minCount**. When the number of cached rows is greater than **CacheCountInfo.maxCount**, the nodes outside the specified range will be destroyed or reused. When the UI is idle (no animation or user operation), a specified number (specified by **CacheCountInfo.maxCount**) of rows of list items will be preloaded above and below the visible area.

When calculating the number of rows for list items, the system takes into account the number of rows from the list items within a list item group. If a list item group does not contain any list items, then the entire list item group is counted as one row. This attribute can be combined with the [clip](../../universal-attributes/visual-effects/shape-clipping/document.md#clip12) or [clipContent](../scrollable-component-common-apis/document.md#clipcontent14) attributes to display the preloaded nodes.

Default behavior: The **count** parameter is of the **number** type by default, with its value set based on the number of nodes displayed on the screen, up to a maximum of 16. Preloaded **ListItem** components are not involved in drawing by default.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3a/v3/S06kKZU7RaebMH2Xg7_cqg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062238Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=138076E45FC2D9D4CB14CF2B3733CF458B9E02D6344769A07F4A21EB373D95CE)

You are advised to set cachedCount to n/2 (n indicates the number of list items displayed on one screen). You also need to consider other factors to balance the experience and memory usage. Starting from API version 22, setting both minimum and maximum cache counts is supported. The maximum cache count can be set to a moderately higher value, such as twice the minimum cache count, to utilize the UI thread's idle time for node creation. This reduces the need to create nodes during scrolling for preloading and enhances scrolling smoothness. For best practices, see [Cache List Items](https://developer.huawei.com/consumer/en/doc/best-practices/bpta-best-practices-long-list#section11667144010222).

**Widget capability**: This API can be used in ArkTS widgets since API version 22.

**Atomic service API**: This API can be used in atomic services since API version 22.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| count | number | [CacheCountInfo](../../common-definitions/basic-types/document.md#cachecountinfo22) | Yes | 
Number of preloaded **ListItem** components if the parameter is of the **number** type.

Value range: \[0, +∞).

Values less than 0 are treated as **1**.

If the parameter type is CacheCountInfo, the parameter indicates the maximum and minimum preloading range.

 |
| show | boolean | Yes | 

Whether to display the preloaded list items.

**true**: yes

**false**: no

 |

#### \[h2\]edgeEffect

edgeEffect(value: EdgeEffect, options?: EdgeEffectOptions)

Sets the effect used when the scroll boundary is reached.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d6/v3/O9ax4iUKTZGLRKCKOanz1Q/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062238Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=DB388CA94FEEBB104E3B023C96628F397CEE6CD10E8475F2CB06456DACD8D1E0)

By default, this component can produce a bounce effect only when there is more than one screen of content. To produce a bounce effect when there is less than one screen of content, set the **options** parameter of the **edgeEffect** attribute to **{ alwaysEnabled: true }**.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [EdgeEffect](../../common-definitions/enums/document.md#edgeeffect) | Yes | 
Effect used when the scroll boundary is reached. The spring and shadow effects are supported.

Default value: **EdgeEffect.Spring**

 |
| options11+ | [EdgeEffectOptions](../scrollable-component-common-apis/document.md#edgeeffectoptions11) | No | 

Whether to enable the scroll effect when the component content is smaller than the component itself. The value **{ alwaysEnabled: true }** means to enable the scroll effect, and **{ alwaysEnabled: false }** means the opposite.

Default value: **{ alwaysEnabled: false }**

 |

#### \[h2\]chainAnimation

chainAnimation(value: boolean)

Sets whether to enable the chain linkage effect for the current **List** component.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1a/v3/dzA2xycuSKSgBaiurzBJxQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062238Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=29F7DAC8280612F15397BA01A147CD1CDA7A5102869C67D6A9E8009B7A1B6272)

-   The chain linkage effect refers to the interaction where, during finger swiping, the dragged **ListItem** acts as the driving object, while adjacent items are driven objects. The driving object drives the linkage of the driven objects, following a physics-based spring animation.
-   The driving effect of the chain linkage effect is reflected in the spacing between **ListItem**s. The spacing in the static state can be set by using the **space** parameter of the **List** component. If the **space** parameter is not set and the chain linkage effect is enabled, the spacing is 20 vp by default.
-   After the chain linkage effect is enabled, the divider of the **List** component is not displayed.
-   The chain linkage effect takes effect only when the **List** component is in single-column mode and the edge effect is of the **EdgeEffect.Spring** type.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | boolean | Yes | 
Whether to enable chained animations.

**false** (default): Chained animations are disabled. **true**: Chained animations are enabled.

 |

#### \[h2\]multiSelectable8+

multiSelectable(value: boolean)

Sets whether to enable multiselect.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | boolean | Yes | 
Whether to enable multiselect.

**false** (default): Multiselect is disabled. **true**: Multiselect is enabled.

 |

#### \[h2\]lanes9+

lanes(value: number | LengthConstrain, gutter?: Dimension)

Sets the number of columns or rows in the **List** component. (When the **List** is scrolled vertically, the number of columns is displayed. When the **List** is scrolled horizontally, the number of rows is displayed.)

The following example describes how to set the number of columns:

-   If **value** is a number, the number of columns is specified based on the number.
-   If **value** is of the **LengthConstrain** type, **minLength** in **LengthConstrain** indicates the minimum column width. The **List** component calculates the maximum number of columns based on its minimum column width. In addition, **LengthConstrain** is passed to the child components of the **List** component as the maximum and minimum layout width constraints. These constraints take effect when the child components do not have a specified width.
-   Each list item group occupies one row in multi-column mode. Its child list items are arranged based on the **lanes** attribute of the list.
-   If **value** is of the **LengthConstrain** type, the number of columns in **ListItemGroup** is calculated based on the width of **ListItemGroup**. Therefore, when the width of **ListItemGroup** is different from that of the **List** component, the number of columns in **ListItemGroup** may be different from that in the **List** component.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | number | [LengthConstrain](../../common-definitions/basic-types/document.md#lengthconstrain) | Yes | 
Number of columns or rows in the list.

Default value: **1**

Value range: \[1, +∞)

 |
| gutter10+ | [Dimension](../../common-definitions/basic-types/document.md#dimension10) | No | 

Column gap or row gap.

Default value: **0**

Value range: \[0, +∞)

**NOTE**

This parameter takes effect when the number of columns or rows is greater than 1.

 |

#### \[h2\]lanes22+

lanes(value: number | LengthConstrain | ItemFillPolicy, gutter?: Dimension)

Sets the number of columns and the column spacing of the **List** component. By default, the **List** component is displayed in one column.

**Widget capability**: This API can be used in ArkTS widgets since API version 22.

**Atomic service API**: This API can be used in atomic services since API version 22.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | number | [LengthConstrain](../../common-definitions/basic-types/document.md#lengthconstrain) | [ItemFillPolicy](../../common-definitions/basic-types/document.md#itemfillpolicy22) | Yes | 
Number of columns in the layout of the **List** component.

If this parameter is set to a number, the number of columns is determined by this value. The value range of the number type is \[1, +∞).

If this parameter is set to a value of the **LengthConstrain** type, the number of columns is determined based on the maximum and minimum values specified in **LengthConstrain**.

If this parameter is set to a value of the **ItemFillPolicy** type, the number of columns is determined based on the [breakpoint type](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-layout-development-grid-layout#breakpoints) corresponding to the width of the **List** component. This type takes effect only when the scrolling direction of the list is vertical.

 |
| gutter | [Dimension](../../common-definitions/basic-types/document.md#dimension10) | No | 

Gap between columns.

Default value: **0**

Value range: \[0, +∞)

 |

#### \[h2\]alignListItem9+

alignListItem(value: ListItemAlign)

Sets the layout mode of list items along the cross axis when the cross-axis width of the list is greater than the value calculated by the following formula: cross-axis width of list items × lanes + (lanes – 1) × gutter.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [ListItemAlign](#listitemalign9) | Yes | 
Alignment mode of list items along the cross axis.

Default value: **ListItemAlign.Start**

 |

#### \[h2\]sticky9+

sticky(value: StickyStyle)

Sets whether to pin the header to the top or the footer to the bottom in the [list item group](../listitemgroup/document.md), if set. To support both the pin-to-top and pin-to-bottom features, set **sticky** to **StickyStyle.Header | StickyStyle.Footer**. From API version 20, the **sticky** attribute can also be set to **StickyStyle.BOTH** to enable both sticky header and sticky footer at the same time.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4e/v3/aR_0cOo7Sce8NuxpOqbNIQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062238Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=600931389418345821557EE9934893FE097DC443804053F980C50B90AF2B4109)

Occasionally, after **sticky** is set, floating-point calculation precision may result in small gaps appearing during scrolling. To address this issue, you can apply the [pixelRound](../../universal-attributes/layout-and-borders/component-level-pixel-rounding/document.md#pixelround) attribute to the current component, which rounds down the pixel values and help eliminate the gaps.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [StickyStyle](#stickystyle9) | Yes | 
Whether to pin the header to the top or the footer to the bottom in the list item group.

Default value: **StickyStyle.None**

 |

#### \[h2\]scrollSnapAlign10+

scrollSnapAlign(value: ScrollSnapAlign)

Sets the scroll snap alignment effect for list items when scrolling ends.

This API is available only when the heights of list items are the same. During the alignment animation, the scroll operation source type reported by the [onWillScroll](../scrollable-component-common-apis/document.md#onwillscroll12) event is **ScrollSource.FLING**.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [ScrollSnapAlign](#scrollsnapalign10) | Yes | 
Alignment mode of the scroll snap position.

Default value: **ScrollSnapAlign.NONE**

 |

#### \[h2\]scrollSnapAnimationSpeed22+

scrollSnapAnimationSpeed(speed: ScrollSnapAnimationSpeed)

Sets the speed of the snap animation for list item scrolling. This parameter takes effect only when the scroll alignment effect is set.

**Atomic service API**: This API can be used in atomic services since API version 22.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| speed | [ScrollSnapAnimationSpeed](#scrollsnapanimationspeed22) | Yes | 
Speed of the snap animation for listing scrolling.

Default value: **ScrollSnapAnimationSpeed.NORMAL**

 |

#### \[h2\]enableScrollInteraction10+

enableScrollInteraction(value: boolean)

Sets whether to support the scroll gesture.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | boolean | Yes | 
Whether to support the scroll gesture. With the value **true**, scrolling via finger or mouse is enabled. With the value **false**, scrolling via finger or mouse is disabled, but this does not affect the scrolling APIs of the [Scroller](../scroll/document.md#scroller).

Default value: **true**

 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6a/v3/cAaJEiNAQZCW4ccs9DW_Zw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062238Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=920CE5158168D83D9ADB6DD164D2494424F9E84EA1BACA695770DD37E56B15DA)

The component cannot be scrolled through mouse press-and-drag operations.

#### \[h2\]nestedScroll10+

nestedScroll(value: NestedScrollOptions)

Sets the nested scrolling mode in the forward and backward directions to implement scrolling linkage with the parent component.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [NestedScrollOptions](../scrollable-component-common-apis/document.md#nestedscrolloptions10) | Yes | 
Nested scrolling options.

Default value: **{ scrollForward: NestedScrollMode.SELF\_ONLY, scrollBackward: NestedScrollMode.SELF\_ONLY }**

 |

#### \[h2\]friction10+

friction(value: number | Resource)

Sets the friction coefficient. It applies only to gestures in the scrolling area, and it affects only the inertial scrolling process. A value less than or equal to 0 evaluates to the default value.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | number | [Resource](../../common-definitions/basic-types/document.md#resource) | Yes | 
Friction coefficient.

Default value: **0.6** for non-wearable devices and **0.9** for wearable devices.

Since API version 11, the default value for non-wearable devices is **0.7**.

Since API version 12, the default value for non-wearable devices is **0.75**.

 |

#### \[h2\]contentStartOffset11+

contentStartOffset(value: number)

Sets the offset from the start of the list content to the boundary of the list display area.

If the sum of **contentStartOffset** and **contentEndOffset** exceeds the length of the list content area, both offsets are reset to **0**.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | number | Yes | 
Offset from the start of the list content to the boundary of the list display area.

Default value: **0**

Unit: vp

**NOTE**

If the set value is a negative number, the default value will be used.

 |

#### \[h2\]contentStartOffset22+

contentStartOffset(offset: number | Resource)

Sets the offset from the start of the list content to the boundary of the list display area. Compared with [contentStartOffset11+](#contentstartoffset11), the parameter name is changed to **offset** and the Resource type is supported.

If the sum of **contentStartOffset** and **contentEndOffset** exceeds the length of the list content area, both offsets are reset to **0**.

**Atomic service API**: This API can be used in atomic services since API version 22.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| offset | number | [Resource](../../common-definitions/basic-types/document.md#resource) | Yes | 
Offset from the start of the list content to the boundary of the list display area.

Default value: **0**

Unit: vp

Invalid values (negative numbers or non-numeric Resource values) are treated as the default value.

 |

#### \[h2\]contentEndOffset11+

contentEndOffset(value: number)

Sets the offset from the end of the list content to the boundary of the list display area.

If the sum of **contentStartOffset** and **contentEndOffset** exceeds the length of the list content area, both offsets are reset to **0**.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | number | Yes | 
Offset from the end of the list content to the boundary of the list display area.

Default value: **0**

Unit: vp

**NOTE**

If the set value is a negative number, the default value will be used.

 |

#### \[h2\]contentEndOffset22+

contentEndOffset(offset: number | Resource)

Sets the offset from the end of the list content to the boundary of the list display area. Compared with [contentEndOffset11+](#contentendoffset11), the parameter name is changed to **offset** and the Resource type is supported.

If the sum of **contentStartOffset** and **contentEndOffset** exceeds the length of the list content area, both offsets are reset to **0**.

**Atomic service API**: This API can be used in atomic services since API version 22.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| offset | number | [Resource](../../common-definitions/basic-types/document.md#resource) | Yes | 
Offset from the end of the list content to the boundary of the list display area.

Default value: **0**

Unit: vp

Invalid values (negative numbers or non-numeric Resource values) are treated as the default value.

 |

#### \[h2\]childrenMainSize12+

childrenMainSize(value: ChildrenMainSize)

Sets the size information of the child components of a **List** component along the main axis.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/36/v3/K6GT7CKzRCSX_NahXNVRbg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062238Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7D6CEF6D664859604E24BD8A690DADD8ACCBCA14C827A78DDBDF9D8ED9C0C034)

-   This attribute provides the **List** component with the size of all child components in the main-axis direction. This ensures that the **List** component can maintain the accuracy of the scrolling position in scenarios such as varying main-axis sizes among child components, adding or removing child components, or using [scrollToIndex](../scroll/document.md#scrolltoindex). In this way, [scrollTo](../scroll/document.md#scrollto) can accurately jump to the specified position, [currentOffset](../scroll/document.md#currentoffset) can obtain the accurate scroll position, and the built-in scroll bar can be smoothly moved without jumps.
-   If a child component is **ListItemGroup**, the overall size of **ListItemGroup** in the main-axis direction needs to be accurately calculated based on the column count of **ListItemGroup**, the spacing between list items in **ListItemGroup** in the main-axis direction, and the size of the header, footer, and **ListItem** components in **ListItemGroup**. This calculated size must then be passed to the **List** component.
-   If a child component contains **ListItemGroup** components, the [childrenMainSize](../listitemgroup/document.md#childrenmainsize12) attribute must be set for each **ListItemGroup** component. The **List** component and each **ListItemGroup** component must be bound to a **ChildrenMainSize** object through the **childrenMainSize** attribute in one-to-one mode.
-   For a multi-column list where child components are generated using **LazyForEach**, ensure that **LazyForEach** generates either all **ListItemGroup** components or all **ListItem** components.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [ChildrenMainSize](../scrollable-component-common-apis/document.md#childrenmainsize12) | Yes | Size information of child components in the main axis direction. |

#### \[h2\]maintainVisibleContentPosition12+

maintainVisibleContentPosition(enabled: boolean)

Sets whether to maintain the visible content's position when data is inserted or deleted outside the display area of the component.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| enabled | boolean | Yes | 
Whether to maintain the visible content's position when data is inserted or deleted outside the visible area of the component.

Default value: **false**

**false**: The visible content position will change when data is inserted or deleted. **true**: The visible content position remains unchanged when data is inserted or deleted.

 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e5/v3/-0vtbCD_RfiLlV2ecapDeg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062238Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F9303A62217866835AF03BB78728E82138A6C85D276D5A659409DC6CF8286BA2)

-   The visible content position will remain unchanged if this attribute is set to **true** only when **LazyForEach** is used to insert or delete data outside the visible area. If **ForEach** is used to insert or delete data, or if **LazyForEach** is used for data reloading, the visible content position will change even if **maintainVisibleContentPosition** is set to **true**.
-   Since API version 20, if [Repeat](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-new-rendering-control-repeat) is used for lazy loading, the position of the visible content remains unchanged when data is inserted or deleted outside the visible area even if the **maintainVisibleContentPosition** attribute is set to **true**.
-   When **maintainVisibleContentPosition** is set to **true**, inserting or deleting data above the visible area will trigger [onDidScroll](../scrollable-component-common-apis/document.md#ondidscroll12) and **onScrollIndex** events.
-   In a multi-column scenario, setting **maintainVisibleContentPosition** to **true** allows you to insert or delete entire rows of data while keeping the visible content position unchanged. If the insertion or deletion does not involve entire rows, however, the visible content position will still change.

#### \[h2\]stackFromEnd19+

stackFromEnd(enabled: boolean)

Whether the list's layout starts from the bottom (end) rather than the top (beginning).

**Atomic service API**: This API can be used in atomic services since API version 19.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| enabled | boolean | Yes | 
Whether the list's layout starts from the bottom (end) rather than the top (beginning).

**false** (default): The layout starts from the top. **true**: The layout starts from the bottom.

 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4a/v3/1fm7TYRYTVOUeMp8n_XfiQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062238Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=FED13E4670A1C9672112C5E4CB9EC74FA7D82D2079E4238357E94A4E6B10B962)

-   When **stackFromEnd** is set to **true**, the following rules apply:
    
    If the content of the **List** component is shorter than the component height, the content will be aligned to the bottom of the component.
    
-   If the height of a list item in the visible area changes, or if a new list item is inserted, the list items above the changed or inserted item will move upwards to accommodate the new layout.
-   When **stackFromEnd** is set to **true**, the default value of **initialIndex** in [ListOptions](#listoptions18) is the total number of items minus 1.

#### \[h2\]focusWrapMode20+

focusWrapMode(mode: Optional<FocusWrapMode>)

Sets the focus wrap mode for arrow keys.

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| mode | [Optional](../../universal-attributes/modifiers-and-custom-property/custom-property/document.md#optionalt)<[FocusWrapMode](../../common-definitions/enums/document.md#focuswrapmode20)\> | Yes | 
Focus wrap mode for cross-axis arrow keys.

Default value: **FocusWrapMode.DEFAULT**

**NOTE**

Abnormal values are treated as the default value, meaning that cross-axis arrow keys cannot wrap.

 |

#### \[h2\]syncLoad20+

syncLoad(enable: boolean)

Sets whether to synchronously load all child components in the list.

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| enable | boolean | Yes | 
Whether to synchronously load all child components in the list.

**true**: yes; **false**: no Default value: **true**

**NOTE**

When this parameter is set to **false**, in the first display or **scrollToIndex** jumps without animation, if the time consumed by the frame layout exceeds 50 ms, the child components that have not been laid out in the list are delayed to the next frame for layout.

 |

#### \[h2\]editMode(deprecated)

editMode(value: boolean)

Sets whether to enable edit mode. For details about how to delete selected list items, see [Example 3](#example-3-setting-the-edit-mode).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5b/v3/HO2-DLcQRPWpFYM6C6tvvQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062238Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8D2B7C26EACC805E778EBAB965B5F142F0AB47C5B22627C17D29F342117814E6)

This API is supported since API version 7 and deprecated since API version 9. No substitute is provided.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | boolean | Yes | 
Whether to enable edit mode.

Default value: **false** (the edit mode is disabled).

 |

#### ListItemAlign9+

Sets the alignment mode of child components in the cross-axis direction of the list.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Value | Description |
| :-- | :-- | :-- |
| Start | 0 | The list items are packed toward the start edge of the **List** component along the cross axis. |
| Center | 1 | The list items are centered in the **List** component along the cross axis. |
| End | 2 | The list items are packed toward the end edge of the **List** component along the cross axis. |

#### StickyStyle9+

Enumerates the sticky styles.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Value | Description |
| :-- | :-- | :-- |
| None | 0 | 
In the **ListItemGroup** component, the header is not pinned to the top, and the footer is not pinned to the bottom.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| Header | 1 | 

In the **ListItemGroup** component, the header is pinned to the top, and the footer is not pinned to the bottom.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| Footer | 2 | 

In the **ListItemGroup** component, the footer is pinned to the bottom, and the header is not pinned to the top.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| BOTH20+ | 3 | 

In the **ListItemGroup** component, the header is pinned to the top, and the footer is pinned to the bottom.

**Widget capability**: This API can be used in ArkTS widgets since API version 20.

**Atomic service API**: This API can be used in atomic services since API version 20.

 |

#### ScrollSnapAlign10+

Enumerates the alignment modes of list items when scrolling ends.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Value | Description |
| :-- | :-- | :-- |
| NONE | 0 | No alignment. This is the default value. |
| START | 1 | 
The first item in the view is aligned at the start of the list.

**NOTE**

When the list hits the end, the items at the end must be completely displayed. In this case, the items at the start may not be aligned.

 |
| CENTER | 2 | 

The middle items in the view are aligned in the center of the list.

**NOTE**

The top and end items can be aligned to the center of the list. In this case, which may cause empty space to be visible in the list display.

 |
| END | 3 | 

The last item in the view is aligned at the end of the list.

**NOTE**

When the list hits the start, the items at the start must be completely displayed. In this case, the items at the end may not be aligned.

 |

#### ScrollSnapAnimationSpeed22+

Enumerates speeds of the snap animation for list scrolling.

**Atomic service API**: This API can be used in atomic services since API version 22.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Value | Description |
| :-- | :-- | :-- |
| NORMAL | 0 | Default snap animation speed for the list, typically used when list items are large and scrolling moves one item per swipe. |
| SLOW | 1 | Slower snap animation speed, typically used when list items are small and scrolling moves multiple items per swipe. |

#### CloseSwipeActionOptions11+

Implements the callbacks and events for the [ListItem](../listitem/document.md) in the [expanded](../listitem/document.md#swipeactionstate11) state.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| onFinish | ()=>void | No | Yes | Triggered after the collapse animation is complete. |

#### ListDividerOptions18+

Defines the divider style of the list or list item group.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cf/v3/hD6akFNqTiue4CEpXbipwQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062238Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=36C683B865A9BB40731840F95550C74219B542E21D821257598DE67DD877436D)

To standardize anonymous object definitions, the element definitions here have been revised in API version 18. While historical version information is preserved for anonymous objects, there may be cases where the outer element's @since version number is higher than inner elements'. This does not affect interface usability.

**Widget capability**: This API can be used in ArkTS widgets since API version 18.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| strokeWidth7+ | [Length](../../common-definitions/basic-types/document.md#length) | No | No | 
Width of the divider.

Unit: vp

**NOTE**

If this parameter is set to a negative number, a percentage, or a value greater than or equal to the length of the list content area, the value **0** will be used.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| color7+ | [ResourceColor](../../common-definitions/basic-types/document.md#resourcecolor) | No | Yes | 

Color of the divider.

Default value: **0x08000000**

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| startMargin7+ | [Length](../../common-definitions/basic-types/document.md#length) | No | Yes | 

Distance between the divider and the start edge of the list.

Default value: **0**

Unit: vp

**NOTE**

If this parameter is set to a negative number or a percentage, the default value will be used.

If **endMargin** and **startMargin** add up to a value that exceeds the column width, they will be set to **0**.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| endMargin7+ | [Length](../../common-definitions/basic-types/document.md#length) | No | Yes | 

Distance between the divider and the end edge of the list.

Default value: **0**

Unit: vp

**NOTE**

If this parameter is set to a negative number or a percentage, the default value will be used.

If **endMargin** and **startMargin** add up to a value that exceeds the column width, they will be set to **0**.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |

#### Events

In addition to [universal events](../../universal-events/document.md) and [scrollable component common events](../scrollable-component-common-apis/document.md#events), the following events are also supported.

#### \[h2\]onScrollIndex

onScrollIndex(event: (start: number, end: number, center: number) => void)

Triggered when a child component enters or leaves the list display area. During index calculation, each **ListItemGroup** component is taken as a whole and assigned an index, and the indexes of the list items within are not included in the calculation.

When the list edge scrolling effect is the spring effect, the **onScrollIndex** event is not triggered when the user scrolls the list to the edge or releases the list to rebound.

This event is triggered once when the list is initialized and when the index of the first child component or the next child component in the list display area changes.

Since API version 10, this event is also triggered when the child component in the center of the list display area changes.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| start | number | Yes | Index of the first child component in the list display area. |
| end | number | Yes | Index of the last child component in the list display area. |
| center10+ | number | Yes | Index of the center child component in the list display area. |

#### \[h2\]onReachStart

onReachStart(event: () => void)

Triggered when the list reaches the start position.

This event is triggered once when **initialIndex** is **0** during list initialization and once when the list scrolls to the start position. When the list edge scrolling effect is the spring effect, this event is triggered once when the list passes the start position and is triggered again when the list returns to the start position.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| event | () => void | Yes | Callback triggered when the list reaches the start position. |

#### \[h2\]onReachEnd

onReachEnd(event: () => void)

Called when the list reaches the end position. This callback is triggered when the last child component appears in the list view due to scrolling or content/layout changes.

If the child component does not fill the list and can be completely displayed in the list without scrolling, this event is triggered during the first loading.

When the list edge scrolling effect is the spring effect, this event is triggered once when the list passes the end position and is triggered again when the list returns to the end position.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| event | () => void | Yes | Callback triggered when the list reaches the end position. |

#### \[h2\]onScrollFrameBegin9+

onScrollFrameBegin(event: OnScrollFrameBeginCallback)

When this API is called back, the event parameter passes the scroll offset that is about to occur. The event processing function can calculate the actually required scroll offset based on the application scenario and return it as the return value. The list will then scroll according to this returned actual scroll offset.

If **listDirection** is set to **Axis.Vertical**, the return value is the amount by which the list needs to scroll in the vertical direction. If **listDirection** is set to **Axis.Horizontal**, the return value is the amount by which the list needs to scroll in the horizontal direction.

This event is triggered when either of the following conditions is met:

1.  Scrolling is initiated by user interaction (for example, finger swipe, keyboard, or mouse operation).
2.  The **List** component scrolls by inertia.
3.  Call the [fling](../scroll/document.md#fling12) API to trigger scrolling.

This event is not triggered in the following scenarios:

1.  A scroll control API other than [fling](../scroll/document.md#fling12) is called.
2.  The out-of-bounds bounce effect is active.
3.  The scrollbar is dragged.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| event | [OnScrollFrameBeginCallback](../scroll/document.md#onscrollframebegincallback18) | Yes | Callback triggered when each frame scrolling starts. |

#### \[h2\]onScrollStart9+

onScrollStart(event: () => void)

Triggered when the list starts scrolling initiated by the user's finger dragging the list or its scrollbar. This event is also triggered when the animation contained in the scrolling triggered by [Scroller](../scroll/document.md#scroller) starts.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| event | () => void | Yes | Callback invoked when the list starts scrolling. |

#### \[h2\]onScrollStop

onScrollStop(event: () => void)

Triggered when the list stops scrolling after the user's finger leaves the screen. This event is also triggered when the animation contained in the scrolling triggered by [Scroller](../scroll/document.md#scroller) stops.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| event | () => void | Yes | Callback triggered when the list stops sliding. |

#### \[h2\]onItemMove

onItemMove(event: (from: number, to: number) => boolean)

Triggered when a list item moves.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| from | number | Yes | Index of the item before moving. |
| to | number | Yes | Index of the item after moving. |

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Whether the item is moved. If the return value is **true**, the list item is moved. If the return value is **false**, the list item is not moved. |

#### \[h2\]onItemDragStart8+

onItemDragStart(event: (event: ItemDragInfo, itemIndex: number) => ((() => any) | void))

Triggered when a list item starts to be dragged.

Automatic scrolling of the list cannot be triggered when a list item is dragged to the edge of the list. You can use the [onMove](../../universal-attributes/interaction-properties/drag-and-drop-sorting/document.md#onmove) API of **ForEach**, **LazyForEach**, or **Repeat** to implement this effect. For details, see [Example 12: Implementing Dragging with OnMove](#example-12-implementing-dragging-with-onmove). However, note that the [onMove](../../universal-attributes/interaction-properties/drag-and-drop-sorting/document.md#onmove) API does not support cross-**ListItemGroup** dragging.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/98/v3/XcplJF3nRFS4aRFSfArp9g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062238Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3CEAA7B7B451A66DB61957A0E1949E77119BAB1886FFBA6CF488BA4F4AAB2E5E)

This API can be called within [attributeModifier](../../universal-attributes/modifiers-and-custom-property/attribute-modifier/document.md#attributemodifier) since API version 14.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| event | [ItemDragInfo](../scrollable-component-common-apis/document.md#itemdraginfo) | Yes | Information about the drag point. |
| itemIndex | number | Yes | Index of the dragged item. |

#### \[h2\]onItemDragEnter8+

onItemDragEnter(event: (event: ItemDragInfo) => void)

Called when a dragged list item enters the list.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| event | [ItemDragInfo](../scrollable-component-common-apis/document.md#itemdraginfo) | Yes | Information about the drag point. |

#### \[h2\]onItemDragMove8+

onItemDragMove(event: (event: ItemDragInfo, itemIndex: number, insertIndex: number) => void)

Called when a dragged list item moves in the list.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| event | [ItemDragInfo](../scrollable-component-common-apis/document.md#itemdraginfo) | Yes | Information about the drag point. |
| itemIndex | number | Yes | Initial position of the dragged item. |
| insertIndex | number | Yes | Index of the position to which the dragged item is dropped. |

#### \[h2\]onItemDragLeave8+

onItemDragLeave(event: (event: ItemDragInfo, itemIndex: number) => void)

Called when a dragged list item leaves the list.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| event | [ItemDragInfo](../scrollable-component-common-apis/document.md#itemdraginfo) | Yes | Information about the drag point. |
| itemIndex | number | Yes | Index of the dragged item. |

#### \[h2\]onItemDrop8+

onItemDrop(event: (event: ItemDragInfo, itemIndex: number, insertIndex: number, isSuccess: boolean) => void)

Triggered when the dragged item is dropped on the drop target of the list.

During dragging across lists, **isSuccess** is set to **true** if the drop target is bound to **onItemDrop**. Otherwise, **isSuccess** is set to **false**. During dragging within a list, **isSuccess** is the return value of the **onItemMove** event.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| event | [ItemDragInfo](../scrollable-component-common-apis/document.md#itemdraginfo) | Yes | Information about the drag point. |
| itemIndex | number | Yes | Initial position of the dragged item. |
| insertIndex | number | Yes | Index of the position to which the dragged item is dropped. |
| isSuccess | boolean | Yes | Whether the dragged item is successfully dropped. If the return value is **true**, the list item is successfully dropped. If the return value is **false**, the list item is not successfully dropped. |

#### \[h2\]onScrollVisibleContentChange12+

onScrollVisibleContentChange(handler: OnScrollVisibleContentChangeCallback)

Triggered when a child component enters or leaves the list display area. During index calculation, the list item, header of the list item group, and footer of the list item group each are counted as a child component.

When the list edge scrolling effect is the spring effect, the **onScrollVisibleContentChange** event is not triggered when the user scrolls the list to the edge or releases the list to rebound.

This event is triggered once when the list is initialized and when the index of the first child component or the next child component in the list display area changes.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| handler | [OnScrollVisibleContentChangeCallback](#onscrollvisiblecontentchangecallback12) | Yes | Callback invoked when the displayed content changes. |

#### \[h2\]onItemDelete(deprecated)

onItemDelete(event: (index: number) => boolean)

Triggered when a list item is deleted.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/66/v3/6Ep7uuF9SHyVbDZ6UPgLDQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062238Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=252A011879B2B7138D7BAEF3AC32B11B188DE0665B90ADA6F159A7DBDB59415A)

This API is supported since API version 7 and deprecated since API version 9. No substitute is provided.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| index | number | Yes | Index of the deleted list item. |

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Whether the list item is deleted. |

#### \[h2\]onScroll(deprecated)

onScroll(event: (scrollOffset: number, scrollState: [ScrollState](#scrollstate)) => void)

Triggered when the list scrolls.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/34/v3/LZQUQfeIQJOKnzVWGq35Lg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062238Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E36DE31FB88586CD84E0393E86BDC1803AE8B98778D3AACD75BDB92743F468C3)

This API is supported since API version 7 and deprecated since API version 12. You are advised to use [onDidScroll](../scrollable-component-common-apis/document.md#ondidscroll12) instead.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| scrollOffset | number | Yes | 
Offset relative to the previous frame. The offset is positive when the list content scrolls up and negative when the list content scrolls down.

Unit: vp

 |
| scrollState | [ScrollState](#scrollstate) | Yes | Current scroll state. |

#### ScrollState

Enumerates the scrolling states.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Value | Description |
| :-- | :-- | :-- |
| Idle | 0 | Idle state. Triggered when the scroll state returns to idle, and when the controller's non-animated methods are used to control the scroll. |
| Scroll | 1 | Scrolling state. Triggered when the list is dragged with the finger, when the scrollbar is dragged, or when the mouse scroll wheel is used. |
| Fling | 2 | 
Inertial scrolling state. Triggered by all animated scroll actions. This includes: Inertial scrolling that occurs after a fling;

Bounce-back scrolling when the swipe reaches the edge; Inertial scrolling after quickly dragging the built-in scrollbar and releasing;

Scrolling controlled by the animated methods provided by the scroller.

 |

#### ListScroller11+

Implements the scroll controller of the **List** component. A **List** component is bound to a **ListScroller** on a one-to-one basis.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/62/v3/8Fk-YmzORTuGJy5P5S9TEw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062238Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=226A30AC4D20E56AD2472B95518CCEFF57777F2F791F409D298163B085E823FF)

**ListScroller** inherits from [Scroller](../scroll/document.md#scroller) and has all methods of [Scroller](../scroll/document.md#scroller).

## Objects to Import

listScroller: ListScroller = new ListScroller();

#### \[h2\]getItemRectInGroup11+

getItemRectInGroup(index: number, indexInGroup: number): RectResult

Obtains the size of a [list item](../listitem/document.md) in a [list item group](../listitemgroup/document.md) and its position relative to the list.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| index | number | Yes | Index of the list item group in the list. |
| indexInGroup | number | Yes | Index of the list item in the list item group. |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ca/v3/fpsKu69jTlCsH4q5a1R6Mw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062238Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F09C7DA0C44C25413A82CDEDE115E0A0F194128F3503ADFCA2FFC0C89FEB3A68)

-   The value of **index** must be the index of a child component visible in the display area. Otherwise, the value is considered invalid.
-   The child component for which **index** is set must be a list item group. Otherwise, the **index** value is considered invalid.
-   The value of **indexInGroup** must be the index of a list item in the list item group visible in the display area. Otherwise, the value is considered invalid.
-   When **index** or **indexInGroup** is set to an invalid value, the returned size and position are both **0**.

**Return value**

| Type | Description |
| :-- | :-- |
| [RectResult](../../universal-events/event-dispatch-control/custom-event-dispatch/document.md#rectresult) | 
Size of the list item in the list item group and its position relative to the list.

Unit: vp

 |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [Scrollable Component Error Codes](../../../error-codes/ui/scrollable-component-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.Incorrect parameters types; 3. Parameter verification failed. |
| 100004 | Controller not bound to component. |

#### \[h2\]getVisibleListContentInfo14+

getVisibleListContentInfo(x: number, y: number): VisibleListContentInfo

Obtains the index information of the child component at the specified coordinates.

**Atomic service API**: This API can be used in atomic services since API version 14.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| x | number | Yes | X-coordinate, in vp. |
| y | number | Yes | Y-coordinate, in vp. |

**Return value**

| Type | Description |
| :-- | :-- |
| [VisibleListContentInfo](#visiblelistcontentinfo12) | Index information of a child component at the specified coordinates. |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/77/v3/rpGBAVtrT_OHtCIzspmlLw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062238Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F8640BF4112273F464DFE94DE3D516D578A219FDA16B2D5B246025173C2E91F1)

-   The reference point of the input coordinates (x, y) is the position of the **List** component.
-   If the coordinate position falls within the area of the **ListItem** component whose parent component is **List**, the index of a return value object member will be the index of the **ListItem** component in **List**, **itemGroupArea** will return **undefined**, and **itemIndexInGroup** will return **undefined**.
-   If the coordinate position falls within the area of the **ListItem** component whose parent component is **ListItemGroup**, the index of a return value object member will be the index of the **ListItemGroup** component in **List**, **itemGroupArea** will return **ListItemGroupArea.IN\_LIST\_ITEM\_AREA**, and **itemIndexInGroup** will return the index of **ListItem** in **ListItemGroup**.
-   If the coordinates are not within the range of **ListItem** but within the range of header or footer of **ListItemGroup**, the index of the returned object member is the index of **ListItemGroup** in **List**, and **itemIndexInGroup** will return **undefined**. If the coordinates are within the range of header, **itemGroupArea** will return **ListItemGroupArea.IN\_HEADER\_AREA**. If the coordinates are within the range of footer, **itemGroupArea** will return **ListItemGroupArea.IN\_FOOTER\_AREA**.
-   If the coordinates are not within the area of a **ListItem** component, nor within the header or footer area of a **ListItemGroup** component, but is within the area of a **ListItemGroup** component, the index of the returned object member will be the index of that **ListItemGroup** within the **List**, **itemIndexInGroup** will return **undefined**, and **itemGroupArea** will return **ListItemGroupArea.NONE**.
-   If the coordinates are not within a **ListItem** or **ListItemGroup** component, the index of the returned object member is **\-1** and both **itemIndexInGroup** and **itemGroupArea** will return **undefined**.

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [Scrollable Component Error Codes](../../../error-codes/ui/scrollable-component-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.Incorrect parameters types; 3. Parameter verification failed. |
| 100004 | The controller not bound to component. |

#### \[h2\]scrollToItemInGroup11+

scrollToItemInGroup(index: number, indexInGroup: number, smooth?: boolean, align?: ScrollAlign): void

Scrolls to the specified list item in the specified list item group.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| index | number | Yes | 
Index of the target list item group in the current container.

**NOTE**

If the value set is a negative value or greater than the maximum index of the items in the container, the value is deemed abnormal, and no scrolling will be performed.

 |
| indexInGroup | number | Yes | 

Index of the target list item in the list item group specified by **index**.

**NOTE**

If the value set is a negative value or greater than the maximum index of the items in the list item group, the value is deemed abnormal, and no scrolling will be performed.

 |
| smooth | boolean | No | 

Whether the scroll animation is enabled. The options are **true** (enabled) and **false** (disabled).

Default value: **false**

**NOTE**

When **smooth** is set to **true**, all passed items are loaded and counted in layout calculation. This may result in performance issues if a large number of items are involved.

 |
| align | [ScrollAlign](../scroll/document.md#scrollalign10) | No | 

How the list item to scroll to is aligned with the container.

Default value: **ScrollAlign.START**

 |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [Scrollable Component Error Codes](../../../error-codes/ui/scrollable-component-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.Incorrect parameters types; 3. Parameter verification failed. |
| 100004 | Controller not bound to component. |

#### \[h2\]closeAllSwipeActions11+

closeAllSwipeActions(options?: CloseSwipeActionOptions): void

Collapses the [list items](../listitem/document.md) in the [EXPANDED](../listitem/document.md#swipeactionstate11) state and sets callback events.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| options | [CloseSwipeActionOptions](#closeswipeactionoptions11) | No | Callback events for collapsing [list items](../listitem/document.md) in the [EXPANDED](../listitem/document.md#swipeactionstate11) state. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [Scrollable Component Error Codes](../../../error-codes/ui/scrollable-component-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.Incorrect parameters types; 3. Parameter verification failed. |
| 100004 | Controller not bound to component. |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/76/v3/MONSplSqSTeFlIr9zOzvYw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062238Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C5E2CCA7C4FDCDE27ED15E09AF38F11E6D8D079F2B81E77B23ACABE46C8ECA12)

-   A **ListScroller** must be bound to the **List** component.

#### OnScrollVisibleContentChangeCallback12+

type OnScrollVisibleContentChangeCallback = (start: VisibleListContentInfo, end: VisibleListContentInfo) => void

Triggered when a child component enters or leaves the list display area.

If the values of **start** and **end** are both **\-1**, the **List** component becomes empty.

If the values of **start** and **end** are both **0**, the **List** component contains only one child component.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/77/v3/N-VJCflGSCCTBFLv7kXfLA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062238Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=AD78C21BCBBC127F1A2A76BB5AAFD4D78D748749A67C9FF55C28C577119015E9)

This API can be called within [attributeModifier](../../universal-attributes/modifiers-and-custom-property/attribute-modifier/document.md#attributemodifier) since API version 14.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| start | [VisibleListContentInfo](#visiblelistcontentinfo12) | Yes | 
1\. Index of the first child component in the list display area.

2\. If the first child component in the list display area is **ListItemGroup**, you can obtain the area where the first child component belongs.

3\. If the first child component in the list display area is **ListItem** in **ListItemGroup**, you can obtain the index of **ListItem** in **ListItemGroup**.

 |
| end | [VisibleListContentInfo](#visiblelistcontentinfo12) | Yes | 

1\. Index of the last child component in the list display area.

2\. If the last child component in the list display area is **ListItemGroup**, you can obtain the area where the last child component belongs.

3\. If the last child component in the list display area is **ListItem** in **ListItemGroup**, you can obtain the index of **ListItem** in **ListItemGroup**.

 |

#### VisibleListContentInfo12+

Describes the details of the child components in the visible area of a list.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| index | number | No | No | Index of **ListItem** or **ListItemGroup** in the **List** component. |
| itemGroupArea | [ListItemGroupArea](#listitemgrouparea12) | No | Yes | Area where **ListItemGroup** is located. |
| itemIndexInGroup | number | No | Yes | Index of **ListItem** in **ListItemGroup**. |

#### ListItemGroupArea12+

Enumerates the areas of **ListItemGroup**.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Value | Description |
| :-- | :-- | :-- |
| NONE | 0 | Area other than the **ListItem**, header, and footer areas in **ListItemGroup**. |
| IN\_LIST\_ITEM\_AREA | 1 | **ListItem** area in **ListItemGroup**. |
| IN\_HEADER\_AREA | 2 | Header area in **ListItemGroup**. |
| IN\_FOOTER\_AREA | 3 | Footer area in **ListItemGroup**. |

#### UIListEvent19+

Represents the return value of the [getEvent('List')](../../../arkts-api/ui/arkui/framenode/document.md#geteventlist19) method in **frameNode**, which can be used to set scroll events for a **List** node.

**UIListEvent** inherits from [UIScrollableCommonEvent](../scrollable-component-common-apis/document.md#uiscrollablecommonevent19).

#### \[h2\]setOnWillScroll19+

setOnWillScroll(callback: OnWillScrollCallback | undefined): void

Sets the callback for the [onWillScroll](../scrollable-component-common-apis/document.md#onwillscroll12) event.

If the input parameter is **undefined**, the event callback is reset.

**Atomic service API**: This API can be used in atomic services since API version 19.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | [OnWillScrollCallback](../scrollable-component-common-apis/document.md#onwillscrollcallback12) | undefined | Yes | Callback for the **onWillScroll** event. |

#### \[h2\]setOnDidScroll19+

setOnDidScroll(callback: OnScrollCallback | undefined): void

Sets the callback for the [onDidScroll](../scrollable-component-common-apis/document.md#ondidscroll12) event.

If the input parameter is **undefined**, the event callback is reset.

**Atomic service API**: This API can be used in atomic services since API version 19.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | [OnScrollCallback](../scrollable-component-common-apis/document.md#onscrollcallback12) | undefined | Yes | Callback for the **onDidScroll** event. |

#### \[h2\]setOnScrollIndex19+

setOnScrollIndex(callback: OnListScrollIndexCallback | undefined): void

Sets the callback of the [onScrollIndex](#onscrollindex) event.

If the input parameter is **undefined**, the event callback is reset.

**Atomic service API**: This API can be used in atomic services since API version 19.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | [OnListScrollIndexCallback](#onlistscrollindexcallback19) | undefined | Yes | Callback for the **onScrollIndex** event. |

#### \[h2\]setOnScrollVisibleContentChange19+

setOnScrollVisibleContentChange(callback: OnScrollVisibleContentChangeCallback | undefined): void

Sets the callback of the [onScrollVisibleContentChange](#onscrollvisiblecontentchange12) event.

If the input parameter is **undefined**, the event callback is reset.

**Atomic service API**: This API can be used in atomic services since API version 19.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | [OnScrollVisibleContentChangeCallback](#onscrollvisiblecontentchangecallback12) | undefined | Yes | Callback for the **onScrollVisibleContentChange** event. |

#### OnListScrollIndexCallback19+

type OnListScrollIndexCallback = (start: number, end: number, center: number) => void

Represents a callback for item changes in the visible area of the **List** component.

**Widget capability**: This API can be used in ArkTS widgets since API version 19.

**Atomic service API**: This API can be used in atomic services since API version 19.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| start | number | Yes | Index of the first child component in the list display area. |
| end | number | Yes | Index of the last child component in the list display area. |
| center | number | Yes | Index of the center child component in the list display area. |

#### Example

## Example 1: Adding a Scroll Event

In this example, a vertical list is implemented, and a callback is invoked when the first or last item displayed in the list changes.

**ListDataSource** implements the **LazyForEach** data source API [IDataSource](../../state-management-and-rendering-control/lazyforeach/document.md#idatasource), which is used to provide child components for **List** through **LazyForEach**.

// ListDataSource.ets
export class ListDataSource implements IDataSource {
  private list: number\[\] = \[\];
  private listeners: DataChangeListener\[\] = \[\];

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
    if (this.listeners.indexOf(listener) < 0) {
      this.listeners.push(listener);
    }
  }

  unregisterDataChangeListener(listener: DataChangeListener): void {
    const pos = this.listeners.indexOf(listener);
    if (pos >= 0) {
      this.listeners.splice(pos, 1);
    }
  }

  // Notify LazyForEach that all child components need to be reloaded.
  notifyDataReload(): void {
    this.listeners.forEach(listener => {
      listener.onDataReloaded();
    });
  }

  // Notify the controller of data deletion.
  notifyDataDelete(index: number): void {
    this.listeners.forEach(listener => {
      listener.onDataDelete(index);
    });
  }

  // Notify the controller of data insertion.
  notifyDataAdd(index: number): void {
    this.listeners.forEach(listener => {
      listener.onDataAdd(index);
    });
  }

  // Delete an element at the specified index.
  public deleteItem(index: number): void {
    this.list.splice(index, 1);
    this.notifyDataDelete(index);
  }

  // Insert an element at the specified index.
  public insertItem(index: number, data: number): void {
    this.list.splice(index, 0, data);
    this.notifyDataAdd(index);
  }

  public reloadData(): void {
    this.notifyDataReload();
  }
}

// xxx.ets
import { ListDataSource } from './ListDataSource';

@Entry
@Component
struct ListExample {
  private arr: ListDataSource = new ListDataSource(\[0, 1, 2, 3, 4, 5, 6, 7, 8, 9\]);

  build() {
    Column() {
      List({ space: 20, initialIndex: 0 }) {
        LazyForEach(this.arr, (item: number) => {
          ListItem() {
            Text('' + item)
              .width('100%').height(100).fontSize(16)
              .textAlign(TextAlign.Center).borderRadius(10).backgroundColor(0xFFFFFF)
          }
        }, (item: number) => item.toString())
      }
      .listDirection(Axis.Vertical) // Arrangement direction
      .scrollBar(BarState.Off)
      .friction(0.6)
      .divider({ strokeWidth: 2, color: 0xFFFFFF, startMargin: 20, endMargin: 20 }) // Divider
      .edgeEffect(EdgeEffect.Spring) // Set the edge scrolling effect to Spring.
      .onScrollIndex((firstIndex: number, lastIndex: number, centerIndex: number) => {
        console.info('first' + firstIndex);
        console.info('last' + lastIndex);
        console.info('center' + centerIndex);
      })
      .onScrollVisibleContentChange((start: VisibleListContentInfo, end: VisibleListContentInfo) => {
        console.info(' start index: ' + start.index +
                    ' start item group area: ' + start.itemGroupArea +
                    ' start index in group: ' + start.itemIndexInGroup);
        console.info(' end index: ' + end.index +
                    ' end item group area: ' + end.itemGroupArea +
                    ' end index in group: ' + end.itemIndexInGroup);
      })
      .onDidScroll((scrollOffset: number, scrollState: ScrollState) => {
        console.info(\`onScroll scrollState = ScrollState\` + scrollState + \`, scrollOffset = \` + scrollOffset);
      })
      .width('90%')
    }
    .width('100%')
    .height('100%')
    .backgroundColor(0xDCDCDC)
    .padding({ top: 5 })
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4a/v3/kXMUc0gFRTSYkbvNRo53Pg/en-us_image_0000002568765237.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062238Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C4419317576D18C15DC4466E5882308342D68529822B876378974DD04CBFC41F)

## Example 2: Setting Child Element Alignment

This example showcases the alignment effects of child elements in the cross-axis direction of the **List** component using different **ListItemAlign** enumeration values.

For details about **ListDataSource** and the complete code, see [Example 1: Adding a Scroll Event](#example-1-adding-a-scroll-event).

// xxx.ets
import { ListDataSource } from './ListDataSource';

@Entry
@Component
struct ListLanesExample {
  arr: ListDataSource = new ListDataSource(\[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19\]);
  @State alignListItem: ListItemAlign = ListItemAlign.Start;

  build() {
    Column() {
      List({ space: 20, initialIndex: 0 }) {
        LazyForEach(this.arr, (item: string) => {
          ListItem() {
            Text('' + item)
              .width('100%')
              .height(100)
              .fontSize(16)
              .textAlign(TextAlign.Center)
              .borderRadius(10)
              .backgroundColor(0xFFFFFF)
          }
          .border({ width: 2, color: Color.Green })
        }, (item: string) => item)
      }
      .height(300)
      .width('90%')
      .friction(0.6)
      .border({ width: 3, color: Color.Red })
      .lanes({ minLength: 40, maxLength: 40 })
      .alignListItem(this.alignListItem)
      .scrollBar(BarState.Off)

      Button('Change alignListItem:' + this.alignListItem).onClick(() => {
        if (this.alignListItem == ListItemAlign.Start) {
          this.alignListItem = ListItemAlign.Center;
        } else if (this.alignListItem == ListItemAlign.Center) {
          this.alignListItem = ListItemAlign.End;
        } else {
          this.alignListItem = ListItemAlign.Start;
        }
      })
    }.width('100%').height('100%').backgroundColor(0xDCDCDC).padding({ top: 5 })
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b4/v3/hg1XEqGFR-yA724nUL-Agg/en-us_image_0000002537765512.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062238Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=EDC4F200C07E836E9279451CCE540C71CFC571783EB00CFE0AFB2F9968FC41E9)

## Example 3: Setting the Edit Mode

This example illustrates how to set whether the current **List** component is in edit mode.

For details about **ListDataSource** and the complete code, see [Example 1: Adding a Scroll Event](#example-1-adding-a-scroll-event).

// xxx.ets
import { ListDataSource } from './ListDataSource';

@Entry
@Component
struct ListExample {
  arr: ListDataSource = new ListDataSource(\[0, 1, 2, 3, 4, 5, 6, 7, 8, 9\]);
  @State editFlag: boolean = false;

  build() {
    Stack({ alignContent: Alignment.TopStart }) {
      Column() {
        List({ space: 20, initialIndex: 0 }) {
          LazyForEach(this.arr, (item: number, index?: number) => {
            ListItem() {
              Flex({ direction: FlexDirection.Row, alignItems: ItemAlign.Center }) {
                Text('' + item)
                  .width('100%')
                  .height(80)
                  .fontSize(20)
                  .textAlign(TextAlign.Center)
                  .borderRadius(10)
                  .backgroundColor(0xFFFFFF)
                  .flexShrink(1)
                if (this.editFlag) {
                  Button() {
                    Text('delete').fontSize(16)
                  }.width('30%').height(40)
                  .onClick(() => {
                    if (index != undefined) {
                      console.info(this.arr.getData(index) + 'Delete');
                      this.arr.deleteItem(index);
                      this.arr.reloadData();
                      console.info(JSON.stringify(this.arr));
                      this.editFlag = false;
                    }
                  }).stateEffect(true)
                }
              }
            }
          }, (item: number, index: number) => item.toString() + index.toString())
        }.width('90%')
        .scrollBar(BarState.Off)
        .friction(0.6)
      }.width('100%')

      Button('edit list')
        .onClick(() => {
          this.editFlag = !this.editFlag;
        }).margin({ top: 5, left: 20 })
    }.width('100%').height('100%').backgroundColor(0xDCDCDC).padding({ top: 5 })
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7b/v3/32PJRpr-S0auvwfYgTzppQ/en-us_image_0000002537925452.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062238Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B3FB928B847D1D669E69704DD398A0AC3D995BED80F1248596C956C8BB747244)

## Example 4: Setting the Alignment Mode for the Scroll Snap Position

This example shows how to configure the **List** component to align the scroll snap position to the center.

For details about **ListDataSource** and the complete code, see [Example 1: Adding a Scroll Event](#example-1-adding-a-scroll-event).

// xxx.ets
import { ListDataSource } from './ListDataSource';

@Entry
@Component
struct ListExample {
  private arr: ListDataSource=new ListDataSource(\[\]);
  private scrollerForList: Scroller = new Scroller();

  aboutToAppear() {
    let list: number\[\] = \[\];
    for (let i = 0; i < 20; i++) {
      list.push(i);
    }
    this.arr = new ListDataSource(list);
  }

  build() {
    Column() {
      Row() {
        List({ space: 20, initialIndex: 3, scroller: this.scrollerForList }) {
          LazyForEach(this.arr, (item: number) => {
            ListItem() {
              Text('' + item)
                .width('100%').height(100).fontSize(16)
                .textAlign(TextAlign.Center)
            }
            .borderRadius(10).backgroundColor(0xFFFFFF)
            .width('60%')
            .height('80%')
          }, (item: number) => JSON.stringify(item))
        }
        .chainAnimation(true)
        .edgeEffect(EdgeEffect.Spring)
        .listDirection(Axis.Horizontal)
        .height('100%')
        .width('100%')
        .scrollSnapAlign(ScrollSnapAlign.CENTER)
        .borderRadius(10)
        .backgroundColor(0xDCDCDC)
      }
      .width('100%')
      .height('100%')
      .backgroundColor(0xDCDCDC)
      .padding({ top: 10 })
    }
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2e/v3/wEWoXW3NT7Gj6WyneSidHQ/en-us_image_0000002568685229.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062238Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0CF001F912A5570E944075BA61778FC6BF2C5F0EF67A0B2B37D2E481053DC984)

## Example 5: Implementing Accurate Scrolling

This example shows that, by setting the [childrenMainSize](#childrenmainsize12) attribute, the list can jump to an exact specific location when the **scrollTo** API is called, even when the heights of the child components are inconsistent.

For usage with state management V2, see [List and makeObserved](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-v1-v2-migration-inner-object#scrollable-component).

For details about **ListDataSource** and the complete code, see [Example 1: Adding a Scroll Event](#example-1-adding-a-scroll-event).

// xxx.ets
import { ListDataSource } from './ListDataSource';

@Entry
@Component
struct ListExample {
  private arr: ListDataSource = new ListDataSource(\[\]);
  private scroller: ListScroller = new ListScroller();
  @State listSpace: number = 10;
  @State listChildrenSize: ChildrenMainSize = new ChildrenMainSize(100);
  aboutToAppear(){
    // Initialize the data source.
    let list: number\[\] = \[\];
    for (let i = 0; i < 10; i++) {
      list.push(i);
    }
    this.arr = new ListDataSource(list);
    // The first five items do not have a default main axis size of 100; therefore, it is necessary to inform the list through the ChildrenMainSize.
    this.listChildrenSize.splice(0, 5, \[300, 300, 300, 300, 300\]);
  }

  build() {
    Column() {
      List({ space: this.listSpace, initialIndex: 4, scroller: this.scroller }) {
        LazyForEach(this.arr, (item: number) => {
          ListItem() {
            Text('item-' + item)
              .height( item < 5 ? 300 : this.listChildrenSize.childDefaultSize)
              .width('90%')
              .fontSize(16)
              .textAlign(TextAlign.Center)
              .borderRadius(10)
              .backgroundColor(0xFFFFFF)
          }
        }, (item: string) => item)
      }
      .backgroundColor(Color.Gray)
      .layoutWeight(1)
      .scrollBar(BarState.On)
      .childrenMainSize(this.listChildrenSize)
      .alignListItem(ListItemAlign.Center)
      Row({ space: 18 }) {
        Button() { Text('item size + 50') }.onClick(()=>{
          this.listChildrenSize.childDefaultSize += 50;
        }).height('50%').width('30%').backgroundColor(0xADD8E6)
        Button() { Text('item size - 50') }.onClick(()=>{
          if (this.listChildrenSize.childDefaultSize === 0) {
            return;
          }
          this.listChildrenSize.childDefaultSize -= 50;
        }).height('50%').width('30%').backgroundColor(0xADD8E6)
        Button() { Text('scrollTo (0, 310)') }.onClick(()=>{
          // 310: Jump to the position where the top of item 1 is aligned with the top of the list.
          // If childrenMainSize is not set, the scrollTo API may not work correctly when the heights of the list items are inconsistent.
          this.scroller.scrollTo({ xOffset: 0, yOffset: 310 })
        }).height('50%').width('30%').backgroundColor(0xADD8E6)
      }.height('20%')
    }
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7a/v3/Dgw4hYJkQBiUKGeS32wFdw/en-us_image_0000002568765239.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062238Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=BE8C1DE43A6854EA23FCD0A9CCF2A2A9F33C5F976A050C95E5AF9AEEF09072EB)

## Example 6: Obtaining Child Component Index Information

This example demonstrates how to obtain index information of list items in a **List** component when groups are involved.

// xxx.ets
class TimeTableDataSource implements IDataSource {
  private list: TimeTable\[\] = \[\];

  constructor(list: TimeTable\[\]) {
    this.list = list;
  }

  totalCount(): number {
    return this.list.length;
  }

  getData(index: number): TimeTable {
    return this.list\[index\];
  }

  registerDataChangeListener(listener: DataChangeListener): void {
  }

  unregisterDataChangeListener(listener: DataChangeListener): void {
  }
}

class ProjectsDataSource implements IDataSource {
  private list: string\[\] = \[\];

  constructor(list: string\[\]) {
    this.list = list;
  }

  totalCount(): number {
    return this.list.length;
  }

  getData(index: number): string {
    return this.list\[index\];
  }

  registerDataChangeListener(listener: DataChangeListener): void {
  }

  unregisterDataChangeListener(listener: DataChangeListener): void {
  }
}

@Entry
@Component
struct ListItemGroupExample {
  private timeTable: TimeTable\[\] = \[
  {
    title: 'Monday',
    projects: \['Language', 'Math', 'English'\]
  },
  {
    title: 'Tuesday',
    projects: \['Physics', 'Chemistry', 'Biology'\]
  },
  {
    title: 'Wednesday',
    projects: \['History', 'Geography', 'Politics'\]
  },
  {
    title: 'Thursday',
    projects: \['Art', 'Music', 'Sports'\]
  }
\];
  private scroller: ListScroller = new ListScroller();
  @State listIndexInfo: VisibleListContentInfo = { index: -1 };
  @State mess:string = 'null';
  @State itemBackgroundColorArr: boolean\[\] = \[false\];
  @Builder
  itemHead(text: string) {
    Text(text)
      .fontSize(20)
      .backgroundColor(0xAABBCC)
      .width('100%')
      .padding(10)
  }

  @Builder
  itemFoot(num: number) {
    Text('Total lessons: ' + num)
      .fontSize(16)
      .backgroundColor(0xAABBCC)
      .width('100%')
      .padding(5)
  }

  build() {
    Column() {
      List({ space: 20, scroller: this.scroller}) {
        LazyForEach(new TimeTableDataSource(this.timeTable), (item: TimeTable, index: number) => {
          ListItemGroup({ header: this.itemHead(item.title), footer: this.itemFoot(item.projects.length) }) {
            LazyForEach(new ProjectsDataSource(item.projects), (project: string, subIndex: number) => {
              ListItem() {
                Text(project)
                  .width('100%')
                  .height(100)
                  .fontSize(20)
                  .textAlign(TextAlign.Center)
                  .backgroundColor(this.itemBackgroundColorArr\[index \* 3 +subIndex\] ? 0x68B4FF: 0xFFFFFF)
              }
            }, (item: string) => item)
          }
          .divider({ strokeWidth: 1, color: Color.Blue }) // Divider between lines
        },(item: string) => item)
      }
      .width('90%')
      .sticky(StickyStyle.Header | StickyStyle.Footer)
      .scrollBar(BarState.Off)
      .gesture(
        PanGesture()
          .onActionUpdate((event: GestureEvent) => {
            if (event.fingerList\[0\] != undefined && event.fingerList\[0\].localX != undefined && event.fingerList\[0\].localY != undefined) {
              this.listIndexInfo  = this.scroller.getVisibleListContentInfo(event.fingerList\[0\].localX, event.fingerList\[0\].localY);
              let itemIndex:string = 'undefined';
              if (this.listIndexInfo.itemIndexInGroup != undefined ) {
                itemIndex = this.listIndexInfo.itemIndexInGroup.toString();
                if (this.listIndexInfo.index != undefined && this.listIndexInfo.index >= 0 &&
                  this.listIndexInfo.itemIndexInGroup >= 0 ) {
                  this.itemBackgroundColorArr\[this.listIndexInfo.index \* 3 + this.listIndexInfo.itemIndexInGroup\] = true;
                }
              }
              this.mess = 'index:' + this.listIndexInfo.index.toString() + ' itemIndex:' + itemIndex;
            }
          }))
      .gesture(
        TapGesture({ count: 1 })
          .onAction((event: GestureEvent) => {
            if (event) {
              this.itemBackgroundColorArr.splice(0,this.itemBackgroundColorArr.length);
            }
          })
      )
      Text('You are currently at index '+ this.mess)
        .fontColor(Color.Red)
        .height(50)
    }.width('100%').height('90%').backgroundColor(0xDCDCDC).padding({ top: 5 })
  }
}

interface TimeTable {
  title: string;
  projects: string\[\];
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/59/v3/iGLCMBqETmGxdNxitt-USA/en-us_image_0000002537765514.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062238Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=00D6CF99A543056EB9EF530FD256C1AE08E160B27B13F1926B6D7380597624F0)

## Example 7: Setting Edge Fading

This example demonstrates how to implement a **List** component with an edge fading effect and set the length of the fading edge.

For details about **ListDataSource** and the complete code, see [Example 1: Adding a Scroll Event](#example-1-adding-a-scroll-event).

import { LengthMetrics } from '@kit.ArkUI'
import { ListDataSource } from './ListDataSource';
@Entry
@Component
struct ListExample {
  private arr: ListDataSource=new ListDataSource(\[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11\]);
  scrollerForList: Scroller = new Scroller();

  build() {
    Column() {

      List({ space: 20, initialIndex: 0, scroller: this.scrollerForList }) {
        LazyForEach(this.arr, (item: number) => {
          ListItem() {
            Text('' + item)
              .width('100%').height(100).fontSize(16)
              .textAlign(TextAlign.Center).borderRadius(10).backgroundColor(0xFFFFFF)
          }
        }, (item: number) => item.toString())
      }
      .fadingEdge(true, { fadingEdgeLength: LengthMetrics.vp(80) })
    }
    .width('100%')
    .height('100%')
    .backgroundColor(0xDCDCDC)
    .padding({ top: 5 })
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ff/v3/OwFNgvNSTvqoYIwGJ8Mdqg/en-us_image_0000002537925454.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062238Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=223EC1246A4747EE0A3E300F449354BFD780D183127C2AE48C7B3446722780C7)

## Example 8: Setting the Single-Side Edge Effect

This example demonstrates how to set a single-side edge effect for the **List** component using the **edgeEffect** API.

For details about **ListDataSource** and the complete code, see [Example 1: Adding a Scroll Event](#example-1-adding-a-scroll-event).

// xxx.ets
import { ListDataSource } from './ListDataSource';

@Entry
@Component
struct ListExample {
  private arr: ListDataSource = new ListDataSource(\[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11\]);
  scrollerForList: Scroller = new Scroller();
  build() {
    Column() {
      List({ space: 20, initialIndex: 0, scroller: this.scrollerForList }) {
        LazyForEach(this.arr, (item: number) => {
          ListItem() {
            Text('' + item)
              .width('100%').height(100).fontSize(16)
              .textAlign(TextAlign.Center).borderRadius(10).backgroundColor(0xFFFFFF)
          }
        }, (item: string) => item)
      }
      .edgeEffect(EdgeEffect.Spring, {alwaysEnabled: true, effectEdge: EffectEdge.START})
      .width('90%').height('90%')
    }
    .width('100%')
    .height('100%')
    .backgroundColor(0xDCDCDC)
    .padding({ top: 5 })
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/31/v3/tss7g7mTSai7zuRk7KsEfg/en-us_image_0000002568685231.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062238Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=ADA52858AA9B069A2275A6AA9A57F1FCA126D7140B4175BA1EC047E4DAF42721)

## Example 9: Setting Focus Wrap on a List

In API version 20 and later versions, this example uses the [focusWrapMode](#focuswrapmode20) API to implement the effect of line-wrapping focus navigation with arrow keys in the **List** component.

@Entry
@Component
struct ListExample {
  @State arr: number\[\] = \[0, 1, 2, 3, 4, 5, 6, 7, 8, 9\]
  build() {
    Stack({ alignContent: Alignment.TopStart }) {
      Column() {
        List({ space: 40, initialIndex: 0 }) {
          ForEach(this.arr, (item: number, index?: number) => {
            ListItem() {
              Flex({ direction: FlexDirection.Row, alignItems: ItemAlign.Center }) {
                Text('' + item)
                  .width(150)
                  .height(93)
                  .fontSize(30)
                  .textAlign(TextAlign.Center)
                  .borderRadius(10)
                  .backgroundColor(0xFFFFFF)
                  .flexShrink(1)
                  .focusable(true)
                  .offset({ left: 5 })
              }
            }
          }, (item: string, index?: number) => item)
        }
        .lanes(2)
        .contentStartOffset(20)
        .contentEndOffset(20)
        .width('100%')
        .scrollBar(BarState.Off)
        .friction(0.6)
        .focusWrapMode(FocusWrapMode.WRAP\_WITH\_ARROW)
        .alignListItem(ListItemAlign.Center)
        .offset({ left: 20 })
      }.width('90%')
    }.width('100%').height('100%').backgroundColor(0xDCDCDC).padding({ top: 5 })
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ba/v3/xWImKR1mTy29D9CnFBKbLA/en-us_image_0000002568765241.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062238Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=DD3C85AB88399354CB48F280FEC799A6DE280E4CD5B1DD7D7CB37AE8EAF502EC)

## Example 10: Keeping the Display Content Unchanged When Data Is Inserted Outside the Display Area

This example uses the **maintainVisibleContentPosition** API to implement infinite loading of historical messages when the screen is swiped up.

For details about **ListDataSource** and the complete code, see [Example 1: Adding a Scroll Event](#example-1-adding-a-scroll-event).

import { ListDataSource } from './ListDataSource';

@Entry
@Component
struct ListExample {
  private arr: ListDataSource = new ListDataSource(\[990, 991, 992, 993, 994, 995, 996, 997, 998, 999\]);
  build() {
    Column() {
      List({ space: 20, initialIndex: 9 }) {
        LazyForEach(this.arr, (item: number) => {
          ListItem() {
            Text('message:' + item)
              .width('100%').height(100)
              .fontSize(16)
              .textAlign(TextAlign.Center)
              .borderRadius(10)
              .backgroundColor(0xFFFFFF)
          }
        }, (item: number) => item.toString())
      }
      .maintainVisibleContentPosition(true)
      .onScrollIndex((start:number)=>{
        if (start < 5) {
          for (let i = 0; i < 10; i++) {
            this.arr.insertItem(0, this.arr.getData(0) - 1);
          }
        }
      })
    }
    .width('100%')
    .height('100%')
    .backgroundColor(0xDCDCDC)
    .padding(12)
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/64/v3/-5KFd9JtQeeHZZSvXWxgwQ/en-us_image_0000002537765516.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062238Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=BAD8ED25AEDE06C6860ADB9CB13736B477338AAF37E62D45756EF63F3BCDE516)

## Example 11: Setting the Margin of the Scrollbar

Starting from API version 20, this example shows how to use the [scrollBarMargin](../scrollable-component-common-apis/document.md#scrollbarmargin20) attribute to set the scrollbar margin and avoid the [contentStartOffset](#contentstartoffset11) and [contentEndOffset](#contentendoffset11) areas.

// xxx.ets
import { LengthMetrics } from '@kit.ArkUI';

@Entry
@Component
struct ListScrollBarMarginExample {
  @State arr: number\[\] = \[0, 1, 2, 3, 4, 5, 6, 7, 8, 9\];

  build() {
    Column() {
      List({ space: 40, initialIndex: 0 }) {
        ForEach(this.arr, (item: number, index?: number) => {
          ListItem() {
            Text('' + item)
              .width('100%')
              .height(100)
              .fontSize(16)
              .textAlign(TextAlign.Center)
              .borderRadius(10)
              .backgroundColor(0xFFFFFF)
          }
        }, (item: string, index?: number) => item)
      }
      .contentStartOffset(20)
      .contentEndOffset(20)
      .scrollBar(BarState.On)
      .scrollBarMargin({ start: LengthMetrics.vp(20), end: LengthMetrics.vp(20) })
      .width('90%')
    }
    .width('100%')
    .height('100%')
    .backgroundColor(0xDCDCDC)
    .padding({ top: 5 })
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/64/v3/GfHiPqkAQHyYPRq0pAiY3g/en-us_image_0000002537925456.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062238Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=CFB3FBAC111308B47505F510B86F8DA71FB9BCF262D786C6BFAE37ACC32657C9)

## Example 12: Implementing Dragging with OnMove

Starting from API version 12, this example demonstrates how to use the [onMove](../../universal-attributes/interaction-properties/drag-and-drop-sorting/document.md#onmove) API of **ForEach** to sort items by dragging them. The list can automatically scroll when an item is dragged to the edge of the list.

@Entry
@Component
struct ForEachSort {
  @State arr: Array<string> = \[\];

  build() {
    Row() {
      List() {
        ForEach(this.arr, (item: string) => {
          ListItem() {
            Text(item.toString())
              .fontSize(16)
              .textAlign(TextAlign.Center)
              .size({ height: 100, width: '100%' })
          }.margin(10)
          .borderRadius(10)
          .backgroundColor('#FFFFFFFF')
        }, (item: string) => item)
          .onMove((from: number, to: number) => {
            let tmp = this.arr.splice(from, 1);
            this.arr.splice(to, 0, tmp\[0\]);
          })
      }
      .width('100%')
      .height('100%')
      .backgroundColor('#FFDCDCDC')
    }
  }

  aboutToAppear(): void {
    for (let i = 0; i < 100; i++) {
      this.arr.push(i.toString());
    }
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/93/v3/u3NZSbt-TbKyTQmSZW1A2g/en-us_image_0000002568685233.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062238Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3586B02DEB3587149D2F732097806050CB3749D0FE4D039180634104B19DF567)

## Example 13: Configuring Lanes Based on Breakpoints

In API version 22 and later versions, this example shows how to configure lanes in the **List** component based on breakpoints.

For details about **ListDataSource** and the complete code, see [Example 1: Adding a Scroll Event](#example-1-adding-a-scroll-event).

// xxx.ets
import { ListDataSource } from './ListDataSource';

@Entry
@Component
struct ListExample {
  private arr: ListDataSource = new ListDataSource(\[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11\]);
  scrollerForList: Scroller = new Scroller();

  build() {
    Column() {
      List({ space: 20, initialIndex: 0, scroller: this.scrollerForList }) {
        LazyForEach(this.arr, (item: number) => {
          ListItem() {
            Text('' + item)
              .width('100%').height(100).fontSize(16)
              .textAlign(TextAlign.Center).borderRadius(10).backgroundColor(0xFFFFFF)
          }
        }, (item: string) => item)
      }
      .lanes({ fillType: PresetFillType.BREAKPOINT\_SM2MD3LG5}, 10)
      .width('90%').height(600)
    }
    .width('100%')
    .height('100%')
    .backgroundColor(0xDCDCDC)
    .padding({ top: 5 })
  }
}

When the list width is within the breakpoint range of sm or smaller, two columns are displayed.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8f/v3/uH-hRTt3SO-jyjbpzk3kXw/en-us_image_0000002568765243.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062238Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D7C4A6BECACED1A084A16AA81AF9104F526B024BB6FBF14E45869C9981AE6A1B)

When the list width is within the breakpoint range of md, three columns are displayed.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/76/v3/3zRz2c7aQhCMXFbePmnqgA/en-us_image_0000002537765518.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062238Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1C22DECFFD13B8EA46F74144EFC9B7361D3555719B60D00BFB76AE6830EED4EE)

When the list width is within the breakpoint range of lg or larger, five columns are displayed.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7d/v3/eIjSr6qwQGCJYRY4uLCqwg/en-us_image_0000002537925458.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062238Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=770395CE9A60732F7716712E3BA88A9A5B94F2F49F2F9760CB08919F92294A58)

## Example 14: Obtaining the Total Content Size

This example demonstrates how to obtain the total content size of the **List** component. This functionality is supported since API version 22.

// xxx.ets
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct ListExample {
  private arr: number\[\] = \[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11\]
  scrollerForList: Scroller = new Scroller()
  @State contentWidth: number = -1;
  @State contentHeight: number = -1;

  build() {
    Column() {
      List({ space: 20, initialIndex: 0, scroller: this.scrollerForList }) {
        ForEach(this.arr, (item: number) => {
          ListItem() {
            Text('' + item)
              .width('100%')
              .height(100)
              .fontSize(16)
              .textAlign(TextAlign.Center)
              .borderRadius(10)
              .backgroundColor(0xFFFFFF)
          }
        }, (item: string) => item)
      }
      .width('90%').height('90%')

      // Button to obtain the content size.
      Button('GetContentSize')
        .onClick(() => {
          // Scroller throws an exception when not bound to a component; wrap with try-catch for safety.
          try {
            // Obtain the content width using contentSize.
            this.contentWidth = this.scrollerForList.contentSize().width;
            // Obtain the content height using contentSize.
            this.contentHeight = this.scrollerForList.contentSize().height;
          } catch (error) {
            let err: BusinessError = error as BusinessError;
            console.error(\`Failed to get contentSize of the grid, code=${err.code}, message=${err.message}\`);
          }
        })
      // Display the obtained content size.
      Text('Width: ' + this.contentWidth + ', Height: ' + this.contentHeight)
        .fontColor(Color.Red)
        .height(50)
    }
    .width('100%')
    .height('100%')
    .backgroundColor(0xDCDCDC)
    .padding({ top: 5 })
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/40/v3/sVeKbwAdQ3GfoVOvDOtxfg/en-us_image_0000002568685235.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062238Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=401BC6DB237C9A22CF2E977B9A97ED910EEC580512AD067C7F422848F642EA67)

## Example 15: Dragging Between Two Lists

This example demonstrates the drag and drop effect of list times between two **List** components using events such as **OnItemDragStart**.

// xxx.ets
@ObservedV2
class ListData {
  @Trace public title: string = '';
  @Trace public data: string\[\] = \[\];

  constructor(title: string, data: string\[\]) {
    this.title = title;
    this.data = data;
  }
}

class DraggingData {
  public data?: string;
}

@ComponentV2
struct DraggableList {
  @Require @Param data: string\[\];
  @Require @Param draggingData: DraggingData;

  @Builder
  ItemBuilder(data: string, size: SizeOptions, event: ItemDragInfo): void {
    Stack() {
      Text(data)
    }
    .backgroundColor(Color.White)
    .borderRadius(4)
    .size(size)
  }

  viewWidth: number = 0;
  lastInsertIndex: number = 0;
  scroller: Scroller = new Scroller();

  build() {
    List({ scroller: this.scroller }) {
      ForEach(this.data, (item: string) => {
        ListItem() {
          Text(item)
        }
        .width('100%')
        .height('10%')
        .margin(10)
        .backgroundColor(Color.White)
        .borderRadius(4)
        .aspectRatio(1)
      }, (item: string) => item)
    }
    .width('50%')
    .layoutWeight(1)
    .padding(10)
    .onItemDragStart((event: ItemDragInfo, itemIndex: number) => {
      let rect = this.scroller.getItemRect(itemIndex);
      let size: SizeOptions = {
        width: rect.width,
        height: rect.height
      };
      this.lastInsertIndex = itemIndex;
      this.draggingData.data = this.data\[itemIndex\];
      this.data.splice(itemIndex, 1);

      return this.ItemBuilder(this.draggingData.data, size, event);
    })
    .onItemDragEnter((event: ItemDragInfo) => {
      console.info('Item drag enter at position:', event.x, event.y);
    })
    .onItemDragMove((event: ItemDragInfo, itemIndex: number, insertIndex: number) => {
      if (this.lastInsertIndex != insertIndex){
        console.info('insertIndex change from ', this.lastInsertIndex, 'to', insertIndex);
        this.lastInsertIndex = insertIndex;
      }
    })
    .onItemDragLeave((event: ItemDragInfo, itemIndex: number) => {
      console.info('Item ' + itemIndex + ' drag leave at position:', event.x, event.y);
    })
    .onItemDrop((event: ItemDragInfo, itemIndex: number, insertIndex: number, isSuccess: boolean) => {
      if (!isSuccess) {
        this.draggingData.data = undefined;
        return;
      }
      if (insertIndex >= 0) {
        this.data.splice(insertIndex, 0, this.draggingData.data!);
      }
      this.draggingData.data = undefined;
    })
    .onSizeChange((oldValue: SizeOptions, newValue: SizeOptions) => {
      this.viewWidth = newValue.width as number;
    })
  }
}

@Entry
@ComponentV2
struct Index {
  @Local data: ListData\[\] = \[
    new ListData('A', \['A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8'\]),
    new ListData('B', \['B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'B7', 'B8'\]),
  \]
  @Local draggingData: DraggingData = new DraggingData();

  build() {
    Stack() {
      Row() {
        DraggableList({ data: this.data\[0\].data, draggingData: this.draggingData })
        DraggableList({ data: this.data\[1\].data, draggingData: this.draggingData })
      }
    }
    .backgroundColor('#FFDCDCDC')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/28/v3/1e57_49vRwCJuxlBQMaZ1w/en-us_image_0000002568765245.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062238Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C6685EB0C0DD33347FEAADA3BC46E43291C35F89E9F87CC1460AE74463D656CD)

## Example 16: Centering the Clicked Item in ListItemGroup

This example uses the [scrollToItemInGroup](#scrolltoitemingroup11) API to implement the effect of centering the [ListItem](../listitem/document.md) component in the [ListItemGroup](../listitemgroup/document.md) when the [ListItem](../listitem/document.md) is clicked.

import { util } from '@kit.ArkTS';

class Contact {
  key: string = util.generateRandomUUID(true);
  name: string;
  icon: Resource;

  constructor(name: string, icon: Resource) {
    this.name = name;
    this.icon = icon;
  }
}

class ContactsGroup {
  title: string = '';
  contacts: Array<object> | null = null;
  key: string = '';
}

@Entry
@Component
struct ContactsList {
  private scroller: ListScroller = new ListScroller();
  private contactsGroups: ContactsGroup\[\] = \[
    {
      title: 'A',
      contacts: \[
        new Contact('Alice', $r('app.media.icon')),  // Replace $r('app.media.icon') with the image resource file you use.
        new Contact('Ann', $r('app.media.icon')),
        new Contact('Angela', $r('app.media.icon'))
        // ...
      \],
      key: util.generateRandomUUID(true)
    } as ContactsGroup,
    {
      title: 'B',
      contacts: \[
        new Contact('Ben', $r('app.media.icon')),
        new Contact('Bryan', $r('app.media.icon'))
        // ...
      \],
      key: util.generateRandomUUID(true)
    } as ContactsGroup,
    // ...
  \]

  @Builder
  itemHead(text: string) {
    Text(text)
      .fontSize(20)
      .backgroundColor('#fff1f3f5')
      .width('100%')
      .padding(5)
  }

  build() {
    List({ scroller: this.scroller }) {
      ForEach(this.contactsGroups, (item: ContactsGroup, index: number) => {
        ListItemGroup({ header: this.itemHead(item.title) }) {
          ForEach(item.contacts, (contact: Contact, subIndex: number) => {
            ListItem() {
              Row() {
                Image(contact.icon)
                  .width(40)
                  .height(40)
                  .margin(10)
                Text(contact.name).fontSize(20)
              }
              .width('100%')
              .justifyContent(FlexAlign.Start)
              .margin(10)
            }
            .gesture(
              TapGesture({ count: 1 })
                .onAction((event: GestureEvent) => {
                  if (event) {
                    const itemRect = this.scroller.getItemRectInGroup(index, subIndex);
                    console.info('The', index + 1, 'ListItemGroup of the', subIndex + 1, 'ListItem', x:', itemRect.x,
                      ' y:', itemRect.y, ' width:', itemRect.width, ' height:', itemRect.height)
                    this.scroller.scrollToItemInGroup(index, subIndex, true, ScrollAlign.CENTER);
                  }
                })
            )
          }, (contact: Contact) => JSON.stringify(contact))
        }
        .divider({ strokeWidth: 4 })
        .width('100%')
      }, (item: ContactsGroup) => JSON.stringify(item))
    }
    .onScrollFrameBegin((offset: number, state: ScrollState) => {
      console.info('List scrollFrameBegin offset: ' + offset + ' state: ' + state.toString());
      return { offsetRemain: offset };
    })
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a1/v3/wpfEnNexQ4CRut01WiKztw/en-us_image_0000002537765520.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062238Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=35057248BA64C3E531C96330D779FA83B3FCD7481D22DA074465181A88842221)
