# ArkUI\_AccessibleGridItemInfo

typedef struct {...} ArkUI\_AccessibleGridItemInfo

#### Overview

Configures the attributes of a specific component (such as [List](../../../arkts-components/scroll-and-swipe/list/document.md), [Flex](../../../arkts-components/rows-columns-and-stacking/flex/document.md), [Select](../../../arkts-components/buttons-and-selections/select/document.md), or [Swiper](../../../arkts-components/scroll-and-swipe/swiper/document.md)).

**Since**: 13

**Related module**: [ArkUI\_Accessibility](../../modules/arkui-accessibility/document.md)

**Header file**: [native\_interface\_accessibility.h](../../header-files/native-interface-accessibility-h/document.md)

#### Summary

#### \[h2\]Member Variables

| Name | Description |
| :-- | :-- |
| bool heading | Whether the item is a heading. **true** for heading, **false** for non-heading. |
| bool selected | Whether the item is selected. **true** for selected, **false** for unselected. |
| int32\_t columnIndex | Row index of the item. The value is an integer greater than 0. |
| int32\_t rowIndex | Column index of the item. The value is an integer greater than 0. |
| int32\_t columnSpan | Number of rows that the item spans. The value is an integer greater than 0. |
| int32\_t rowSpan | Number of columns that the item spans. The value is an integer greater than 0. |
