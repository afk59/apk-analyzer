# drawable\_descriptor.h

#### Overview

Declares the APIs of **NativeDrawableDescriptor**.

**File to include**: <arkui/drawable\_descriptor.h>

**Library**: libace\_ndk.z.so

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Since**: 12

**Related module**: [ArkUI\_NativeModule](../../modules/arkui-nativemodule/document.md)

**Sample**: [DrawableDescriptorSample](https://gitcode.com/openharmony/applications_app_samples/tree/master/code/DocsSample/ArkUISample/DrawableDescriptorSample)

#### Summary

#### \[h2\]Structs

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [ArkUI\_DrawableDescriptor](../../structs/arkui-drawabledescriptor/document.md) | ArkUI\_DrawableDescriptor | Defines a struct for the **DrawableDescriptor** object. |
| [OH\_PixelmapNative](../../../../../media/image-kit/c-apis/structs/oh-pixelmapnative/document.md) | \- | Defines an **OH\_PixelmapNative** object on the native side using Image Kit. |
| [OH\_PixelmapNative\*](../../structs/oh-pixelmapnative/document.md) | OH\_PixelmapNativeHandle | Defines a struct for the pointer to an **OH\_PixelmapNative** object. |
| [ArkUI\_Node](../../structs/arkui-node/document.md) | \- | 
Defines the ArkUI native component instance object.

**Since**: 22

 |
| [ArkUI\_Node\*](../../structs/arkui-node--00020177/document.md) | ArkUI\_NodeHandle | 

Defines the pointer type for an ArkUI native component instance object.

**Since**: 22

 |
| [ArkUI\_DrawableDescriptor\_AnimationController](../../structs/arkui-drawabledescriptor-animationcontroller/document.md) | ArkUI\_DrawableDescriptor\_AnimationController | 

Defines the DrawableDescriptor animation controller object.

**Since**: 22

 |

#### \[h2\]Enums

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [DrawableDescriptor\_AnimationStatus](#drawabledescriptor_animationstatus) | DrawableDescriptor\_AnimationStatus | Enumerates the playback states of DrawableDescriptor animations. |

#### \[h2\]Functions

| Name | Description |
| :-- | :-- |
| [ArkUI\_DrawableDescriptor\* OH\_ArkUI\_DrawableDescriptor\_CreateFromPixelMap(OH\_PixelmapNativeHandle pixelMap)](#oh_arkui_drawabledescriptor_createfrompixelmap) | Creates a **DrawableDescriptor** object from a **PixelMap** object. |
| [ArkUI\_DrawableDescriptor\* OH\_ArkUI\_DrawableDescriptor\_CreateFromAnimatedPixelMap(OH\_PixelmapNativeHandle\* array, int32\_t size)](#oh_arkui_drawabledescriptor_createfromanimatedpixelmap) | Creates a **DrawableDescriptor** object from an array of **PixelMap** objects. |
| [void OH\_ArkUI\_DrawableDescriptor\_Dispose(ArkUI\_DrawableDescriptor\* drawableDescriptor)](#oh_arkui_drawabledescriptor_dispose) | Disposes of the pointer to a **DrawableDescriptor** object. |
| [OH\_PixelmapNativeHandle OH\_ArkUI\_DrawableDescriptor\_GetStaticPixelMap(ArkUI\_DrawableDescriptor\* drawableDescriptor)](#oh_arkui_drawabledescriptor_getstaticpixelmap) | Obtains the pointer to a **PixelMap** object. |
| [OH\_PixelmapNativeHandle\* OH\_ArkUI\_DrawableDescriptor\_GetAnimatedPixelMapArray(ArkUI\_DrawableDescriptor\* drawableDescriptor)](#oh_arkui_drawabledescriptor_getanimatedpixelmaparray) | Obtains an array of **PixelMap** objects for playing an animation. |
| [int32\_t OH\_ArkUI\_DrawableDescriptor\_GetAnimatedPixelMapArraySize(ArkUI\_DrawableDescriptor\* drawableDescriptor)](#oh_arkui_drawabledescriptor_getanimatedpixelmaparraysize) | Obtains an array of **PixelMap** objects for playing an animation. |
| [void OH\_ArkUI\_DrawableDescriptor\_SetAnimationDuration(ArkUI\_DrawableDescriptor\* drawableDescriptor, int32\_t duration)](#oh_arkui_drawabledescriptor_setanimationduration) | Sets the total playback duration for an array of **PixelMap** objects. |
| [int32\_t OH\_ArkUI\_DrawableDescriptor\_GetAnimationDuration(ArkUI\_DrawableDescriptor\* drawableDescriptor)](#oh_arkui_drawabledescriptor_getanimationduration) | Obtains the total playback duration for an array of **PixelMap** objects. |
| [void OH\_ArkUI\_DrawableDescriptor\_SetAnimationIteration(ArkUI\_DrawableDescriptor\* drawableDescriptor, int32\_t iteration)](#oh_arkui_drawabledescriptor_setanimationiteration) | Sets the number of times that an array of **PixelMap** objects is played. |
| [int32\_t OH\_ArkUI\_DrawableDescriptor\_GetAnimationIteration(ArkUI\_DrawableDescriptor\* drawableDescriptor)](#oh_arkui_drawabledescriptor_getanimationiteration) | Obtains the number of times that an array of **PixelMap** objects is played. |
| [int32\_t OH\_ArkUI\_DrawableDescriptor\_SetAnimationFrameDurations(ArkUI\_DrawableDescriptor\* drawableDescriptor, uint32\_t\* durations, size\_t size)](#oh_arkui_drawabledescriptor_setanimationframedurations) | Sets the duration for each frame in a DrawableDescriptor animation. |
| [int32\_t OH\_ArkUI\_DrawableDescriptor\_GetAnimationFrameDurations(ArkUI\_DrawableDescriptor\* drawableDescriptor, uint32\_t\* durations, size\_t\* size)](#oh_arkui_drawabledescriptor_getanimationframedurations) | Obtains the duration of each frame in a DrawableDescriptor animation. |
| [int32\_t OH\_ArkUI\_DrawableDescriptor\_SetAnimationAutoPlay(ArkUI\_DrawableDescriptor\* drawableDescriptor, uint32\_t autoPlay)](#oh_arkui_drawabledescriptor_setanimationautoplay) | Specifies whether to enable autoplay for a DrawableDescriptor animation. |
| [int32\_t OH\_ArkUI\_DrawableDescriptor\_GetAnimationAutoPlay(ArkUI\_DrawableDescriptor\* drawableDescriptor, uint32\_t\* autoPlay)](#oh_arkui_drawabledescriptor_getanimationautoplay) | Checks whether autoplay is enabled for a DrawableDescriptor animation. |
| [int32\_t OH\_ArkUI\_DrawableDescriptor\_CreateAnimationController(ArkUI\_DrawableDescriptor\* drawableDescriptor, ArkUI\_NodeHandle node, ArkUI\_DrawableDescriptor\_AnimationController\*\* controller)](#oh_arkui_drawabledescriptor_createanimationcontroller) | Creates an animation controller for the DrawableDescriptor. |
| [void OH\_ArkUI\_DrawableDescriptor\_DisposeAnimationController( ArkUI\_DrawableDescriptor\_AnimationController\* controller)](#oh_arkui_drawabledescriptor_disposeanimationcontroller) | Disposes of the DrawableDescriptor animation controller. |
| [int32\_t OH\_ArkUI\_DrawableDescriptor\_StartAnimation(ArkUI\_DrawableDescriptor\_AnimationController\* controller)](#oh_arkui_drawabledescriptor_startanimation) | Starts the DrawableDescriptor animation from the first frame. |
| [int32\_t OH\_ArkUI\_DrawableDescriptor\_StopAnimation(ArkUI\_DrawableDescriptor\_AnimationController\* controller)](#oh_arkui_drawabledescriptor_stopanimation) | Stops the DrawableDescriptor animation and returns to the first frame. |
| [int32\_t OH\_ArkUI\_DrawableDescriptor\_ResumeAnimation(ArkUI\_DrawableDescriptor\_AnimationController\* controller)](#oh_arkui_drawabledescriptor_resumeanimation) | Resumes the DrawableDescriptor animation from the current frame. |
| [int32\_t OH\_ArkUI\_DrawableDescriptor\_PauseAnimation(ArkUI\_DrawableDescriptor\_AnimationController\* controller)](#oh_arkui_drawabledescriptor_pauseanimation) | Pauses the DrawableDescriptor animation at the current frame. |
| [int32\_t OH\_ArkUI\_DrawableDescriptor\_GetAnimationStatus(ArkUI\_DrawableDescriptor\_AnimationController\* controller, DrawableDescriptor\_AnimationStatus\* status)](#oh_arkui_drawabledescriptor_getanimationstatus) | Obtains the playback status of the DrawableDescriptor animation. |

#### Enum Description

#### \[h2\]DrawableDescriptor\_AnimationStatus

enum DrawableDescriptor\_AnimationStatus

**Description**

Enumerates the playback states of DrawableDescriptor animations.

**Since**: 22

| Value | Description |
| :-- | :-- |
| DRAWABLE\_DESCRIPTOR\_ANIMATION\_STATUS\_INITIAL = 0 | The animation is in the initial state. |
| DRAWABLE\_DESCRIPTOR\_ANIMATION\_STATUS\_RUNNING = 1 | The animation is being played. |
| DRAWABLE\_DESCRIPTOR\_ANIMATION\_STATUS\_PAUSED = 2 | The animation is paused. |
| DRAWABLE\_DESCRIPTOR\_ANIMATION\_STATUS\_STOPPED = 3 | The animation is stopped. |

#### Function Description

#### \[h2\]OH\_ArkUI\_DrawableDescriptor\_CreateFromPixelMap()

ArkUI\_DrawableDescriptor\* OH\_ArkUI\_DrawableDescriptor\_CreateFromPixelMap(OH\_PixelmapNativeHandle pixelMap)

**Description**

Creates a **DrawableDescriptor** object from a **PixelMap** object.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_PixelmapNativeHandle](../../structs/oh-pixelmapnative/document.md) pixelMap | Pointer to the [OH\_PixelmapNative](../../structs/oh-pixelmapnative--00020177/document.md) object. |

**Return value**

| Type | Description |
| :-- | :-- |
| [ArkUI\_DrawableDescriptor](../../structs/arkui-drawabledescriptor/document.md)\* | Pointer to the **DrawableDescriptor** object. |

#### \[h2\]OH\_ArkUI\_DrawableDescriptor\_CreateFromAnimatedPixelMap()

ArkUI\_DrawableDescriptor\* OH\_ArkUI\_DrawableDescriptor\_CreateFromAnimatedPixelMap(OH\_PixelmapNativeHandle\* array, int32\_t size)

**Description**

Creates a **DrawableDescriptor** object from an array of **PixelMap** objects.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_PixelmapNativeHandle](../../structs/oh-pixelmapnative/document.md)\* array | Pointer to the array of **PixelMap** objects. |
| int32\_t size | Size of the **PixelMap** object array. |

**Return value**

| Type | Description |
| :-- | :-- |
| [ArkUI\_DrawableDescriptor](../../structs/arkui-drawabledescriptor/document.md)\* | Pointer to the **DrawableDescriptor** object. |

#### \[h2\]OH\_ArkUI\_DrawableDescriptor\_Dispose()

void OH\_ArkUI\_DrawableDescriptor\_Dispose(ArkUI\_DrawableDescriptor\* drawableDescriptor)

**Description**

Disposes of the pointer to a **DrawableDescriptor** object.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_DrawableDescriptor](../../structs/arkui-drawabledescriptor/document.md)\* drawableDescriptor | Pointer to a **DrawableDescriptor** object. |

#### \[h2\]OH\_ArkUI\_DrawableDescriptor\_GetStaticPixelMap()

OH\_PixelmapNativeHandle OH\_ArkUI\_DrawableDescriptor\_GetStaticPixelMap(ArkUI\_DrawableDescriptor\* drawableDescriptor)

**Description**

Obtains the pointer to a **PixelMap** object.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_DrawableDescriptor](../../structs/arkui-drawabledescriptor/document.md)\* drawableDescriptor | Pointer to a **DrawableDescriptor** object. |

**Return value**

| Type | Description |
| :-- | :-- |
| [OH\_PixelmapNativeHandle](../../structs/oh-pixelmapnative/document.md) | Pointer to the [OH\_PixelmapNative](../../structs/oh-pixelmapnative--00020177/document.md) object. |

#### \[h2\]OH\_ArkUI\_DrawableDescriptor\_GetAnimatedPixelMapArray()

OH\_PixelmapNativeHandle\* OH\_ArkUI\_DrawableDescriptor\_GetAnimatedPixelMapArray(ArkUI\_DrawableDescriptor\* drawableDescriptor)

**Description**

Obtains an array of **PixelMap** objects for playing an animation.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_DrawableDescriptor](../../structs/arkui-drawabledescriptor/document.md)\* drawableDescriptor | Pointer to a **DrawableDescriptor** object. |

**Return value**

| Type | Description |
| :-- | :-- |
| [OH\_PixelmapNativeHandle](../../structs/oh-pixelmapnative/document.md)\* | Pointer to the array of **PixelMap** objects. |

#### \[h2\]OH\_ArkUI\_DrawableDescriptor\_GetAnimatedPixelMapArraySize()

int32\_t OH\_ArkUI\_DrawableDescriptor\_GetAnimatedPixelMapArraySize(ArkUI\_DrawableDescriptor\* drawableDescriptor)

**Description**

Obtains an array of **PixelMap** objects for playing an animation.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_DrawableDescriptor](../../structs/arkui-drawabledescriptor/document.md)\* drawableDescriptor | Pointer to a **DrawableDescriptor** object. |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | Size of the **PixelMap** object array. |

#### \[h2\]OH\_ArkUI\_DrawableDescriptor\_SetAnimationDuration()

void OH\_ArkUI\_DrawableDescriptor\_SetAnimationDuration(ArkUI\_DrawableDescriptor\* drawableDescriptor, int32\_t duration)

**Description**

Sets the total playback duration for an array of **PixelMap** objects.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_DrawableDescriptor](../../structs/arkui-drawabledescriptor/document.md)\* drawableDescriptor | Pointer to a **DrawableDescriptor** object. |
| int32\_t duration | Total playback duration, in ms. Value range: \[0, +∞). If a negative value is passed in, **0** is used. |

#### \[h2\]OH\_ArkUI\_DrawableDescriptor\_GetAnimationDuration()

int32\_t OH\_ArkUI\_DrawableDescriptor\_GetAnimationDuration(ArkUI\_DrawableDescriptor\* drawableDescriptor)

**Description**

Obtains the total playback duration for an array of **PixelMap** objects.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_DrawableDescriptor](../../structs/arkui-drawabledescriptor/document.md)\* drawableDescriptor | Pointer to a **DrawableDescriptor** object. |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | Total playback duration, in ms. |

#### \[h2\]OH\_ArkUI\_DrawableDescriptor\_SetAnimationIteration()

void OH\_ArkUI\_DrawableDescriptor\_SetAnimationIteration(ArkUI\_DrawableDescriptor\* drawableDescriptor, int32\_t iteration)

**Description**

Sets the number of times that an array of **PixelMap** objects is played.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_DrawableDescriptor](../../structs/arkui-drawabledescriptor/document.md)\* drawableDescriptor | Pointer to a **DrawableDescriptor** object. |
| int32\_t iteration | Number of playback times. Value range: \[0, +∞). The value **0** indicates infinite playback. If a negative value is passed in, **0** is used. |

#### \[h2\]OH\_ArkUI\_DrawableDescriptor\_GetAnimationIteration()

int32\_t OH\_ArkUI\_DrawableDescriptor\_GetAnimationIteration(ArkUI\_DrawableDescriptor\* drawableDescriptor)

**Description**

Obtains the number of times that an array of **PixelMap** objects is played.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_DrawableDescriptor](../../structs/arkui-drawabledescriptor/document.md)\* drawableDescriptor | Pointer to a **DrawableDescriptor** object. |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | Number of playback times. |

#### \[h2\]OH\_ArkUI\_DrawableDescriptor\_SetAnimationFrameDurations()

int32\_t OH\_ArkUI\_DrawableDescriptor\_SetAnimationFrameDurations(ArkUI\_DrawableDescriptor\* drawableDescriptor, uint32\_t\* durations, size\_t size)

**Description**

Sets the duration for each frame in a DrawableDescriptor animation.

**Since**: 22

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_DrawableDescriptor](../../structs/arkui-drawabledescriptor/document.md)\* drawableDescriptor | Pointer to a **DrawableDescriptor** object. |
| uint32\_t\* durations | 
Array of the playback durations for each frame in the animation, in ms.

If this parameter is not set, the playback follows the total duration. This parameter takes precedence over [OH\_ArkUI\_DrawableDescriptor\_SetAnimationDuration](#oh_arkui_drawabledescriptor_setanimationduration). That is, if both **OH\_ArkUI\_DrawableDescriptor\_SetAnimationDuration** and **OH\_ArkUI\_DrawableDescriptor\_SetAnimationFrameDurations** are set, **OH\_ArkUI\_DrawableDescriptor\_SetAnimationDuration** does not take effect.

The array size must match the number of frames in the PixelMap image array.

Valid range for each frame's playback duration: \[0, +∞). Default value: evenly distributed total duration.

 |
| size\_t size | Array size. |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

 |

#### \[h2\]OH\_ArkUI\_DrawableDescriptor\_GetAnimationFrameDurations()

int32\_t OH\_ArkUI\_DrawableDescriptor\_GetAnimationFrameDurations(ArkUI\_DrawableDescriptor\* drawableDescriptor, uint32\_t\* durations, size\_t\* size)

**Description**

Obtains the duration of each frame in a DrawableDescriptor animation.

**Since**: 22

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_DrawableDescriptor](../../structs/arkui-drawabledescriptor/document.md)\* drawableDescriptor | Pointer to a **DrawableDescriptor** object. |
| uint32\_t\* durations | Array of the playback durations for each frame in the animation, in ms. |
| size\_t\* size | Array size. |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

 |

#### \[h2\]OH\_ArkUI\_DrawableDescriptor\_SetAnimationAutoPlay()

int32\_t OH\_ArkUI\_DrawableDescriptor\_SetAnimationAutoPlay(ArkUI\_DrawableDescriptor\* drawableDescriptor, uint32\_t autoPlay)

**Description**

Specifies whether to enable autoplay for a DrawableDescriptor animation.

**Since**: 22

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_DrawableDescriptor](../../structs/arkui-drawabledescriptor/document.md)\* drawableDescriptor | Pointer to a **DrawableDescriptor** object. |
| uint32\_t autoPlay | 
Whether to enable autoplay.

**1** to enable, **0** otherwise.

The default value is **1**.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

 |

#### \[h2\]OH\_ArkUI\_DrawableDescriptor\_GetAnimationAutoPlay()

int32\_t OH\_ArkUI\_DrawableDescriptor\_GetAnimationAutoPlay(ArkUI\_DrawableDescriptor\* drawableDescriptor, uint32\_t\* autoPlay)

**Description**

Checks whether autoplay is enabled for a DrawableDescriptor animation.

**Since**: 22

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_DrawableDescriptor](../../structs/arkui-drawabledescriptor/document.md)\* drawableDescriptor | Pointer to a **DrawableDescriptor** object. |
| uint32\_t\* autoPlay | Whether autoplay is enabled. |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

 |

#### \[h2\]OH\_ArkUI\_DrawableDescriptor\_CreateAnimationController()

int32\_t OH\_ArkUI\_DrawableDescriptor\_CreateAnimationController(ArkUI\_DrawableDescriptor\* drawableDescriptor, ArkUI\_NodeHandle node, ArkUI\_DrawableDescriptor\_AnimationController\*\* controller)

**Description**

Creates an animation controller for the DrawableDescriptor.

**Since**: 22

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_DrawableDescriptor](../../structs/arkui-drawabledescriptor/document.md)\* drawableDescriptor | Pointer to a **DrawableDescriptor** object. |
| [ArkUI\_NodeHandle](../../structs/arkui-node--00020177/document.md) node | Pointer to the component node. |
| [ArkUI\_DrawableDescriptor\_AnimationController](../../structs/arkui-drawabledescriptor-animationcontroller/document.md)\*\* controller | Pointer to a **DrawableDescriptor** animation controller. |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

 |

#### \[h2\]OH\_ArkUI\_DrawableDescriptor\_DisposeAnimationController()

void OH\_ArkUI\_DrawableDescriptor\_DisposeAnimationController(ArkUI\_DrawableDescriptor\_AnimationController\* controller)

**Description**

Disposes of the DrawableDescriptor animation controller.

**Since**: 22

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_DrawableDescriptor\_AnimationController](../../structs/arkui-drawabledescriptor-animationcontroller/document.md)\* controller | Pointer to a **DrawableDescriptor** animation controller. |

#### \[h2\]OH\_ArkUI\_DrawableDescriptor\_StartAnimation()

int32\_t OH\_ArkUI\_DrawableDescriptor\_StartAnimation(ArkUI\_DrawableDescriptor\_AnimationController\* controller);

**Description**

Starts playback from the first frame.

**Since**: 22

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_DrawableDescriptor\_AnimationController](../../structs/arkui-drawabledescriptor-animationcontroller/document.md)\* controller | Pointer to a **DrawableDescriptor** animation controller. |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

 |

#### \[h2\]OH\_ArkUI\_DrawableDescriptor\_StopAnimation()

int32\_t OH\_ArkUI\_DrawableDescriptor\_StopAnimation(ArkUI\_DrawableDescriptor\_AnimationController\* controller);

**Description**

Stops the DrawableDescriptor animation and returns to the first frame.

**Since**: 22

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_DrawableDescriptor\_AnimationController](../../structs/arkui-drawabledescriptor-animationcontroller/document.md)\* controller | Pointer to a **DrawableDescriptor** animation controller. |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

 |

#### \[h2\]OH\_ArkUI\_DrawableDescriptor\_ResumeAnimation()

int32\_t OH\_ArkUI\_DrawableDescriptor\_ResumeAnimation(ArkUI\_DrawableDescriptor\_AnimationController\* controller);

**Description**

Resumes the DrawableDescriptor animation from the current frame.

**Since**: 22

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_DrawableDescriptor\_AnimationController](../../structs/arkui-drawabledescriptor-animationcontroller/document.md)\* controller | Pointer to a **DrawableDescriptor** animation controller. |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

 |

#### \[h2\]OH\_ArkUI\_DrawableDescriptor\_PauseAnimation()

int32\_t OH\_ArkUI\_DrawableDescriptor\_PauseAnimation(ArkUI\_DrawableDescriptor\_AnimationController\* controller);

**Description**

Pauses playback on the current frame.

**Since**: 22

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_DrawableDescriptor\_AnimationController](../../structs/arkui-drawabledescriptor-animationcontroller/document.md)\* controller | Pointer to a **DrawableDescriptor** animation controller. |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

 |

#### \[h2\]OH\_ArkUI\_DrawableDescriptor\_GetAnimationStatus()

int32\_t OH\_ArkUI\_DrawableDescriptor\_GetAnimationStatus(ArkUI\_DrawableDescriptor\_AnimationController\* controller, DrawableDescriptor\_AnimationStatus\* status);

**Description**

Obtains the playback status of the DrawableDescriptor animation.

**Since**: 22

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_DrawableDescriptor\_AnimationController](../../structs/arkui-drawabledescriptor-animationcontroller/document.md)\* controller | Pointer to a **DrawableDescriptor** animation controller. |
| [DrawableDescriptor\_AnimationStatus](#drawabledescriptor_animationstatus)\* status | Playback state of the DrawableDescriptor animation. |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

 |
