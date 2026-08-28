# HiDebug\_StackFrame

typedef struct HiDebug\_StackFrame {...} HiDebug\_StackFrame

#### Overview

Defines the stack frame content.

**Since**: 20

**Related module**: [HiDebug](../../modules/hidebug/document.md)

**Header file**: [hidebug\_type.h](../../header-files/hidebug-type-h/document.md)

#### Summary

#### \[h2\]Member Variables

| Name | Description |
| :-- | :-- |
| [HiDebug\_StackFrameType](../../header-files/hidebug-type-h/document.md#hidebug_stackframetype) type | Type of the current stack. |
| struct [HiDebug\_JsStackFrame](../hidebug-jsstackframe/document.md) js | JS stack frame content defined by [HiDebug\_JsStackFrame](../hidebug-jsstackframe/document.md). |
| struct [HiDebug\_NativeStackFrame](../hidebug-nativestackframe/document.md) native | Native stack frame content defined by [HiDebug\_NativeStackFrame](../hidebug-nativestackframe/document.md). |
