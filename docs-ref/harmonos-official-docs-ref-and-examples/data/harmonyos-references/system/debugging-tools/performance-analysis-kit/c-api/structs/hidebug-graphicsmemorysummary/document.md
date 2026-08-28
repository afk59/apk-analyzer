# HiDebug\_GraphicsMemorySummary

typedef struct HiDebug\_GraphicsMemorySummary {...} HiDebug\_GraphicsMemorySummary

#### Overview

Defines a struct for the application graphics memory usage details.

**Since**: 21

**Related module**: [HiDebug](../../modules/hidebug/document.md)

**Header file**: [hidebug\_type.h](../../header-files/hidebug-type-h/document.md)

#### Summary

#### \[h2\]Member Variables

| Name | Description |
| :-- | :-- |
| uint32\_t gl | GL memory size (memory occupied by RenderService for loading required resources, such as images and textures), in KB. |
| uint32\_t graph | Graph memory size (DMA memory usage of the process), in KB, including the DMA buffers obtained directly through the API and those obtained through **allocator\_host**. |
