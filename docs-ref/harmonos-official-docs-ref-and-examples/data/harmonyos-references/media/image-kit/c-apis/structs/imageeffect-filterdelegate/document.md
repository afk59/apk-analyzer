# ImageEffect\_FilterDelegate

typedef struct ImageEffect\_FilterDelegate {...} ImageEffect\_FilterDelegate

#### Overview

The struct describes the callback functions of a custom image effect filter.

**Since**: 12

**Related module**: [ImageEffect](../../modules/imageeffect/document.md)

**Header file**: [image\_effect\_filter.h](../../header-files/image-effect-filter-h/document.md)

#### Summary

#### \[h2\]Member Variables

| Name | Description |
| :-- | :-- |
| [OH\_EffectFilterDelegate\_SetValue](../../header-files/image-effect-filter-h/document.md#oh_effectfilterdelegate_setvalue) setValue | Pointer to the parameter setting function. |
| [OH\_EffectFilterDelegate\_Render](../../header-files/image-effect-filter-h/document.md#oh_effectfilterdelegate_render) render | Pointer to the filter rendering function. |
| [OH\_EffectFilterDelegate\_Save](../../header-files/image-effect-filter-h/document.md#oh_effectfilterdelegate_save) save | Pointer to the filter serialization function. |
| [OH\_EffectFilterDelegate\_Restore](../../header-files/image-effect-filter-h/document.md#oh_effectfilterdelegate_restore) restore | Pointer to the filter deserialization function. |
