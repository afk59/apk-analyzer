# OHExtDataHandle

typedef struct {...} OHExtDataHandle

#### **Overview**

Describes the extended data handle.

**Since**: 9

**Deprecated**: This enum is deprecated since API version 10. No substitute is provided.

**Related module**: [NativeWindow](../../modules/nativewindow/document.md)

**Header file**: [external\_window.h](../../header-files/external-window-h/document.md)

#### Summary

## Member Variables

| Name | Description |
| :-- | :-- |
| int32\_t fd | File descriptor handle. The value **\-1** indicates that the handle is not supported. |
| uint32\_t reserveInts | Number of reserved arrays. |
| int32\_t reserve\[0\] | Reserved array. |
