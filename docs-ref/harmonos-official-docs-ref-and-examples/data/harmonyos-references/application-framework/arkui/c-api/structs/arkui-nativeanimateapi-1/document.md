# ArkUI\_NativeAnimateAPI\_1

typedef struct {...} ArkUI\_NativeAnimateAPI\_1

#### Overview

Declares the native animation APIs provided by ArkUI.

**Since**: 12

**Related module**: [ArkUI\_NativeModule](../../modules/arkui-nativemodule/document.md)

**Header file**: [native\_animate.h](../../header-files/native-animate-h/document.md)

#### Summary

#### \[h2\]Member Functions

| Name | Description |
| :-- | :-- |
| [int32\_t (\*animateTo)(ArkUI\_ContextHandle context, ArkUI\_AnimateOption\* option, ArkUI\_ContextCallback\* update,ArkUI\_AnimateCompleteCallback\* complete)](#animateto) | Defines an explicit animation. |
| [int32\_t (\*keyframeAnimateTo)(ArkUI\_ContextHandle context, ArkUI\_KeyframeAnimateOption\* option)](#keyframeanimateto) | Defines a keyframe animation. |
| [ArkUI\_AnimatorHandle (\*createAnimator)(ArkUI\_ContextHandle context, ArkUI\_AnimatorOption\* option)](#createanimator) | Creates an animator object. |
| [void (\*disposeAnimator)(ArkUI\_AnimatorHandle animatorHandle)](#disposeanimator) | Disposes of an animator object. |

#### Member Function Description

#### \[h2\]animateTo()

int32\_t (\*animateTo)(ArkUI\_ContextHandle context, ArkUI\_AnimateOption\* option, ArkUI\_ContextCallback\* update,ArkUI\_AnimateCompleteCallback\* complete)

**Description**

Defines an explicit animation.

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_ContextHandle](../arkui-context--00020177/document.md) context | **UIContext** instance. |
| [ArkUI\_AnimateOption](../arkui-animateoption/document.md)\* option | Defines the animation configuration. |
| [ArkUI\_ContextCallback](../arkui-contextcallback/document.md)\* update | 
Closure function for the animation. The system automatically inserts the transition animation if the state changes in the closure function.

Note: Make sure the component attributes to be set in the closure function have been set before.

 |
| [ArkUI\_AnimateCompleteCallback](../arkui-animatecompletecallback/document.md)\* complete | Callback invoked when the animation playback is complete. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../../header-files/native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../../header-files/native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

 |

#### \[h2\]keyframeAnimateTo()

int32\_t (\*keyframeAnimateTo)(ArkUI\_ContextHandle context, ArkUI\_KeyframeAnimateOption\* option)

**Description**

Defines a keyframe animation.

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_ContextHandle](../arkui-context--00020177/document.md) context | **UIContext** instance. |
| [ArkUI\_KeyframeAnimateOption](../arkui-keyframeanimateoption/document.md)\* option | Keyframe animation parameter. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../../header-files/native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../../header-files/native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

 |

#### \[h2\]createAnimator()

ArkUI\_AnimatorHandle (\*createAnimator)(ArkUI\_ContextHandle context, ArkUI\_AnimatorOption\* option)

**Description**

Creates an animator object.

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_ContextHandle](../arkui-context--00020177/document.md) context | **UIContext** instance. |
| [ArkUI\_AnimatorOption](../arkui-animatoroption/document.md)\* option | Animator parameter. |

**Returns**

| Type | Description |
| :-- | :-- |
| [ArkUI\_AnimatorHandle](../arkui-animator/document.md) | Returns the pointer to the animator object; returns **NULL** if a parameter error occurs. |

#### \[h2\]disposeAnimator()

void (\*disposeAnimator)(ArkUI\_AnimatorHandle animatorHandle)

**Description**

Disposes of an animator object.

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_AnimatorHandle](../arkui-animator/document.md) animatorHandle | Animator object. |
