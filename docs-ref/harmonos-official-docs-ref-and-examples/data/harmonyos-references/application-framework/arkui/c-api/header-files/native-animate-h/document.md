# native\_animate.h

#### Overview

Defines a set of animation APIs of ArkUI on the native side. The APIs in **native\_animate.h** must be called in the main thread.

**File to include**: <arkui/native\_animate.h>

**Library**: libace\_ndk.z.so

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Since**: 12

**Related module**: [ArkUI\_NativeModule](../../modules/arkui-nativemodule/document.md)

**Sample**: [AnimationNDK](https://gitcode.com/openharmony/applications_app_samples/tree/master/code/DocsSample/ArkUISample/AnimationNDK)

#### Summary

#### \[h2\]Structs

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [ArkUI\_ExpectedFrameRateRange](../../structs/arkui-expectedframeraterange/document.md) | ArkUI\_ExpectedFrameRateRange | Defines a struct for the expected frame rate range of the animation. |
| [ArkUI\_AnimateCompleteCallback](../../structs/arkui-animatecompletecallback/document.md) | ArkUI\_AnimateCompleteCallback | Defines the callback type for when the animation playback is complete. |
| [ArkUI\_NativeAnimateAPI\_1](../../structs/arkui-nativeanimateapi-1/document.md) | ArkUI\_NativeAnimateAPI\_1 | Defines a struct for the animation APIs of ArkUI on the native side. |
| [ArkUI\_AnimateOption](../../structs/arkui-animateoption/document.md) | ArkUI\_AnimateOption | Animation settings. |
| [ArkUI\_Curve](../../structs/arkui-curve/document.md) | ArkUI\_Curve | Defines an interpolation curve. |
| [ArkUI\_Curve\*](../../structs/arkui-curve--00020177/document.md) | ArkUI\_CurveHandle | Defines a struct for the pointer to an interpolation curve. |
| [ArkUI\_KeyframeAnimateOption](../../structs/arkui-keyframeanimateoption/document.md) | ArkUI\_KeyframeAnimateOption | Defines the keyframe animation parameter object. |
| [ArkUI\_AnimatorOption](../../structs/arkui-animatoroption/document.md) | ArkUI\_AnimatorOption | Defines the animator parameter object. |
| [ArkUI\_Animator\*](../../structs/arkui-animator/document.md) | ArkUI\_AnimatorHandle | Defines the pointer to an animator object. |
| [ArkUI\_AnimatorEvent](../../structs/arkui-animatorevent/document.md) | ArkUI\_AnimatorEvent | Defines the animator callback event object. |
| [ArkUI\_AnimatorOnFrameEvent](../../structs/arkui-animatoronframeevent/document.md) | ArkUI\_AnimatorOnFrameEvent | Defines the callback object when the animator receives a frame. |
| [ArkUI\_TransitionEffect](../../structs/arkui-transitioneffect/document.md) | ArkUI\_TransitionEffect | Defines the transition effect. |

#### \[h2\]Functions

| Name | Description |
| :-- | :-- |
| [ArkUI\_AnimateOption\* OH\_ArkUI\_AnimateOption\_Create()](#oh_arkui_animateoption_create) | Creates an animation configuration. |
| [void OH\_ArkUI\_AnimateOption\_Dispose(ArkUI\_AnimateOption\* option)](#oh_arkui_animateoption_dispose) | Disposes of an animation configuration. |
| [uint32\_t OH\_ArkUI\_AnimateOption\_GetDuration(ArkUI\_AnimateOption\* option)](#oh_arkui_animateoption_getduration) | Obtains the animation duration, in milliseconds. |
| [float OH\_ArkUI\_AnimateOption\_GetTempo(ArkUI\_AnimateOption\* option)](#oh_arkui_animateoption_gettempo) | Obtains the playback speed of an animation. |
| [ArkUI\_AnimationCurve OH\_ArkUI\_AnimateOption\_GetCurve(ArkUI\_AnimateOption\* option)](#oh_arkui_animateoption_getcurve) | Obtains an animation curve. |
| [int32\_t OH\_ArkUI\_AnimateOption\_GetDelay(ArkUI\_AnimateOption\* option)](#oh_arkui_animateoption_getdelay) | Obtains the animation delay, in milliseconds. |
| [int32\_t OH\_ArkUI\_AnimateOption\_GetIterations(ArkUI\_AnimateOption\* option)](#oh_arkui_animateoption_getiterations) | Obtains the number of times that an animation is played. |
| [ArkUI\_AnimationPlayMode OH\_ArkUI\_AnimateOption\_GetPlayMode(ArkUI\_AnimateOption\* option)](#oh_arkui_animateoption_getplaymode) | Obtains the playback mode of an animation. |
| [ArkUI\_ExpectedFrameRateRange\* OH\_ArkUI\_AnimateOption\_GetExpectedFrameRateRange(ArkUI\_AnimateOption\* option)](#oh_arkui_animateoption_getexpectedframeraterange) | Obtains the expected frame rate range of an animation. |
| [void OH\_ArkUI\_AnimateOption\_SetDuration(ArkUI\_AnimateOption\* option, int32\_t value)](#oh_arkui_animateoption_setduration) | Sets the animation duration, in milliseconds. |
| [void OH\_ArkUI\_AnimateOption\_SetTempo(ArkUI\_AnimateOption\* option, float value)](#oh_arkui_animateoption_settempo) | Sets the playback speed of an animation. |
| [void OH\_ArkUI\_AnimateOption\_SetCurve(ArkUI\_AnimateOption\* option, ArkUI\_AnimationCurve value)](#oh_arkui_animateoption_setcurve) | Animation curve. |
| [void OH\_ArkUI\_AnimateOption\_SetDelay(ArkUI\_AnimateOption\* option, int32\_t value)](#oh_arkui_animateoption_setdelay) | Sets the animation delay, in milliseconds. |
| [void OH\_ArkUI\_AnimateOption\_SetIterations(ArkUI\_AnimateOption\* option, int32\_t value)](#oh_arkui_animateoption_setiterations) | Sets the number of times that an animation is played. |
| [void OH\_ArkUI\_AnimateOption\_SetPlayMode(ArkUI\_AnimateOption\* option, ArkUI\_AnimationPlayMode value)](#oh_arkui_animateoption_setplaymode) | Sets the playback mode for an animation. |
| [void OH\_ArkUI\_AnimateOption\_SetExpectedFrameRateRange(ArkUI\_AnimateOption\* option, ArkUI\_ExpectedFrameRateRange\* value)](#oh_arkui_animateoption_setexpectedframeraterange) | Defines a struct for the expected frame rate range of the animation. |
| [void OH\_ArkUI\_AnimateOption\_SetICurve(ArkUI\_AnimateOption\* option, ArkUI\_CurveHandle value)](#oh_arkui_animateoption_seticurve) | Sets the animation curve for an animation. |
| [ArkUI\_CurveHandle OH\_ArkUI\_AnimateOption\_GetICurve(ArkUI\_AnimateOption\* option)](#oh_arkui_animateoption_geticurve) | Obtains the animation curve of an animation. |
| [ArkUI\_KeyframeAnimateOption\* OH\_ArkUI\_KeyframeAnimateOption\_Create(int32\_t size)](#oh_arkui_keyframeanimateoption_create) | Creates a keyframe animation parameter object. |
| [void OH\_ArkUI\_KeyframeAnimateOption\_Dispose(ArkUI\_KeyframeAnimateOption\* option)](#oh_arkui_keyframeanimateoption_dispose) | Disposes of a keyframe animation parameter object. |
| [int32\_t OH\_ArkUI\_KeyframeAnimateOption\_SetDelay(ArkUI\_KeyframeAnimateOption\* option, int32\_t value)](#oh_arkui_keyframeanimateoption_setdelay) | Sets the overall delay of a keyframe animation, in milliseconds. By default, the keyframe animation starts without any delay. |
| [int32\_t OH\_ArkUI\_KeyframeAnimateOption\_SetIterations(ArkUI\_KeyframeAnimateOption\* option, int32\_t value)](#oh_arkui_keyframeanimateoption_setiterations) | Sets the number of times that the keyframe animation is played. By default, the animation is played once. The value **\-1** indicates that the animation is played for an unlimited number of times. The value **0** indicates that no animation is played. |
| [int32\_t OH\_ArkUI\_KeyframeAnimateOption\_RegisterOnFinishCallback(ArkUI\_KeyframeAnimateOption\* option, void\* userData, void (\*onFinish)()(void\* userData))](#oh_arkui_keyframeanimateoption_registeronfinishcallback) | Sets the callback invoked when the keyframe animation playback is complete. This function is called after the [keyframe animation](../../structs/arkui-keyframeanimateoption/document.md) has played for the specified number of times. |
| [int32\_t OH\_ArkUI\_KeyframeAnimateOption\_SetExpectedFrameRate(ArkUI\_KeyframeAnimateOption\* option, ArkUI\_ExpectedFrameRateRange\* frameRate)](#oh_arkui_keyframeanimateoption_setexpectedframerate) | Sets the expected frame rate for a keyframe animation. |
| [int32\_t OH\_ArkUI\_KeyframeAnimateOption\_SetDuration(ArkUI\_KeyframeAnimateOption\* option, int32\_t value, int32\_t index)](#oh_arkui_keyframeanimateoption_setduration) | Sets the duration of a keyframe animation, in milliseconds. |
| [int32\_t OH\_ArkUI\_KeyframeAnimateOption\_SetCurve(ArkUI\_KeyframeAnimateOption\* option, ArkUI\_CurveHandle value, int32\_t index)](#oh_arkui_keyframeanimateoption_setcurve) | Sets the animation curve for a specific keyframe animation segment. |
| [int32\_t OH\_ArkUI\_KeyframeAnimateOption\_RegisterOnEventCallback(ArkUI\_KeyframeAnimateOption\* option, void\* userData, void (\*event)(void\* userData), int32\_t index)](#oh_arkui_keyframeanimateoption_registeroneventcallback) | Sets the closure function of the state at the time of the keyframe, that is, the state to be reached at the time of the keyframe. |
| [int32\_t OH\_ArkUI\_KeyframeAnimateOption\_GetDelay(ArkUI\_KeyframeAnimateOption\* option)](#oh_arkui_keyframeanimateoption_getdelay) | Obtains the overall delay of a keyframe animation, in milliseconds. |
| [int32\_t OH\_ArkUI\_KeyframeAnimateOption\_GetIterations(ArkUI\_KeyframeAnimateOption\* option)](#oh_arkui_keyframeanimateoption_getiterations) | Obtains the number of times that a keyframe animation is played. |
| [ArkUI\_ExpectedFrameRateRange\* OH\_ArkUI\_KeyframeAnimateOption\_GetExpectedFrameRate(ArkUI\_KeyframeAnimateOption\* option)](#oh_arkui_keyframeanimateoption_getexpectedframerate) | Obtains the expected frame rate from keyframe animation parameters. |
| [int32\_t OH\_ArkUI\_KeyframeAnimateOption\_GetDuration(ArkUI\_KeyframeAnimateOption\* option, int32\_t index)](#oh_arkui_keyframeanimateoption_getduration) | Obtains the duration of a specific state in a keyframe animation, in milliseconds. |
| [ArkUI\_CurveHandle OH\_ArkUI\_KeyframeAnimateOption\_GetCurve(ArkUI\_KeyframeAnimateOption\* option, int32\_t index)](#oh_arkui_keyframeanimateoption_getcurve) | Obtains the animation curve of a specific state in a keyframe animation. |
| [ArkUI\_AnimatorOption\* OH\_ArkUI\_AnimatorOption\_Create(int32\_t keyframeSize)](#oh_arkui_animatoroption_create) | Creates an **AnimatorOption** object. |
| [void OH\_ArkUI\_AnimatorOption\_Dispose(ArkUI\_AnimatorOption\* option)](#oh_arkui_animatoroption_dispose) | Disposes of the animator parameters object. |
| [int32\_t OH\_ArkUI\_AnimatorOption\_SetDuration(ArkUI\_AnimatorOption\* option, int32\_t value)](#oh_arkui_animatoroption_setduration) | Sets the duration of the animator playback, in milliseconds. |
| [int32\_t OH\_ArkUI\_AnimatorOption\_SetDelay(ArkUI\_AnimatorOption\* option, int32\_t value)](#oh_arkui_animatoroption_setdelay) | Sets the delay time of the animator playback, in milliseconds. |
| [int32\_t OH\_ArkUI\_AnimatorOption\_SetIterations(ArkUI\_AnimatorOption\* option, int32\_t value)](#oh_arkui_animatoroption_setiterations) | Sets the number of times that an animator animation is played. By default, the animation is played once. The value **\-1** indicates that the animation is played for an unlimited number of times. The value **0** indicates that no animation is played. |
| [int32\_t OH\_ArkUI\_AnimatorOption\_SetFill(ArkUI\_AnimatorOption\* option, ArkUI\_AnimationFillMode value)](#oh_arkui_animatoroption_setfill) | Sets the status of the component before and after the animator animation execution. |
| [int32\_t OH\_ArkUI\_AnimatorOption\_SetDirection(ArkUI\_AnimatorOption\* option, ArkUI\_AnimationDirection value)](#oh_arkui_animatoroption_setdirection) | Set the playback direction. |
| [int32\_t OH\_ArkUI\_AnimatorOption\_SetCurve(ArkUI\_AnimatorOption\* option, ArkUI\_CurveHandle value)](#oh_arkui_animatoroption_setcurve) | Sets the interpolation curve for the animation of an animator. |
| [int32\_t OH\_ArkUI\_AnimatorOption\_SetBegin(ArkUI\_AnimatorOption\* option, float value)](#oh_arkui_animatoroption_setbegin) | Sets the interpolation start point of an animation. |
| [int32\_t OH\_ArkUI\_AnimatorOption\_SetEnd(ArkUI\_AnimatorOption\* option, float value)](#oh_arkui_animatoroption_setend) | Sets the interpolation end point for the animation of an animator. |
| [int32\_t OH\_ArkUI\_AnimatorOption\_SetExpectedFrameRateRange(ArkUI\_AnimatorOption\* option, ArkUI\_ExpectedFrameRateRange\* value)](#oh_arkui_animatoroption_setexpectedframeraterange) | Sets the expected frame rate range of an animator animation. |
| [int32\_t OH\_ArkUI\_AnimatorOption\_SetKeyframe(ArkUI\_AnimatorOption\* option, float time, float value, int32\_t index)](#oh_arkui_animatoroption_setkeyframe) | Sets the keyframe parameters of an animator animation. |
| [int32\_t OH\_ArkUI\_AnimatorOption\_SetKeyframeCurve(ArkUI\_AnimatorOption\* option, ArkUI\_CurveHandle value, int32\_t index)](#oh_arkui_animatoroption_setkeyframecurve) | Sets the keyframe curve type for the animation of an animator. |
| [int32\_t OH\_ArkUI\_AnimatorOption\_GetDuration(ArkUI\_AnimatorOption\* option)](#oh_arkui_animatoroption_getduration) | Obtains the duration for playing an animator animation. |
| [int32\_t OH\_ArkUI\_AnimatorOption\_GetDelay(ArkUI\_AnimatorOption\* option)](#oh_arkui_animatoroption_getdelay) | Obtains the delay for playing an animator animation. |
| [int32\_t OH\_ArkUI\_AnimatorOption\_GetIterations(ArkUI\_AnimatorOption\* option)](#oh_arkui_animatoroption_getiterations) | Obtains the number of times that an animator animation is played. |
| [ArkUI\_AnimationFillMode OH\_ArkUI\_AnimatorOption\_GetFill(ArkUI\_AnimatorOption\* option)](#oh_arkui_animatoroption_getfill) | Obtains the status of the component before and after the animator animation execution. |
| [ArkUI\_AnimationDirection OH\_ArkUI\_AnimatorOption\_GetDirection(ArkUI\_AnimatorOption\* option)](#oh_arkui_animatoroption_getdirection) | Obtains the playback direction of an animator animation. |
| [ArkUI\_CurveHandle OH\_ArkUI\_AnimatorOption\_GetCurve(ArkUI\_AnimatorOption\* option)](#oh_arkui_animatoroption_getcurve) | Obtains the interpolation curve of an animator animation. |
| [float OH\_ArkUI\_AnimatorOption\_GetBegin(ArkUI\_AnimatorOption\* option)](#oh_arkui_animatoroption_getbegin) | Obtains the interpolation start point of an animator animation. |
| [float OH\_ArkUI\_AnimatorOption\_GetEnd(ArkUI\_AnimatorOption\* option)](#oh_arkui_animatoroption_getend) | Obtains the interpolation end point of an animator animation. |
| [ArkUI\_ExpectedFrameRateRange\* OH\_ArkUI\_AnimatorOption\_GetExpectedFrameRateRange(ArkUI\_AnimatorOption\* option)](#oh_arkui_animatoroption_getexpectedframeraterange) | Obtains the expected frame rate range of an animator animation. |
| [float OH\_ArkUI\_AnimatorOption\_GetKeyframeTime(ArkUI\_AnimatorOption\* option, int32\_t index)](#oh_arkui_animatoroption_getkeyframetime) | Obtains the keyframe time of the animator playback, in milliseconds. |
| [float OH\_ArkUI\_AnimatorOption\_GetKeyframeValue(ArkUI\_AnimatorOption\* option, int32\_t index)](#oh_arkui_animatoroption_getkeyframevalue) | Obtains the keyframe value of an animation. |
| [ArkUI\_CurveHandle OH\_ArkUI\_AnimatorOption\_GetKeyframeCurve(ArkUI\_AnimatorOption\* option, int32\_t index)](#oh_arkui_animatoroption_getkeyframecurve) | Obtains the interpolation curve for a keyframe in the animation of an animator. |
| [void\* OH\_ArkUI\_AnimatorEvent\_GetUserData(ArkUI\_AnimatorEvent\* event)](#oh_arkui_animatorevent_getuserdata) | Obtains the custom object in an animation event object. |
| [void\* OH\_ArkUI\_AnimatorOnFrameEvent\_GetUserData(ArkUI\_AnimatorOnFrameEvent\* event)](#oh_arkui_animatoronframeevent_getuserdata) | Obtains the user-defined object in the frame event of an animation. |
| [float OH\_ArkUI\_AnimatorOnFrameEvent\_GetValue(ArkUI\_AnimatorOnFrameEvent\* event)](#oh_arkui_animatoronframeevent_getvalue) | Obtains the interpolation result in the animation frame callback event object. |
| [int32\_t OH\_ArkUI\_AnimatorOption\_RegisterOnFrameCallback(ArkUI\_AnimatorOption\* option, void\* userData, void (\*callback)(ArkUI\_AnimatorOnFrameEvent\* event))](#oh_arkui_animatoroption_registeronframecallback) | Sets the callback invoked when the animator receives a frame. |
| [int32\_t OH\_ArkUI\_AnimatorOption\_RegisterOnFinishCallback(ArkUI\_AnimatorOption\* option, void\* userData, void (\*callback)(ArkUI\_AnimatorEvent\* event))](#oh_arkui_animatoroption_registeronfinishcallback) | Sets the callback invoked when the animation playback is complete. |
| [int32\_t OH\_ArkUI\_AnimatorOption\_RegisterOnCancelCallback(ArkUI\_AnimatorOption\* option, void\* userData, void (\*callback)(ArkUI\_AnimatorEvent\* event))](#oh_arkui_animatoroption_registeroncancelcallback) | Sets the callback invoked when the animation playback is canceled. |
| [int32\_t OH\_ArkUI\_AnimatorOption\_RegisterOnRepeatCallback(ArkUI\_AnimatorOption\* option, void\* userData, void (\*callback)(ArkUI\_AnimatorEvent\* event))](#oh_arkui_animatoroption_registeronrepeatcallback) | Sets the callback invoked when the animation playback is repeated. |
| [int32\_t OH\_ArkUI\_Animator\_ResetAnimatorOption(ArkUI\_AnimatorHandle animatorHandle, ArkUI\_AnimatorOption\* option)](#oh_arkui_animator_resetanimatoroption) | Resets the animation of an animator. |
| [int32\_t OH\_ArkUI\_Animator\_Play(ArkUI\_AnimatorHandle animatorHandle)](#oh_arkui_animator_play) | Starts the animation of an animator. |
| [int32\_t OH\_ArkUI\_Animator\_Finish(ArkUI\_AnimatorHandle animatorHandle)](#oh_arkui_animator_finish) | Ends the animation of an animator. |
| [int32\_t OH\_ArkUI\_Animator\_Pause(ArkUI\_AnimatorHandle animatorHandle)](#oh_arkui_animator_pause) | Pauses the animation of an animator. |
| [int32\_t OH\_ArkUI\_Animator\_Cancel(ArkUI\_AnimatorHandle animatorHandle)](#oh_arkui_animator_cancel) | Cancels the animation of an animator. |
| [int32\_t OH\_ArkUI\_Animator\_Reverse(ArkUI\_AnimatorHandle animatorHandle)](#oh_arkui_animator_reverse) | Plays this animation in reverse order. |
| [ArkUI\_CurveHandle OH\_ArkUI\_Curve\_CreateCurveByType(ArkUI\_AnimationCurve curve)](#oh_arkui_curve_createcurvebytype) | Implements initialization for the interpolation curve, which is used to create an interpolation curve based on the input parameter. |
| [ArkUI\_CurveHandle OH\_ArkUI\_Curve\_CreateStepsCurve(int32\_t count, bool end)](#oh_arkui_curve_createstepscurve) | Creates a step curve. |
| [ArkUI\_CurveHandle OH\_ArkUI\_Curve\_CreateCubicBezierCurve(float x1, float y1, float x2, float y2)](#oh_arkui_curve_createcubicbeziercurve) | Creates a cubic Bezier curve. |
| [ArkUI\_CurveHandle OH\_ArkUI\_Curve\_CreateSpringCurve(float velocity, float mass, float stiffness, float damping)](#oh_arkui_curve_createspringcurve) | Creates a spring curve. The curve shape is determined by the spring parameters, and the animation duration is controlled by the **duration** parameter in [animation](#oh_arkui_transitioneffect_setanimation) and [animateTo](../../structs/arkui-nativeanimateapi-1/document.md#animateto). |
| [ArkUI\_CurveHandle OH\_ArkUI\_Curve\_CreateSpringMotion(float response, float dampingFraction, float overlapDuration)](#oh_arkui_curve_createspringmotion) | Creates a spring animation curve. If multiple spring animations are applied to the same attribute of an object, each animation replaces their predecessor and inherits the velocity. |
| [ArkUI\_CurveHandle OH\_ArkUI\_Curve\_CreateResponsiveSpringMotion(float response, float dampingFraction, float overlapDuration)](#oh_arkui_curve_createresponsivespringmotion) | Creates a responsive spring animation curve. It is a special case of **springMotion**, with the only difference in the default values. It can be used together with **springMotion**. |
| [ArkUI\_CurveHandle OH\_ArkUI\_Curve\_CreateInterpolatingSpring(float velocity, float mass, float stiffness, float damping)](#oh_arkui_curve_createinterpolatingspring) | Creates an interpolating spring curve animated from 0 to 1. The actual animation value is calculated based on the curve. |
| [ArkUI\_CurveHandle OH\_ArkUI\_Curve\_CreateCustomCurve(void\* userData, float (\*interpolate)(float fraction, void\* userdata))](#oh_arkui_curve_createcustomcurve) | Creates a custom curve. |
| [void OH\_ArkUI\_Curve\_DisposeCurve(ArkUI\_CurveHandle curveHandle)](#oh_arkui_curve_disposecurve) | Disposes of a custom curve. |
| [ArkUI\_TransitionEffect\* OH\_ArkUI\_CreateOpacityTransitionEffect(float opacity)](#oh_arkui_createopacitytransitioneffect) | Creates an opacity object for component transition. |
| [ArkUI\_TransitionEffect\* OH\_ArkUI\_CreateTranslationTransitionEffect(ArkUI\_TranslationOptions\* translate)](#oh_arkui_createtranslationtransitioneffect) | Creates a translation effect object for component transition. |
| [ArkUI\_TransitionEffect\* OH\_ArkUI\_CreateScaleTransitionEffect(ArkUI\_ScaleOptions\* scale)](#oh_arkui_createscaletransitioneffect) | Creates a scaling object for component transition. |
| [ArkUI\_TransitionEffect\* OH\_ArkUI\_CreateRotationTransitionEffect(ArkUI\_RotationOptions\* rotate)](#oh_arkui_createrotationtransitioneffect) | Creates a rotation effect object for component transition. |
| [ArkUI\_TransitionEffect\* OH\_ArkUI\_CreateMovementTransitionEffect(ArkUI\_TransitionEdge edge)](#oh_arkui_createmovementtransitioneffect) | Creates a movement object for component transition. |
| [ArkUI\_TransitionEffect\* OH\_ArkUI\_CreateAsymmetricTransitionEffect(ArkUI\_TransitionEffect\* appear, ArkUI\_TransitionEffect\* disappear)](#oh_arkui_createasymmetrictransitioneffect) | Creates an asymmetric transition effect. |
| [void OH\_ArkUI\_TransitionEffect\_Dispose(ArkUI\_TransitionEffect\* effect)](#oh_arkui_transitioneffect_dispose) | Disposes of a transition effect. |
| [int32\_t OH\_ArkUI\_TransitionEffect\_Combine(ArkUI\_TransitionEffect\* firstEffect, ArkUI\_TransitionEffect\* secondEffect)](#oh_arkui_transitioneffect_combine) | Sets a combination of transition effects. |
| [int32\_t OH\_ArkUI\_TransitionEffect\_SetAnimation(ArkUI\_TransitionEffect\* effect, ArkUI\_AnimateOption\* animation)](#oh_arkui_transitioneffect_setanimation) | Sets transition effect animation settings. |

#### Function Description

#### \[h2\]OH\_ArkUI\_AnimateOption\_Create()

ArkUI\_AnimateOption\* OH\_ArkUI\_AnimateOption\_Create()

**Description**

Creates an animation configuration.

**Since**: 12

**Return value**

| Type | Description |
| :-- | :-- |
| [ArkUI\_AnimateOption](../../structs/arkui-animateoption/document.md)\* | Pointer to the created animation configuration. |

#### \[h2\]OH\_ArkUI\_AnimateOption\_Dispose()

void OH\_ArkUI\_AnimateOption\_Dispose(ArkUI\_AnimateOption\* option)

**Description**

Disposes of an animation configuration.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_AnimateOption](../../structs/arkui-animateoption/document.md)\* option | 
Pointer to an animation configuration.

If **option** is set to **NULL**, the operation is invalid.

 |

#### \[h2\]OH\_ArkUI\_AnimateOption\_GetDuration()

uint32\_t OH\_ArkUI\_AnimateOption\_GetDuration(ArkUI\_AnimateOption\* option)

**Description**

Obtains the animation duration, in milliseconds.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_AnimateOption](../../structs/arkui-animateoption/document.md)\* option | 
Pointer to an animation configuration.

If **option** is set to **NULL**, **0** is returned.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| uint32\_t | Animation duration, in milliseconds. If **option** is invalid, **0** is returned. |

#### \[h2\]OH\_ArkUI\_AnimateOption\_GetTempo()

float OH\_ArkUI\_AnimateOption\_GetTempo(ArkUI\_AnimateOption\* option)

**Description**

Obtains the playback speed of an animation.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_AnimateOption](../../structs/arkui-animateoption/document.md)\* option | 
Pointer to an animation configuration.

If **option** is set to **NULL**, **0.0** is returned.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| float | Animation playback speed. Value range: \[0, +∞). If **option** is invalid, **0.0** is returned. |

#### \[h2\]OH\_ArkUI\_AnimateOption\_GetCurve()

ArkUI\_AnimationCurve OH\_ArkUI\_AnimateOption\_GetCurve(ArkUI\_AnimateOption\* option)

**Description**

Obtains an animation curve.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_AnimateOption](../../structs/arkui-animateoption/document.md)\* option | 
Pointer to an animation configuration.

If **option** is set to **NULL**, **\-1** is returned.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| [ArkUI\_AnimationCurve](../native-type-h/document.md#arkui_animationcurve) | Animation curve. If **option** is invalid,**\-1** is returned. |

#### \[h2\]OH\_ArkUI\_AnimateOption\_GetDelay()

int32\_t OH\_ArkUI\_AnimateOption\_GetDelay(ArkUI\_AnimateOption\* option)

**Description**

Obtains the animation delay, in milliseconds.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_AnimateOption](../../structs/arkui-animateoption/document.md)\* option | 
Pointer to an animation configuration.

If **option** is set to **NULL**, **0** is returned.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | Delay of animation playback. If **option** is invalid, **0** is returned. |

#### \[h2\]OH\_ArkUI\_AnimateOption\_GetIterations()

int32\_t OH\_ArkUI\_AnimateOption\_GetIterations(ArkUI\_AnimateOption\* option)

**Description**

Obtains the number of times that an animation is played.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_AnimateOption](../../structs/arkui-animateoption/document.md)\* option | 
Pointer to an animation configuration.

If **option** is set to **NULL**, **0** is returned.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | Number of times that the animation is played. If **option** is invalid, **0** is returned. |

#### \[h2\]OH\_ArkUI\_AnimateOption\_GetPlayMode()

ArkUI\_AnimationPlayMode OH\_ArkUI\_AnimateOption\_GetPlayMode(ArkUI\_AnimateOption\* option)

**Description**

Obtains the playback mode of an animation.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_AnimateOption](../../structs/arkui-animateoption/document.md)\* option | 
Pointer to an animation configuration.

If **option** is set to **NULL**, **\-1** is returned.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| [ArkUI\_AnimationPlayMode](../native-type-h/document.md#arkui_animationplaymode) | Animation playback mode. If **option** is invalid,**\-1** is returned. |

#### \[h2\]OH\_ArkUI\_AnimateOption\_GetExpectedFrameRateRange()

ArkUI\_ExpectedFrameRateRange\* OH\_ArkUI\_AnimateOption\_GetExpectedFrameRateRange(ArkUI\_AnimateOption\* option)

**Description**

Obtains the expected frame rate range of an animation.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_AnimateOption](../../structs/arkui-animateoption/document.md)\* option | 
Pointer to an animation configuration.

If **option** is set to **NULL**, **NULL** is returned.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| [ArkUI\_ExpectedFrameRateRange](../../structs/arkui-expectedframeraterange/document.md)\* | Expected frame rate range of the animation, in fps. If **option** is invalid, **NULL** is returned. |

#### \[h2\]OH\_ArkUI\_AnimateOption\_SetDuration()

void OH\_ArkUI\_AnimateOption\_SetDuration(ArkUI\_AnimateOption\* option, int32\_t value)

**Description**

Sets the animation duration, in milliseconds.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_AnimateOption](../../structs/arkui-animateoption/document.md)\* option | 
Pointer to an animation configuration.

If **option** is set to **NULL**, the operation is invalid.

 |
| int32\_t value | 

Animation duration, in milliseconds. Value range: \[0, +∞).

If the value is less than 0, **0** is used.

 |

#### \[h2\]OH\_ArkUI\_AnimateOption\_SetTempo()

void OH\_ArkUI\_AnimateOption\_SetTempo(ArkUI\_AnimateOption\* option, float value)

**Description**

Sets the playback speed of an animation.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_AnimateOption](../../structs/arkui-animateoption/document.md)\* option | 
Pointer to an animation configuration.

If **option** is set to **NULL**, the operation is invalid.

 |
| float value | 

Animation playback speed. Value range: \[0, +∞).

**NOTE**

If the value is less than 0, the default value **1** is used.

 |

#### \[h2\]OH\_ArkUI\_AnimateOption\_SetCurve()

void OH\_ArkUI\_AnimateOption\_SetCurve(ArkUI\_AnimateOption\* option, ArkUI\_AnimationCurve value)

**Description**

Animation curve.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_AnimateOption](../../structs/arkui-animateoption/document.md)\* option | 
Pointer to an animation configuration.

If **option** is set to **NULL**, the operation is invalid.

 |
| [ArkUI\_AnimationCurve](../native-type-h/document.md#arkui_animationcurve) value | 

Animation curve. Default value: [ARKUI\_CURVE\_LINEAR](../native-type-h/document.md#arkui_animationcurve). You are advised to use [ARKUI\_CURVE\_EASE\_IN\_OUT](../native-type-h/document.md#arkui_animationcurve) to obtain a smoother animation effect.

If the value is abnormal, the setting is invalid.

 |

#### \[h2\]OH\_ArkUI\_AnimateOption\_SetDelay()

void OH\_ArkUI\_AnimateOption\_SetDelay(ArkUI\_AnimateOption\* option, int32\_t value)

**Description**

Sets the animation delay, in milliseconds.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_AnimateOption](../../structs/arkui-animateoption/document.md)\* option | 
Pointer to an animation configuration.

If **option** is set to **NULL**, the operation is invalid.

 |
| int32\_t value | Animation delay, in milliseconds. Value range: (-∞, +∞). Default value: **0**, indicating no animation delay. A value greater than 0 means to begin the animation after the specified amount of time has elapsed. A value less than 0 means to begin the animation in advance. If **value** is less than **0** and the absolute value of **value** is less than the actual animation duration, the animation starts its first frame from the state at the absolute value. If the absolute value of **value** is greater than or equal to the actual animation duration, the animation starts its first frame from the end state. The actual animation duration is equal to the duration of a single animation multiplied by the number of animation playback times. |

#### \[h2\]OH\_ArkUI\_AnimateOption\_SetIterations()

void OH\_ArkUI\_AnimateOption\_SetIterations(ArkUI\_AnimateOption\* option, int32\_t value)

**Description**

Sets the number of times that an animation is played.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_AnimateOption](../../structs/arkui-animateoption/document.md)\* option | 
Pointer to an animation configuration.

If **option** is set to **NULL**, the operation is invalid.

 |
| int32\_t value | 

Number of times that the animation is played. Value range: \[-1, +∞). If this parameter is set to **0**, the animation is not played. If this parameter is set to **\-1**, the animation is played for an infinite number of times. Default value: **1** (played once).

If the value is less than -1, the operation is invalid.

 |

#### \[h2\]OH\_ArkUI\_AnimateOption\_SetPlayMode()

void OH\_ArkUI\_AnimateOption\_SetPlayMode(ArkUI\_AnimateOption\* option, ArkUI\_AnimationPlayMode value)

**Description**

Sets the playback mode for an animation.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_AnimateOption](../../structs/arkui-animateoption/document.md)\* option | 
Pointer to an animation configuration.

If **option** is set to **NULL**, the operation is invalid.

 |
| [ArkUI\_AnimationPlayMode](../native-type-h/document.md#arkui_animationplaymode) value | 

Animation playback mode. Default value: [ARKUI\_ANIMATION\_PLAY\_MODE\_NORMAL](../native-type-h/document.md#arkui_animationplaymode).

If the value is abnormal, the operation is invalid.

 |

#### \[h2\]OH\_ArkUI\_AnimateOption\_SetExpectedFrameRateRange()

void OH\_ArkUI\_AnimateOption\_SetExpectedFrameRateRange(ArkUI\_AnimateOption\* option, ArkUI\_ExpectedFrameRateRange\* value)

**Description**

Defines a struct for the expected frame rate range of the animation.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_AnimateOption](../../structs/arkui-animateoption/document.md)\* option | 
Pointer to an animation configuration.

If **option** is set to **NULL**, the operation is invalid.

 |
| [ArkUI\_ExpectedFrameRateRange](../../structs/arkui-expectedframeraterange/document.md)\* value | 

Expected frame rate range of the animation, in fps.

If **value** is set to **NULL**, the operation is invalid.

 |

#### \[h2\]OH\_ArkUI\_AnimateOption\_SetICurve()

void OH\_ArkUI\_AnimateOption\_SetICurve(ArkUI\_AnimateOption\* option, ArkUI\_CurveHandle value)

**Description**

Sets the animation curve for an animation.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d3/v3/guzfNAUcSge-jdQPDWzmtQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062302Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B27FBCD10C49D7BC6C9C2F56F4E3B9DEC7785FEBCD6AF31CDEDC8CE56ADD2635)

This API takes precedence over [OH\_ArkUI\_AnimateOption\_SetCurve](#oh_arkui_animateoption_setcurve).

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_AnimateOption](../../structs/arkui-animateoption/document.md)\* option | 
Animator animation parameters.

If **option** is set to **NULL**, the operation is invalid.

 |
| [ArkUI\_CurveHandle](../../structs/arkui-curve--00020177/document.md) value | 

Animation curve parameters.

If **value** is set to **NULL**, the operation is invalid.

 |

#### \[h2\]OH\_ArkUI\_AnimateOption\_GetICurve()

ArkUI\_CurveHandle OH\_ArkUI\_AnimateOption\_GetICurve(ArkUI\_AnimateOption\* option)

**Description**

Obtains the animation curve of an animation.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_AnimateOption](../../structs/arkui-animateoption/document.md)\* option | 
Animator animation parameters.

If **option** is set to **NULL**, **NULL** is returned.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| [ArkUI\_CurveHandle](../../structs/arkui-curve--00020177/document.md) | Animation curve parameters. Returns **NULL** if the option parameter is invalid. |

#### \[h2\]OH\_ArkUI\_KeyframeAnimateOption\_Create()

ArkUI\_KeyframeAnimateOption\* OH\_ArkUI\_KeyframeAnimateOption\_Create(int32\_t size)

**Description**

Creates a keyframe animation parameter object.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| int32\_t size | 
Number of keyframe animation states.

Returns **NULL** if the value of **size** is less than 0.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| [ArkUI\_KeyframeAnimateOption](../../structs/arkui-keyframeanimateoption/document.md)\* | Keyframe animation parameter object. If the value of **size** is less than 0 or if **option** is abnormal, **NULL** is returned. |

#### \[h2\]OH\_ArkUI\_KeyframeAnimateOption\_Dispose()

void OH\_ArkUI\_KeyframeAnimateOption\_Dispose(ArkUI\_KeyframeAnimateOption\* option)

**Description**

Disposes of a keyframe animation parameter object.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_KeyframeAnimateOption](../../structs/arkui-keyframeanimateoption/document.md)\* option | 
Keyframe animation parameter object.

If **option** is set to **NULL**, the operation is invalid.

 |

#### \[h2\]OH\_ArkUI\_KeyframeAnimateOption\_SetDelay()

int32\_t OH\_ArkUI\_KeyframeAnimateOption\_SetDelay(ArkUI\_KeyframeAnimateOption\* option, int32\_t value)

**Description**

Sets the overall delay of a keyframe animation, in milliseconds. By default, the keyframe animation starts without any delay.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_KeyframeAnimateOption](../../structs/arkui-keyframeanimateoption/document.md)\* option | 
Keyframe animation parameters.

If **option** is set to **NULL**, the error code [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) is returned.

 |
| int32\_t value | Animation delay, in milliseconds. Value range: (-∞, +∞). Default value: **0**, indicating no animation delay. A value greater than 0 means to begin the animation after the specified amount of time has elapsed. A value less than 0 means to begin the animation in advance. If **value** is less than **0** and the absolute value of **value** is less than the actual animation duration, the animation starts its first frame from the state at the absolute value. If the absolute value of **value** is greater than or equal to the actual animation duration, the animation starts its first frame from the end state. The actual animation duration is equal to the duration of a single animation multiplied by the number of animation playback times. |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

 |

#### \[h2\]OH\_ArkUI\_KeyframeAnimateOption\_SetIterations()

int32\_t OH\_ArkUI\_KeyframeAnimateOption\_SetIterations(ArkUI\_KeyframeAnimateOption\* option, int32\_t value)

**Description**

Sets the number of times that the keyframe animation is played. By default, the animation is played once. The value **\-1** indicates that the animation is played for an unlimited number of times. The value **0** indicates that no animation is played.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_KeyframeAnimateOption](../../structs/arkui-keyframeanimateoption/document.md)\* option | 
Keyframe animation parameters.

If **option** is set to **NULL**, the error code [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) is returned.

 |
| int32\_t value | 

Number of times that the animation is played. Value range: \[-1, +∞). If this parameter is set to **0**, the animation is not played. If this parameter is set to **\-1**, the animation is played for an infinite number of times. Default value: **1**, indicating that the animation is played once.

If the value is less than **\-1**, the operation is invalid, and the error code [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) is returned.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

 |

#### \[h2\]OH\_ArkUI\_KeyframeAnimateOption\_RegisterOnFinishCallback()

int32\_t OH\_ArkUI\_KeyframeAnimateOption\_RegisterOnFinishCallback(ArkUI\_KeyframeAnimateOption\* option, void\* userData, void (\*onFinish)(void\* userData))

**Description**

Sets the callback invoked when the keyframe animation playback is complete. This function is called after the [keyframe animation](../../structs/arkui-keyframeanimateoption/document.md) has played for the specified number of times.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_KeyframeAnimateOption](../../structs/arkui-keyframeanimateoption/document.md)\* option | 
Keyframe animation parameters.

If **option** is set to **NULL**, the error code [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) is returned.

 |
| void\* userData | 

Pointer to a custom object.

Abnormal value processing is not involved.

 |
| void (\*onFinish)(void\* userData) | 

Callback function.

**userData**: input parameter of the callback function, a user-defined object pointer.

If **onFinish** is set to **NULL**, the operation is invalid.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

 |

#### \[h2\]OH\_ArkUI\_KeyframeAnimateOption\_SetExpectedFrameRate()

int32\_t OH\_ArkUI\_KeyframeAnimateOption\_SetExpectedFrameRate(ArkUI\_KeyframeAnimateOption\* option, ArkUI\_ExpectedFrameRateRange\* frameRate)

**Description**

Sets the expected frame rate for a keyframe animation.

**Since**: 19

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_KeyframeAnimateOption](../../structs/arkui-keyframeanimateoption/document.md)\* option | 
Keyframe animation parameters.

If **option** is set to **NULL**, the error code [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) is returned.

 |
| [ArkUI\_ExpectedFrameRateRange](../../structs/arkui-expectedframeraterange/document.md)\* frameRate | 

Expected frame rate for the keyframe animation.

If **frameRate** is set to **NULL**, the error code [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) is returned.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

 |

#### \[h2\]OH\_ArkUI\_KeyframeAnimateOption\_SetDuration()

int32\_t OH\_ArkUI\_KeyframeAnimateOption\_SetDuration(ArkUI\_KeyframeAnimateOption\* option, int32\_t value, int32\_t index)

**Description**

Sets the duration of a keyframe animation, in milliseconds.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_KeyframeAnimateOption](../../structs/arkui-keyframeanimateoption/document.md)\* option | 
Keyframe animation parameters.

If **option** is set to **NULL**, the error code [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) is returned.

 |
| int32\_t value | 

Keyframe animation duration, in ms. The default value is 1000 ms. Value range: \[0, +∞).

If the value is less than 0, **0** is used.

 |
| int32\_t index | 

Index of the keyframe state segment.

If the value of **index** is less than 0, the error code [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) is returned.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

 |

#### \[h2\]OH\_ArkUI\_KeyframeAnimateOption\_SetCurve()

int32\_t OH\_ArkUI\_KeyframeAnimateOption\_SetCurve(ArkUI\_KeyframeAnimateOption\* option, ArkUI\_CurveHandle value, int32\_t index)

**Description**

Sets the animation curve for a specific keyframe animation segment.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fc/v3/qrKY0C1mTiW-uMvKm89f3A/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062302Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=DCDEBCE6A034DBD3B6A58DA0834A212E3E7C801BD562CEEEED8CB075A649949B)

Because the duration of the [springMotion](#oh_arkui_curve_createspringmotion), [responsiveSpringMotion](#oh_arkui_curve_createresponsivespringmotion), and [interpolatingSpring](#oh_arkui_curve_createinterpolatingspring) curves does not take effect, these curves are not supported.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_KeyframeAnimateOption](../../structs/arkui-keyframeanimateoption/document.md)\* option | 
Keyframe animation parameters.

If **option** is set to **NULL**, the error code [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) is returned.

 |
| [ArkUI\_CurveHandle](../../structs/arkui-curve--00020177/document.md) value | Animation curve to set. Default value: [ARKUI\_CURVE\_EASE\_IN\_OUT](../native-type-h/document.md#arkui_animationcurve). |
| int32\_t index | 

Index of the keyframe state segment. Value range: \[0, size – 1\], where **size** indicates the number of keyframe animation states.

If the value of **index** is less than 0 or out of range, the error code [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) is returned.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

 |

#### \[h2\]OH\_ArkUI\_KeyframeAnimateOption\_RegisterOnEventCallback()

int32\_t OH\_ArkUI\_KeyframeAnimateOption\_RegisterOnEventCallback(ArkUI\_KeyframeAnimateOption\* option, void\* userData, void (\*event)(void\* userData), int32\_t index)

**Description**

Sets the closure function of the state at the time of the keyframe, that is, the state to be reached at the time of the keyframe.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_KeyframeAnimateOption](../../structs/arkui-keyframeanimateoption/document.md)\* option | 
Keyframe animation parameters.

If **option** is set to **NULL**, the error code [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) is returned.

 |
| void\* userData | 

Pointer to a user-defined object.

Abnormal value processing is not involved.

 |
| void (\*event)(void\* userData) | 

Closure function.

If **event** is set to **NULL**, the operation is invalid.

 |
| int32\_t index | 

Index of the keyframe state segment. Value range: \[0, size – 1\], where **size** indicates the number of keyframe animation states.

If the value of **index** is less than 0 or out of range, the error code [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) is returned.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

 |

#### \[h2\]OH\_ArkUI\_KeyframeAnimateOption\_GetDelay()

int32\_t OH\_ArkUI\_KeyframeAnimateOption\_GetDelay(ArkUI\_KeyframeAnimateOption\* option)

**Description**

Obtains the overall delay of a keyframe animation, in milliseconds.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_KeyframeAnimateOption](../../structs/arkui-keyframeanimateoption/document.md)\* option | 
Keyframe animation parameters.

If **option** is set to **NULL**, **0** is returned.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | Overall delay, in milliseconds. If **option** is invalid, **0** is returned. |

#### \[h2\]OH\_ArkUI\_KeyframeAnimateOption\_GetIterations()

int32\_t OH\_ArkUI\_KeyframeAnimateOption\_GetIterations(ArkUI\_KeyframeAnimateOption\* option)

**Description**

Obtains the number of times that a keyframe animation is played.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_KeyframeAnimateOption](../../structs/arkui-keyframeanimateoption/document.md)\* option | 
Keyframe animation parameters.

If **option** is set to **NULL**, **0** is returned.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | Number of times that the animation is played. If **option** is invalid, **0** is returned. |

#### \[h2\]OH\_ArkUI\_KeyframeAnimateOption\_GetExpectedFrameRate()

ArkUI\_ExpectedFrameRateRange\* OH\_ArkUI\_KeyframeAnimateOption\_GetExpectedFrameRate(ArkUI\_KeyframeAnimateOption\* option)

**Description**

Obtains the expected frame rate from keyframe animation parameters.

**Since**: 19

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_KeyframeAnimateOption](../../structs/arkui-keyframeanimateoption/document.md)\* option | 
Keyframe animation parameters.

If **option** is set to **NULL**, **NULL** is returned.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| [ArkUI\_ExpectedFrameRateRange](../../structs/arkui-expectedframeraterange/document.md)\* | Returns the expected frame rate obtained. If **option** is invalid, **NULL** is returned. |

#### \[h2\]OH\_ArkUI\_KeyframeAnimateOption\_GetDuration()

int32\_t OH\_ArkUI\_KeyframeAnimateOption\_GetDuration(ArkUI\_KeyframeAnimateOption\* option, int32\_t index)

**Description**

Obtains the duration of a specific state in a keyframe animation, in milliseconds.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_KeyframeAnimateOption](../../structs/arkui-keyframeanimateoption/document.md)\* option | 
Keyframe animation parameters.

If **option** is set to **NULL**, **0** is returned.

 |
| int32\_t index | 

Index of the keyframe state segment.

If the value of **index** is less than 0, **0** is returned.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | Duration, in milliseconds. If **option** is invalid, **0** is returned. |

#### \[h2\]OH\_ArkUI\_KeyframeAnimateOption\_GetCurve()

ArkUI\_CurveHandle OH\_ArkUI\_KeyframeAnimateOption\_GetCurve(ArkUI\_KeyframeAnimateOption\* option, int32\_t index)

**Description**

Obtains the animation curve of a specific state in a keyframe animation.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_KeyframeAnimateOption](../../structs/arkui-keyframeanimateoption/document.md)\* option | 
Keyframe animation parameters.

If **option** is set to **NULL**, **NULL** is returned.

 |
| int32\_t index | 

Index of the keyframe state segment.

If the value of **index** is less than 0, **NULL** is returned.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| [ArkUI\_CurveHandle](../../structs/arkui-curve--00020177/document.md) | Animation curve. If the parameter is abnormal, **NULL** is returned. |

#### \[h2\]OH\_ArkUI\_AnimatorOption\_Create()

ArkUI\_AnimatorOption\* OH\_ArkUI\_AnimatorOption\_Create(int32\_t keyframeSize)

**Description**

Creates an **AnimatorOption** object.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/de/v3/BSwo18DFQE2kmuP-8FTDuQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062302Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5A2291FD53FBBFF3FFA4FC2C8BA0B3CC8A13B457D36C2DFEDD65177185AD7F8E)

If the value of **keyframeSize** is greater than 0, the animation interpolation start point is 0, and the animation interpolation end point is 1; no setting is allowed.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| int32\_t keyframeSize | 
Number of keyframes.

If the value of **keyframeSize** is less than 0, **NULL** is returned.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| [ArkUI\_AnimatorOption](../../structs/arkui-animatoroption/document.md)\* | Pointer to the animator parameter object. If the value of **size** is less than 0 or if **option** is abnormal, **NULL** is returned. |

#### \[h2\]OH\_ArkUI\_AnimatorOption\_Dispose()

void OH\_ArkUI\_AnimatorOption\_Dispose(ArkUI\_AnimatorOption\* option)

**Description**

Disposes of an **AnimatorOption** object.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_AnimatorOption](../../structs/arkui-animatoroption/document.md)\* option | 
Animator parameters.

If **option** is set to **NULL**, the operation is invalid.

 |

#### \[h2\]OH\_ArkUI\_AnimatorOption\_SetDuration()

int32\_t OH\_ArkUI\_AnimatorOption\_SetDuration(ArkUI\_AnimatorOption\* option, int32\_t value)

**Description**

Sets the duration of an animator animation, in milliseconds.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_AnimatorOption](../../structs/arkui-animatoroption/document.md)\* option | 
Animator parameters.

If **option** is set to **NULL**, the error code [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) is returned.

 |
| int32\_t value | 

Playback duration, in ms. The default value is 0 ms. Value range: \[0, +∞).

If the value is less than 0, the error code [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) is returned.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

 |

#### \[h2\]OH\_ArkUI\_AnimatorOption\_SetDelay()

int32\_t OH\_ArkUI\_AnimatorOption\_SetDelay(ArkUI\_AnimatorOption\* option, int32\_t value)

**Description**

Sets the delay time of the animator playback, in milliseconds.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_AnimatorOption](../../structs/arkui-animatoroption/document.md)\* option | 
Animator parameters.

If **option** is set to **NULL**, the error code [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) is returned.

 |
| int32\_t value | Animation delay, in milliseconds. Value range: (-∞, +∞). Default value: **0**, indicating no animation delay. A value greater than 0 means to begin the animation after the specified amount of time has elapsed. A value less than 0 means to begin the animation in advance. If **value** is less than **0** and the absolute value of **value** is less than the actual animation duration, the animation starts its first frame from the state at the absolute value. If the absolute value of **value** is greater than or equal to the actual animation duration, the animation starts its first frame from the end state. The actual animation duration is equal to the duration of a single animation multiplied by the number of animation playback times. |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

 |

#### \[h2\]OH\_ArkUI\_AnimatorOption\_SetIterations()

int32\_t OH\_ArkUI\_AnimatorOption\_SetIterations(ArkUI\_AnimatorOption\* option, int32\_t value)

**Description**

Sets the number of times that an animator animation is played. By default, the animation is played once. The value **\-1** indicates that the animation is played for an unlimited number of times. The value **0** indicates that no animation is played.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/64/v3/N2UPDyH4QXuEua4IHmS4qw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062302Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=82EE204CEA7BCF4FF761C813AB647422BF98C208AEEDDA0EEB355F148E890CA4)

If this parameter is set to a negative value other than **\-1**, the value is invalid. In this case, the animation is played once.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_AnimatorOption](../../structs/arkui-animatoroption/document.md)\* option | 
Animator parameters.

If **option** is set to **NULL**, the error code [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) is returned.

 |
| int32\_t value | 

Value range: \[-1, +∞). If this parameter is set to **0**, the animation is not played. If this parameter is set to **\-1**, the animation is played for an infinite number of times. Default value: **1** (played once).

If the value is less than -1, the operation is invalid.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

 |

#### \[h2\]OH\_ArkUI\_AnimatorOption\_SetFill()

int32\_t OH\_ArkUI\_AnimatorOption\_SetFill(ArkUI\_AnimatorOption\* option, ArkUI\_AnimationFillMode value)

**Description**

Sets the status of the component before and after the animator animation execution.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_AnimatorOption](../../structs/arkui-animatoroption/document.md)\* option | 
Animator parameters.

If **option** is set to **NULL**, the error code [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) is returned.

 |
| [ArkUI\_AnimationFillMode](../native-type-h/document.md#arkui_animationfillmode) value | 

Status of the component before and after the animator animation execution. Default value: [ARKUI\_ANIMATION\_FILL\_MODE\_FORWARDS](../native-type-h/document.md#arkui_animationfillmode).

If the value is less than 0, the error code [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) is returned.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

 |

#### \[h2\]OH\_ArkUI\_AnimatorOption\_SetDirection()

int32\_t OH\_ArkUI\_AnimatorOption\_SetDirection(ArkUI\_AnimatorOption\* option, ArkUI\_AnimationDirection value)

**Description**

Set the playback direction.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_AnimatorOption](../../structs/arkui-animatoroption/document.md)\* option | 
Animator parameters.

If **option** is set to **NULL**, the error code [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) is returned.

 |
| [ArkUI\_AnimationDirection](../native-type-h/document.md#arkui_animationdirection) value | 

Animation playback direction.

If the value is less than 0, the error code [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) is returned.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

 |

#### \[h2\]OH\_ArkUI\_AnimatorOption\_SetCurve()

int32\_t OH\_ArkUI\_AnimatorOption\_SetCurve(ArkUI\_AnimatorOption\* option, ArkUI\_CurveHandle value)

**Description**

Sets the interpolation curve for the animation of an animator.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a6/v3/1G0_cH5kSfiNPV8F-drl8A/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062302Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B515B68A30B8D6852553B3BB7FC8D7C53B72EBC42D15294AC888710891C09C51)

The [springCurve](#oh_arkui_curve_createspringcurve), [springMotion](#oh_arkui_curve_createspringmotion), [responsiveSpringMotion](#oh_arkui_curve_createresponsivespringmotion), [interpolatingSpring](#oh_arkui_curve_createinterpolatingspring), and [customCurve](#oh_arkui_curve_createcustomcurve) animation curves are not supported.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_AnimatorOption](../../structs/arkui-animatoroption/document.md)\* option | 
Animator parameters.

If **option** is set to **NULL**, the error code [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) is returned.

 |
| [ArkUI\_CurveHandle](../../structs/arkui-curve--00020177/document.md) value | 

Interpolation curve. Default value: [ARKUI\_CURVE\_LINEAR](../native-type-h/document.md#arkui_animationcurve). You are advised to use [ARKUI\_CURVE\_EASE\_IN\_OUT](../native-type-h/document.md#arkui_animationcurve) to obtain a smoother animation effect.

If **value** is set to **NULL**, the default curve [ARKUI\_CURVE\_LINEAR](../native-type-h/document.md#arkui_animationcurve) is used.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

 |

#### \[h2\]OH\_ArkUI\_AnimatorOption\_SetBegin()

int32\_t OH\_ArkUI\_AnimatorOption\_SetBegin(ArkUI\_AnimatorOption\* option, float value)

**Description**

Sets the interpolation start point of an animation.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/20/v3/sINfWF49SwSuZcfnpXGWhw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062302Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=BC2CAA008F073266ACBE3B746644E57A6B9A1A5D253182F6086092AB71AE064E)

This API does not take effect when the animation is a [keyframe animation](../../structs/arkui-keyframeanimateoption/document.md).

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_AnimatorOption](../../structs/arkui-animatoroption/document.md)\* option | 
Animator parameters.

If **option** is set to **NULL**, the error code [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) is returned.

 |
| float value | Interpolation start point of the animation. Value range: (-∞, +∞). |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

 |

#### \[h2\]OH\_ArkUI\_AnimatorOption\_SetEnd()

int32\_t OH\_ArkUI\_AnimatorOption\_SetEnd(ArkUI\_AnimatorOption\* option, float value)

**Description**

Sets the interpolation end point for the animation of an animator.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f0/v3/uBGW4UyvSxSJRDd_cCP4_g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062302Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=126872D1BEBBA39342267F47052A7F96AC8056526B53824BEA87C0495E297FBD)

This API does not take effect when the animation is a [keyframe animation](../../structs/arkui-keyframeanimateoption/document.md).

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_AnimatorOption](../../structs/arkui-animatoroption/document.md)\* option | 
Animator parameters.

If **option** is set to **NULL**, the error code [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) is returned.

 |
| float value | Interpolation end point of the animation. Value range: (-∞, +∞). |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

 |

#### \[h2\]OH\_ArkUI\_AnimatorOption\_SetExpectedFrameRateRange()

int32\_t OH\_ArkUI\_AnimatorOption\_SetExpectedFrameRateRange(ArkUI\_AnimatorOption\* option, ArkUI\_ExpectedFrameRateRange\* value)

**Description**

Sets the expected frame rate range of an animation.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_AnimatorOption](../../structs/arkui-animatoroption/document.md)\* option | 
Animator parameters.

If **option** is set to **NULL**, the error code [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) is returned.

 |
| [ArkUI\_ExpectedFrameRateRange](../../structs/arkui-expectedframeraterange/document.md)\* value | 

Expected frame rate range.

If **value** is set to **NULL**, the error code [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) is returned.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

 |

#### \[h2\]OH\_ArkUI\_AnimatorOption\_SetKeyframe()

int32\_t OH\_ArkUI\_AnimatorOption\_SetKeyframe(ArkUI\_AnimatorOption\* option, float time, float value, int32\_t index)

**Description**

Sets the keyframe parameters of an animator animation.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_AnimatorOption](../../structs/arkui-animatoroption/document.md)\* option | 
Animator parameters.

If **option** is set to **NULL**, the error code [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) is returned.

 |
| float time | 

Keyframe time. Value range: \[0, 1\]. The value must be in ascending order. Default value: evenly distributed by index (for example, **0.0** for the first frame, **0.5** for the second frame, and **1.0** for the third frame).

If the value of **time** is less than 0 or greater than 1, the error code [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) is returned.

 |
| float value | Keyframe value. Value range: (-∞, +∞). |
| int32\_t index | 

Keyframe index.

If the value of **index** is less than 0, the error code [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) is returned.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

 |

#### \[h2\]OH\_ArkUI\_AnimatorOption\_SetKeyframeCurve()

int32\_t OH\_ArkUI\_AnimatorOption\_SetKeyframeCurve(ArkUI\_AnimatorOption\* option, ArkUI\_CurveHandle value, int32\_t index)

**Description**

Sets the keyframe curve type for the animation of an animator.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b5/v3/ff3PghBKRGeK3lrGVv-7vQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062302Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1CBC7DC6BB4EAB4A3AB7AF2DC257B936CDDA1B31E72FBDAECB4C8C48B83C86B8)

The [springCurve](#oh_arkui_curve_createspringcurve), [springMotion](#oh_arkui_curve_createspringmotion), [responsiveSpringMotion](#oh_arkui_curve_createresponsivespringmotion), [interpolatingSpring](#oh_arkui_curve_createinterpolatingspring), and [customCurve](#oh_arkui_curve_createcustomcurve) animation curves are not supported.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_AnimatorOption](../../structs/arkui-animatoroption/document.md)\* option | 
Animator parameters.

If **option** is set to **NULL**, the error code [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) is returned.

 |
| [ArkUI\_CurveHandle](../../structs/arkui-curve--00020177/document.md) value | Interpolation curve. Default value: **NULL**, indicating linear interpolation. |
| int32\_t index | 

Keyframe index.

If the value of **index** is less than 0, the error code [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) is returned.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

 |

#### \[h2\]OH\_ArkUI\_AnimatorOption\_GetDuration()

int32\_t OH\_ArkUI\_AnimatorOption\_GetDuration(ArkUI\_AnimatorOption\* option)

**Description**

Obtains the duration for playing an animation.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_AnimatorOption](../../structs/arkui-animatoroption/document.md)\* option | 
Animator animation parameters.

If **option** is set to **NULL**, **0** is returned.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | Duration for playing the animation, in milliseconds. If **option** is invalid, **0** is returned. |

#### \[h2\]OH\_ArkUI\_AnimatorOption\_GetDelay()

int32\_t OH\_ArkUI\_AnimatorOption\_GetDelay(ArkUI\_AnimatorOption\* option)

**Description**

Obtains the delay for playing an animation.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_AnimatorOption](../../structs/arkui-animatoroption/document.md)\* option | Animator animation parameters. If **option** is set to **NULL**, **0** is returned. |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | Delay for playing the animation, in milliseconds. If **option** is invalid, **0** is returned. |

#### \[h2\]OH\_ArkUI\_AnimatorOption\_GetIterations()

int32\_t OH\_ArkUI\_AnimatorOption\_GetIterations(ArkUI\_AnimatorOption\* option)

**Description**

Obtains the number of times that an animator animation is played.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_AnimatorOption](../../structs/arkui-animatoroption/document.md)\* option | Animator parameters. If **option** is set to **NULL**, **0** is returned. |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | Number of times that the animation is played. If **option** is invalid, **0** is returned. |

#### \[h2\]OH\_ArkUI\_AnimatorOption\_GetFill()

ArkUI\_AnimationFillMode OH\_ArkUI\_AnimatorOption\_GetFill(ArkUI\_AnimatorOption\* option)

**Description**

Obtains the status of the component before and after the animator animation execution.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_AnimatorOption](../../structs/arkui-animatoroption/document.md)\* option | Animator animation parameters. |

**Return value**

| Type | Description |
| :-- | :-- |
| [ArkUI\_AnimationFillMode](../native-type-h/document.md#arkui_animationfillmode) | Status of the component before and after the animator animation execution. If **option** is invalid,**\-1** is returned. |

#### \[h2\]OH\_ArkUI\_AnimatorOption\_GetDirection()

ArkUI\_AnimationDirection OH\_ArkUI\_AnimatorOption\_GetDirection(ArkUI\_AnimatorOption\* option)

**Description**

Obtains the playback direction of an animator animation.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_AnimatorOption](../../structs/arkui-animatoroption/document.md)\* option | Animator animation parameters. |

**Return value**

| Type | Description |
| :-- | :-- |
| [ArkUI\_AnimationDirection](../native-type-h/document.md#arkui_animationdirection) | Animation playback direction. If **option** is invalid,**\-1** is returned. |

#### \[h2\]OH\_ArkUI\_AnimatorOption\_GetCurve()

ArkUI\_CurveHandle OH\_ArkUI\_AnimatorOption\_GetCurve(ArkUI\_AnimatorOption\* option)

**Description**

Obtains the interpolation curve of the animation of an animator.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_AnimatorOption](../../structs/arkui-animatoroption/document.md)\* option | Animator animation parameters. |

**Return value**

| Type | Description |
| :-- | :-- |
| [ArkUI\_CurveHandle](../../structs/arkui-curve--00020177/document.md) | Interpolation curve. If **option** is invalid, **NULL** is returned. |

#### \[h2\]OH\_ArkUI\_AnimatorOption\_GetBegin()

float OH\_ArkUI\_AnimatorOption\_GetBegin(ArkUI\_AnimatorOption\* option)

**Description**

Obtains the interpolation start point of an animation.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_AnimatorOption](../../structs/arkui-animatoroption/document.md)\* option | Animator animation parameters. |

**Return value**

| Type | Description |
| :-- | :-- |
| float | Interpolation start point of the animation. If **option** is invalid, **0.0** is returned. |

#### \[h2\]OH\_ArkUI\_AnimatorOption\_GetEnd()

float OH\_ArkUI\_AnimatorOption\_GetEnd(ArkUI\_AnimatorOption\* option)

**Description**

Obtains the interpolation end point of an animation.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_AnimatorOption](../../structs/arkui-animatoroption/document.md)\* option | Animator animation parameters. |

**Return value**

| Type | Description |
| :-- | :-- |
| float | Interpolation end point of the animation. If **option** is invalid, **0.0** is returned. |

#### \[h2\]OH\_ArkUI\_AnimatorOption\_GetExpectedFrameRateRange()

ArkUI\_ExpectedFrameRateRange\* OH\_ArkUI\_AnimatorOption\_GetExpectedFrameRateRange(ArkUI\_AnimatorOption\* option)

**Description**

Obtains the expected frame rate range of an animator animation.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_AnimatorOption](../../structs/arkui-animatoroption/document.md)\* option | Animator animation parameters. |

**Return value**

| Type | Description |
| :-- | :-- |
| [ArkUI\_ExpectedFrameRateRange](../../structs/arkui-expectedframeraterange/document.md)\* | Pointer to the expected frame rate range object. Returns **NULL** if a parameter error occurs. |

#### \[h2\]OH\_ArkUI\_AnimatorOption\_GetKeyframeTime()

float OH\_ArkUI\_AnimatorOption\_GetKeyframeTime(ArkUI\_AnimatorOption\* option, int32\_t index)

**Description**

Obtains the keyframe time of the animator playback, in milliseconds.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_AnimatorOption](../../structs/arkui-animatoroption/document.md)\* option | Animator parameters. |
| int32\_t index | Keyframe index. |

**Return value**

| Type | Description |
| :-- | :-- |
| float | Keyframe time, in milliseconds. |

#### \[h2\]OH\_ArkUI\_AnimatorOption\_GetKeyframeValue()

float OH\_ArkUI\_AnimatorOption\_GetKeyframeValue(ArkUI\_AnimatorOption\* option, int32\_t index)

**Description**

Obtains the keyframe value of an animation.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_AnimatorOption](../../structs/arkui-animatoroption/document.md)\* option | Animator parameters. |
| int32\_t index | Keyframe index. |

**Return value**

| Type | Description |
| :-- | :-- |
| float | Keyframe value. |

#### \[h2\]OH\_ArkUI\_AnimatorOption\_GetKeyframeCurve()

ArkUI\_CurveHandle OH\_ArkUI\_AnimatorOption\_GetKeyframeCurve(ArkUI\_AnimatorOption\* option, int32\_t index)

**Description**

Obtains the interpolation curve for a keyframe in the animation of an animator.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_AnimatorOption](../../structs/arkui-animatoroption/document.md)\* option | Animator parameters. |
| int32\_t index | Keyframe index. |

**Return value**

| Type | Description |
| :-- | :-- |
| [ArkUI\_CurveHandle](../../structs/arkui-curve--00020177/document.md) | Interpolation curve. Returns **NULL** if a parameter error occurs. |

#### \[h2\]OH\_ArkUI\_AnimatorEvent\_GetUserData()

void\* OH\_ArkUI\_AnimatorEvent\_GetUserData(ArkUI\_AnimatorEvent\* event)

**Description**

Obtains the user-defined object in an animation event object.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_AnimatorEvent](../../structs/arkui-animatorevent/document.md)\* event | Animation event object. |

**Return value**

| Type | Description |
| :-- | :-- |
| void\* | User-defined object. |

#### \[h2\]OH\_ArkUI\_AnimatorOnFrameEvent\_GetUserData()

void\* OH\_ArkUI\_AnimatorOnFrameEvent\_GetUserData(ArkUI\_AnimatorOnFrameEvent\* event)

**Description**

Obtains the user-defined object in the frame event of an animation.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_AnimatorOnFrameEvent](../../structs/arkui-animatoronframeevent/document.md)\* event | Animation event object. |

**Return value**

| Type | Description |
| :-- | :-- |
| void\* | User-defined object. |

#### \[h2\]OH\_ArkUI\_AnimatorOnFrameEvent\_GetValue()

float OH\_ArkUI\_AnimatorOnFrameEvent\_GetValue(ArkUI\_AnimatorOnFrameEvent\* event)

**Description**

Obtains the interpolation result in the animation frame callback event object.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_AnimatorOnFrameEvent](../../structs/arkui-animatoronframeevent/document.md)\* event | Animation event object. |

**Return value**

| Type | Description |
| :-- | :-- |
| float | 
Animation interpolation result.

**NOTE**

During the animation, the interpolation result changes between the interpolation start point [OH\_ArkUI\_AnimatorOption\_SetBegin](#oh_arkui_animatoroption_setbegin) and the interpolation end point [OH\_ArkUI\_AnimatorOption\_SetEnd](#oh_arkui_animatoroption_setend) based on the animation parameters.

 |

#### \[h2\]OH\_ArkUI\_AnimatorOption\_RegisterOnFrameCallback()

int32\_t OH\_ArkUI\_AnimatorOption\_RegisterOnFrameCallback(ArkUI\_AnimatorOption\* option, void\* userData, void (\*callback)(ArkUI\_AnimatorOnFrameEvent\* event))

**Description**

Sets the callback invoked when the animator receives a frame.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_AnimatorOption](../../structs/arkui-animatoroption/document.md)\* option | Animator animation parameters. |
| void\* userData | User-defined parameter. |
| void (\*callback)(ArkUI\_AnimatorOnFrameEvent\* event) | 
Callback function.

\- **event**: input parameter of the callback function, an animation event object.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

 |

#### \[h2\]OH\_ArkUI\_AnimatorOption\_RegisterOnFinishCallback()

int32\_t OH\_ArkUI\_AnimatorOption\_RegisterOnFinishCallback(ArkUI\_AnimatorOption\* option, void\* userData, void (\*callback)(ArkUI\_AnimatorEvent\* event))

**Description**

Sets the callback invoked when the animation playback is complete.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_AnimatorOption](../../structs/arkui-animatoroption/document.md)\* option | Animator animation parameters. |
| void\* userData | User-defined parameter. |
| void (\*callback)(ArkUI\_AnimatorEvent\* event) | 
Callback function.

\- **event**: input parameter of the callback function, an animation event object.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

 |

#### \[h2\]OH\_ArkUI\_AnimatorOption\_RegisterOnCancelCallback()

int32\_t OH\_ArkUI\_AnimatorOption\_RegisterOnCancelCallback(ArkUI\_AnimatorOption\* option, void\* userData, void (\*callback)(ArkUI\_AnimatorEvent\* event))

**Description**

Sets the callback invoked when the animation playback is canceled.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_AnimatorOption](../../structs/arkui-animatoroption/document.md)\* option | Animator animation parameters. |
| void\* userData | User-defined parameter. |
| void (\*callback)(ArkUI\_AnimatorEvent\* event) | 
Callback function.

\- **event**: input parameter of the callback function, an animation event object.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

 |

#### \[h2\]OH\_ArkUI\_AnimatorOption\_RegisterOnRepeatCallback()

int32\_t OH\_ArkUI\_AnimatorOption\_RegisterOnRepeatCallback(ArkUI\_AnimatorOption\* option, void\* userData, void (\*callback)(ArkUI\_AnimatorEvent\* event))

**Description**

Sets the callback invoked when the animation playback is repeated.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_AnimatorOption](../../structs/arkui-animatoroption/document.md)\* option | Animator animation parameters. |
| void\* userData | User-defined parameter. |
| void (\*callback)(ArkUI\_AnimatorEvent\* event) | 
Callback function.

\- **event**: input parameter of the callback function, an animation event object.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

 |

#### \[h2\]OH\_ArkUI\_Animator\_ResetAnimatorOption()

int32\_t OH\_ArkUI\_Animator\_ResetAnimatorOption(ArkUI\_AnimatorHandle animatorHandle, ArkUI\_AnimatorOption\* option)

**Description**

Resets the animation of an animator.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_AnimatorHandle](../../structs/arkui-animator/document.md) animatorHandle | Animator object. |
| [ArkUI\_AnimatorOption](../../structs/arkui-animatoroption/document.md)\* option | Animator animation parameters. |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

 |

#### \[h2\]OH\_ArkUI\_Animator\_Play()

int32\_t OH\_ArkUI\_Animator\_Play(ArkUI\_AnimatorHandle animatorHandle)

**Description**

Starts the animation of an animator.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_AnimatorHandle](../../structs/arkui-animator/document.md) animatorHandle | Animator object. |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

 |

#### \[h2\]OH\_ArkUI\_Animator\_Finish()

int32\_t OH\_ArkUI\_Animator\_Finish(ArkUI\_AnimatorHandle animatorHandle)

**Description**

Ends the animation of an animator.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_AnimatorHandle](../../structs/arkui-animator/document.md) animatorHandle | Animator object. |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

 |

#### \[h2\]OH\_ArkUI\_Animator\_Pause()

int32\_t OH\_ArkUI\_Animator\_Pause(ArkUI\_AnimatorHandle animatorHandle)

**Description**

Pauses the animation of an animator.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_AnimatorHandle](../../structs/arkui-animator/document.md) animatorHandle | Animator object. |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

 |

#### \[h2\]OH\_ArkUI\_Animator\_Cancel()

int32\_t OH\_ArkUI\_Animator\_Cancel(ArkUI\_AnimatorHandle animatorHandle)

**Description**

Cancels the animation of an animator.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_AnimatorHandle](../../structs/arkui-animator/document.md) animatorHandle | Animator object. |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

 |

#### \[h2\]OH\_ArkUI\_Animator\_Reverse()

int32\_t OH\_ArkUI\_Animator\_Reverse(ArkUI\_AnimatorHandle animatorHandle)

**Description**

Plays this animation in reverse order.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_AnimatorHandle](../../structs/arkui-animator/document.md) animatorHandle | Animator object. |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

 |

#### \[h2\]OH\_ArkUI\_Curve\_CreateCurveByType()

ArkUI\_CurveHandle OH\_ArkUI\_Curve\_CreateCurveByType(ArkUI\_AnimationCurve curve)

**Description**

Implements initialization for the interpolation curve, which is used to create an interpolation curve based on the input parameter.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_AnimationCurve](../native-type-h/document.md#arkui_animationcurve) curve | Curve type. |

**Return value**

| Type | Description |
| :-- | :-- |
| [ArkUI\_CurveHandle](../../structs/arkui-curve--00020177/document.md) | Pointer to the interpolation object of the curve. Returns **NULL** if a parameter error occurs. |

#### \[h2\]OH\_ArkUI\_Curve\_CreateStepsCurve()

ArkUI\_CurveHandle OH\_ArkUI\_Curve\_CreateStepsCurve(int32\_t count, bool end)

**Description**

Creates a step curve.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| int32\_t count | 
Number of steps. The value must be a positive integer. Value range: \[1, +∞).

If the value of **count** is abnormal, the operation is invalid.

 |
| bool end | Whether the step change occurs at the start or end of each interval. **true**: The step change occurs at the end of each interval. **false**: The step change occurs at the start of each interval. |

**Return value**

| Type | Description |
| :-- | :-- |
| [ArkUI\_CurveHandle](../../structs/arkui-curve--00020177/document.md) | Pointer to the interpolation object of the curve. Returns **NULL** if a parameter error occurs. |

#### \[h2\]OH\_ArkUI\_Curve\_CreateCubicBezierCurve()

ArkUI\_CurveHandle OH\_ArkUI\_Curve\_CreateCubicBezierCurve(float x1, float y1, float x2, float y2)

**Description**

Creates a cubic Bezier curve.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| float x1 | X-coordinate of the first point on the Bezier curve. Value range: \[0, 1\]. A value less than 0 is treated as **0**. A value greater than 1 is treated as **1**. |
| float y1 | Y-coordinate of the first point on the Bezier curve. |
| float x2 | X-coordinate of the second point on the Bezier curve. Value range: \[0, 1\]. A value less than 0 is treated as **0**. A value greater than 1 is treated as **1**. |
| float y2 | Y-coordinate of the second point on the Bezier curve. |

**Return value**

| Type | Description |
| :-- | :-- |
| [ArkUI\_CurveHandle](../../structs/arkui-curve--00020177/document.md) | Pointer to the interpolation object of the curve. Returns **NULL** if a parameter error occurs. |

#### \[h2\]OH\_ArkUI\_Curve\_CreateSpringCurve()

ArkUI\_CurveHandle OH\_ArkUI\_Curve\_CreateSpringCurve(float velocity, float mass, float stiffness, float damping)

**Description**

Creates a spring curve. The curve shape is determined by the spring parameters, and the animation duration is controlled by the **duration** parameter in [animation](#oh_arkui_transitioneffect_setanimation) and [animateTo](../../structs/arkui-nativeanimateapi-1/document.md#animateto).

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| float velocity | Initial velocity. It is applied by external factors to the spring animation, designed to help ensure the smooth transition from the previous motion state. The velocity is the normalized velocity, and its value is equal to the actual velocity at the beginning of the animation divided by the animation attribute change value. |
| float mass | 
Mass. It describes the inertia of the object in the elastic system, affecting the amplitude of oscillation and the speed of return to equilibrium. The greater the mass, the greater the amplitude of the oscillation, and the slower the speed of restoring to the equilibrium position. Value range: \[0, +∞).

If the value is less than or equal to 0, **1** is used.

 |
| float stiffness | 

Stiffness. It is the degree to which an object deforms by resisting the force applied. In an elastic system, the greater the stiffness, the stronger the ability to resist deformation, and the faster the speed of restoring to the equilibrium position. Value range: \[0, +∞).

If the value is less than or equal to 0, **1** is used.

 |
| float damping | 

Damping. It is used to describe the oscillation and attenuation of the system after being disturbed. The larger the damping, the smaller the number of oscillations of elastic motion, and the smaller the oscillation amplitude. Value range: \[0, +∞).

If the value is less than or equal to 0, **1** is used.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| [ArkUI\_CurveHandle](../../structs/arkui-curve--00020177/document.md) | Pointer to the interpolation object of the curve. Returns **NULL** if a parameter error occurs. |

#### \[h2\]OH\_ArkUI\_Curve\_CreateSpringMotion()

ArkUI\_CurveHandle OH\_ArkUI\_Curve\_CreateSpringMotion(float response, float dampingFraction, float overlapDuration)

**Description**

Creates a spring animation curve. If multiple spring animations are applied to the same attribute of an object, each animation replaces their predecessor and inherits the velocity.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/37/v3/xnUG4Z05QACFF7hkQMT6Hg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062302Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=882D2C30736F37F1C2CB66126AFC0D60528139EB90F2B5955C22D037973C92D1)

The animation duration determined by the curve parameters, rather than the **duration** parameter in [animation](#oh_arkui_transitioneffect_setanimation) or [animateTo](../../structs/arkui-nativeanimateapi-1/document.md#animateto).

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| float response | 
Duration of one complete oscillation. Value range: (0, +∞).

If the value is less than or equal to 0, **0.55** is used.

 |
| float dampingFraction | 

Damping coefficient. > 0 and < 1: underdamped. In this case, the spring overshoots the equilibrium position. \*\*1\*\*: critically damped. > 1: overdamped. In this case, the spring approaches equilibrium gradually. Value range: (0, +∞).

If the value is less than or equal to 0, **0.825** is used.

 |
| float overlapDuration | 

Duration for animations to overlap, in seconds. When animations overlap, the **response** values of these animations will transit smoothly over this duration if they are different. Value range: \[0, +∞).

If the value is less than 0, **0** is used.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| [ArkUI\_CurveHandle](../../structs/arkui-curve--00020177/document.md) | Pointer to the interpolation object of the curve. Returns **NULL** if a parameter error occurs. |

#### \[h2\]OH\_ArkUI\_Curve\_CreateResponsiveSpringMotion()

ArkUI\_CurveHandle OH\_ArkUI\_Curve\_CreateResponsiveSpringMotion(float response, float dampingFraction, float overlapDuration)

**Description**

Creates a responsive spring animation curve. It is a special case of **springMotion**, with the only difference in the default values. It can be used together with **springMotion**.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/32/v3/zGLUqz2eQn-SevcrHH1NQQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062302Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0699E543D24CFD908F826B7C63917BF0D0857BBF3AD091AB63984FCBF10827CD)

The animation duration determined by the curve parameters, rather than the **duration** parameter in [animation](#oh_arkui_transitioneffect_setanimation) or [animateTo](../../structs/arkui-nativeanimateapi-1/document.md#animateto).

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| float response | 
Duration of one complete oscillation. Value range: (0, +∞).

If the value is less than or equal to 0, **0.15** is used.

 |
| float dampingFraction | 

Damping coefficient. > 0 and < 1: underdamped. In this case, the spring overshoots the equilibrium position. \*\*1\*\*: critically damped. > 1: overdamped. In this case, the spring approaches equilibrium gradually. Value range: \[0, +∞).

If the value is less than 0, **0.86** is used.

 |
| float overlapDuration | 

Duration for animations to overlap, in seconds. When animations overlap, the **response** values of these animations will transit smoothly over this duration if they are different. Value range: \[0, +∞).

If the value is less than 0, **0.25** is used.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| [ArkUI\_CurveHandle](../../structs/arkui-curve--00020177/document.md) | Pointer to the interpolation object of the curve. Returns **NULL** if a parameter error occurs. |

#### \[h2\]OH\_ArkUI\_Curve\_CreateInterpolatingSpring()

ArkUI\_CurveHandle OH\_ArkUI\_Curve\_CreateInterpolatingSpring(float velocity, float mass, float stiffness, float damping)

**Description**

Creates an interpolating spring curve animated from 0 to 1. The actual animation value is calculated based on the curve.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a5/v3/0DVrJ1QSQaaNSWmyI3Uy0A/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062302Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7B211AA36FD193393555B13750BA7A8F44357B6359F277E5546400477B63C740)

The animation duration determined by the curve parameters, rather than the **duration** parameter in [animation](#oh_arkui_transitioneffect_setanimation) or [animateTo](../../structs/arkui-nativeanimateapi-1/document.md#animateto).

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| float velocity | Initial velocity. It is applied by external factors to the spring animation, designed to help ensure the smooth transition from the previous motion state. The velocity is the normalized velocity, and its value is equal to the actual velocity at the beginning of the animation divided by the animation attribute change value. |
| float mass | 
Mass. It describes the inertia of the object in the elastic system, affecting the amplitude of oscillation and the speed of return to equilibrium. The greater the mass, the greater the amplitude of the oscillation, and the slower the speed of restoring to the equilibrium position. Value range: \[0, +∞).

If the value is less than or equal to 0, **1** is used.

 |
| float stiffness | 

Stiffness. It is the degree to which an object deforms by resisting the force applied. The greater the stiffness, the stronger the ability to resist deformation, and the faster the speed of restoring to the equilibrium position. Value range: \[0, +∞).

If the value is less than or equal to 0, **1** is used.

 |
| float damping | 

Damping. It is used to describe the oscillation and attenuation of the system after being disturbed. The larger the damping, the smaller the number of oscillations of elastic motion, and the smaller the oscillation amplitude. Value range: \[0, +∞).

If the value is less than or equal to 0, **1** is used.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| [ArkUI\_CurveHandle](../../structs/arkui-curve--00020177/document.md) | Pointer to the interpolation object of the curve. Returns **NULL** if a parameter error occurs. |

#### \[h2\]OH\_ArkUI\_Curve\_CreateCustomCurve()

ArkUI\_CurveHandle OH\_ArkUI\_Curve\_CreateCustomCurve(void\* userData, float (\*interpolate)(float fraction, void\* userdata))

**Description**

Creates a custom curve.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| void\* userData | Pointer to user-defined data. |
| float (\*interpolate)(float fraction, void\* userdata) | User-defined interpolation callback. **fraction** indicates the input x value for interpolation when the animation starts; value range: \[0, 1\]. The return value is the **y** value of the curve. value range: \[0, 1\]. If **fraction** is **0**, the return value **0** corresponds to the animation start point; any other return value means that the animation jumps at the start point. If **fraction** is **1**, the return value **1** corresponds to the animation end point; any other return value means that the end value of the animation is not the value of the state variable, which will result in an effect of transition from that end value to the value of the state variable. |

**Return value**

| Type | Description |
| :-- | :-- |
| [ArkUI\_CurveHandle](../../structs/arkui-curve--00020177/document.md) | Pointer to the interpolation object of the curve. Returns **NULL** if a parameter error occurs. |

#### \[h2\]OH\_ArkUI\_Curve\_DisposeCurve()

void OH\_ArkUI\_Curve\_DisposeCurve(ArkUI\_CurveHandle curveHandle)

**Description**

Disposes of a custom curve.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_CurveHandle](../../structs/arkui-curve--00020177/document.md) curveHandle | Pointer to the interpolation object of the curve. |

#### \[h2\]OH\_ArkUI\_CreateOpacityTransitionEffect()

ArkUI\_TransitionEffect\* OH\_ArkUI\_CreateOpacityTransitionEffect(float opacity)

**Description**

Creates an opacity effect object for component transitions.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| float opacity | Opacity. Value range: \[0, 1\]. The default value is **1**. A value less than 0 is treated as 0. A value greater than 1 is treated as 1. The value **1** means fully opaque, and **0** means fully transparent. |

**Return value**

| Type | Description |
| :-- | :-- |
| [ArkUI\_TransitionEffect](../../structs/arkui-transitioneffect/document.md)\* | Opacity effect object for component transitions. |

#### \[h2\]OH\_ArkUI\_CreateTranslationTransitionEffect()

ArkUI\_TransitionEffect\* OH\_ArkUI\_CreateTranslationTransitionEffect(ArkUI\_TranslationOptions\* translate)

**Description**

Creates a translation effect object for component transitions.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_TranslationOptions](../../structs/arkui-translationoptions/document.md)\* translate | Translation parameter object for component transitions. |

**Return value**

| Type | Description |
| :-- | :-- |
| [ArkUI\_TransitionEffect](../../structs/arkui-transitioneffect/document.md)\* | Translation effect object for component transitions. Returns **NULL** if a parameter error occurs. |

#### \[h2\]OH\_ArkUI\_CreateScaleTransitionEffect()

ArkUI\_TransitionEffect\* OH\_ArkUI\_CreateScaleTransitionEffect(ArkUI\_ScaleOptions\* scale)

**Description**

Creates a scaling effect object for component transitions.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_ScaleOptions](../../structs/arkui-scaleoptions/document.md)\* scale | Scaling parameter object for component transitions. |

**Return value**

| Type | Description |
| :-- | :-- |
| [ArkUI\_TransitionEffect](../../structs/arkui-transitioneffect/document.md)\* | Scaling effect object for component transitions. Returns **NULL** if a parameter error occurs. |

#### \[h2\]OH\_ArkUI\_CreateRotationTransitionEffect()

ArkUI\_TransitionEffect\* OH\_ArkUI\_CreateRotationTransitionEffect(ArkUI\_RotationOptions\* rotate)

**Description**

Creates a rotation effect object for component transition.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_RotationOptions](../../structs/arkui-rotationoptions/document.md)\* rotate | Rotation parameter object for component transitions. |

**Return value**

| Type | Description |
| :-- | :-- |
| [ArkUI\_TransitionEffect](../../structs/arkui-transitioneffect/document.md)\* | Rotation effect object for component transitions. Returns **NULL** if a parameter error occurs. |

#### \[h2\]OH\_ArkUI\_CreateMovementTransitionEffect()

ArkUI\_TransitionEffect\* OH\_ArkUI\_CreateMovementTransitionEffect(ArkUI\_TransitionEdge edge)

**Description**

Creates a movement transition effect object for the component.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_TransitionEdge](../native-type-h/document.md#arkui_transitionedge) edge | Movement transition type. |

**Return value**

| Type | Description |
| :-- | :-- |
| [ArkUI\_TransitionEffect](../../structs/arkui-transitioneffect/document.md)\* | Translation effect object for component transitions. Returns **NULL** if a parameter error occurs. |

#### \[h2\]OH\_ArkUI\_CreateAsymmetricTransitionEffect()

ArkUI\_TransitionEffect\* OH\_ArkUI\_CreateAsymmetricTransitionEffect(ArkUI\_TransitionEffect\* appear, ArkUI\_TransitionEffect\* disappear)

**Description**

Creates an asymmetric transition effect.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/79/v3/sqMUU7HVRTWZZpYDD1xVug/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062302Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B7F30E7E27A886EC9E3240D783EEEE8259BF68DE89B0A692BD2EACFB26BE4887)

If this function is not used for [ArkUI\_TransitionEffect](../../structs/arkui-transitioneffect/document.md), the transition effect takes effect for both appearance and disappearance of the component.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_TransitionEffect](../../structs/arkui-transitioneffect/document.md)\* appear | Transition effect for appearance. |
| [ArkUI\_TransitionEffect](../../structs/arkui-transitioneffect/document.md)\* disappear | Transition effect for disappearance. |

**Return value**

| Type | Description |
| :-- | :-- |
| [ArkUI\_TransitionEffect](../../structs/arkui-transitioneffect/document.md)\* | Asymmetric transition effect. Returns **NULL** if a parameter error occurs. |

#### \[h2\]OH\_ArkUI\_TransitionEffect\_Dispose()

void OH\_ArkUI\_TransitionEffect\_Dispose(ArkUI\_TransitionEffect\* effect)

**Description**

Disposes of a transition effect.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_TransitionEffect](../../structs/arkui-transitioneffect/document.md)\* effect | Pointer to the transition effect to be disposed. |

#### \[h2\]OH\_ArkUI\_TransitionEffect\_Combine()

int32\_t OH\_ArkUI\_TransitionEffect\_Combine(ArkUI\_TransitionEffect\* firstEffect, ArkUI\_TransitionEffect\* secondEffect)

**Description**

Sets a combination of transition effects.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_TransitionEffect](../../structs/arkui-transitioneffect/document.md)\* firstEffect | Transition effect. |
| [ArkUI\_TransitionEffect](../../structs/arkui-transitioneffect/document.md)\* secondEffect | Combination of transition effects. |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

 |

#### \[h2\]OH\_ArkUI\_TransitionEffect\_SetAnimation()

int32\_t OH\_ArkUI\_TransitionEffect\_SetAnimation(ArkUI\_TransitionEffect\* effect, ArkUI\_AnimateOption\* animation)

**Description**

Sets transition effect animation settings.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bd/v3/Gq5Mt1miTKSF3gulobuugA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062302Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=AD47159297ED2E2C930079A0DC02E71039D4830C0E539AF231751F2A2BEA4816)

If [OH\_ArkUI\_TransitionEffect\_Combine](#oh_arkui_transitioneffect_combine) is used to combine transition effects, the animation parameter settings of a transition effect are applicable to the one following it.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_TransitionEffect](../../structs/arkui-transitioneffect/document.md)\* effect | Transition effect. |
| [ArkUI\_AnimateOption](../../structs/arkui-animateoption/document.md)\* animation | Animation settings. |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

 |
