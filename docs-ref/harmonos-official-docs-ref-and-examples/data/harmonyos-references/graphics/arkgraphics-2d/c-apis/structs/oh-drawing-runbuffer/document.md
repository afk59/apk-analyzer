# OH\_Drawing\_RunBuffer

typedef struct {...} OH\_Drawing\_RunBuffer

#### Overview

This struct describes a run, which provides storage for glyphs and positions.

**Since**: 11

**Related module**: [Drawing](../../modules/drawing/document.md)

**Header file**: [drawing\_text\_blob.h](../../header-files/drawing-text-blob-h/document.md)

#### Summary

#### \[h2\]Member Variables

| Name | Description |
| :-- | :-- |
| uint16\_t\* glyphs | Storage for glyph indexes in the run. |
| float\* pos | Storage for glyph positions in the run. |
| char\* utf8text | Storage for UTF-8 encoded text units in the run. |
| uint32\_t\* clusters | Storage for glyph clusters (index of the UTF-8 encoded text unit) in the run. |
