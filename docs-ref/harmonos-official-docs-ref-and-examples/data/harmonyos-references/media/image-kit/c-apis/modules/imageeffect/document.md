# ImageEffect

#### Overview

The module provides the APIs for editing an image.

For details about the development guide and sample, see [Using ImageEffect to Edit Images](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/image-effect-guidelines).

**Since**: 12

#### Files

| Name | Description |
| :-- | :-- |
| [image\_effect.h](../../header-files/image-effect-h/document.md) | 
Declares the APIs related to an image effector.

You can use the APIs to add, delete, and query image effect filters. You can connect multiple filters in series to implement complex effect adjustment.

The effector supports multiple input types, such as PixelMap, URI, surface, and picture. Different input types are converted into buffer objects in the effector, and effect processing is implemented through the filters.

 |
| [image\_effect\_errors.h](../../header-files/image-effect-errors-h/document.md) | Declares the error codes used by the image effector. |
| [image\_effect\_filter.h](../../header-files/image-effect-filter-h/document.md) | 

Declares the APIs related to an image effect filter.

With these APIs, you can quickly implement basic effect processing or connect multiple filters in series in an image effector to implement complex effect processing. The system provides basic effect processing filters such as brightness and crop filters.

 |
