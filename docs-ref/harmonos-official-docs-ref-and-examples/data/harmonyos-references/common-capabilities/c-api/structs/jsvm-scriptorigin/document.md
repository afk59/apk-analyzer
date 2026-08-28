# JSVM\_ScriptOrigin

typedef struct {...} JSVM\_ScriptOrigin

#### Overview

Defines the original information about a JavaScript code segment, such as the source map path, source file name, and start line/column number in the source file.

**Since**: 12

**Related module**: [JSVM](../../modules/jsvm/document.md)

**Header file**: [jsvm\_types.h](../../header-files/jsvm-types-h/document.md)

#### Summary

#### \[h2\]Member Variables

| Name | Description |
| :-- | :-- |
| const char\* sourceMapUrl | Source map path. |
| const char\* resourceName | Source file name. |
| size\_t resourceLineOffset | Start line number of the code segment in the source file. |
| size\_t resourceColumnOffset | Start column number of the code segment in the source file. |
