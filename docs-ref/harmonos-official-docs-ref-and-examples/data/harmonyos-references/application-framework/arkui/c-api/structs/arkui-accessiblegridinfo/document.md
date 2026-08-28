# ArkUI\_AccessibleGridInfo

typedef struct {...} ArkUI\_AccessibleGridInfo

#### Overview

Configures the grid layout attributes of a specific component (such as [List](../../../arkts-components/scroll-and-swipe/list/document.md), [Flex](../../../arkts-components/rows-columns-and-stacking/flex/document.md), [Select](../../../arkts-components/buttons-and-selections/select/document.md), or [Swiper](../../../arkts-components/scroll-and-swipe/swiper/document.md)).

**Since**: 13

**Related module**: [ArkUI\_Accessibility](../../modules/arkui-accessibility/document.md)

**Header file**: [native\_interface\_accessibility.h](../../header-files/native-interface-accessibility-h/document.md)

#### Summary

#### \[h2\]Member Variables

| Name | Description |
| :-- | :-- |
| int32\_t rowCount | Number of rows of the component. The value is an integer greater than 0. |
| int32\_t columnCount | Number of columns of the component. The value is an integer greater than 0. |
| int32\_t selectionMode | Selection mode. If the value is **0**, only a single row in the grid can be selected. If the value is not 0, multiple rows can be selected. |
