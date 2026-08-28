# OH\_AI\_ShapeInfo

typedef struct OH\_AI\_ShapeInfo {...} OH\_AI\_ShapeInfo

#### Overview

Defines the maximum number of shapes. The maximum value reserved is **32**, and the maximum number currently supported is **8**.

**Since**: 9

**Related module**: [MindSpore](../../modules/mindspore/document.md)

**Header file**: [model.h](../../header-files/model-h/document.md)

#### Summary

#### \[h2\]Member Variables

| Name | Description |
| :-- | :-- |
| size\_t shape\_num | Dimension array length. |
| int64\_t shape\[OH\_AI\_MAX\_SHAPE\_NUM\] | Dimension array. |
