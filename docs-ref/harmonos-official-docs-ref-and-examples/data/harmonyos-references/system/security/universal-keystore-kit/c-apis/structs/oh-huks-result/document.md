# OH\_Huks\_Result

#### Overview

Defines the returned data, including a status code and related description.

**Since**: 9

**Related module**: [HuksTypeApi](../../modules/hukstypeapi/document.md)

**Header file**: [native\_huks\_type.h](../../header-files/native-huks-type-h/document.md)

#### Summary

#### \[h2\]Member Variables

| Name | Description |
| :-- | :-- |
| int32\_t errorCode | Status code. For details, see [OH\_Huks\_ErrCode](../../header-files/native-huks-type-h/document.md#oh_huks_errcode). |
| const char \*errorMsg | Description of the status code. |
| uint8\_t \*data | Other data. |
