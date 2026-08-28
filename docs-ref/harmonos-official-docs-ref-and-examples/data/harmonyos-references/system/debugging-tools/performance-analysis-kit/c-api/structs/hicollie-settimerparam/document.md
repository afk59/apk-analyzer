# HiCollie\_SetTimerParam

typedef struct HiCollie\_SetTimerParam {...} HiCollie\_SetTimerParam

#### Overview

Defines the input parameters of the **OH\_HiCollie\_SetTimer** function.

**Since**: 18

**Related module**: [HiCollie](../../modules/hicollie/document.md)

**Header file**: [hicollie.h](../../header-files/hicollie-h/document.md)

#### Summary

#### \[h2\]Member Variables

| Name | Description |
| :-- | :-- |
| const char \*name | Timer task name. |
| unsigned int timeout | Task timeout threshold, in seconds. |
| [OH\_HiCollie\_Callback](../../header-files/hicollie-h/document.md#oh_hicollie_callback) func | Callback executed when a timeout occurs. |
| void \*arg | Parameters of the callback. |
| [HiCollie\_Flag](../../header-files/hicollie-h/document.md#hicollie_flag) flag | Action performed when a timeout occurs. For details, see [HiCollie\_Flag](../../header-files/hicollie-h/document.md#hicollie_flag). |
