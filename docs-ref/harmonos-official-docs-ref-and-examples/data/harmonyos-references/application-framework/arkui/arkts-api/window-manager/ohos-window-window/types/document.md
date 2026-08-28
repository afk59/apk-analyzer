# Types

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c9/v3/zo1_BLT0QBupo5iNa2_6Fg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062230Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B7A3489896436D0717B9FB2F126E25B112F16DF54D2197946B07FFC554640FA1)

-   The initial APIs of this module are supported since API version 6. Newly added APIs will be marked with a superscript to indicate their earliest API version.
    
-   For the system capability SystemCapability.Window.SessionManager, use [canIUse()](../../../../../../common-capabilities/arkts-api/syscap/document.md#caniuse) to check whether the device supports this system capability and the corresponding APIs.
    

#### SpecificSystemBar11+

type SpecificSystemBar = 'status' | 'navigation' | 'navigationIndicator'

Defines the type of system bar that can be displayed or hidden.

**System capability**: SystemCapability.Window.SessionManager

**Atomic service API**: This API can be used in atomic services since API version 11.

| Type | Description |
| :-- | :-- |
| 'status' | Status bar. |
| 'navigation' | 
This enum is not supported by HarmonyOS devices.

Three-button navigation bar.

 |
| 'navigationIndicator' | Bottom navigation bar. It may appear as a navigation bar or a three-button navigation bar depending on user settings. |

#### WindowAnimationCurveParam20+

type WindowAnimationCurveParam = Array<number>

Defines the parameters for the animation curve. The meaning of **WindowAnimationCurveParam** varies depending on the type of [WindowAnimationCurve](../enums/document.md#windowanimationcurve20).

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.Window.SessionManager

| Type | Description |
| :-- | :-- |
| Array<number> | An array of numbers. The range of values for each element depends on the specific curve type. |

When the curve type is **LINEAR**, **WindowAnimationCurveParam** is optional and have no effect.

When the curve type is **INTERPOLATION\_SPRING**, **WindowAnimationCurveParam** must be set as an array of length 4: \[velocity,mass,stiffness,damping\].

-   **velocity**: initial velocity, which is of the number type. This parameter is mandatory. The value range is (-∞, +∞).
    
    It describes the impact of external factors to the spring animation, designed to help ensure smooth transition from the previous motion state. This is a normalized velocity, and it is calculated as the actual initial velocity divided by the change in the animation property.
    
-   **mass**: mass, which is of the number type. This parameter is mandatory. The value range is (0, +∞). If the value is less than or equal to 0, the value **1** is used.
    
    It describes the inertia of the object in the elastic system, affecting the amplitude of oscillation and the speed of return to equilibrium. The greater the mass, the greater the amplitude of the oscillation, and the slower the speed of restoring to the equilibrium position.
    
-   **stiffness**: stiffness, which is of the number type. This parameter is mandatory. The value range is (0, +∞). If the value is less than or equal to 0, the value **1** is used.
    
    It describes the degree to which an object deforms by resisting the force applied. In an elastic system, the greater the stiffness, the stronger the capability to resist deformation, and the faster the speed of restoring to the equilibrium position.
    
-   **damping**: damping, which is of the number type. This parameter is mandatory. The value range is (0, +∞). If the value is less than or equal to 0, the value **1** is used.
    
    It is used to describe the oscillation and attenuation of the system after being disturbed. The larger the damping, the smaller the number of oscillations of elastic motion, and the smaller the oscillation amplitude.
    

When the curve type is **CUBIC\_BEZIER**, **WindowAnimationCurveParam** must be set as an array of length 4: \[x1, y1, x2, y2\].

-   x1: horizontal coordinate of the first point of the Bezier curve. It is of the number type, mandatory, with a range of \[0, 1\]. Values less than 0 are treated as 0, and values greater than 1 are treated as 1.
    
-   y1: vertical coordinate of the first point of the Bezier curve. It is of the number type, mandatory, with a range of (-∞, +∞).
    
-   x2: horizontal coordinate of the second point of the Bezier curve. It is of the number type, mandatory, with a range of \[0, 1\]. Values less than 0 are treated as 0, and values greater than 1 are treated as 1.
    
-   y2: vertical coordinate of the second point of the Bezier curve. It is of the number type, mandatory, with a range of (-∞, +∞).
