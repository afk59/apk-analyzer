# OH\_Drawing\_LineMetrics

typedef struct {...} OH\_Drawing\_LineMetrics

#### Overview

This struct describes the measurement information about a line of text.

**Since**: 12

**Related module**: [Drawing](../../modules/drawing/document.md)

**Header file**: [drawing\_text\_typography.h](../../header-files/drawing-text-typography-h/document.md)

#### Summary

#### \[h2\]Member Variables

| Name | Description |
| :-- | :-- |
| double ascender | Part of a lowercase letter that extends beyond the meanline. |
| double descender | Part of a lowercase letter that extends below the baseline. |
| double capHeight | Height of an uppercase letter above the baseline. |
| double xHeight | Height of a lowercase letter, specifically the lowercase x, not including ascenders and descenders. |
| double width | Horizontal space taken up by a character. |
| double height | Line height. |
| double x | Distance from the left edge of the leftmost character to the left edge of the container. For left alignment, the value is 0. For right alignment, the value is the container width minus the text width. |
| double y | Height from the top edge of the character to the top of the container. The first line is 0, and the second line is the height of the first line. |
| size\_t startIndex | Index of the first character in the line. |
| size\_t endIndex | Index of the last character in the line. |
| [OH\_Drawing\_Font\_Metrics](../oh-drawing-font-metrics/document.md) firstCharMetrics | Measurement information of the first character. |
