# ArkUI\_AnimateCompleteCallback

typedef struct {...} ArkUI\_AnimateCompleteCallback

#### Overview

Defines the callback type for when the animation playback is complete.

**Since**: 12

**Related module**: [ArkUI\_NativeModule](../../modules/arkui-nativemodule/document.md)

**Header file**: [native\_animate.h](../../header-files/native-animate-h/document.md)

#### Summary

#### \[h2\]Member Variables

| Name | Description |
| :-- | :-- |
| [ArkUI\_FinishCallbackType](../../header-files/native-type-h/document.md#arkui_finishcallbacktype) type | Callback type for when the animation playback is complete. |
| void\* userData | Custom data passed upon animation end callback. |

#### \[h2\]Member Functions

| Name | Description |
| :-- | :-- |
| [void (\*callback)(void\* userData)](#callback) | Callback invoked when the animation playback is complete. |

#### Member Function Description

#### \[h2\]callback()

void (\*callback)(void\* userData)

**Description**

Callback invoked when the animation playback is complete.
